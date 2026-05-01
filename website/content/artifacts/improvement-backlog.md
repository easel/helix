---
title: "Improvement Backlog"
slug: improvement-backlog
phase: "Iterate"
weight: 600
generated: true
aliases:
  - /reference/glossary/artifacts/improvement-backlog
---

## What it is

Prioritized improvement inventory derived from iteration learnings and
tracker-backed follow-up work.

## Phase

**[Phase 6 — Iterate](/reference/glossary/phases/)** — Measure, align, and improve. Close the feedback loop back into the planning strand.

## Output location

`docs/helix/06-iterate/improvement-backlog.md`

## Relationships

### Requires (upstream)

- [Metrics Dashboard](../metrics-dashboard/)
- [Security Metrics](../security-metrics/)

### Enables (downstream)

_None._

### Informs

- Tracker Issues

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Improvement Backlog Generation Prompt
Document the prioritized improvement inventory produced from iteration learnings.

## Focus
- Turn the current iteration's learnings into a ranked list of follow-up work.
- Prefer concrete tracker-backed items over vague TODOs.
- Use metrics, feedback, and retrospective findings as evidence.
- Make the next selection obvious by sorting by priority and impact.
- Link each item to the relevant bead, report, or supporting artifact.

## Completion Criteria
- The inventory is prioritized.
- Every item has an evidence source.
- The next iteration candidates are explicit.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: improvement-backlog
  depends_on:
    - metrics-dashboard
---
# Improvement Backlog

**Iteration**: [iteration or release]
**Source Learnings**: [metrics, feedback, retrospective, incident review]

## Prioritization Rules

- [Rule for ordering work]
- [Rule for handling safety or risk]

## Backlog Items

| Priority | Item | Evidence | Tracker Ref | Why Now | Status |
|----------|------|----------|-------------|---------|--------|
| P1 | [item] | [metric or finding] | [bead ID] | [reason] | [open/blocked] |

## Selection for Next Iteration

- [Chosen item]
- [Why it wins the next slot]

## Review Checklist

- [ ] Each item cites evidence
- [ ] Tracker references are included
- [ ] Ordering is deterministic
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
