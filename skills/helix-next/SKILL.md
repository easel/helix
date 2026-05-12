---
name: helix-next
description: Show the recommended next HELIX work item without starting execution.
disable-model-invocation: true
---

# Next

Show the recommended next work item from the project tracker. This is an
orientation skill, not an execution skill.

## Methodology

1. Inspect the ready work set for the current scope.
2. Prefer work that is unblocked, execution-ready, and highest priority.
3. Explain why the selected item is next.
4. If no work is ready, say so plainly and point to the appropriate check or
   planning action.

## Output

- recommended work item ID and title when available
- short rationale
- blocker or next planning action when no work is ready

## Running with DDx

The current wrapper command is:

```bash
helix next
```

If no issue is ready, point to:

```bash
helix check
ddx bead ready
```
