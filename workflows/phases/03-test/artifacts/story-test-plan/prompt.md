# Story Test Plan Generation

## Required Inputs
- `docs/helix/01-frame/user-stories/US-{XXX}-*.md` - User story with acceptance criteria
- `docs/helix/02-design/technical-designs/TD-{XXX}-*.md` - Technical design for story

## Produced Output
- `docs/helix/03-test/test-plans/TP-{XXX}-*.md` - Test plan for specific story

## Prompt

You are creating a test plan for a specific user story. Your goal is to define tests that verify all acceptance criteria are met.

Based on the user story (US-{XXX}) and its technical design (TD-{XXX}), create a test plan that includes:

1. **Story Reference**
   - Story ID and title
   - Acceptance criteria (copied from story)
   - Technical design reference

2. **Test Case Matrix**
   | AC# | Test Case | Type | Input | Expected Output | Priority |
   |-----|-----------|------|-------|-----------------|----------|
   | AC1 | [Description] | Unit/Integration/E2E | [Data] | [Result] | P0/P1/P2 |

3. **Test Implementation**
   For each acceptance criterion:
   - Happy path test
   - Edge case tests
   - Error handling tests

4. **Test Data Requirements**
   - Required test fixtures
   - Mock/stub requirements
   - Test database state

5. **Coverage Targets**
   - Line coverage target
   - Branch coverage target
   - Mutation testing considerations

Use the template at `workflows/helix/phases/03-test/artifacts/story-test-plan/template.md`.

## Completion Criteria
- [ ] Every acceptance criterion has at least one test case
- [ ] Edge cases identified and covered
- [ ] Test data requirements documented
- [ ] Tests can be implemented as failing tests (TDD)
