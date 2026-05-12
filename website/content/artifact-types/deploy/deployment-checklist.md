---
title: "Deployment Checklist"
linkTitle: "Deployment Checklist"
slug: deployment-checklist
phase: "Deploy"
artifactRole: "core"
weight: 10
generated: true
---

## Purpose

Short, execution-ready release readiness checklist that captures the
technical go/no-go checks, rollout verification, and rollback triggers for a
service deployment.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Deploy</strong></a> — Ship to users with appropriate operational support, monitoring, and rollback plans.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/05-deploy/deployment-checklist.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/deploy/monitoring-setup/">Monitoring Setup</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/deployment-checklist.md"><code>docs/helix/05-deploy/deployment-checklist.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Deployment Checklist Generation Prompt

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
- The final decision section makes the release auditable.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
- Notes: [exceptions, deferred checks, follow-up]</code></pre></details></td></tr>
</tbody>
</table>
