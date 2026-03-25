# Story Build Bead Generation

## Required Inputs
- `docs/helix/03-test/test-plans/TP-{XXX}-*.md` - Failing tests for story
- `docs/helix/02-design/technical-designs/TD-{XXX}-*.md` - Technical design
- `docs/helix/04-build/implementation-plan.md` - Project build plan

## Produced Output
- one or more upstream `bd` issues labeled `helix`, `phase:build`, `story:US-{XXX}`

## Prompt

You are creating build beads for a specific user story. Your goal is to define
scoped, deterministic implementation tasks that make the failing tests pass
using TDD.

Based on the test plan (TP-{XXX}), technical design (TD-{XXX}), and project
build plan, create one or more build beads that:

1. Cite the governing canonical artifacts
2. Define a single coherent goal per bead
3. List only the files and tests relevant to that bead
4. Make dependencies between beads explicit
5. Specify deterministic implementation and verification steps

Use the mapping guidance at:
`workflows/phases/04-build/artifacts/story-implementation-plan/template.md`

Use upstream Beads guidance at:
`workflows/BEADS.md`

## Completion Criteria
- [ ] Each failing test is covered by one or more build beads
- [ ] Each bead is independently completable
- [ ] Dependencies between beads are explicit
- [ ] No `[NEEDS CLARIFICATION]` markers remain
