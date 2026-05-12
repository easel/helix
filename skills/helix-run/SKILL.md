---
name: helix-run
description: Run the HELIX bounded operator loop until work completes or human guidance is required.
argument-hint: "[scope|issue-id]"
---

# Run

Run the HELIX bounded operator loop. The loop keeps moving across framing,
design, refinement, implementation, review, alignment, and backfill until the
next safe action requires human judgment or no actionable work remains.

## Use This Skill When

- the user wants HELIX work to keep advancing inline
- ready work should be executed until a bounded stop condition is reached
- queue-drain decisions should be honored instead of a blind loop
- the user wants HELIX to keep moving across requirements, designs, work items,
  build work, and review until guidance is required

For command-specific work, prefer companion skills such as `helix-build`,
`helix-check`, `helix-align`, and `helix-backfill`.

## HELIX Phases

`FRAME -> DESIGN -> TEST -> BUILD -> DEPLOY -> ITERATE`

- `Frame`: define the problem, users, requirements, and acceptance criteria
- `Design`: define architecture, contracts, and technical approach
- `Test`: write failing tests that specify behavior
- `Build`: implement the minimum code to make tests pass
- `Deploy`: release with monitoring and rollback readiness
- `Iterate`: learn from production and plan the next cycle

## Authority Order

When artifacts disagree, prefer:

1. Product Vision
2. Product Requirements
3. Feature Specs / User Stories
4. Architecture / ADRs
5. Solution / Technical Designs
6. Test Plans / Tests
7. Implementation Plans
8. Source Code / Build Artifacts

Tests govern build execution, but they do not override upstream requirements or
design.

## Runtime-Neutral Execution Model

1. Load the execution contract, routing rules, and relevant artifact templates.
2. Inspect ready work for the requested scope.
3. Execute one bounded work item at a time using the project's runtime.
4. When no execution-ready work remains, run the check decision to choose the
   next safe action: build, design, align, backfill, wait, guidance, or stop.
5. Do not treat vague work as execution-ready. If acceptance cannot name
   commands, checks, files, or observable end state, route it to refinement.
6. If the user provides a scope or selector, narrow all steps to that scope.

## On Invocation

When this skill is invoked inline, execute work immediately. Do not merely
report status, describe what you would do, or ask for confirmation unless the
next safe action is guidance.

## How To Work

1. Identify the current phase from artifacts and tests.
2. Do the minimum correct work for that phase.
3. Preserve traceability to upstream artifacts.
4. Keep Build subordinate to failing tests.
5. If build work reveals design drift, refine upstream artifacts explicitly.

## Core Questions

- `Frame`: what problem are we solving, for whom, and how will we know it works?
- `Design`: what structure, contracts, and constraints satisfy the requirement?
- `Test`: what failing tests prove the behavior?
- `Build`: what is the minimum implementation to make those tests pass?
- `Deploy`: how do we release safely and observe health?
- `Iterate`: what did we learn, and what follow-up work belongs in the tracker?

## Notes

- Use TDD strictly: Red -> Green -> Refactor.
- Security belongs in every phase.
- Escalate contradictions instead of patching around them in code.
- For repo-wide reconciliation or traceability work, use the alignment review flow.
- For repo-wide documentation reconstruction, use the backfill flow rather than inventing requirements from code alone.
- When ready work drains, use the check flow before deciding to align, backfill, wait, or stop.

## When to Use HELIX

Good fit:

- new products or features requiring high quality
- mission-critical systems where bugs are expensive
- teams practicing or adopting TDD
- AI-assisted development needing structure
- security-sensitive applications

Not ideal for:

- quick prototypes or proofs of concept
- simple scripts with minimal complexity
- emergency fixes needing immediate deployment

Always enforce the test-first approach: specifications drive implementation,
quality is built in from the start.

## Running with DDx

When the project uses DDx as its HELIX runtime, shared resources live under:

- `.ddx/plugins/helix/workflows/`

Reference docs:

- `.ddx/plugins/helix/workflows/README.md`
- `.ddx/plugins/helix/workflows/actions/check.md`
- `.ddx/plugins/helix/workflows/actions/implementation.md`
- relevant phase README and artifact prompts/templates

DDx execution layer:

- HELIX uses the built-in tracker (`ddx bead`) for execution tracking.
- Issues are stored in `.ddx/beads.jsonl`.
- Use `ddx bead` issues, dependencies, parents, `spec-id`, and labels.
- Recommended labels: `helix`, plus phase/kind/traceability labels as needed.
- See `ddx bead --help` for tracker command mapping.
- `ddx agent execute-loop` is the primary queue-drain surface for execution-ready work.
- `ddx agent execute-bead <bead-id> [--from <rev>] [--no-merge]` is the bounded single-bead managed execution primitive.
- `helix run` is a compatibility controller over DDx-managed execution plus HELIX supervisory routing (`check`, `design`, `polish`, review, alignment).
- Direct `ddx agent run` remains appropriate only for non-managed prompts such as planning, review, alignment, and other work that should not auto-claim or auto-close execution beads.

Inline DDx steps:

```bash
ddx bead ready --json
```

If execution-ready work exists, prefer the DDx-managed queue-drain path over a
hand-rolled claim/execute/close loop.

Use the right execution surface:

- If the user wants the actual compatibility controller, invoke `helix run` rather than re-implementing it bead-by-bead inside the skill.
- If the user wants a single explicit bead run, use `helix build` or `ddx agent execute-bead`, not a direct `ddx agent run` prompt.
- If the work is planning, review, alignment, or another non-managed prompt, use the corresponding HELIX skill or direct `ddx agent run` flow instead of the managed execution lane.

When the DDx ready queue drains, read and execute `.ddx/plugins/helix/workflows/actions/check.md`. That action produces a `NEXT_ACTION` code:

- `BUILD` -> go back to execution
- `DESIGN` -> run the design action once, then re-evaluate the queue
- `ALIGN` -> read and execute `.ddx/plugins/helix/workflows/actions/reconcile-alignment.md`
- `BACKFILL` -> read and execute `.ddx/plugins/helix/workflows/actions/backfill-helix-docs.md`
- `WAIT` / `GUIDANCE` -> report what is blocking and stop
- `STOP` -> report that no actionable work remains

Do not treat a build/deploy/iterate bead as queue-ready unless its acceptance
criteria are machine-auditable enough for DDx-managed execution to decide
success from the bead contract itself. Route vague work to `helix polish` or
`helix triage` instead.

For long-running work, use the `helix-worker` skill. It launches `helix run` as
a background CLI process with `--summary` mode and monitors progress via log files.
