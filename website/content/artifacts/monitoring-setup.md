---
title: "Monitoring Setup"
slug: monitoring-setup
phase: "Deploy"
weight: 500
generated: true
aliases:
  - /reference/glossary/artifacts/monitoring-setup
---

## What it is

Service-specific observability and alerting setup required before or during
rollout.

## Phase

**[Phase 5 — Deploy](/reference/glossary/phases/)** — Ship to users with appropriate operational support, monitoring, and rollback plans.

## Output location

`docs/helix/05-deploy/monitoring-setup.md`

## Relationships

### Requires (upstream)

- [Deployment Checklist](../deployment-checklist/) *(optional)*
- [Architecture](../architecture/) *(optional)*

### Enables (downstream)

_None._

### Informs

- Deployment Verification
- [Metrics Dashboard](../metrics-dashboard/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
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
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Monitoring Setup

## Service Summary

- Service: [service name]
- Signals that matter most: [availability, latency, throughput, errors, business KPIs]

## Metrics Collection

| Category | Metrics | Notes |
|----------|---------|-------|
| Application | [Latency, throughput, error rate] | [By endpoint or workload if needed] |
| System | [CPU, memory, disk, network] | [Only what affects service health] |
| Business | [KPI names] | [Only if operationally relevant] |
| Custom | [Metric name] | [Why it matters] |

## Alerting Rules

| Alert | Condition | Action |
|-------|-----------|--------|
| [Critical alert] | [Page threshold] | [Page path] |
| [Warning alert] | [Notification threshold] | [Notify path] |

## Dashboards

| Dashboard | Must Show |
|-----------|-----------|
| Operations | [Health, latency, errors, dependency status] |
| Business | [Adoption or outcome metrics] |
| Technical | [Resource use, queues, caches, jobs] |

## Logs and Tracing

### Logging
- Required fields: `timestamp`, `level`, `service`, `trace_id`, `message`
- Retention: [hot and cold retention]

### Tracing
- Critical journeys: [What must be traceable]
- Sampling: [Baseline and overrides]

## Health Checks

| Check | Endpoint or Mechanism | What It Verifies |
|-------|-----------------------|------------------|
| Liveness | `GET /health/live` | [Process is running] |
| Readiness | `GET /health/ready` | [Dependencies, capacity, migrations] |

## SLI/SLO Tracking

| Indicator | SLI | SLO |
|-----------|-----|-----|
| Availability | [Formula] | [Target] |
| Latency | [Formula] | [Target] |
| Quality | [Formula] | [Target] |

### Error Budget
- [Budget and escalation thresholds]

## Incident Response

### Response Entry Points
- Primary owner or schedule: [Who handles the first page]
- Secondary owner or schedule: [Who backs up the first responder]
- Immediate containment actions: [Safe first actions before deeper procedures exist]
- Existing runbook links (optional): [Add links once a runbook exists]

### Routing
- Primary: [Schedule]
- Secondary: [Schedule]
- Escalation: [Manager]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
