---
title: "Deployment Checklist"
slug: deployment-checklist
phase: "Deploy"
weight: 500
generated: true
aliases:
  - /reference/glossary/artifacts/deployment-checklist
---

## What it is

Short, execution-ready release readiness checklist that captures the
technical go/no-go checks, rollout verification, and rollback triggers for a
service deployment.

## Phase

**[Phase 5 — Deploy](/reference/glossary/phases/)** — Ship to users with appropriate operational support, monitoring, and rollback plans.

## Output location

`docs/helix/05-deploy/deployment-checklist.md`

## Relationships

### Requires (upstream)

- [Implementation Plan](../implementation-plan/) *(optional)*

### Enables (downstream)

_None._

### Informs

- [Monitoring Setup](../monitoring-setup/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Deployment Checklist Generation Prompt

Create a concise, service-specific deployment checklist for this release.

## Focus

- Keep the checklist short enough to use during the release itself.
- Include only the checks that materially change the technical go/no-go decision.
- Make rollout verification and rollback triggers explicit.
- Point to supporting artifacts such as `monitoring-setup` or `runbook`
  instead of duplicating them.
- Avoid communication boilerplate, launch marketing tasks, or generic
  enterprise release wish lists.

## Completion Criteria

- Prerequisites and owners are explicit.
- Rollout verification names the signals or commands that prove health.
- Rollback triggers and rollback entrypoint are explicit.
- The final decision section makes the release auditable.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Deployment Checklist

## Release Scope

- Service or component: [name]
- Version or commit: [tag or SHA]
- Deployment window: [date and time]
- Release owner: [name]
- Rollback owner: [name]

## Pre-Deploy Checks

| Area | Check | Evidence or Command | Status |
|------|-------|---------------------|--------|
| Build | [CI, tests, approvals] | [link or command] | [ ] |
| Config | [Secrets, flags, env vars] | [link or command] | [ ] |
| Data | [Migrations, backups, compatibility] | [link or command] | [ ] |
| Ops | [Dashboards, alerts, on-call] | [link or command] | [ ] |

## Rollout Plan

| Stage | Action | Exit Condition |
|-------|--------|----------------|
| Staging | [deploy and validate] | [what must be true] |
| Initial production | [first step or canary] | [what must be true] |
| Full rollout | [complete rollout] | [what must be true] |

## Verification Checks

| Signal or Check | Expected Result | Evidence or Command | Status |
|-----------------|-----------------|---------------------|--------|
| [health check] | [healthy value] | [command or dashboard] | [ ] |
| [error rate] | [threshold] | [dashboard or query] | [ ] |
| [latency] | [threshold] | [dashboard or query] | [ ] |
| [critical user journey] | [pass condition] | [test or observation] | [ ] |

## Rollback Triggers

| Trigger | Threshold or Condition | Immediate Action | Owner |
|---------|------------------------|------------------|-------|
| [trigger] | [threshold] | [rollback step or runbook] | [name] |
| [trigger] | [threshold] | [rollback step or runbook] | [name] |

## Go or No-Go Decision

- Decision: [Go / Hold / Roll Back]
- Decision time: [timestamp]
- Notes: [exceptions, deferred checks, follow-up]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
