---
name: helix-experiment
description: Run an autonomous metric-driven optimization loop for an explicit goal.
argument-hint: "[issue-id|goal]"
disable-model-invocation: true
---

# Experiment

Run a metric-optimization loop: try ideas, keep what works, discard what does
not, and repeat until converged or interrupted.

## When to Use

- performance tuning such as test speed, latency, or throughput
- size optimization such as bundle size, binary size, or memory usage
- model or training optimization such as loss, accuracy, or bits per byte
- any measurable optimization target on existing, tested code

## Methodology

1. **Start or resume** — establish the optimization goal, baseline, metric,
   allowed scope, and session log. On subsequent runs, continue from the
   existing session state.
2. **Loop** — after each iteration, evaluate the metric and decide whether to
   continue, revert, or keep the change.
3. **Stop conditions** — stop when the metric converges, repeated iterations do
   not improve it, or the user interrupts or redirects.
4. **Steer** — incorporate user messages into the next hypothesis. Finish the
   current iteration before changing direction.
5. **Close** — when done, land the chosen changes, update metric floors or
   expectations where appropriate, and close the associated work item.

## Constraints

- Only modify files declared in scope.
- Existing tests remain the specification and must continue to pass when validating.
- Prefer simpler solutions over marginal complexity gains.
- Do not change test expectations to manufacture an improvement.

## Running with DDx

When DDx supplies the HELIX runtime, use these references:

- Action prompt: `.ddx/plugins/helix/workflows/actions/experiment.md`
- Session doc template: `.ddx/plugins/helix/workflows/templates/autoresearch-session.md`
- Worklog template: `.ddx/plugins/helix/workflows/templates/autoresearch-worklog.md`
- Metric definition template: `.ddx/plugins/helix/workflows/templates/metric-definition.yaml`
- Ratchet integration: `.ddx/plugins/helix/workflows/ratchets.md`
- Autoresearch ecosystem: compatible with pi-autoresearch JSONL protocol

DDx status markers include:

- `EXPERIMENT_STATUS: CONVERGED`
- `EXPERIMENT_STATUS: NO_IMPROVEMENT`
