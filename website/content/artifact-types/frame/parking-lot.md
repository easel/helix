---
title: "Parking Lot"
linkTitle: "Parking Lot"
slug: parking-lot
phase: "Frame"
artifactRole: "supporting"
weight: 18
generated: true
---

## Purpose

Project-level registry for deferred and future work that is kept
out of the main PRD flow. Parked artifacts remain in their normal
HELIX locations and are flagged with ddx.parking_lot: true.

## Example

<details open>
<summary>Show a worked example of this artifact</summary>

``````markdown
---
ddx:
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
- Any parked artifact must set `ddx.parking_lot: true`.

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

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/parking-lot.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Parking Lot Prompt
Capture deferred work that should not stay in the active path.

## Focus
- Record the item, why it is deferred, and where it belongs next.
- Keep the entry short.
- Link to any relevant artifact or issue.

## Completion Criteria
- Deferred items are easy to find later.
- Nothing active is buried here.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Parking Lot (Deferred / Future Work)

## Policy
- Out-of-scope items do not belong here.
- Deferred items must include rationale and revisit trigger.
- Any parked artifact must set `ddx.parking_lot: true` in its frontmatter.

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
- **Status**: Parking Lot (Deferred | Future)</code></pre></details></td></tr>
</tbody>
</table>
