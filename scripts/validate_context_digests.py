#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DIGEST_PATTERN = re.compile(r"<context-digest>\s*.*?</context-digest>", re.DOTALL)


def review_finding_missing_area(labels: list[str]) -> bool:
    return "review-finding" in labels and not any(
        label.startswith("area:") for label in labels
    )


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
    missing_digest: list[tuple[int, str, str]] = []
    missing_review_area: list[tuple[int, str, str]] = []

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
        if review_finding_missing_area(labels):
            missing_review_area.append(
                (line_number, bead.get("id", "<unknown>"), bead.get("title", ""))
            )
        description = bead.get("description") or ""
        if DIGEST_PATTERN.search(description):
            continue
        missing_digest.append(
            (line_number, bead.get("id", "<unknown>"), bead.get("title", ""))
        )

    if missing_digest or missing_review_area:
        for line_number, bead_id, title in missing_digest:
            print(
                f"{tracker_path}:{line_number}: bead {bead_id} is missing <context-digest>: {title}",
                file=sys.stderr,
            )
        for line_number, bead_id, title in missing_review_area:
            print(
                f"{tracker_path}:{line_number}: review-finding bead {bead_id} is missing area:* label(s): {title}",
                file=sys.stderr,
            )
        print(
            "validated context digests on 0 bead(s): "
            f"{len(missing_digest)} missing digest(s), "
            f"{len(missing_review_area)} review-finding bead(s) missing area labels",
            file=sys.stderr,
        )
        return 1

    print(f"validated context digests on open HELIX bead(s) in {tracker_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
