# Beads Usage

Use native upstream Beads only.

## Review Epic

```bash
bd create "HELIX alignment review: <scope>" \
  --type epic \
  --labels helix,phase:review,kind:review \
  --spec-id <closest-governing-artifact>
```

## Review Bead

```bash
bd create "Review <functional area>" \
  --type task \
  --parent <review-epic-id> \
  --labels helix,phase:review,kind:review,area:<area>
```

## Execution Bead

```bash
bd create "<deterministic follow-up work>" \
  --type task \
  --labels helix,phase:<phase>,kind:<kind> \
  --spec-id <closest-governing-artifact>
```

Add blockers with:

```bash
bd dep add <blocked-id> <blocker-id>
```

Use:

- `bd ready` for unblocked work
- `bd blocked` for blocked work
- `bd show <id>` for context
- `bd update <id> --claim` to claim work
- `bd close <id>` when complete
