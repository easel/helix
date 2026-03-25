# Build Plan Generation Prompt

Create the canonical project-level build plan for the Build phase.

## Storage Location

Store the build plan at: `docs/helix/04-build/implementation-plan.md`

## Purpose

The build plan is the authoritative execution strategy for the Build phase. It
does not replace story-level task tracking. Instead, it defines:

- the build order across stories or functional areas
- shared constraints and standards
- integration checkpoints
- the rules for decomposing work into build beads

Story-level implementation work belongs in upstream Beads (`bd`), not in custom
HELIX bead files or markdown story implementation plans.

## Required Inputs

- `docs/helix/03-test/test-plan.md`
- `docs/helix/03-test/test-plans/TP-*.md`
- `docs/helix/02-design/technical-designs/TD-*.md`
- project-level design artifacts that constrain implementation

## Output Requirements

The build plan must include:

1. **Scope and authority**
   - Governing artifacts
   - Assumptions and constraints
   - What the plan does and does not control

2. **Build sequencing**
   - Story or functional area ordering
   - Shared dependencies
   - Critical integration points

3. **Bead decomposition strategy**
   - Which stories or areas become build beads
   - Recommended bead boundaries
   - Required `bd` labels, parents, and dependency rules

4. **Quality and verification rules**
   - Required tests
   - Build review checkpoints
   - Conditions for closing build beads

5. **Risks and blockers**
   - Known implementation risks
   - Escalation triggers
   - When to refine upstream artifacts instead of continuing implementation

## Bead Rules

- Do not embed a long-lived task log in the canonical build plan.
- Use the build plan to drive creation of upstream `bd` issues.
- Each build bead must cite the test plan, technical design, and this build plan.
- If a story needs multiple independent implementation slices, create multiple beads.

## Template

Use the template at
`workflows/helix/phases/04-build/artifacts/implementation-plan/template.md`.
Use HELIX bead guidance at `workflows/helix/BEADS.md`.

## Completion Criteria

- [ ] Build sequencing is explicit
- [ ] Shared dependencies are identified
- [ ] Build bead decomposition is defined
- [ ] Quality gates and verification are clear
- [ ] No `[NEEDS CLARIFICATION]` markers remain
