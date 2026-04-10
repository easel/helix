# Monitoring Setup

`monitoring-setup` is restored as the canonical deploy-phase artifact for
service-specific observability configuration and alerting readiness.

## Decision

This artifact is restored rather than retired.

Current HELIX still requires `docs/helix/05-deploy/monitoring-setup.md` in the
deploy and iterate gates, and the deploy guidance still treats monitoring as a
first-class readiness concern. That responsibility is not replaced cleanly by a
deployment checklist, runbook, or metrics dashboard.

## Why It Exists

- The deployment checklist confirms release readiness tasks were completed.
- The runbook explains how operators respond when something goes wrong.
- The metrics dashboard summarizes what the system is doing over time.
- Monitoring setup defines the concrete metrics, alerts, dashboards, logging,
  tracing, health checks, and SLO signals that must exist before release.

## Canonical Inputs

- deployment strategy and rollout plan
- service architecture and dependency boundaries
- health-check surfaces and operational invariants
- runbook escalation paths
- security monitoring requirements when alerting or audit signals overlap

## Minimum Prompt Bar

- Keep the setup service-specific rather than producing a generic observability checklist.
- Define the metrics, dashboards, logs, traces, and alerts that operators will actually use.
- Include measurable thresholds, routing, and escalation expectations where they matter.
- Tie health checks and SLI/SLO signals to deploy readiness and rollback decisions.
- Link incident response expectations back to the runbook and operator flow.

## Minimum Template Bar

- service summary
- metrics collection
- alerting rules
- dashboards
- logs and tracing
- health checks
- SLI/SLO tracking
- incident-response routing

## Canonical Replacement Status

`monitoring-setup` is not replaced by `deployment-checklist`, `runbook`, or
`metrics-dashboard`. Those artifacts consume or reference observability setup,
but this document remains the canonical place where deploy-time monitoring
requirements are made explicit.

The deleted `security-monitoring` artifact stays superseded rather than
restored. Its surviving intent, security-focused alerts, audit signals,
escalation paths, and compliance-relevant monitoring, is now part of
`monitoring-setup`. Restoring a second deploy artifact for the same operational
surface would reintroduce overlap without adding a distinct prompt or template
responsibility.
