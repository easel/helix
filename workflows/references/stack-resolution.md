---
dun:
  id: helix.workflow.stack-resolution
  depends_on:
    - helix.workflow.principles-resolution
    - FEAT-006
---
# Stack and Practices Resolution

This reference defines the shared pattern that HELIX action prompts follow
to load the active technology stack and associated practices.

## Resolution Logic

### Stack

1. Check: does `docs/helix/01-frame/stack.md` exist and have content?
   - Yes -> load it as the active stack document.
   - No -> no active stack. Omit stack and practices from context.

There is no default stack. Unlike principles, stacks are always
project-specific. A project without a stack file simply has no declared
technology selections.

### Practices

1. Parse the active stack document for selected stacks (listed under
   `## Active Stacks`).
2. For each selected stack name, load
   `workflows/stacks/<stack-name>/practices.md` from the library.
3. Apply project overrides (listed under `## Project Overrides` in the
   stack document) on top of library practices.

Project overrides take full precedence. If the project says "use Vitest
instead of bun:test", the merged practices reflect Vitest.

## Injection Preamble

After resolving the active stack and merged practices, include them in
your working context:

```markdown
## Active Stack

{components section from the resolved stack document}

## Active Practices

{merged practices with project overrides applied}

Use the declared stack and practices when making technology choices.
When the stack specifies a tool or convention, use it rather than
choosing an alternative.
```

## When to Apply

Action prompts that involve technology choices — implementation,
architecture, design, testing — must resolve and inject stacks at their
Phase 0 or Bootstrap step, alongside principles.

| Action | Injection Point |
|--------|----------------|
| `implementation.md` | Phase 0 (Bootstrap) — alongside principles and quality gates |
| `fresh-eyes-review.md` | Phase 0 — verify implementation follows stack conventions |
| `plan.md` | Before first refinement round — stack constrains architecture |
| `evolve.md` | Phase 1 — stack affects scope of downstream changes |
| `reconcile-alignment.md` | Phase 0 — stack drift is an alignment concern |
| `polish.md` | Bootstrap — verify beads reference correct stack context |
| `frame.md` | Bootstrap — stack selection happens during framing |
| `experiment.md` | Bootstrap — experiments must use declared stack |

**Not injected**: `check.md` (mechanical queue evaluation),
`backfill-helix-docs.md` (reconstructs what exists).

## Stack Selection in helix frame

When `helix frame` runs and no `docs/helix/01-frame/stack.md` exists:

1. List available stacks from `workflows/stacks/`.
2. Ask the user:
   - "What language and runtime does this project use?"
   - "What database or data layer?"
   - "Where will this deploy?"
3. Match answers to available stacks.
4. If custom needs exist, document them as project overrides.
5. Write `docs/helix/01-frame/stack.md`.

## Conflict Detection

When a project selects multiple stacks, check for conflicting practices:

1. For each practice category (linter, formatter, testing, etc.), check
   whether multiple stacks declare different values.
2. If a conflict exists and no project override resolves it, flag it to
   the user with a concrete example.
3. Conflicts must be resolved via project overrides before the stack is
   considered complete.

## Relationship to ADRs and Spikes

Stack selections should be traceable to the decisions that justified them:

- A spike or POC investigates a technology question.
- An ADR records the decision with rationale.
- The stack document references the ADR in its selection.
- Project overrides that depart from library defaults should cite the
  governing ADR.

When a referenced ADR is superseded, `helix polish` must flag the
affected stack selection for re-evaluation.
