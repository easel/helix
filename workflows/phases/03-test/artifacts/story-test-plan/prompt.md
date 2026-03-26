# Story Test Plan Generation

## Required Inputs
- `docs/helix/01-frame/user-stories/US-{XXX}-*.md`
- `docs/helix/02-design/technical-designs/TD-{XXX}-*.md`

## Produced Output
- `docs/helix/03-test/test-plans/TP-{XXX}-*.md`

Create a concise test plan for one user story. Map each acceptance criterion to the minimum set of failing tests needed to prove the story, including data setup, edge cases, and any coverage expectations that matter for this project.

Keep the plan specific:
- prefer one small matrix over repeated prose
- call out only the tests that are needed to drive implementation
- include any setup or mocks required to make the tests executable

Use template at `workflows/phases/03-test/artifacts/story-test-plan/template.md`.
