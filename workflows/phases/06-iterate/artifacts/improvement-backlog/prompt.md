# Improvement Backlog Generation

## Required Inputs
- `docs/helix/06-iterate/lessons-learned.md` - Lessons learned
- `docs/helix/06-iterate/feedback-analysis.md` - User feedback
- `docs/helix/06-iterate/metrics-dashboard.md` - Production metrics

## Produced Output
- `docs/helix/06-iterate/improvement-backlog.md` - Prioritized backlog index
- upstream `bd` issues labeled `helix`, `phase:iterate`, `kind:backlog`

## Prompt

You are creating the improvement backlog for the next iteration. Your goal is
to prioritize actionable follow-up work and store each actionable item as a
backlog bead.

Based on lessons learned, user feedback, and metrics:

1. Create or update one backlog bead per actionable item
2. Group and prioritize the beads in the backlog index document
3. Distinguish actionable work from observations, risks, and open questions
4. Mark items that need canonical artifact updates before execution

Use the index template at:
`workflows/phases/06-iterate/artifacts/improvement-backlog/template.md`

Use upstream Beads guidance at:
`workflows/BEADS.md`

## Completion Criteria
- [ ] All improvement sources reviewed
- [ ] Every actionable item has a backlog bead
- [ ] Beads are prioritized consistently in the index
- [ ] Dependencies are identified
- [ ] The index references bead IDs explicitly
