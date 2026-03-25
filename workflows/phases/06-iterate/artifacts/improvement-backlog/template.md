# Improvement Backlog

This document is the canonical index for prioritized backlog beads. Actionable
work should be tracked in upstream Beads (`bd`), not embedded here as free-form
task lists or custom HELIX bead files.

## Summary

- **Total Beads**: [COUNT]
- **P0 Beads**: [COUNT]
- **P1 Beads**: [COUNT]
- **P2 Beads**: [COUNT]

## Prioritization Rules

- Prioritize work that resolves authoritative-plan drift first
- Prioritize user-facing correctness over speculative optimization
- Prefer beads that unblock multiple downstream items
- Split oversized items before scheduling them

## Open Backlog Beads

| Bead ID | Type | Title | Priority | Source | Dependencies | Status |
|---------|------|-------|----------|--------|--------------|--------|
| [prefix]-abc123 | [task/chore/bug/decision] | [Title] | P0/P1/P2 | [metrics/feedback/retrospective/report] | [Deps] | open/in_progress/deferred/blocked |

## Grouped by Source

### From Production Metrics
- `[prefix]-abc123` - [Why it exists]

### From User Feedback
- `[prefix]-abc123` - [Why it exists]

### From Team Learnings
- `[prefix]-abc123` - [Why it exists]

### From Incidents or Defects
- `[prefix]-abc123` - [Why it exists]

## Candidate Beads for Next Iteration

| Bead ID | Why Now | Required Canonical Updates First? |
|---------|---------|-----------------------------------|
| [prefix]-abc123 | [Reason] | [Yes/No + artifact] |

## Deferred or Parked

| Bead ID | Reason Deferred | Revisit Trigger |
|---------|-----------------|-----------------|
| [prefix]-abc123 | [Reason] | [Trigger] |

## Notes

- Non-actionable observations stay in reports, analyses, or retrospectives.
- Actionable work items must exist as beads before being scheduled.
- Use `bd ready` to review actionable iterate work. Keep backlog beads labeled
  with `helix`, `phase:iterate`, and `kind:backlog` so they are easy to triage
  when they become ready.
