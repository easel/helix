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

### AC1: [First Acceptance Criterion]
**Given** [precondition], **When** [action], **Then** [expected outcome]

| Test Case | Type | What it Verifies |
|-----------|------|-----------------|
| `test_[name]` | Happy path | [Description] |
| `test_[name]_edge` | Edge case | [Description] |
| `test_[name]_error` | Error | [Description] |

### AC2: [Second Acceptance Criterion]
**Given** [precondition], **When** [action], **Then** [expected outcome]

| Test Case | Type | What it Verifies |
|-----------|------|-----------------|
| `test_[name]` | Happy path | [Description] |
| `test_[name]_boundary` | Boundary | [Description] |

## Test Categories

### Unit Tests
```yaml
test_suite: unit/[component]
coverage_target: 80%
test_cases:
  - name: test_[function]
    input: [test data]
    expected: [expected result]
```

### Integration Tests
```yaml
test_suite: integration/[feature]
test_cases:
  - name: test_components_integrate
    setup: [required setup]
    expected: [expected behavior]
```

### API Tests (if applicable)
```yaml
test_suite: api/[resource]
test_cases:
  - endpoint: POST /api/v1/[resource]
    scenarios:
      - { name: success, response: {status: 201} }
      - { name: validation_error, response: {status: 400} }
```

### E2E Tests
```yaml
test_suite: e2e/[story]
test_cases:
  - name: complete_user_flow
    steps: [User action 1, User action 2, Verify outcome]
```

## Test Data Requirements

```yaml
valid_data:
  fields: { field1: value1, field2: value2 }
edge_case_data:
  fields: [{ field1: minimum_value }, { field1: maximum_value }]
invalid_data:
  fields: [{ field1: null }, { field1: invalid_format }]
```

## Edge Cases and Error Scenarios

- Boundary values (min, max, empty/null)
- Concurrency (race conditions)
- Invalid input (validation errors)
- Missing dependencies (graceful degradation)
- Authorization failures (401/403)

## Definition of Done

- [ ] All acceptance criteria have test cases
- [ ] Edge cases identified and covered
- [ ] Error scenarios covered
- [ ] Test data requirements documented
- [ ] Tests can be implemented as failing tests (TDD)
