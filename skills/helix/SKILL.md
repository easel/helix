---
name: helix-workflow
description: HELIX test-first workflow with authority-ordered planning stack and Beads execution tracking. Use when working through Frame/Design/Test/Build/Deploy/Iterate phases, executing beads, or aligning implementation to specs.
argument-hint: "[scope|bead-id]"
---

# HELIX Workflow Skill

Guide development using the HELIX methodology: a test-first workflow with a
canonical planning stack and an execution layer tracked in upstream Beads
(`bd`).

## Use This Skill When

- the user is building or refining a feature under HELIX
- the repo has `docs/helix/` or `workflows/helix/`
- the user wants TDD phase guidance or artifact sequencing
- the user wants implementation kept aligned to requirements, design, and tests
- the user wants a ready HELIX bead executed end-to-end with the right quality gates
- the user wants to know whether more HELIX work remains or what the next action should be
- the user wants a repo-wide reconciliation, drift analysis, or traceability audit
- the user wants to backfill HELIX documentation from an existing repo or subsystem

For alignment review, documentation backfill, or other cross-phase repo work, read:

- [cross-phase-actions.md](references/cross-phase-actions.md)

The separate `helix-alignment-review` skill remains available as a narrower
specialist alias for review-heavy requests.

## HELIX Phases

`FRAME -> DESIGN -> TEST -> BUILD -> DEPLOY -> ITERATE`

- `Frame`: define the problem, users, requirements, and acceptance criteria
- `Design`: define architecture, contracts, and technical approach
- `Test`: write failing tests that specify behavior
- `Build`: implement the minimum code to make tests pass
- `Deploy`: release with monitoring and rollback readiness
- `Iterate`: learn from production and plan the next cycle

## Authority Order

When artifacts disagree, prefer:

1. Product Vision
2. Product Requirements
3. Feature Specs / User Stories
4. Architecture / ADRs
5. Solution / Technical Designs
6. Test Plans / Tests
7. Implementation Plans
8. Source Code / Build Artifacts

Tests govern build execution, but they do not override upstream requirements or
design.

## Execution Layer

HELIX uses upstream Beads (`bd`) for execution tracking.

- Use `bd` (or `br`) issues, dependencies, parents, `spec-id`, and labels.
- Do not invent custom bead files or custom status taxonomies.
- Recommended labels: `helix`, plus phase/kind/traceability labels as needed.
- See `workflows/helix/BEADS.md` for bd/br command mapping.

Reference docs (read as needed):

- `workflows/helix/README.md`
- `workflows/helix/BEADS.md`
- `workflows/helix/actions/check.md` when the user wants queue health or the next action
- `workflows/helix/actions/implementation.md` when the user wants ready work executed
- relevant phase README and artifact prompts/templates

## On Invocation

When this skill is invoked, **execute work immediately** — do not just report
status, do not just describe what you would do, do not ask for confirmation.
Start doing real work right now.

### Step 1 — Find ready beads

Run this command:

```bash
bd ready --json    # or: br ready --json
```

If no ready beads exist, skip to Step 6 (Queue Drain).

### Step 2 — Select and claim one bead

Pick the best ready bead (smallest unblocked bead with clear governing
artifacts). Inspect it:

```bash
bd show <id>
bd dep tree <id>
```

Then claim it:

```bash
bd update <id> --claim    # or: br update <id> --status in_progress
```

### Step 3 — Load context and implement

1. Read the bead's `spec-id`, parent, labels, and acceptance criteria.
2. Read the governing artifacts (requirements, design, tests) referenced by
   the bead.
3. Read `workflows/helix/actions/implementation.md` for full phase-specific
   rules (build, deploy, iterate).
4. Implement the work: write code, update docs, create follow-on beads for
   any out-of-scope work discovered.

### Step 4 — Verify

Run all project verification: tests, lint, type checks, format checks. If
verification fails, fix within scope or leave the bead open with a status note.

### Step 5 — Commit and close

1. Commit with the bead ID in the message.
2. Close the bead: `bd close <id>` (or `br close <id>`)
3. Go back to Step 1 for the next ready bead.

### Step 6 — Queue drain

When no ready beads remain, read and execute
`workflows/helix/actions/check.md` to decide what happens next. That action
produces a `NEXT_ACTION` code:

- `IMPLEMENT` → go to Step 1
- `ALIGN` → read and execute `workflows/helix/actions/reconcile-alignment.md`
- `BACKFILL` → read and execute `workflows/helix/actions/backfill-helix-docs.md`
- `WAIT` / `GUIDANCE` → report what is blocking and stop
- `STOP` → report that no actionable work remains

### Scope narrowing

If the user provides a scope or selector (e.g., a bead ID, feature name, or
phase), narrow all steps to that scope.

## How To Work

1. Identify the current phase from the docs and tests.
2. Do the minimum correct work for that phase.
3. Preserve traceability to upstream artifacts.
4. Keep Build subordinate to failing tests.
5. If implementation reveals plan drift, refine upstream artifacts explicitly.

## Core Questions

- `Frame`: what problem are we solving, for whom, and how will we know it works?
- `Design`: what structure, contracts, and constraints satisfy the requirement?
- `Test`: what failing tests prove the behavior?
- `Build`: what is the minimum implementation to make those tests pass?
- `Deploy`: how do we release safely and observe health?
- `Iterate`: what did we learn, and what follow-up work belongs in `bd`?

## Notes

- Use TDD strictly: Red -> Green -> Refactor.
- Security belongs in every phase.
- Escalate contradictions instead of patching around them in code.
- For repo-wide reconciliation or traceability work, use the alignment review flow.
- For repo-wide documentation reconstruction, use the backfill flow rather than inventing requirements from code alone.
- When the ready queue drains, use the check flow before deciding to align, backfill, wait, or stop.

### Test Phase Artifacts
- Test Plan
- Test Suites
- Security Tests

### Build Phase Artifacts
- Implementation Plan
- Secure Coding Guidelines

### Deploy Phase Artifacts
- Deployment Checklist
- Monitoring Setup
- Runbooks

### Iterate Phase Artifacts
- Metrics Dashboard
- Lessons Learned
- Improvement Backlog

## When to Use HELIX

**Good fit**:
- New products or features requiring high quality
- Mission-critical systems where bugs are expensive
- Teams practicing or adopting TDD
- AI-assisted development needing structure
- Security-sensitive applications

**Not ideal for**:
- Quick prototypes or POCs
- Simple scripts with minimal complexity
- Emergency fixes needing immediate deployment

Always enforce the test-first approach: specifications drive implementation, quality is built in from the start.
