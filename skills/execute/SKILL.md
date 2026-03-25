---
name: execute
description: Pick the next bead, implement it, pass tests, commit, and close it. Use when the user wants one bead executed end-to-end.
argument-hint: "[bead-id|scope]"
disable-model-invocation: true
---

# Execute

Pick the next bead from the queue, implement it fully, and close it.

If a specific bead or scope is given, use: $ARGUMENTS

## Steps

1. **Identify the next bead** — run `bd ready` (or `br ready`). Pick the
   highest-priority actionable bead with clear governing artifacts.

2. **Claim it** — `bd update <id> --claim` (or `br update <id> --status in_progress`).

3. **Load context** — read the governing artifacts referenced by the bead's
   spec-id and description. Understand what "done" means from the acceptance
   criteria.

4. **Implement** — write the code, docs, or config changes needed to satisfy
   the bead. Stay within scope. Do not add unspecified functionality.

5. **Verify** — run the project's test suite and quality checks. Ensure:
   - All relevant tests pass
   - No previously passing checks now fail
   - Test coverage improves or stays stable
   - Lint, format, and static analysis gates pass

6. **Commit** — create a commit with:
   - Bead ID in the message
   - Concise summary of what was done
   - Reference to governing artifacts

7. **Close** — `bd close <id>` (or `br close <id>`).

8. **Capture follow-on work** — if implementation revealed additional work,
   create new beads for it. Do not silently absorb extra scope.
