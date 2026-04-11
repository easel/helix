#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DIGEST_PATTERN = re.compile(r"<context-digest>\s*.*?</context-digest>", re.DOTALL)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate that open HELIX beads carry a context digest."
    )
    parser.add_argument(
        "--tracker",
        default=".ddx/beads.jsonl",
        help="Tracker JSONL path (default: .ddx/beads.jsonl).",
    )
    parser.add_argument(
        "--status",
        action="append",
        default=[],
        help="Status to validate (repeatable, default: open).",
    )
    args = parser.parse_args()

    tracker_path = Path(args.tracker)
    statuses = set(args.status or ["open"])
    missing: list[tuple[int, str, str]] = []

    for line_number, raw_line in enumerate(
        tracker_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line.strip():
            continue
        bead = json.loads(raw_line)
        if bead.get("status") not in statuses:
            continue
        labels = bead.get("labels", [])
        if "helix" not in labels:
            continue
        description = bead.get("description") or ""
        if DIGEST_PATTERN.search(description):
            continue
        missing.append((line_number, bead.get("id", "<unknown>"), bead.get("title", "")))

    if missing:
        for line_number, bead_id, title in missing:
            print(
                f"{tracker_path}:{line_number}: bead {bead_id} is missing <context-digest>: {title}",
                file=sys.stderr,
            )
        print(
            f"validated context digests on 0 bead(s): {len(missing)} missing",
            file=sys.stderr,
        )
        return 1

    print(f"validated context digests on open HELIX bead(s) in {tracker_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
