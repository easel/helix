# Metric Definition Prompt

Create a shared metric definition that can be referenced by ratchets, experiments, monitoring, and dashboards.

## Storage Location

Store the metric definition at: `docs/helix/06-iterate/metrics/<name>.yaml`

Each metric gets its own file. The filename must match the `name` field inside the YAML.

## What Is a Metric Definition?

A metric definition is a **shared, authoritative specification** for a single measurable quantity. It answers three questions:

1. **What** is being measured (name, description, unit, direction)
2. **How** to measure it (command, output pattern)
3. **How much noise** is acceptable (tolerance)

Without metric definitions, the same metric gets defined inline in multiple places — ratchet floor fixtures, monitoring configs, experiment sessions, dashboards — with subtle inconsistencies. A metric definition is the single source of truth that all consumers reference.

## Authority Level

Metric definitions sit at **authority level 5-6** (Solution Designs / Test Plans). They define *what to measure and how*, derived from requirements and architecture. A metric definition that contradicts architecture must be corrected at the metric level, not worked around in consumers.

## Key Principles

### The Command Must Be Deterministic and Repeatable

The `command` field is a shell command that produces the measurement. It must satisfy:

- **Deterministic**: given the same code state, it produces results within the tolerance band
- **Repeatable**: it can be run multiple times without side effects
- **Self-contained**: it does not depend on external services or transient state

If the command cannot be made deterministic (e.g., it depends on network latency), document the expected variance in the `tolerance` field.

### Output Convention

By default, the command should emit a line matching:

```
METRIC <name>=<value>
```

where `<name>` matches the metric definition's `name` field. This convention comes from autoresearch and is recognized by ratchet enforcement and experiment runners.

If the command's output uses a different format, specify a regex in `output_pattern` with a capture group for the numeric value.

### Tolerance Defines the Noise Band

The `tolerance` field tells ratchet enforcement how much measurement noise to accept. A measurement within the tolerance band of the current floor is not a regression. Express tolerance as a percentage (e.g., `5%`) or an absolute value with units (e.g., `100ms`, `0.5s`).

## How Consumers Reference Metric Definitions

| Consumer | Reference mechanism |
|----------|-------------------|
| Ratchet floor fixture | `metric: docs/helix/06-iterate/metrics/<name>.yaml` field |
| Monitoring setup | References definition for name, unit, labels |
| Metrics dashboard | Links to definition for units and direction |
| Experiment session | Reads command, direction, tolerance from definition |

## Required Fields

- **name** — unique kebab-case identifier
- **description** — human-readable explanation
- **unit** — measurement unit (seconds, bytes, percent, count, etc.)
- **direction** — `lower` or `higher`
- **command** — repeatable shell command that produces the measurement

## Optional Fields

- **output_pattern** — regex with capture group (default: `METRIC <name>=<value>`)
- **tolerance** — noise band for ratchet enforcement
- **labels** — key-value map for monitoring/dashboard categorization
