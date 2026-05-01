---
title: "Runbook"
slug: runbook
phase: "Deploy"
weight: 500
generated: true
aliases:
  - /reference/glossary/artifacts/runbook
---

## What it is

Service-specific operational procedures for on-call response, rollback,
recovery, and routine maintenance tied to a deployed system.

## Phase

**[Phase 5 — Deploy](/reference/glossary/phases/)** — Ship to users with appropriate operational support, monitoring, and rollback plans.

## Output location

`docs/helix/05-deploy/runbook.md`

## Relationships

### Requires (upstream)

- [Architecture](../architecture/) *(optional)*
- [Deployment Checklist](../deployment-checklist/) *(optional)*
- [Monitoring Setup](../monitoring-setup/) *(optional)*
- [Security Architecture](../security-architecture/) *(optional)*

### Enables (downstream)

_None._

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Runbook Prompt

Create a service-specific operational runbook for one deployed system.

## Required Inputs
- deployment checklist or rollout entrypoints
- monitoring setup, dashboards, and alert routing
- architecture or dependency boundaries
- on-call ownership and escalation expectations
- security-response constraints, if the service has them

## Produced Output
- `docs/helix/05-deploy/runbook.md`

## Focus

Keep the runbook executable during an incident or maintenance window. Include
only the checks, commands, decisions, and escalation paths that are specific
to this service.

Differentiate the runbook from adjacent deploy artifacts:

- `deployment-checklist` decides whether a release can proceed
- `monitoring-setup` defines signals, dashboards, and alerts
- `runbook` explains what operators do when those signals fire or when
  rollback, recovery, or routine maintenance is required

Map alerts or symptoms to first checks, dashboards, commands, and next
decisions. Include rollback and recovery steps with prerequisites, stop
conditions, and validation. Include recurring operational procedures only when
somebody actually performs them.

Do not produce a generic SRE handbook, sample vendor command dump, or broad
release coordination plan.

## Completion Criteria
- [ ] Operator entry points map situations to first checks, commands, and owners
- [ ] Alert triage is tied to concrete dashboards, logs, or commands
- [ ] Rollback and recovery steps include prerequisites, stop conditions, and validation
- [ ] Routine operational procedures are explicit or the document says none exist
- [ ] Escalation and communication paths are explicit

Use the template at `.ddx/plugins/helix/workflows/phases/05-deploy/artifacts/runbook/template.md`.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Runbook - [Service / System]

## Service Summary

- Service or component: [name]
- Primary function: [what it does]
- Business impact if degraded: [who is affected and how]
- Ownership team: [team]
- On-call rotation: [link or contact]
- Environments covered: [production, staging, regional variants]

## Operator Entry Points

| Situation | First dashboard, log, or query | First command or check | Owner |
|-----------|--------------------------------|------------------------|-------|
| [rollout regression] | [dashboard or log] | [command or query] | [name or role] |
| [service degradation] | [dashboard or log] | [command or query] | [name or role] |
| [dependency failure] | [dashboard or log] | [command or query] | [name or role] |

## Dependencies and Failure Boundaries

| Dependency or boundary | Why it matters | Failure signal | Fallback or escalation |
|------------------------|----------------|----------------|------------------------|
| [database, queue, third-party API] | [impact] | [signal] | [action] |
| [critical upstream or downstream] | [impact] | [signal] | [action] |

## Alert Triage

| Alert or symptom | Likely causes | Immediate checks | Stop and escalate when |
|------------------|---------------|------------------|------------------------|
| [high error rate] | [deploy, dependency, config] | [dashboard, logs, health check] | [condition] |
| [latency spike] | [capacity, dependency, hot path] | [dashboard, trace, query] | [condition] |
| [queue growth or saturation] | [worker failure, downstream slowness] | [dashboard, queue depth check] | [condition] |

## Common Incident Procedures

### [Incident Name]

- Trigger: [how you know this procedure applies]
- Immediate actions:
  1. [first safe action]
  2. [second safe action]
  3. [containment or mitigation]
- Validation:
  - [signal proving recovery]
  - [signal proving rollback or mitigation worked]
- Escalate to: [role, team, or vendor]

### [Security or Data-Safety Incident]

- Trigger: [alert, report, or symptom]
- Immediate actions:
  1. [containment]
  2. [evidence preservation]
  3. [notification or coordination]
- Validation:
  - [proof the service is safe or contained]
- Escalate to: [security owner or incident commander]

## Rollback and Recovery

### Rollback Entry Conditions

- [condition that requires rollback]
- [condition that requires holding rollout]

### Rollback Procedure

1. [rollback entrypoint or command]
2. [stabilize traffic, config, or workers]
3. [verify previous version or safe state]

### Recovery Validation

- [health check, dashboard, or user journey]
- [error-rate or latency threshold]
- [dependency confirmation]

## Routine Operations

| Operation | Trigger or cadence | Command or workflow | Verification |
|-----------|--------------------|---------------------|--------------|
| [key rotation, replay, cache warmup] | [when it happens] | [command or steps] | [proof] |
| [backup or maintenance task] | [when it happens] | [command or steps] | [proof] |

If no recurring operational tasks exist, state that explicitly and point to the
systems that own them instead.

## Escalation and Communications

1. Primary on-call: [name, rotation, or channel]
2. Secondary escalation: [name, team, or channel]
3. Incident coordinator or manager: [name, team, or channel]
4. External dependency or vendor support: [link, account, or contact]

## References

- Deployment checklist: [link]
- Monitoring setup: [link]
- Architecture or dependency map: [link]
- Security architecture or policy, if applicable: [link]
``````

</details>

## Example

This example is HELIX's actual runbook, sourced from [`docs/helix/05-deploy/runbook.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/runbook.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Runbook — `ddx-server`

### Service Summary

- Service or component: `ddx-server` — the long-running platform service
  that owns the bead tracker (`.ddx/beads.jsonl`), agent worker pool, and
  execution evidence under `.ddx/exec-runs.d/`.
- Primary function: Accept `ddx agent execute-bead` / `ddx agent execute-loop`
  dispatch from HELIX skills, run the resulting model-provider calls, and
  persist execution records that HELIX consumes during review.
- Business impact if degraded: HELIX `helix run` and `helix build` cannot
  advance the bead queue. Existing claims may go stale (orphan-recovery
  threshold default 7200s) but no data is lost — `.ddx/beads.jsonl` is
  durable on disk under git.
- Ownership team: HELIX maintainers (this is a developer-local service; the
  operator running it is the on-call).
- On-call rotation: N/A — single-operator service. The operator is expected
  to be present when `ddx-server` is running.
- Environments covered: One per repo working tree. The default deployment
  is `systemd --user` on the operator's workstation, listening on
  `127.0.0.1:7743`.

### Operator Entry Points

| Situation | First dashboard, log, or query | First command or check | Owner |
|-----------|--------------------------------|------------------------|-------|
| `helix run` reports `BLOCKED` with no obvious bead-side cause | `helix status` | `ddx server workers list` and `curl -fsS http://127.0.0.1:7743/healthz` | Operator |
| Agent dispatch hangs or times out | `.ddx/agent-logs/<latest>` | `ddx server workers list` then `ddx server stop` / `ddx server start` | Operator |
| Tracker writes appear torn or out of order | `git diff -- .ddx/beads.jsonl` | `ddx bead list --status in_progress --json` to find unreleased claims | Operator |
| Port 7743 is in use at startup | `ss -lntp '( sport = :7743 )'` | Identify the conflicting process; kill it or change the bind port | Operator |
| Model-provider auth errors | `.ddx/agent-logs/<latest>` | `echo "${OPENROUTER_API_KEY:0:8}…"` to verify env, then re-source rc | Operator |

### Dependencies and Failure Boundaries

| Dependency or boundary | Why it matters | Failure signal | Fallback or escalation |
|------------------------|----------------|----------------|------------------------|
| Model provider (OpenRouter, Anthropic, etc.) | Every agent call routes here | 4xx/5xx in agent logs; `ddx agent execute-bead` exits with provider error | Switch provider via env (`OPENROUTER_API_KEY` → `ANTHROPIC_API_KEY` etc.); operator-driven |
| `.ddx/beads.jsonl` on local filesystem | Tracker durability | `ddx bead list` errors; corrupt-JSON parse failures | Restore from git: `git checkout .ddx/beads.jsonl` after stopping the server |
| Loopback port 7743 | Local control-plane access | Bind failure on startup | Kill conflicting process; or set `DDX_SERVER_PORT` to a free port and update `ddx server start` config |
| `~/.ddx/` user-state dir | Server-managed state outside the repo | Permission errors at startup | Verify ownership; recreate if missing (state is reproducible from repo) |
| Tailscale (`tsnet`) sidecar (opt-in) | Remote control-plane access | Tailscale connectivity errors | Service still works on loopback; tailnet failure is non-blocking |

### Alert Triage

| Alert or symptom | Likely causes | Immediate checks | Stop and escalate when |
|------------------|---------------|------------------|------------------------|
| `helix run` repeatedly returns `NEXT_ACTION: WAIT` | No ready beads; or queue-drain gate is blocking on missing context | `ddx bead ready --json`; `helix status`; check focused-epic state | Beads exist as ready but workers idle — restart `ddx-server` |
| `ddx server workers list` shows zero healthy workers | Server crashed; or all workers wedged on a long model call | Check `.ddx/agent-logs/<latest>`; check `systemctl --user status ddx-server` | Crash loops more than 3x — capture logs and stop, do not restart blindly |
| `claimed-at` ages exceed `HELIX_ORPHAN_THRESHOLD` (default 7200s) | Worker died without `--unclaim`; orphan recovery not yet swept | Wait for next sweep, or run `ddx bead unclaim <id>` manually after confirming the worker is dead | Recovery does not free the claim — investigate before forcing |
| Provider 401/403 spikes | API key revoked, expired, or rate-limited | `echo "${OPENROUTER_API_KEY:0:8}…"`; provider dashboard | Key is valid but provider rejects — escalate to provider support |
| Tracker file shows torn writes | Concurrent direct edit during a live run | `git diff .ddx/beads.jsonl`; check `events[]` for the affected bead | The bead `events[]` log does not match observable state — restore from git |

### Common Incident Procedures

#### Stuck Claim After Worker Death

- Trigger: `ddx bead list --status in_progress` shows a bead with stale
  `claimed-at` (older than the orphan threshold) and the recorded
  `claimed-pid` is no longer running.
- Immediate actions:
  1. Confirm the PID is dead: `ps -p <claimed-pid>` returns nothing.
  2. Capture the bead state: `ddx bead show <id> --json > /tmp/<id>-stuck.json`.
  3. Run `ddx bead unclaim <id>` to release the claim.
- Validation:
  - `ddx bead show <id>` reports `status: open` and no claim metadata.
  - `helix run` resumes and either reclaims or skips per the queue ordering.
- Escalate to: N/A (operator-only service).

#### Tracker File Corruption

- Trigger: `ddx bead list` exits non-zero with a JSON parse error, or
  `git diff -- .ddx/beads.jsonl` shows a malformed line.
- Immediate actions:
  1. Stop the server: `ddx server stop`.
  2. Capture evidence: `cp .ddx/beads.jsonl /tmp/beads-corrupt.jsonl`.
  3. Restore from git: `git checkout .ddx/beads.jsonl`.
  4. Replay any lost work by inspecting recent agent logs and re-issuing
     `ddx bead update` calls if needed.
- Validation:
  - `ddx bead list --status open --json | jq length` returns the expected
    count.
  - `helix status` shows a coherent queue.
- Escalate to: HELIX maintainers via repo issues if corruption is
  reproducible.

#### Provider Auth Failure

- Trigger: Agent logs show repeated 401 / 403 from the model provider.
- Immediate actions:
  1. Verify the env var is set in the server's environment:
     `systemctl --user show-environment | grep -i api_key` (presence only —
     never echo the value).
  2. Re-source the operator rc file or `direnv reload` and restart the
     server: `ddx server stop && ddx server start`.
  3. If the key is genuinely expired, rotate at the provider, update the
     env, and restart.
- Validation:
  - One successful `ddx agent execute-bead --dry-run` against any ready bead.
- Escalate to: Provider support if the key is valid but rejected.

### Rollback and Recovery

#### Rollback Entry Conditions

- A `ddx-server` upgrade caused crash loops on startup.
- A schema-incompatible bead was written by a newer DDx version and the
  current `ddx bead` cannot parse it.

#### Rollback Procedure

1. Stop the running server: `ddx server stop`.
2. Reinstall the previous DDx version (operator's preferred path —
   typically `mise` or `asdf`).
3. If the tracker file was rewritten by the newer version, restore the
   previous tracker state: `git checkout HEAD~1 -- .ddx/beads.jsonl`
   (after capturing the current file for forensics).
4. Restart: `ddx server start`.

#### Recovery Validation

- `curl -fsS http://127.0.0.1:7743/healthz` returns `200 OK`.
- `ddx server workers list` shows at least one healthy worker.
- `helix run --dry-run` produces a coherent next-action summary against
  the current queue.

### Routine Operations

| Operation | Trigger or cadence | Command or workflow | Verification |
|-----------|--------------------|---------------------|--------------|
| Orphan-claim sweep | Automatic on each `helix run` cycle | Internal — no operator action required | `ddx bead list --status in_progress` shows no claims older than `HELIX_ORPHAN_THRESHOLD` |
| `.ddx/agent-logs/` rotation | Operator discretion (logs are gitignored runtime state) | Manual: prune older than 30 days | Disk usage in `.ddx/agent-logs/` stays bounded |
| Worker pool restart | After provider config or env change | `ddx server stop && ddx server start` | One successful execute against a ready bead |
| API-key rotation | When provider issues a new key | Update env in operator rc; restart server | Single dry-run against a ready bead succeeds |

If no recurring operational tasks exist beyond these, no other periodic
procedures are documented. Other system maintenance (OS updates, disk
cleanup) belongs to the operator's host-level workflow, not this service.

### Escalation and Communications

1. Primary on-call: The operator running `ddx-server`.
2. Secondary escalation: HELIX maintainers via the repo issue tracker for
   reproducible bugs in `ddx-server` itself.
3. Incident coordinator or manager: N/A — single-operator service.
4. External dependency or vendor support: Model provider support
   (OpenRouter / Anthropic / etc.) for provider-side outages or
   credential issues.

### References

- Deployment checklist: [`deployment-checklist.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/deployment-checklist.md)
- Monitoring setup: [`monitoring-setup.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/monitoring-setup.md)
- Architecture: [`../02-design/architecture.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/architecture.md)
- Security architecture: [`../02-design/security-architecture.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/security-architecture.md)
- DDx/HELIX boundary contract: [`../02-design/contracts/CONTRACT-001-ddx-helix-boundary.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md)
