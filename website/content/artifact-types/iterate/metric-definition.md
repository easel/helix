---
title: "Metric Definition"
linkTitle: "Metric Definition"
slug: metric-definition
phase: "Iterate"
artifactRole: "core"
weight: 10
generated: true
---

## Purpose

Reusable metric contract that defines what is measured, how it is measured,
expected directionality, and how results feed ratchets or dashboards.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Iterate</strong></a> — Measure, align, and improve. Close the feedback loop back into the planning strand.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/06-iterate/metrics/[name].yaml</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/iterate/metrics-dashboard/">Metrics Dashboard</a><br><a href="/artifact-types/deploy/monitoring-setup/">Monitoring Setup</a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Metric Definition Prompt

Create one reusable metric definition.

## Focus
Define the metric as the authoritative source for ratchets, dashboards, experiments, and monitoring.

Keep the definition minimal: required fields are `name`, `description`, `unit`, `direction`, and `command`. Add `output_pattern`, `tolerance`, and `labels` only when needed.

The command must be deterministic, repeatable, and free of side effects or external service dependencies. Prefer `METRIC &lt;name&gt;=&lt;value&gt;` output unless an `output_pattern` is required.

## Completion Criteria
- All required fields are populated.
- The command is deterministic and repeatable.
- The filename matches the `name` field.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Metric Definition: [NAME]

&gt; Store at `docs/helix/06-iterate/metrics/[NAME].yaml`

```yaml
name: [kebab-case-identifier]
description: [What this metric measures]
unit: [seconds|bytes|percent|count|...]
direction: [lower|higher]
command: [repeatable shell command]
output_pattern: &quot;[regex with capture group]&quot;
tolerance: [noise band, e.g. &quot;5%&quot; or &quot;100ms&quot;]
labels:
  [key]: [value]
```</code></pre></details></td></tr>
</tbody>
</table>
