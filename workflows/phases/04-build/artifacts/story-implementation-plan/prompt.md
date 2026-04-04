# Story Build Issue Generation

## Required Inputs
- `docs/helix/03-test/test-plans/TP-{XXX}-*.md`
- `docs/helix/02-design/technical-designs/TD-{XXX}-*.md`
- `docs/helix/04-build/implementation-plan.md`

## Produced Output
- one or more tracker issues labeled `helix`, `phase:build`, `story:US-{XXX}`

Create scoped build issues for one story. Each issue should be a deterministic TDD task that makes a specific set of failing tests pass with minimal files, explicit dependencies, and clear verification steps.

Use mapping guidance at `workflows/phases/04-build/artifacts/story-implementation-plan/template.md`.
For tracker conventions see `helix tracker --help`.
