---
name: polish
description: Iteratively refine beads before implementation. Deduplication, plan coverage verification, acceptance criteria sharpening, and dependency correction.
disable-model-invocation: true
---

# Polish

Refine the bead queue through multiple passes before implementation begins.

"Check your beads N times, implement once."

## When to Use

- After creating beads from a plan
- Before starting a `helix run` cycle
- When bead quality is uneven or coverage gaps are suspected
- After importing beads from another source

## Steps

1. **Load current state** — all open beads for the scope, plus the governing
   plan document if one exists.

2. **For 4-6 rounds, refine** — each pass performs:
   - **Deduplication**: find and merge overlapping beads
   - **Coverage verification**: ensure every plan section has a bead
   - **Acceptance criteria sharpening**: replace vague criteria with testable
     statements
   - **Dependency verification**: correct missing, circular, or incorrect deps
   - **Sizing**: split oversized beads into independently verifiable slices
   - **Label hygiene**: ensure helix, phase, kind, and area labels are correct

3. **Detect convergence** — stop when change count drops below 3 for two
   consecutive rounds.

4. **Report** — summarize modifications across rounds.

## References

- Action prompt: `workflows/actions/polish.md`
- Output template: `workflows/templates/polish-report.md`
- CLI: `helix polish [--rounds N] [scope]`
