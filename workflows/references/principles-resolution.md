---
dun:
  id: helix.workflow.principles-resolution
  depends_on:
    - helix.workflow.principles
---
# Principles Resolution

This reference defines the shared pattern that all judgment-making HELIX
action prompts follow to load and apply active design principles.

## Resolution Logic

1. Check: does `docs/helix/01-frame/principles.md` exist and have content?
   - Yes → load it as the active principles document.
   - No → load `workflows/principles.md` (HELIX defaults).

The project file takes full precedence — there is no merging or layering.
When the project file exists, the HELIX defaults are ignored completely.

## Injection Preamble

After loading the active principles, include them in your working context:

```markdown
## Active Principles

{contents of the resolved principles document}

Apply these principles when making judgment calls in this task.
When two options are both valid, prefer the one that better aligns
with the principles above.
```

## When to Apply

Action prompts that involve judgment — design choices, prioritization,
scope decisions, quality trade-offs — must resolve and inject principles
at their Phase 0 or Bootstrap step.

| Action | Injection Point |
|--------|----------------|
| `implementation.md` | Phase 0 (Bootstrap) — alongside quality gates |
| `fresh-eyes-review.md` | Phase 0 (Identify Review Target) — as review criteria |
| `plan.md` | Before first refinement round — as design guidance |
| `evolve.md` | Phase 1 (Requirement Analysis) — as scoping guidance |
| `reconcile-alignment.md` | Phase 0 — as alignment criteria |
| `polish.md` | Bootstrap — as refinement guidance |
| `frame.md` | Bootstrap — to shape requirements priorities |
| `experiment.md` | Bootstrap — to inform metric selection and experiment design |

**Not injected**: `check.md` (mechanical queue evaluation), `backfill-helix-docs.md`
(reconstructs what exists, does not make design choices).

## Bootstrap in helix frame

When `helix frame` runs and no `docs/helix/01-frame/principles.md` exists:

1. Read `workflows/principles.md` (HELIX defaults).
2. Present the defaults to the user and ask:
   - "What does your project value most?"
   - "What trade-offs do you consistently lean toward?"
   - "What past mistakes should these principles help you avoid?"
3. Synthesize user input + defaults into a project principles document.
4. Check for tensions between principles (see Tension Detection below).
5. Write `docs/helix/01-frame/principles.md`.

The user owns the file from this point forward. Only `helix frame` and
direct user editing may write to the principles file.

## Tension Detection

When managing principles, check for conflicts between them:

1. For each pair of principles, evaluate whether they could pull in
   opposite directions for a realistic decision.
2. For each detected tension, check whether the tension resolution section
   already addresses it.
3. Flag unresolved tensions with a concrete example scenario.
4. Accept the user's resolution strategy before completing.

Size ceiling guidance (from `workflows/principles.md`):
- At 8 principles: prompt to review which ones change decisions.
- At 12: suggest consolidating.
- At 15+: strongly recommend pruning.
