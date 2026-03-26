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

### Contract Test Pattern

```typescript
describe('[METHOD] /api/[resource]', () => {
  it('covers the success path', async () => { /* ... */ });
  it('covers validation and auth failures', async () => { /* ... */ });
  it('covers not-found or conflict cases', async () => { /* ... */ });
});
```

## Integration Tests

| Component A | Component B | Test File | Status |
|------------|-------------|-----------|--------|
| [Service] | [Repository] | [service]-persistence.test.ts | Red |
| [Service] | [External API] | [service]-api.test.ts | Red |

### Integration Test Pattern

```typescript
describe('[Feature] Integration', () => {
  beforeEach(() => { /* minimal setup */ });
  it('coordinates components', async () => { /* ... */ });
  it('handles downstream failure', async () => { /* ... */ });
});
```

## Unit Tests

| Module | Function | Test File | Status |
|--------|----------|-----------|--------|
| [validators] | validate[Entity] | validators.test.ts | Red |
| [calculators] | calculate[Metric] | calculators.test.ts | Red |

### Unit Test Pattern

```typescript
describe('[functionName]', () => {
  it('covers the happy path', () => { /* ... */ });
  it('covers edge and error cases', () => { /* ... */ });
  it('covers business rules', () => { /* ... */ });
});
```

## E2E Tests

| Journey | Steps | Critical | Test File | Status |
|---------|-------|----------|-----------|--------|
| [User Registration] | 5 | Yes | registration.e2e.test.ts | Red |
| [Purchase Flow] | 8 | Yes | purchase.e2e.test.ts | Red |

## Test Data

### Fixtures
```typescript
export const [entity]Fixtures = {
  valid: { minimal: () => ({/* ... */}), complete: () => ({/* ... */}) },
  invalid: { missingRequired: () => ({...}), invalidFormat: () => ({...}) },
  edge: { empty: () => ({}), maxLength: () => ({...}) }
};
```

### Factory Pattern
```typescript
export class [Entity]Factory {
  static build(overrides = {}) {
    return { id: faker.datatype.uuid(), name: faker.name.fullName(), ...overrides };
  }
}
```

## Coverage Targets

| Metric | Target |
|--------|--------|
| Overall Line Coverage | 80% |
| Contract Test Coverage | 100% |
| Critical Path Coverage | 100% |
| Error Handling Coverage | 90% |

## Definition of Done

- [ ] All API endpoints have contract tests
- [ ] All components have integration tests
- [ ] All business logic has unit tests
- [ ] Critical user journeys have E2E tests
- [ ] Test data fixtures and factories are prepared
- [ ] Mocks for external services are ready
- [ ] CI pipeline is configured
- [ ] All suites start in RED
