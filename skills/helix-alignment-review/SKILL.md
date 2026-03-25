---
name: helix-alignment-review
description: Top-down reconciliation review of a HELIX project. Use for alignment audits, drift analysis, traceability checks, or generating remediation beads.
argument-hint: "[scope]"
---

# HELIX Alignment Review

Use this skill for repo-wide or area-scoped reconciliation reviews.

## When To Use

- the user asks for an alignment review, reconciliation, traceability audit, or drift analysis
- the project uses HELIX artifacts or a similar planning stack
- the user wants deterministic follow-up work in upstream Beads (`bd`)
- the review should produce one durable consolidated report plus ephemeral review/execution beads

## Startup

Reference docs:

- `workflows/helix/actions/reconcile-alignment.md`
- `workflows/helix/templates/alignment-review.md`
- `workflows/helix/BEADS.md`

## Core Rules

- Review top-down, not code-first.
- Planning intent comes from canonical artifacts, not from implementation.
- Use the HELIX authority order from the references.
- Use native upstream Beads only: `bd` (or `br`) issues, parents, dependencies, `spec-id`, and labels.
- Create or reconcile one review epic plus one review bead per functional area.
- Create execution beads only after the consolidated report exists.

## Output Model

Produce:

1. Upstream review epic in `bd`
2. Upstream review beads in `bd`
3. Durable report at `docs/helix/06-iterate/alignment-reviews/AR-YYYY-MM-DD[-scope].md`
4. Upstream execution beads only for approved gaps

## Required Evidence

Every non-trivial finding must cite:

- planning evidence
- implementation evidence
- a classification
- a recommended resolution direction

Use these references as needed:

- [review-flow.md](references/review-flow.md)
- [alignment-report.md](references/alignment-report.md)
- [beads.md](references/beads.md)
