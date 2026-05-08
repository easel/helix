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
ddx:
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

This example is HELIX's actual metrics dashboard, sourced from [`docs/helix/06-iterate/metrics-dashboard.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/06-iterate/metrics-dashboard.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Metrics Dashboard: HELIX 2026-Q2 (post-`v0.3.3`)

> Illustrative example using representative measurements taken from
> the live HELIX repo around the `v0.3.3` release window. Exact values
> reflect a single sampling period and will drift; the dashboard's
> structure and decision logic are the canonical part.

**Review Window**: 2026-04-01 → 2026-04-30
**Baseline**: `v0.3.2` release window (2026-03-01 → 2026-03-31)
**Status**: Complete

### Decision

The 2026-Q2 changes (CI stability fix, `--review-threshold` knob, plugin
manifest cleanup) **improved overall execution stability** with no
regression in cycle time or escalation frequency. The wrapper-CLI test
suite is now reliably green; bead close rate and agent attempt success
both moved in the right direction. No metric crossed a degradation
threshold.

### Summary

`v0.3.3` is a stability release: the CI green rate moved from intermittent
to reliable, and operator review-cadence noise dropped after the
`--review-threshold` knob landed. Bead close rate is up modestly; cycle
time is essentially flat (within noise). No alerting or backlog growth
signals indicate degradation.

### Metrics Table

| Metric | Baseline | Current | Direction | Result | Source |
|--------|----------|---------|-----------|--------|--------|
| Bead close rate (closed/week) | ~22 | ~26 | higher is better | pass | `ddx bead list --status closed --json` filtered by `updated_at` |
| Agent attempt success rate (closed without retry) | ~78% | ~82% | higher is better | pass | `events[]` array on closed beads |
| Median cycle time (claim → close) | ~38m | ~36m | lower is better | noise (within ±10%) | `events[]` timestamps; sampled across the 2026-Q2 window |
| Escalation frequency (`NEXT_ACTION: WAIT` per `helix run`) | ~0.18 | ~0.15 | lower is better | pass | `helix status` snapshot history |
| Review-cycle noise (review passes per closed bead) | ~1.4 | ~1.1 | lower is better | pass (driven by `--review-threshold`) | `ddx bead show <id>` review events on closed beads |
| Wrapper-CLI test green rate (CI) | ~85% | ~99% | higher is better | pass | GitHub Actions runs of `tests/helix-cli.sh` |

### Trend Notes

- The wrapper-CLI green-rate jump is directly attributable to the DDx
  update-notice filter landed in `92293fd` and shipped in `v0.3.3`.
- Review-cycle noise dropped because `--review-threshold` lets operators
  raise the periodic-alignment trigger when the queue is short.
- Cycle time is flat — the release did not target latency, and no
  regression appeared.
- Close rate moved up but is partially explained by the iterate cycle
  consuming a batch of artifact-restoration beads in parallel; this is
  expected to normalize once the AR-2026-05-01 follow-ups are exhausted.

### Follow-Up

- Continue draining the AR-2026-05-01 artifact-restoration backlog
  (tracked in `improvement-backlog.md`).
- Re-measure cycle time after the FEAT-006 context-digest propagation
  beads close — those are expected to reduce mean cycle time.
- File a tracker bead to add a deterministic close-rate metric script
  under `scripts/` so this dashboard can be regenerated mechanically next
  iteration instead of sampled by hand.

### Review Checklist

- [x] Baseline is explicit (`v0.3.2` release window)
- [x] Each metric cites a source (the actual command or events array)
- [x] The summary states the decision implication (`v0.3.3` improved
      stability; no regression)
