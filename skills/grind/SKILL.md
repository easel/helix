---
name: grind
description: Continuous issue queue execution with sub-agents. Use when the user wants sustained forward progress on the issue queue.
disable-model-invocation: true
---

# Grind

You are running a continuous execution loop against the issue queue.

## Objective

Make steady forward progress by reviewing the queue, picking the best work,
and executing it. Do not stop iterating unless there is no actionable work
remaining.

## Execution discipline

1. **Review the queue** — run `helix tracker ready` to see available work.
   Understand the current state of the queue, blockers, and dependencies.

2. **Pick the best work** — choose the highest-impact actionable issue. Do not
   default to the easiest or lowest-priority item. If a high-priority issue is
   blocked, consider whether unblocking it is the real best work.

3. **Use sub-agents** — delegate implementation work to sub-agents to preserve
   your context window for queue management and decision-making.

4. **Maintain alignment** — check that issue work stays aligned with the
   governing specs and planning artifacts. If you identify drift, adjust issue
   descriptions, add new issues, or fix dependencies.

5. **Measure progress** — after each issue, confirm that forward progress was
   made. If an issue completed without meaningful change, investigate why.

6. **Capture follow-on work** — if implementation reveals new work, create
   issues for it immediately. Do not absorb undocumented scope.

7. **Commit and close** — ensure all tests and checks pass before closing an
   issue. Commit with clear traceability to the issue ID.

## When to stop

- No ready issues remain and no blocked issues can be unblocked
- A decision or guidance from the user is required
- The queue needs restructuring that requires user input
