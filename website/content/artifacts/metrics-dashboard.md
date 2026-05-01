---
title: "Metrics Dashboard"
slug: metrics-dashboard
phase: "Iterate"
weight: 600
generated: true
aliases:
  - /reference/glossary/artifacts/metrics-dashboard
---

## What it is

Iteration-level metrics summary that compares current values to a prior
baseline and answers whether the latest change improved the system.

## Phase

**[Phase 6 — Iterate](/reference/glossary/phases/)** — Measure, align, and improve. Close the feedback loop back into the planning strand.

## Output location

`docs/helix/06-iterate/metrics-dashboard.md`

## Relationships

### Requires (upstream)

- Metric Definitions

### Enables (downstream)

_None._

### Informs

- [Improvement Backlog](../improvement-backlog/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Metrics Dashboard Generation Prompt
Document the iteration-level metrics summary used to judge whether the latest
changeset improved the system.

## Focus
- Start from the canonical metric definitions in `docs/helix/06-iterate/metrics/`.
- Compare the current measurement against the previous baseline or committed floor.
- State whether the change improved, regressed, or stayed within noise.
- Include only the metrics needed to support the decision.
- Cite the source of each metric and the measurement command or report.
- Keep raw observability setup and implementation details out of this artifact.

## Completion Criteria
- Every metric cited has a source definition and current value.
- The comparison baseline is explicit.
- The conclusion is actionable and easy to hand to the next iteration.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: metrics-dashboard
  depends_on:
    - metric-definition
---
# Metrics Dashboard: [iteration or release]

**Review Window**: [start date - end date]
**Baseline**: [previous iteration, ratchet floor, or benchmark]
**Status**: [draft | complete]

## Decision

[State whether the latest change improved the system and why.]

## Summary

[One concise paragraph that summarizes the result of the measured change.]

## Metrics Table

| Metric | Baseline | Current | Direction | Result | Source |
|--------|----------|---------|-----------|--------|--------|
| [name] | [value] | [value] | [higher/lower] | [pass/fail/noise] | [metric definition or report] |

## Trend Notes

- [Trend or anomaly]
- [What changed relative to the baseline]

## Follow-Up

- [Tracker issue ID or next step]

## Review Checklist

- [ ] Baseline is explicit
- [ ] Each metric cites a source
- [ ] The summary states the decision implication
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
