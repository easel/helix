#!/usr/bin/env python3
"""Verify a HELIX demo session.jsonl against its assertions.yml.

Each demo can ship an `assertions.yml` alongside its `session.jsonl`. The
file is a small declarative contract about what the captured session
contains. Schema:

    slug: helix-align               # must match the dir name
    min_duration_s: 5               # rendered cast must run at least this long
    min_assistant_chars: 200        # total length of typed assistant text
    expect:
      - kind: tool_call             # one entry per claim
        name: Read
        args_contain:               # substring match on the rendered args
          file_path: "docs/helix/01-frame/prd.md"
      - kind: assistant
        contains: "Found 3 alignment findings"
      - kind: shell
        contains: "tree docs/helix"
      - kind: output
        contains: "ADR-002-oauth-pivot.md"
      - kind: narration
        contains: "API-key only"

`expect` entries are matched in order against session events; a later
entry can only match an event at or after the previous match position.
This catches "the events happened, but in the wrong order" mistakes.

No jsonschema or PyYAML dependency: assertions.yml uses a tight subset
parsed by hand, same shape across demos.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def parse_assertions(path: Path) -> dict:
    """Minimal YAML subset parser tailored to the assertions schema."""
    text = path.read_text(encoding="utf-8")
    obj: dict = {"expect": []}
    current_entry: dict | None = None
    current_subkey: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        # Top-level scalar: `key: value`
        if not line.startswith(" "):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key == "expect":
                # start the list, entries follow as `  - kind: ...`
                current_entry = None
                current_subkey = None
            else:
                obj[key] = _coerce_scalar(value)
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        if indent == 2 and stripped.startswith("- "):
            # New expect entry
            current_entry = {}
            obj["expect"].append(current_entry)
            inner = stripped[2:].strip()
            if inner:
                k, _, v = inner.partition(":")
                current_entry[k.strip()] = _coerce_scalar(v.strip().strip('"').strip("'"))
            current_subkey = None
            continue

        if indent == 4 and ":" in stripped and current_entry is not None:
            k, _, v = stripped.partition(":")
            key = k.strip()
            value = v.strip().strip('"').strip("'")
            if value == "":
                current_subkey = key
                current_entry[key] = {}
            else:
                current_entry[key] = _coerce_scalar(value)
                current_subkey = None
            continue

        if indent == 6 and ":" in stripped and current_entry is not None and current_subkey:
            k, _, v = stripped.partition(":")
            current_entry[current_subkey][k.strip()] = _coerce_scalar(
                v.strip().strip('"').strip("'")
            )
            continue

    return obj


def _coerce_scalar(value: str):
    if value == "":
        return value
    if value in {"true", "false"}:
        return value == "true"
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def load_session(path: Path) -> list[dict]:
    events: list[dict] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if raw:
            events.append(json.loads(raw))
    return events


def derive_metrics(events: list[dict]) -> dict:
    duration_s = 0.0
    assistant_chars = 0
    DEFAULT_PACE_MS = 25
    for ev in events:
        if "narration" in ev:
            duration_s += float(ev.get("pause_s", 1.0))
        elif "shell" in ev:
            duration_s += float(ev.get("pause_s", 0.4))
        elif "output" in ev:
            duration_s += float(ev.get("pause_s", 0.1))
        elif "prompt" in ev:
            duration_s += float(ev.get("pause_s", 1.0))
        elif "assistant" in ev:
            text: str = ev["assistant"]
            pace = float(ev.get("pace_ms", DEFAULT_PACE_MS)) / 1000.0
            duration_s += len(text) * pace + float(ev.get("pause_s", 0.4))
            assistant_chars += len(text)
        elif "tool_call" in ev:
            duration_s += float(ev.get("pause_s", 0.5))
        elif "tool_result" in ev:
            duration_s += float(ev.get("pause_s", 0.3))
        elif "pause" in ev:
            duration_s += float(ev["pause"])
    return {"duration_s": duration_s, "assistant_chars": assistant_chars}


def event_matches(event: dict, claim: dict) -> bool:
    kind = claim.get("kind")
    if kind == "tool_call":
        if "tool_call" not in event:
            return False
        call = event["tool_call"]
        if claim.get("name") and call.get("name") != claim["name"]:
            return False
        args_contain = claim.get("args_contain", {})
        if args_contain:
            args = call.get("args", {})
            for k, want in args_contain.items():
                got = str(args.get(k, ""))
                if str(want) not in got:
                    return False
        return True

    if kind == "assistant":
        if "assistant" not in event:
            return False
        contains = claim.get("contains")
        if contains and contains not in event["assistant"]:
            return False
        return True

    if kind in {"shell", "output", "narration", "prompt"}:
        if kind not in event:
            return False
        contains = claim.get("contains")
        if contains and contains not in event[kind]:
            return False
        return True

    return False


def check_assertions(session_path: Path, assertions_path: Path) -> list[str]:
    events = load_session(session_path)
    claims = parse_assertions(assertions_path)
    errors: list[str] = []

    metrics = derive_metrics(events)
    min_dur = claims.get("min_duration_s")
    if min_dur is not None and metrics["duration_s"] < float(min_dur):
        errors.append(
            f"{session_path}: rendered duration {metrics['duration_s']:.1f}s < "
            f"min_duration_s={min_dur}"
        )
    min_chars = claims.get("min_assistant_chars")
    if min_chars is not None and metrics["assistant_chars"] < int(min_chars):
        errors.append(
            f"{session_path}: assistant text {metrics['assistant_chars']} chars < "
            f"min_assistant_chars={min_chars}"
        )

    slug_expected = claims.get("slug")
    slug_actual = session_path.parent.name
    if slug_expected and slug_expected != slug_actual:
        errors.append(
            f"{assertions_path}: slug field '{slug_expected}' does not match "
            f"directory name '{slug_actual}'"
        )

    cursor = 0
    for claim in claims.get("expect", []):
        found = False
        for idx in range(cursor, len(events)):
            if event_matches(events[idx], claim):
                cursor = idx + 1
                found = True
                break
        if not found:
            errors.append(
                f"{session_path}: unmet expectation (or out of order): {claim}"
            )

    return errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "demos",
        nargs="+",
        type=Path,
        help="One or more demo directories containing session.jsonl + assertions.yml",
    )
    args = parser.parse_args(argv)

    all_errors: list[str] = []
    checked = 0
    for demo_dir in args.demos:
        session = demo_dir / "session.jsonl"
        assertions = demo_dir / "assertions.yml"
        if not assertions.is_file():
            continue
        if not session.is_file():
            all_errors.append(f"{demo_dir}: assertions.yml present but session.jsonl missing")
            continue
        all_errors.extend(check_assertions(session, assertions))
        checked += 1

    if all_errors:
        for e in all_errors:
            print(e, file=sys.stderr)
        return 1

    print(f"checked {checked} demo assertion file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
