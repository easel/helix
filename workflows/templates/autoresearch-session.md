# Autoresearch Session: {{goal}}

## Objective

{{objective_description}}

## Metrics

### Primary

- **Definition:** `docs/helix/06-iterate/metrics/{{metric_name}}.yaml`
- **Name:** {{metric_name}}
- **Unit:** {{metric_unit}}
- **Direction:** {{lower_or_higher}}

### Secondary (optional)

{{secondary_metrics_or_none}}

## How to Run

```bash
./autoresearch.sh
```

Outputs `METRIC {{metric_name}}={{value}}` lines to stdout.

## Correctness Check

```bash
{{test_command}}
```

Tests MUST pass after every iteration. If tests fail, the experiment is
discarded regardless of metric improvement.

## Files in Scope

Every file the agent may modify during this experiment:

| File | Notes |
|------|-------|
| `{{file_path}}` | {{brief_description}} |

## Off Limits

Files and directories that must NOT be modified:

- {{off_limits_path_or_pattern}}

## Constraints

- All existing tests must pass after every edit
- No new dependencies without explicit approval
- Do not change test expectations
- Only modify files listed in "Files in Scope"
- {{additional_constraint}}

## What's Been Tried

_Updated every 5 iterations with a summary of experiments._

### Iterations 1-5

{{summary_of_experiments}}

### Key Patterns

{{patterns_observed}}
