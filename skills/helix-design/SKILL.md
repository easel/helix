---
name: helix-design
description: Create a comprehensive HELIX design document through iterative refinement before build work.
argument-hint: "[scope]"
disable-model-invocation: true
---

# Design

Create a thorough design document through iterative self-critique and
refinement. Invest deeply in planning quality before any implementation work is
started.

## When to Use

- starting a new feature or project
- a functionality change requires new or expanded design authority before build work can continue
- HELIX itself changes in a way that affects workflow contract, skill behavior, packaging, or control rules
- a large scope needs implementation work items derived from a design
- existing planning artifacts are thin or incomplete
- the implementation path is unclear

## Methodology

1. **Load context** — read existing planning artifacts, current implementation,
   tests, and open work for the requested scope.
2. **Draft a comprehensive design** covering problem statement, requirements,
   architecture decisions with alternatives, interface contracts, data model,
   error handling, security, test strategy, implementation ordering, risk
   register, and observability.
3. **Refine iteratively** — after each draft round, assume important elements
   are missed or underspecified. Challenge assumptions, interfaces, error
   paths, edge cases, and sequencing.
4. **Detect convergence** — stop when substantive changes remain low for two
   consecutive rounds.
5. **Output the design** to the project's HELIX design artifact location.
6. **Capture execution work** — once the design is clear enough, create or
   refine work items that represent the implementation slices needed to make
   the design real.

## After Design

Run a refinement pass over the derived work items before implementation begins.
The goal is not only to have a design, but to have executable, ordered,
verifiable work.

## Running with DDx

When DDx supplies the HELIX runtime, use the packaged workflow assets:

- Action prompt: `.ddx/plugins/helix/workflows/actions/plan.md`
- Output template: `.ddx/plugins/helix/workflows/templates/plan-document.md`
- CLI: `helix design [--rounds N] [scope]`

DDx-oriented next step:

```bash
helix polish
helix run --summary
```
