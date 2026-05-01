---
title: "Parking Lot"
slug: parking-lot
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/parking-lot
---

## What it is

Project-level registry for deferred and future work that is kept
out of the main PRD flow. Parked artifacts remain in their normal
HELIX locations and are flagged with dun.parking_lot: true.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/parking-lot.md`

## Relationships

### Requires (upstream)

- [PRD](../prd/) — captures deferred items that arise during framing *(optional)*

### Enables (downstream)

_None._

### Informs

- [Improvement Backlog](../improvement-backlog/)

### Referenced by

- [Prd](../prd/)
- [Improvement Backlog](../improvement-backlog/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Parking Lot Prompt
Capture deferred work that should not stay in the active path.

## Focus
- Record the item, why it is deferred, and where it belongs next.
- Keep the entry short.
- Link to any relevant artifact or issue.

## Completion Criteria
- Deferred items are easy to find later.
- Nothing active is buried here.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: helix.parking-lot
  depends_on:
    - helix.prd
  parking_lot: true
---
# Parking Lot (Deferred / Future Work)

## Policy
- Out-of-scope items do not belong here.
- Deferred items must include rationale and revisit trigger.
- Any parked artifact must set `dun.parking_lot: true` in its frontmatter.

## Deferred / Future Items

### [Item Title]
- **Type**: Deferred | Future
- **Artifact Type**: Feature Spec | User Story | ADR | Solution Design | Implementation Plan | Other
- **Source**: FEAT-XXX / US-XXX / ADR-XXX / external
- **Rationale**: [Why deferred / why future]
- **Impact if Omitted**: [Risk/impact]
- **Dependencies**: [Blocked by / prerequisites]
- **Revisit Trigger**: [What must happen before reconsidering]
- **Target Phase/Milestone**: [Phase or release]

## Parked Artifacts (Links)

### [Artifact Title]
- **Artifact File**: [path to parked artifact]
- **Status**: Parking Lot (Deferred | Future)
``````

</details>

## Example

<details>
<summary>Show a worked example of this artifact</summary>

``````markdown
---
dun:
  id: helix.parking-lot
  parking_lot: true
---
# Parking Lot (Deferred / Future Work)

## Purpose
Track deferred and future work without cluttering core HELIX artifacts.

## Policy
- Out of Scope items do not belong here.
- Deferred items must include a rationale and revisit trigger.
- Future items must include a source and expected value.
- Any parked artifact must set `dun.parking_lot: true`.

## Deferred / Future Items

### Just-in-Time Provisioning for SSO
- **Type**: Deferred
- **Artifact Type**: Feature Spec
- **Source**: FEAT-042
- **Rationale**: Reduce auth scope for MVP
- **Impact if Omitted**: Manual provisioning for enterprise customers
- **Dependencies**: SSO base integration
- **Revisit Trigger**: Enterprise onboarding pipeline active
- **Target Phase/Milestone**: Post-MVP
- **Artifact File**: docs/helix/01-frame/features/FEAT-042-sso-jit-provisioning.md
- **Link/Owner**: #142 / Identity Team
- **Last Reviewed**: 2026-01-15

### Secrets Rotation Policy
- **Type**: Future
- **Artifact Type**: ADR
- **Source**: ADR-017
- **Rationale**: Needs infra work and key management decision
- **Impact if Omitted**: Elevated operational risk
- **Dependencies**: KMS provider selection
- **Revisit Trigger**: KMS decision approved
- **Target Phase/Milestone**: Q3 hardening
- **Artifact File**: docs/helix/02-design/adr/ADR-017-secrets-rotation.md
- **Link/Owner**: #189 / Platform Team
- **Last Reviewed**: 2026-01-15

### Support-Driven Audit Trail Export
- **Type**: Future
- **Artifact Type**: Feature Spec
- **Source**: Support ticket #8891
- **Rationale**: Requires data retention policy alignment
- **Impact if Omitted**: Manual exports remain a support burden
- **Dependencies**: Data retention policy update
- **Revisit Trigger**: Policy approved by legal
- **Target Phase/Milestone**: 2026-H2
- **Artifact File**: docs/helix/01-frame/features/FEAT-051-audit-trail-export.md
- **Link/Owner**: #8891 / Support Ops
- **Last Reviewed**: 2026-01-15

## Parked Artifacts (Links)

### FEAT-042 SSO JIT Provisioning
- **Artifact File**: docs/helix/01-frame/features/FEAT-042-sso-jit-provisioning.md
- **Status**: Parking Lot (Deferred)

### ADR-017 Secrets Rotation
- **Artifact File**: docs/helix/02-design/adr/ADR-017-secrets-rotation.md
- **Status**: Parking Lot (Future)
``````

</details>
