---
name: helix-polish
description: Refine HELIX work items before implementation through deduplication, acceptance sharpening, and dependency correction.
argument-hint: "[scope]"
disable-model-invocation: true
---

# Polish

Refine the work queue through multiple passes before implementation begins.

"Check your issues N times, implement once."

## When to Use

- after creating work from a plan
- whenever governing specs or designs change while open work still exists
- HELIX itself changes and the tracker needs to reflect the resulting implementation and verification work precisely
- before starting an execution loop
- work-item quality is uneven or coverage gaps are suspected
- after importing work from another source

## Methodology

1. **Load current state** — all open work for the scope, plus the governing
   plan document if one exists.
2. **Refine for several rounds** — each pass performs deduplication, coverage
   verification, acceptance sharpening, dependency verification, sizing, and
   label or taxonomy hygiene.
3. **Detect convergence** — stop when change count stays low for two
   consecutive rounds.
4. **Report** — summarize modifications across rounds.
5. **Preserve executability** — ensure work items are small enough to verify,
   explicit about governing artifacts, and ordered so tests and safety work
   land before behavior changes where required.

## Acceptance Quality

Polish must require execution-ready beads to name exact commands, checks, files,
fields, or observable repository states rather than vague phrases like "works
correctly." If acceptance cannot be sharpened from governing artifacts, flag it as not execution-ready
and route it back through planning.

## Running with DDx

When DDx supplies the HELIX runtime, use these packaged resources:

- Action prompt: `.ddx/plugins/helix/workflows/actions/polish.md`
- Output template: `.ddx/plugins/helix/workflows/templates/polish-report.md`
- CLI: `helix polish [--rounds N] [scope]`

DDx-specific note: execution-ready beads should name exact commands, checks, or
observable repository states so DDx-managed execution can decide success from
the bead contract itself.
