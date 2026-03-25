# Story Build Bead Template Guidance

Story implementation work is stored as build beads, not as markdown
implementation plans.

Use upstream Beads via `bd create`, `bd update`, `bd dep add`, and `bd ready`.
See `workflows/helix/BEADS.md`.

## Required Story Build Bead Mapping

- native upstream `type: task`
- labels:
  - `helix`
  - `phase:build`
  - `kind:build`
  - `story:US-XXX`
- governing references in `spec-id` and/or description to:
  - `docs/helix/01-frame/user-stories/US-{XXX}-*.md`
  - `docs/helix/02-design/technical-designs/TD-{XXX}-*.md`
  - `docs/helix/03-test/test-plans/TP-{XXX}-*.md`
  - `docs/helix/04-build/implementation-plan.md`
- implementation notes in `description` / `design`
- verification contract in `acceptance`
- blockers in dependency links rather than a custom blocked field

## Queue Check

Use `bd ready` to pick the next executable build bead. Confirm the bead carries
the labels `helix`, `phase:build`, and `story:US-{story-id}`, then inspect it
with `bd show <id>` before implementing.

## Sizing Rule

Split the story into multiple beads if any of the following are true:

- one bead would touch unrelated components
- one bead would take more than one focused implementation session
- one bead would require independent review or rollout sequencing
- one bead would mix feature work with cleanup or refactoring
