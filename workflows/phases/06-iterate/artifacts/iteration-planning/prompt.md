# Iteration Planning Generation

## Required Inputs
- `docs/helix/06-iterate/improvement-backlog.md` - Improvement backlog
- upstream backlog beads in `bd`
- `docs/helix/06-iterate/lessons-learned.md` - Lessons learned
- Resource availability

## Produced Output
- `docs/helix/06-iterate/next-iteration.md` - Next iteration plan

## Prompt

You are planning the next iteration. Your goal is to define scope, goals, and
success criteria by selecting a coherent set of backlog beads.

Create a plan that includes:

1. **Iteration Goals**
   - Primary objectives
   - Success criteria
   - Key results

2. **Selected Bead Set**
   - Which backlog beads are in scope
   - Why each bead is included now
   - Which canonical artifacts must be updated before execution

3. **Resource Allocation**
   - Ownership and sequencing assumptions
   - Skills needed
   - External dependencies

4. **Timeline**
   - Iteration duration
   - Key milestones
   - Critical path and parallel work

5. **Risk Assessment**
   - Scope risks
   - Technical risks
   - Resource risks
   - Mitigation plans

6. **Success Metrics**
   - How success will be measured
   - Baseline values
   - Target values

Use the template at `workflows/helix/phases/06-iterate/artifacts/iteration-planning/template.md`.
Use HELIX bead guidance at `workflows/helix/BEADS.md`.

## Completion Criteria
- [ ] Scope is well-defined
- [ ] In-scope work is expressed as bead IDs
- [ ] Goals are measurable
- [ ] Resources allocated
- [ ] Risks identified with mitigations
