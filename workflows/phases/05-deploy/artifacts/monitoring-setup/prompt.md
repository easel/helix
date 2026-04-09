# Monitoring Setup Generation Prompt

Create a concise, service-specific monitoring setup for this deployment.

## Focus
- Include only the metrics, logs, alerts, dashboards, and tracing needed to operate this service.
- Define measurable thresholds, routing, and escalation where they matter.
- Connect health checks and SLOs to rollout safety and rollback decisions.
- Avoid generic observability boilerplate that does not change operator behavior.

## Completion Criteria
- Core metrics and dashboards are defined.
- Alert thresholds and routing are explicit.
- Logging, tracing, and health-check expectations are clear.
- The setup is specific enough to support deployment and incident response.
