---
title: "Metric Definition"
slug: metric-definition
phase: "Iterate"
weight: 600
generated: true
aliases:
  - /reference/glossary/artifacts/metric-definition
---

## What it is

_(metric-definition — description not yet captured in upstream `meta.yml`.)_

## Phase

**[Phase 6 — Iterate](/reference/glossary/phases/)** — Measure, align, and improve. Close the feedback loop back into the planning strand.

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

_None._

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Metric Definition Prompt

Create one reusable metric definition.

## Focus
Define the metric as the authoritative source for ratchets, dashboards, experiments, and monitoring.

Keep the definition minimal: required fields are `name`, `description`, `unit`, `direction`, and `command`. Add `output_pattern`, `tolerance`, and `labels` only when needed.

The command must be deterministic, repeatable, and free of side effects or external service dependencies. Prefer `METRIC <name>=<value>` output unless an `output_pattern` is required.

## Completion Criteria
- All required fields are populated.
- The command is deterministic and repeatable.
- The filename matches the `name` field.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Metric Definition: [NAME]

> Store at `docs/helix/06-iterate/metrics/[NAME].yaml`

```yaml
name: [kebab-case-identifier]
description: [What this metric measures]
unit: [seconds|bytes|percent|count|...]
direction: [lower|higher]
command: [repeatable shell command]
output_pattern: "[regex with capture group]"
tolerance: [noise band, e.g. "5%" or "100ms"]
labels:
  [key]: [value]
```
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
