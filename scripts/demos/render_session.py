#!/usr/bin/env python3
"""Render a HELIX demo session.jsonl into an asciinema v2 cast.

Session record format (each line is a JSON object):

    {"meta": {"title": "...", "width": 100, "height": 30, "scenario": "align"}}
    {"narration": "What's happening at this point"}
    {"shell": "$ helix --version"}
    {"output": "helix 0.4.0\\n"}
    {"prompt": "User typed input to the agent"}
    {"assistant": "Agent reply text", "pace_ms": 30}
    {"tool_call": {"name": "Read", "args": {"file_path": "..."}}}
    {"tool_result": "trimmed result text", "lines": 5}
    {"pause": 1.5}

The first line MUST be a `meta` event. Other event types may appear in any
order; timing accumulates monotonically.

The renderer is deterministic — timing comes from event fields, not wall
clock — so the same session.jsonl always produces the same .cast.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Iterable

CAST_VERSION = 2
DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 30
DEFAULT_ASSISTANT_PACE_MS = 25
DEFAULT_SHELL_PROMPT_PAUSE_S = 0.4
DEFAULT_NARRATION_PAUSE_S = 1.0
DEFAULT_TOOL_CALL_PAUSE_S = 0.5
DEFAULT_TOOL_RESULT_PAUSE_S = 0.3


def crlf(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\n", "\r\n")


def emit(events: list, t: float, payload: str) -> None:
    events.append([round(t, 6), "o", payload])


def render(session_path: Path) -> tuple[dict, list]:
    lines = [
        line for line in session_path.read_text(encoding="utf-8").splitlines() if line.strip()
    ]
    if not lines:
        raise SystemExit(f"{session_path}: empty session")

    first = json.loads(lines[0])
    meta = first.get("meta")
    if not meta:
        raise SystemExit(f"{session_path}: first event must be a `meta` block")

    header = {
        "version": CAST_VERSION,
        "width": meta.get("width", DEFAULT_WIDTH),
        "height": meta.get("height", DEFAULT_HEIGHT),
        "timestamp": meta.get("timestamp", int(time.time())),
        "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"},
        "title": meta.get("title", "HELIX Demo"),
    }

    events: list = []
    t = 0.0

    # ANSI: bold + dim styles
    GREEN_BOLD = "\x1b[1;32m"
    CYAN = "\x1b[36m"
    DIM = "\x1b[2m"
    RESET = "\x1b[0m"

    for raw in lines[1:]:
        if not raw.strip():
            continue
        event = json.loads(raw)

        if "narration" in event:
            text = event["narration"]
            banner = f"\r\n{DIM}# {text}{RESET}\r\n"
            emit(events, t, banner)
            t += event.get("pause_s", DEFAULT_NARRATION_PAUSE_S)

        elif "shell" in event:
            command = event["shell"]
            emit(events, t, f"\r\n{GREEN_BOLD}{command}{RESET}\r\n")
            t += event.get("pause_s", DEFAULT_SHELL_PROMPT_PAUSE_S)

        elif "output" in event:
            emit(events, t, crlf(event["output"]))
            t += event.get("pause_s", 0.1)

        elif "prompt" in event:
            user_text = event["prompt"]
            emit(events, t, f"\r\n{CYAN}> {user_text}{RESET}\r\n")
            t += event.get("pause_s", DEFAULT_NARRATION_PAUSE_S)

        elif "assistant" in event:
            text = event["assistant"]
            pace = event.get("pace_ms", DEFAULT_ASSISTANT_PACE_MS) / 1000.0
            # Type out one character at a time
            for ch in text:
                emit(events, t, crlf(ch))
                t += pace
            # Trailing newline if not present
            if not text.endswith("\n"):
                emit(events, t, "\r\n")
            t += event.get("pause_s", 0.4)

        elif "tool_call" in event:
            call = event["tool_call"]
            name = call.get("name", "Tool")
            args = call.get("args", {})
            summary = ", ".join(f"{k}={v!r}" for k, v in args.items())
            emit(
                events,
                t,
                f"{DIM}  ⚙ {name}({summary}){RESET}\r\n",
            )
            t += event.get("pause_s", DEFAULT_TOOL_CALL_PAUSE_S)

        elif "tool_result" in event:
            text = event["tool_result"]
            line_count = event.get("lines")
            if line_count:
                emit(events, t, f"{DIM}  → {line_count} lines{RESET}\r\n")
            elif text:
                emit(events, t, f"{DIM}  → {crlf(text)}{RESET}\r\n")
            t += event.get("pause_s", DEFAULT_TOOL_RESULT_PAUSE_S)

        elif "pause" in event:
            t += float(event["pause"])

        else:
            raise SystemExit(f"{session_path}: unknown event keys: {list(event.keys())}")

    return header, events


def write_cast(out_path: Path, header: dict, events: list) -> None:
    with out_path.open("w", encoding="utf-8") as f:
        f.write(json.dumps(header) + "\n")
        for ev in events:
            f.write(json.dumps(ev) + "\n")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("session", type=Path, help="Path to session.jsonl")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output .cast path (default: alongside session, named after directory)",
    )
    args = parser.parse_args(argv)

    session_path: Path = args.session
    if not session_path.is_file():
        print(f"error: {session_path} not found", file=sys.stderr)
        return 1

    out_path: Path = args.output or (
        session_path.parent.parent.parent.parent
        / "website"
        / "static"
        / "demos"
        / f"{session_path.parent.name}.cast"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    header, events = render(session_path)
    write_cast(out_path, header, events)
    duration = events[-1][0] if events else 0.0
    print(
        f"rendered {session_path.parent.name}: {len(events)} events, "
        f"{duration:.1f}s → {out_path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
