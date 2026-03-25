---
dun:
  id: helix.test-plan
  depends_on:
    - helix.architecture
---
# Test Plan

| Project | Version | Date | Status |
|---------|---------|------|--------|
| [Name] | 1.0.0 | [Date] | Draft |

## Testing Strategy

**Goals**: [Primary objective] | [Quality gates]
**Out of Scope**: [Excluded areas]

### Test Levels

| Level | Coverage Target | Priority |
|-------|-----------------|----------|
| Contract | 100% API endpoints | P0 |
| Integration | 90% component interactions | P0 |
| Unit | 80% business logic | P1 |
| E2E | Critical paths only | P1 |

### Frameworks

| Type | Framework | Reason |
|------|-----------|--------|
| Contract | [Framework] | [Why] |
| Integration | [Framework] | [Why] |
| Unit | [Framework] | [Why] |
| E2E | [Framework] | [Why] |

## Test Data

| Type | Strategy |
|------|----------|
| Fixtures | [Static data approach] |
| Factories | [Dynamic generation] |
| Mocks | [External service mocking] |

## Coverage Requirements

| Metric | Target | Minimum | Enforcement |
|--------|--------|---------|-------------|
| Line | 80% | 70% | CI blocks |
| Branch | 75% | 65% | CI blocks |
| Function | 85% | 75% | CI blocks |
| Critical | 100% | 100% | Required |

### Critical Paths (P0)

1. [Auth flow]
2. [Core transaction]
3. [Data persistence]
4. [Error handling]

### Secondary Paths (P1-P2)

- P1: [Secondary features, admin, reporting]
- P2: [Edge cases, rare scenarios]

## Implementation Phases

| Phase | Days | Deliverables |
|-------|------|--------------|
| Foundation | 1-2 | Infrastructure, frameworks, mocks, CI |
| Contract | 3 | API tests, schemas, auth, errors |
| Integration | 4 | Services, DB, external, state |
| Unit | 5 | Logic, validation, calculations |
| E2E | 6 | Journeys, workflows, recovery |

## Infrastructure

| Requirement | Specification |
|-------------|---------------|
| CI Tool | [Tool, version] |
| Test DB | [Type, seeding, cleanup] |
| Services | [Required services] |

### Tools

| Tool | Version | Purpose |
|------|---------|---------|
| [Runner] | [Ver] | Execution |
| [Assert] | [Ver] | Assertions |
| [Coverage] | [Ver] | Reporting |
| [Mock] | [Ver] | Mocking |

## Risks

| Risk | Impact | Prob | Mitigation |
|------|--------|------|------------|
| Flaky tests | High | Med | Retry logic |
| Slow execution | Med | High | Parallelize |
| Env dependencies | High | Low | Containers |

**Known Gaps**: [Limitations and accepted risks]

## Success Metrics

| Metric | Target |
|--------|--------|
| Execution time | <5 min |
| Flakiness | <1% |
| Bug escape | <5% |
| Maintenance | <20% effort |

## Build Handoff

**Commands**: `npm test` | `npm run test:watch` | `npm run test:coverage`

**Priority**: Contract -> Integration -> Unit -> E2E

**Deliverables**: Failing test suite, test docs, configured infrastructure
