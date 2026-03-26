# Build Procedures

## TDD Cycle: Red-Green-Refactor

For each failing test:

1. **Red** - confirm the test fails.
2. **Green** - write the smallest change to pass.
3. **Refactor** - improve the code without breaking tests.
4. **Commit** - keep changes small and reviewable.

### Implementation Order

1. **Contract tests** - external interfaces first.
2. **Integration tests** - service and repository interactions.
3. **Unit tests** - business logic and validation.

### Key Principles

- Start with minimal implementations.
- Keep components testable.
- Change one small area at a time.
- Run the full suite regularly.

## Quality Gates

- [ ] P0 tests pass
- [ ] Coverage target is met
- [ ] Lint is clean
- [ ] Code is reviewed
