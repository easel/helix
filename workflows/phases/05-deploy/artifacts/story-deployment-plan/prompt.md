# Story Deploy Bead Generation

## Required Inputs
- upstream build bead issue(s) labeled `helix`, `phase:build`, `story:US-{XXX}`
- `docs/helix/05-deploy/deployment-checklist.md` - Project deployment readiness
- `docs/helix/05-deploy/monitoring-setup.md` - Monitoring requirements
- `docs/helix/05-deploy/runbook.md` - Operational procedures

## Produced Output
- one or more upstream `bd` issues labeled `helix`, `phase:deploy`, `story:US-{XXX}`

## Prompt

You are creating deploy beads for a specific user story. Your goal is to define
scoped rollout work that safely moves already-built functionality through the
deployment process.

Each deploy bead must:

1. Reference the governing deploy artifacts and the build bead(s) it depends on
2. Define a rollout objective and rollback trigger
3. Specify monitoring and verification steps
4. Stay small enough to execute and close independently

Use the mapping guidance at:
`workflows/phases/05-deploy/artifacts/story-deployment-plan/template.md`

Use upstream Beads guidance at:
`workflows/BEADS.md`

## Completion Criteria
- [ ] Every story rollout task is captured by one or more deploy beads
- [ ] Rollback and monitoring checks are explicit
- [ ] Dependencies on build beads are explicit
