---
name: grind
description: Continuous bead queue execution with sub-agents. Use when the user wants sustained forward progress on the beads queue.
disable-model-invocation: true
---

# Grind

You are running a continuous execution loop against the beads queue.

## Objective

Make steady forward progress by reviewing the queue, picking the best work,
and executing it. Do not stop iterating unless there is no actionable work
remaining.

## Execution discipline

1. **Review the queue** — run `bd ready` (or `br ready`) to see available work.
   Understand the current state of the queue, blockers, and dependencies.

2. **Pick the best work** — choose the highest-impact actionable bead. Do not
   default to the easiest or lowest-priority item. If a high-priority bead is
   blocked, consider whether unblocking it is the real best work.

3. **Use sub-agents** — delegate implementation work to sub-agents to preserve
   your context window for queue management and decision-making.

4. **Maintain alignment** — check that bead work stays aligned with the
   governing specs and planning artifacts. If you identify drift, adjust bead
   descriptions, add new beads, or fix dependencies.

5. **Measure progress** — after each bead, confirm that forward progress was
   made. If a bead completed without meaningful change, investigate why.

6. **Capture follow-on work** — if implementation reveals new work, create
   beads for it immediately. Do not absorb undocumented scope.

7. **Commit and close** — ensure all tests and checks pass before closing a
   bead. Commit with clear traceability to the bead ID.

## When to stop

- No ready beads remain and no blocked beads can be unblocked
- A decision or guidance from the user is required
- The queue needs restructuring that requires user input
