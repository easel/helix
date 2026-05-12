---
name: helix-review
description: Run a HELIX fresh-eyes review after implementation or for a requested scope.
argument-hint: "[scope]"
---

# Review

Run a fresh-eyes review focused on bugs, regressions, missing tests, and
follow-on work. Findings come first; summaries are secondary.

## Methodology

1. Scope the review to `$ARGUMENTS` when provided, otherwise review the recent
   implementation work.
2. Inspect the governing artifacts, changed implementation, tests, and public
   projection relevant to the scope.
3. Prioritize concrete correctness issues, behavioral regressions, missing
   tests, and follow-on work.
4. Report findings with evidence and severity before any overview.
5. If the work is clean, say so briefly and identify residual risks or testing gaps.
6. Create durable follow-up work for actionable medium-or-higher findings.

## Output

- findings first
- concrete evidence
- filed follow-up work for actionable findings
- trailer lines: `REVIEW_STATUS`, `ISSUES_COUNT`, `FINDINGS_FILED`,
  `AGENTS_MD_UPDATED`, `LEARNINGS_FILED`

## Running with DDx

When DDx supplies the HELIX runtime, read and apply:

- `.ddx/plugins/helix/workflows/actions/fresh-eyes-review.md`

DDx-specific follow-up policy:

- Every actionable follow-up with critical, high, or medium severity must be
  filed as a tracker bead via `ddx bead create` before the review closes.
- Do not close the review with prose suggestions that have no corresponding
  bead; the ready queue is the durable hand-off mechanism between review and
  execution.
- See the "Filing Findings as Tracker Issues" section in `.ddx/plugins/helix/workflows/actions/fresh-eyes-review.md` for the exact bead format.
