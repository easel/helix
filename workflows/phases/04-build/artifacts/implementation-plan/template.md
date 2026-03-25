---
dun:
  id: helix.implementation-plan
  depends_on:
    - helix.test-plan
---
# Build Plan

**Project**: [Project Name]
**Date**: [Date]
**Status**: Draft | Approved

## Scope and Authority

**Purpose**: Define the canonical build strategy for the current implementation cycle.

**Governing Artifacts**:
- [docs/helix/01-frame/...]
- [docs/helix/02-design/...]
- [docs/helix/03-test/...]

**Out of Scope**:
- Story-level task tracking
- Deployment execution details
- Backlog prioritization for future iterations

## Build Objectives

- [Objective 1]
- [Objective 2]
- [Objective 3]

## Shared Constraints

- [Constraint from requirements or design]
- [Constraint from architecture or tests]
- [Operational or security constraint]

## Build Sequencing

| Order | Story / Area | Governing Artifacts | Depends On | Notes |
|------|---------------|---------------------|------------|-------|
| 1 | [US-XXX or area] | [TP/TD refs] | None | [Why first] |
| 2 | [US-XXX or area] | [TP/TD refs] | [Dependency] | [Why next] |

## Build Bead Strategy

Story-level execution work is tracked as upstream Beads issues in `.beads/`.

**Beads Tool**:
`bd`

**Required Labels Per Build Bead**:
- `helix`
- `phase:build`
- `kind:build`
- `story:US-{story-id}`

**Required References Per Build Bead**:
- User Story
- Technical Design
- Story Test Plan
- This build plan

**Required Native Fields**:
- `type: task` unless there is a strong reason to use another native upstream type
- `spec-id` pointing at the nearest governing artifact
- dependency links for blockers rather than a custom blocked field

### Planned Bead Decomposition

| Story / Area | Build Bead Labels / Query | Goal | Dependencies |
|--------------|--------------------|------|--------------|
| [US-XXX] | `helix`, `phase:build`, `story:US-XXX` | [Outcome] | [Deps] |
| [US-YYY] | `helix`, `phase:build`, `story:US-YYY` | [Outcome] | [Deps] |

## Integration Checkpoints

- [Checkpoint 1]
- [Checkpoint 2]
- [Checkpoint 3]

## Quality Gates

- [ ] Failing tests exist before implementation starts
- [ ] Build beads cite their governing artifacts
- [ ] All required tests pass before closing a build bead
- [ ] Behavior changes trigger required canonical document updates
- [ ] Code review is completed before phase exit

## Risks and Escalation

| Risk | Impact | Trigger | Response |
|------|--------|---------|----------|
| [Risk] | [High/Med/Low] | [Trigger] | [Refine / escalate / split bead] |

## Exit Criteria

- [ ] Build bead set is defined
- [ ] Sequence and dependencies are approved
- [ ] Shared constraints are documented
- [ ] Verification expectations are explicit
