# Alignment Report Structure

Use this section order:

1. Review Metadata
2. Scope and Governing Artifacts
3. Intent Summary
4. Planning Stack Findings
5. Implementation Map
6. Acceptance Criteria Status
7. Gap Register (with Quality Findings)
8. Traceability Matrix
9. Review Bead Summary
10. Execution Beads Generated
11. Bead Coverage Verification
12. Execution Order
13. Open Decisions

## Required Tables

### Acceptance Criteria Status

| Story / Feature | Criterion | Test Reference | Status | Evidence |
|-----------------|-----------|----------------|--------|----------|
| [US-XXX] | [criterion] | [test path or "none"] | [SATISFIED/TESTED_NOT_PASSING/UNTESTED/UNIMPLEMENTED] | [refs] |

### Gap Register

| Area | Classification | Planning Evidence | Implementation Evidence | Resolution Direction | Review Bead | Notes |
|------|----------------|-------------------|--------------------------|----------------------|-------------|-------|

### Traceability Matrix

| Vision Item | Requirement | Feature / Story | Architecture / ADR | Solution / Technical Design | Test Reference | Implementation Plan | Code Status | Classification |
|-------------|-------------|-----------------|--------------------|-----------------------------|----------------|---------------------|-------------|----------------|

### Review Bead Summary

| Review Bead | Functional Area | Status | Key Findings | Recommended Direction |
|-------------|-----------------|--------|--------------|-----------------------|

### Execution Beads Generated

| Bead ID | Type | HELIX Labels | Parent / Source | Goal | Dependencies | Verification |
|---------|------|--------------|-----------------|------|--------------|-------------|

### Bead Coverage Verification

| Gap / Criterion | Covering Bead | Status |
|-----------------|---------------|--------|
| [gap or criterion] | [bd ID or "MISSING"] | [covered/missing/deferred] |
