---
title: "Test Suites"
slug: test-suites
phase: "Test"
weight: 300
generated: true
aliases:
  - /reference/glossary/artifacts/test-suites
---

## What it is

_(test-suites — description not yet captured in upstream `meta.yml`.)_

## Activity

**[Test](/reference/glossary/activities/)** — Define how we know it works. Plans, suites, and procedures that bind specs to implementation.

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

_None._

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Test Suites Generation Prompt

Create the test suite layout for the Red phase. Keep it concise and project-specific: define the suite boundaries, the minimum behavior each suite must cover, and any shared data conventions needed to make the tests executable.

## Storage Location

`tests/` at the project root

## Include

- contract, integration, unit, and E2E boundaries
- the behaviors each suite owns
- required fixtures, factories, or mocks
- any coverage target that matters for this stack

## Keep Out

- generic TDD teaching text
- oversized code examples
- repeated explanations of why tests come first

Use template at `.ddx/plugins/helix/workflows/phases/03-test/artifacts/test-suites/template.md`.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Test Suite Structure

**Project**: [Project Name]
**Coverage Target**: [Percentage]%
**Test Framework**: [Framework]

## Test Organization

```
tests/
├── contract/           # API endpoint tests
├── integration/        # Component interaction tests
├── unit/              # Business logic tests
├── e2e/               # End-to-end user journeys
├── fixtures/          # Test data
├── factories/         # Data generators
├── mocks/             # Service mocks
├── helpers/           # Test utilities
└── setup/             # Test configuration
```

## Contract Tests

| Endpoint | Method | Test File | Status |
|----------|--------|-----------|--------|
| /api/[resource] | GET | [resource].get.test.ts | Red |
| /api/[resource] | POST | [resource].post.test.ts | Red |

Coverage: success path, validation, auth, and not-found/conflict behavior.

## Integration Tests

| Component A | Component B | Test File | Status |
|------------|-------------|-----------|--------|
| [Service] | [Repository] | [service]-persistence.test.ts | Red |
| [Service] | [External API] | [service]-api.test.ts | Red |

Coverage: component coordination, persistence, and downstream failure handling.

## Unit Tests

| Module | Function | Test File | Status |
|--------|----------|-----------|--------|
| [validators] | validate[Entity] | validators.test.ts | Red |
| [calculators] | calculate[Metric] | calculators.test.ts | Red |

Coverage: happy path, edge/error cases, and business rules.

## E2E Tests

| Journey | Steps | Critical | Test File | Status |
|---------|-------|----------|-----------|--------|
| [User Registration] | 5 | Yes | registration.e2e.test.ts | Red |
| [Purchase Flow] | 8 | Yes | purchase.e2e.test.ts | Red |

## Test Data

| Asset | Purpose |
|-------|---------|
| Fixtures | [Canonical valid, invalid, and edge payloads] |
| Factories | [Generated test objects] |
| Mocks | [External services or time/network controls] |

## Coverage Targets

| Metric | Target |
|--------|--------|
| Overall Line Coverage | 80% |
| Contract Test Coverage | 100% |
| Critical Path Coverage | 100% |
| Error Handling Coverage | 90% |

## Readiness
- [ ] Suite boundaries are defined
- [ ] Shared test data assets are identified
- [ ] All planned suites begin in RED
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
