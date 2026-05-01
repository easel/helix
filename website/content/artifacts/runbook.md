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

_No worked example captured yet. The prompt and template above describe the canonical structure._
