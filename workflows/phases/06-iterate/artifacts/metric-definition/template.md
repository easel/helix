# Metric Definition: [NAME]

> Store at `docs/helix/06-iterate/metrics/[NAME].yaml`

```yaml
# Required fields
name: [kebab-case-identifier]
description: [What this metric measures]
unit: [seconds|bytes|percent|count|...]
direction: [lower|higher]
command: [repeatable shell command]

# Optional fields
output_pattern: "[regex with capture group]"
tolerance: [noise band, e.g. "5%" or "100ms"]
labels:
  [key]: [value]
```

## Field Guide

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique kebab-case identifier; must match filename |
| `description` | Yes | Human-readable explanation of what is measured |
| `unit` | Yes | Measurement unit (seconds, bytes, percent, count) |
| `direction` | Yes | `lower` (less is better) or `higher` (more is better) |
| `command` | Yes | Deterministic, repeatable shell command |
| `output_pattern` | No | Regex with capture group; default: `METRIC <name>=<value>` |
| `tolerance` | No | Noise band for ratchet enforcement (e.g. `5%`, `0.5s`) |
| `labels` | No | Key-value map for monitoring/dashboard categorization |

## Example

```yaml
name: test-suite-runtime
description: Wall-clock time for the full test suite
unit: seconds
direction: lower
command: ./scripts/run-tests.sh
output_pattern: "METRIC test_suite_runtime=([0-9.]+)"
tolerance: 5%
labels:
  area: testing
  phase: iterate
```
