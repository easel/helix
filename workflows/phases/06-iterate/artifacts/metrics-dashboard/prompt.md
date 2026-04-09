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
