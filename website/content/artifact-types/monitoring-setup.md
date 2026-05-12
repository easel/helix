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

## Activity

**[Deploy](/reference/glossary/activities/)** — Ship to users with appropriate operational support, monitoring, and rollback plans.

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

This example is HELIX's actual monitoring setup, sourced from [`docs/helix/05-deploy/monitoring-setup.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/monitoring-setup.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Monitoring Setup — `ddx-server`

### Service Summary

- Service: `ddx-server` (loopback `127.0.0.1:7743` by default; opt-in
  Tailscale exposure via `tsnet`).
- Signals that matter most: server liveness, worker pool health, bead-queue
  depth (open / ready / blocked), claim freshness (orphan-recovery health),
  and provider-call success rate.

### Metrics Collection

| Category | Metrics | Notes |
|----------|---------|-------|
| Application | Worker count (healthy / unhealthy), in-flight executions, recent execution success / failure counts, average execution duration | From `ddx server workers list --json`; emitted to `.ddx/exec-runs.jsonl` for historical reads |
| System | Process memory (RSS), CPU, file-descriptor count, `.ddx/agent-logs/` disk usage | Operator workstation `top` / `du -sh`; not actively scraped |
| Business | Bead queue depth by status (`open`, `in_progress`, `blocked`, `closed` over the last 24h), close rate | From `ddx bead list --status <s> --json`; surfaced via `helix status` |
| Custom | Orphan-recovery sweeps performed, claims released, stale-claim age distribution | Computed by HELIX from `events[]` arrays during `helix status` |

### Alerting Rules

| Alert | Condition | Action |
|-------|-----------|--------|
| Server unhealthy | `GET /healthz` returns non-200 for 2 consecutive checks | Operator notification: `ddx-server down` (no automated paging — single-operator service) |
| All workers unhealthy | `ddx server workers list --json` reports zero healthy workers for 60s | Operator-visible: `helix status` and `ddx server workers list` show the failure |
| Queue blocked depth growing | `ddx bead list --status blocked --json` count grows by ≥3 in the same `helix run` cycle | Operator-visible warning in `helix status`; surfaces as backlog drift |
| Stale claims exceed threshold | Any `claimed-at` older than `HELIX_ORPHAN_THRESHOLD` (default 7200s) without a recovery sweep | Next `helix run` cycle should sweep; if it doesn't, operator runs `ddx bead unclaim` manually |
| Provider error spike | `>5` consecutive provider 4xx/5xx responses in `.ddx/agent-logs/` | Operator-visible: tail of agent log; check API key + provider status |

### Dashboards

| Dashboard | Must Show |
|-----------|-----------|
| Operations | `GET /healthz` status; worker pool size and health; in-flight executions; latest provider errors |
| Business | Bead counts by status; close rate over the last 24h; focused-epic state; ready-queue depth |
| Technical | `.ddx/agent-logs/` disk usage; recent execution evidence size in `.ddx/exec-runs.d/`; tracker file size and last-modified timestamp |

In practice the "dashboards" surface for a single-operator developer
service is `helix status` plus `ddx server workers list`. There is no
Grafana / Datadog setup; alerting is operator-driven.

### Logs and Tracing

#### Logging

- Required fields (per agent-execution log entry): `timestamp`,
  `level`, `service`, `run-id`, `bead-id`, `message`. Provider names
  appear; provider request bodies and API keys never appear.
- Retention: `.ddx/agent-logs/` is gitignored runtime state. Operators
  prune on their own schedule; HELIX does not auto-rotate.
- Authoritative execution audit: `.ddx/exec-runs.jsonl` (one record per
  agent run) plus the per-run evidence directory under
  `.ddx/exec-runs.d/<run-id>/`. These are durable and committed when
  appropriate.

#### Tracing

- Critical journeys: `helix run` cycle → bead claim → `ddx agent execute-bead`
  dispatch → provider call → result capture → bead update / close.
- Sampling: 100% — every agent run produces a durable execution record
  by design. Sampling is not configurable; the audit trail is the
  product.

### Health Checks

| Check | Endpoint or Mechanism | What It Verifies |
|-------|-----------------------|------------------|
| Liveness | `GET http://127.0.0.1:7743/healthz` | Process is running and responsive on the loopback bind |
| Readiness | `ddx server workers list --json` (returns ≥1 healthy worker) | Worker pool is healthy and capable of executing |
| Tracker integrity | `ddx bead list --status open --json` exits 0 | `.ddx/beads.jsonl` is parseable and locks acquire cleanly |
| Provider connectivity | `ddx agent execute-bead --dry-run <ready-bead>` | API key resolves; provider TLS handshake succeeds |

### SLI/SLO Tracking

| Indicator | SLI | SLO |
|-----------|-----|-----|
| Availability | (`/healthz` 200 responses) / (total checks) over a 24h operator session | ≥99% during active sessions |
| Execution success | (Closed beads with `status: closed`) / (Total claimed beads) over a `helix run` cycle | ≥80% (the rest are blockers, supersessions, or stop-for-guidance — all valid outcomes) |
| Tracker durability | (Cycles with no torn writes) / (Total cycles) | 100% (any tear is a release-blocker bug) |

#### Error Budget

Because this is a developer-local service, the "error budget" is not
formal. The operator stops the service and investigates whenever any SLI
above degrades; there is no auto-escalation.

### Incident Response

#### Response Entry Points

- Primary owner or schedule: The operator running `ddx-server`.
- Secondary owner or schedule: HELIX maintainers via the repo issue
  tracker for reproducible bugs in the service itself.
- Immediate containment actions: `ddx server stop` is always safe — claims
  are durable in `.ddx/beads.jsonl` and orphan recovery picks up stale
  claims on next run.
- Existing runbook links: [`runbook.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/runbook.md) — the canonical
  incident-response surface.

#### Routing

- Primary: Operator on the workstation.
- Secondary: HELIX maintainers (issue tracker).
- Escalation: Model-provider support for provider-side outages.
