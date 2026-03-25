# HELIX Action: Polish Beads

You are performing iterative bead refinement before implementation begins.

"Check your beads N times, implement once."

Your goal is to improve bead quality through multiple refinement passes:
deduplication, coverage verification against the plan, acceptance criteria
sharpening, dependency correction, and convergence detection. This front-loaded
investment prevents expensive rework during implementation.

## Action Input

You may receive:

- no argument (default: all open beads)
- a scope such as `auth`, `FEAT-003`, `phase:build`
- `--rounds N` controlling maximum refinement passes (default: 6)

Examples:

- `helix polish`
- `helix polish auth`
- `helix polish --rounds 10 FEAT-003`

## Beads Rules

Use native upstream Beads only. Follow:

- `workflows/BEADS.md`
- <https://github.com/steveyegge/beads>
- <https://steveyegge.github.io/beads/>

Do not create custom HELIX bead files.

## PHASE 0 - Load Current State

0. **Context Recovery**: Re-read AGENTS.md so project instructions are fresh
   in your working memory. After long sessions, context compaction may have
   dropped critical project rules. This step is cheap insurance against drift.
1. Verify upstream Beads is available.
   - If live `bd` access is missing or unhealthy, stop immediately.
2. Load all open beads for the scope.
   - `bd list --status open --json`
   - `bd list --status in_progress --json` (if relevant to scope)
3. Load the governing plan document if one exists.
   - Check `docs/helix/02-design/plan-*.md` for the scope
   - Check other planning artifacts (PRD, feature specs, architecture docs)
4. Record initial bead count and state as the baseline.

## PHASE 1 through N - Refinement Passes

Each pass performs ALL of the following checks. Track changes made per pass.

### Deduplication

- Find beads with overlapping scope, description, or acceptance criteria.
- Merge duplicates into a single canonical bead that preserves the strongest
  elements of each.
- When merging, preserve all dependency relationships from both beads.
- Close the redundant bead with a note pointing to the canonical one.

### Plan Coverage Verification

- If a plan document exists, verify every section has at least one bead.
- If a section has no bead, create one with proper labels, spec-id, and
  acceptance criteria derived from the plan.
- If a bead exists but doesn't map to any plan section, flag it for review.

### Acceptance Criteria Sharpening

- Replace vague criteria with testable statements.
  - Bad: "auth should work correctly"
  - Good: "login with valid credentials returns 200 and a JWT; login with
    invalid credentials returns 401 with error code AUTH_INVALID"
- Ensure every bead has at least one concrete acceptance criterion.
- Add verification method: what command or test proves this criterion is met?

### Dependency Verification

- Verify dependency chains are correct: if bead A depends on bead B, does B
  actually produce what A needs?
- Look for missing dependencies: does this bead assume work that hasn't been
  captured as a dependency?
- Look for circular dependencies and break them.
- Verify `spec-id` points to the correct governing artifact.

### Sizing

- Flag beads that are too large for a single bounded implementation pass.
  A bead is too large if it touches more than 3 files in different subsystems
  or requires more than one architectural decision.
- Split oversized beads into smaller, independently verifiable slices.
- Preserve the dependency ordering when splitting.

### Label Hygiene

- Ensure every bead has the `helix` label.
- Ensure every bead has exactly one phase label (`phase:build`, `phase:deploy`,
  or `phase:iterate`).
- Ensure area labels are present where applicable.
- Ensure `kind:*` labels match the bead's actual type.

## Convergence Detection

Track a change count per round: number of beads modified, created, or merged.

When change count drops below 3 for two consecutive rounds, declare convergence
and stop refinement.

If max rounds is reached without convergence, report the current state and
recommend additional rounds or user guidance.

## Output

Report a summary of all modifications made across rounds, then these trailer
lines:

```
POLISH_STATUS: CONVERGED|IN_PROGRESS
POLISH_ROUNDS: N
BEADS_MODIFIED: count
BEADS_CREATED: count
BEADS_MERGED: count
```

- `CONVERGED`: change velocity dropped below threshold
- `IN_PROGRESS`: max rounds reached but velocity still above threshold
