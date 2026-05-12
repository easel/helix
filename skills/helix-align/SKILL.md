---
name: helix-align
description: Run a HELIX alignment review that reconciles downstream work against governing artifacts.
argument-hint: "[scope]"
---

# Align

Use this skill for repo-wide or area-scoped reconciliation reviews. Alignment
checks whether implementation, tests, plans, and public documentation still
match the highest-authority HELIX artifacts.

The methodology is substrate-neutral: produce one durable alignment report,
classify gaps, and create explicit follow-up work in the project's chosen work
tracking system.

## When To Use

- the user asks for an alignment review, reconciliation, traceability audit, or drift analysis
- product, requirements, design, or implementation artifacts may disagree
- functionality changes imply upstream specification or design reconciliation
- a release or public documentation update needs confidence that the artifact stack is coherent
- review findings need durable follow-up work rather than conversational notes

## Methodology

1. **Start from authority.** Read the highest-authority artifacts first:
   product vision, requirements, feature specifications, architecture,
   decisions, designs, test plans, and then implementation.
2. **Scope the review.** Use the provided scope when present; otherwise review
   the repo or product area that changed.
3. **Classify each finding.** Use explicit classifications such as aligned,
   stale, incomplete, divergent, or blocked.
4. **Write one durable report.** Capture evidence, classification, impact, and
   recommended resolution direction in a stable alignment-review artifact.
5. **Create follow-up work.** Every non-aligned gap needs at least one tracked
   work item before the review is considered complete.
6. **Preserve ordering.** If gaps depend on each other, encode that ordering in
   the work tracker rather than relying on prose.

## Required Evidence

Every non-trivial finding must cite:

- planning evidence
- implementation or projection evidence
- classification
- recommended resolution direction

## Output Model

Produce:

1. One governing alignment-review work item for the pass
2. Optional review-area work items for large scopes
3. A durable report at `docs/helix/06-iterate/alignment-reviews/AR-YYYY-MM-DD[-scope].md`
4. Follow-up work items for every non-aligned gap

## Running with DDx

When the project uses DDx as its HELIX runtime, use the packaged workflow and
tracker surfaces directly.

Reference docs:

- `.ddx/plugins/helix/workflows/actions/reconcile-alignment.md`
- `.ddx/plugins/helix/workflows/templates/alignment-review.md`
- Tracker conventions: `ddx bead --help` (DDx FEAT-004)

DDx-specific rules:

- Use the built-in tracker only: `ddx bead` issues, parents, dependencies, `spec-id`, and labels.
- Before writing the report or filing follow-on issues, create or claim the governing `kind:planning,action:align` bead for this pass.
- Create or reconcile one review epic plus one review issue per functional area.
- Create execution issues only after the consolidated report exists.
- If follow-on work has real ordering constraints, encode them with parents and `ddx bead dep add` rather than prose.
- See Phase 7 (Execution Issues) and Issue Coverage Verification in `.ddx/plugins/helix/workflows/actions/reconcile-alignment.md` for the exact rules and format.

Skill-local references:

- [review-flow.md](references/review-flow.md)
- [alignment-report.md](references/alignment-report.md)
- [tracker.md](references/tracker.md)
