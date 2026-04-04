# Story Deploy Issue Template Guidance

Story deployment work is stored as deploy issues, not markdown deployment plans.

Use `ddx bead create`, `ddx bead update`, and `ddx bead ready`.
See `ddx bead --help` for tracker conventions.

## Required Story Deploy Issue Mapping

- `type: task`
- labels: `helix`, `phase:deploy`, `kind:deploy`, `story:US-XXX`
- references to dependent build issue(s) and the governing deploy artifacts in `spec-id` or description
- rollout steps in `description` or `design`
- rollback triggers and verification in `acceptance`
- blockers expressed as dependencies

## Queue Check

Use `ddx bead ready` to pick the next deploy issue, then inspect it with
`ddx bead show <id>` before rollout work.
