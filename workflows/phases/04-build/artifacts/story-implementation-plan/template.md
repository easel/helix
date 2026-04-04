# Story Build Issue Guidance

Story implementation work is tracked as build issues, not markdown plans.

Use `helix tracker create`, `helix tracker update`, and `helix tracker ready`.
See `helix tracker --help` for tracker conventions.

## Required Issue Fields

- Type: `task`
- Labels: `helix`, `phase:build`, `kind:build`, `story:US-XXX`
- `spec-id` and/or description references to:
  - `docs/helix/01-frame/user-stories/US-{XXX}-*.md`
  - `docs/helix/02-design/technical-designs/TD-{XXX}-*.md`
  - `docs/helix/03-test/test-plans/TP-{XXX}-*.md`
  - `docs/helix/04-build/implementation-plan.md`
- Implementation notes in `description` / `design`
- Verification contract in `acceptance`
- Blockers as dependency links

## Queue Check

Use `helix tracker ready` to pick the next executable issue. Confirm labels, then inspect with `helix tracker show <id>` before implementing.

## Sizing Rule

Split a story into multiple issues if any single issue would:
- touch unrelated components
- take more than one focused implementation session
- require independent review or rollout sequencing
- mix feature work with cleanup or refactoring
