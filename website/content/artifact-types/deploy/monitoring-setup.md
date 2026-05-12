---
title: "Monitoring Setup"
linkTitle: "Monitoring Setup"
slug: monitoring-setup
phase: "Deploy"
artifactRole: "supporting"
weight: 12
generated: true
---

## Purpose

Service-specific observability and alerting setup required before or during
rollout.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Deploy</strong></a> — Ship to users with appropriate operational support, monitoring, and rollback plans.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/05-deploy/monitoring-setup.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td>Deployment Verification<br><a href="/artifact-types/iterate/metrics-dashboard/">Metrics Dashboard</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/monitoring-setup.md"><code>docs/helix/05-deploy/monitoring-setup.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Monitoring Setup Generation Prompt

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
- The setup is specific enough to support deployment and incident response.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
- Escalation: [Manager]</code></pre></details></td></tr>
</tbody>
</table>
