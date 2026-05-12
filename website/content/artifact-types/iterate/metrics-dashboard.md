---
title: "Metrics Dashboard"
linkTitle: "Metrics Dashboard"
slug: metrics-dashboard
phase: "Iterate"
artifactRole: "core"
weight: 11
generated: true
---

## Purpose

Iteration-level metrics summary that compares current values to a prior
baseline and answers whether the latest change improved the system.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Iterate</strong></a> — Measure, align, and improve. Close the feedback loop back into the planning strand.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/06-iterate/metrics-dashboard.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/iterate/improvement-backlog/">Improvement Backlog</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/06-iterate/metrics-dashboard.md"><code>docs/helix/06-iterate/metrics-dashboard.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Metrics Dashboard Generation Prompt
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
- The conclusion is actionable and easy to hand to the next iteration.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
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
- [ ] The summary states the decision implication</code></pre></details></td></tr>
</tbody>
</table>
