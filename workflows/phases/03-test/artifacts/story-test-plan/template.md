---
dun:
  id: TP-XXX
  depends_on:
    - TD-XXX
---
# Story Test Plan: TP-XXX-[story-name]

## Story Reference

**User Story**: [[US-XXX-[story-name]]]
**Technical Design**: [[TD-XXX-[story-name]]]

## Objective

**Goal**: Verify the story acceptance criteria with failing tests first.
**Scope**: [What is covered] | **Out of scope**: [What is not covered]

## Acceptance Criteria Test Mapping

| Acceptance Criterion | Test Type | Test Cases | Setup or Data | Notes |
|----------------------|-----------|------------|---------------|-------|
| [Given/When/Then criterion] | Unit / Integration / API / E2E | `[test_name]`, `[test_name_error]` | [Fixtures, mocks, seed data] | [Edge cases or constraints] |

## Test Categories

### Unit Tests
- [Modules or rules to cover]

### Integration Tests
- [Component boundaries or dependencies to cover]

### API Tests (if applicable)
- [Endpoints and key scenarios]

### E2E Tests
- [Only if needed for story confidence]

## Test Data Requirements

| Kind | Needed For | Notes |
|------|------------|-------|
| Valid data | [Tests] | [Shape or fixture] |
| Edge data | [Tests] | [Boundary values] |
| Invalid data | [Tests] | [Validation failures] |

## Edge Cases and Error Scenarios

- Boundary values (min, max, empty/null)
- Concurrency (race conditions)
- Invalid input (validation errors)
- Missing dependencies (graceful degradation)
- Authorization failures (401/403)

## Build Handoff
- [Implementation order or notable sequencing constraints]
