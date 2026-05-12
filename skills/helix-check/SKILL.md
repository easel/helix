---
name: helix-check
description: Decide the next safe HELIX action when execution work is exhausted or ambiguous.
argument-hint: "[scope]"
disable-model-invocation: true
---

# Check

Check evaluates the current planning and execution state and returns the next
safe action. It is a decision action, not an implementation action.

## Methodology

1. Use `$ARGUMENTS` as the scope when provided, otherwise default to repo scope.
2. Inspect the current work queue, governing artifacts, and known blockers.
3. Decide conservatively whether the next action is build, design, alignment,
   backfill, wait, guidance, or stop.
4. Prefer waiting or asking for guidance over unsafe execution.
5. If the check reveals missing tracked work, create explicit work items before
   returning the decision.
6. Return a machine-readable decision marker and the next recommended command
   or operator action.

## Constraints

- Do not guess past missing evidence.
- Do not dispatch implementation, alignment, or backfill silently.
- Do not leave durable work only as prose suggestions.
- Make blockers explicit enough for the next operator or agent to continue.

## Output

Return the exact next-action line expected by the surrounding runtime, plus the
next command or clarification question.

## Running with DDx

When DDx supplies the runtime, read and apply:

- `.ddx/plugins/helix/workflows/actions/check.md`

DDx-specific hand-off rule:

- If the check reveals work that should be tracked, such as stale artifacts,
  missing designs, or untracked blockers, file beads via `ddx bead create`
  before returning the `NEXT_ACTION` code. The ready queue is the durable
  hand-off; prose suggestions without beads are lost between sessions.
