---
dun:
  id: helix.parking-lot
  depends_on:
    - helix.prd
  parking_lot: true
---
# Parking Lot (Deferred / Future Work)

## Purpose
Capture deferred and future work without adding inline sections to core HELIX artifacts.

## Policy
- Out of Scope items do not belong here.
- Deferred items must include a rationale and revisit trigger.
- Future items must include a source and expected value.
- Any parked artifact must set `dun.parking_lot: true` in its frontmatter.

## Deferred / Future Items
Use short, editable entries (list format).

### [Item Title]
- **Type**: Deferred | Future
- **Artifact Type**: Feature Spec | User Story | ADR | Solution Design | Implementation Plan | Other
- **Source**: FEAT-XXX / US-XXX / ADR-XXX / external (ticket, note, roadmap)
- **Rationale**: [Why it was deferred / why it is future work]
- **Impact if Omitted**: [Risk/impact]
- **Dependencies**: [Blocked by / prerequisites]
- **Revisit Trigger**: [What must happen before reconsidering]
- **Target Phase/Milestone**: [Phase or release]
- **Artifact File**: [Path to parked artifact, if any]
- **Link/Owner**: [Issue link; owner optional]
- **Last Reviewed**: [YYYY-MM-DD, optional]

## Parked Artifacts (Links)
If a full artifact exists, keep it in its normal location and link it here.

### [Artifact Title]
- **Artifact File**: [docs/helix/02-design/adr/ADR-008-example.md]
- **Status**: Parking Lot (Deferred | Future)
