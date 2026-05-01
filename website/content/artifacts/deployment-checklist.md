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

This example is HELIX's actual deployment checklist, sourced from [`docs/helix/05-deploy/deployment-checklist.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/deployment-checklist.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Deployment Checklist — HELIX Plugin and Website Release

### Release Scope

- Service or component: HELIX plugin (`.claude-plugin/`, `skills/`,
  `workflows/`, `bin/helix`, `scripts/helix`) and the public website
  (`website/`, deployed to GitHub Pages).
- Version or commit: `vX.Y.Z` tag at the release commit SHA.
- Deployment window: Operator-driven; HELIX releases ship when the release
  bead reaches `Go` on this checklist. There is no fixed schedule.
- Release owner: HELIX maintainer cutting the tag.
- Rollback owner: Same operator (single-operator release flow).

### Pre-Deploy Checks

| Area | Check | Evidence or Command | Status |
|------|-------|---------------------|--------|
| Build | Wrapper-CLI test suite is green | `bash tests/helix-cli.sh` | [ ] |
| Build | Plugin layout validation passes | `bash tests/validate-skills.sh` | [ ] |
| Build | Website builds clean (no Hugo errors, no broken shortcodes) | `cd website && hugo --gc --minify` | [ ] |
| Build | Reference generator runs without stale-mapping errors | `uv run scripts/generate-reference.py` | [ ] |
| Build | Workflow-paths pre-commit check passes | `lefthook run pre-commit --all-files` (or `git diff --check`) | [ ] |
| Config | No tracked secrets in repo | `git grep -nE 'OPENROUTER_API_KEY|ANTHROPIC_API_KEY|sk-[a-zA-Z0-9]'` returns only documentation | [ ] |
| Config | Plugin manifest version matches the tag | `grep '"version"' .claude-plugin/plugin.json` | [ ] |
| Data | No tracker drift between live `.ddx/beads.jsonl` and any docs being shipped as examples | `uv run scripts/generate-reference.py` (validates HELIX_REAL_EXAMPLES paths) | [ ] |
| Ops | `helix run --dry-run` produces a coherent next-action summary against the release tag | `helix run --dry-run` | [ ] |
| Ops | Release notes draft exists and references the tag | `docs/helix/05-deploy/release-notes.md` | [ ] |
| Ops | Demos still record cleanly | `cd website && bash record-demos.sh` (when demos changed in the release) | [ ] |

### Rollout Plan

| Stage | Action | Exit Condition |
|-------|--------|----------------|
| Local proof | Run all pre-deploy checks against the release commit | All checks above are checked |
| Tag and push | `git tag -a vX.Y.Z -m "..."` then `git push origin main vX.Y.Z` | Tag visible on origin; CI starts |
| Plugin publication | Plugin is consumed by users via repo URL — no separate registry push | Tag exists; `git fetch --tags` from a fresh clone resolves the manifest |
| Website rollout | GitHub Actions builds the site from the tagged commit and publishes to GitHub Pages | Pages workflow run succeeds; public URL serves the new content |
| Full rollout | Smoke-test the public site for the released artifact pages | Critical pages (`/`, `/why/`, `/use/`, `/artifacts/<each>/`) return 200 |

### Verification Checks

| Signal or Check | Expected Result | Evidence or Command | Status |
|-----------------|-----------------|---------------------|--------|
| Public site root reachable | HTTP 200 | `curl -fsS -o /dev/null -w '%{http_code}' https://documentdrivendx.github.io/helix/` | [ ] |
| Released artifact pages render | HTTP 200 with expected H1 | `curl -fsS https://documentdrivendx.github.io/helix/artifacts/contract/ \| grep -q "DDx"` | [ ] |
| Plugin install from tag works | A fresh clone of the tag installs and `helix run --dry-run` runs | Manual: clone tag, run `bash scripts/install-local-skills.sh`, then `helix run --dry-run` | [ ] |
| `helix run` against a sample bead succeeds | `NEXT_ACTION` is one of the documented values | `helix run --dry-run` in a sample repo | [ ] |
| No regressions in deterministic tests | All pass | `bash tests/helix-cli.sh && bash tests/validate-skills.sh` against the tag | [ ] |

### Rollback Triggers

| Trigger | Threshold or Condition | Immediate Action | Owner |
|---------|------------------------|------------------|-------|
| Public site fails to build under the new tag | Pages workflow run fails | Re-run the workflow once; if still failing, revert the tag commit and re-tag | Operator |
| Plugin install breaks for a fresh consumer | `bash scripts/install-local-skills.sh` exits non-zero on a clean checkout | Move the `vX.Y.Z` tag back one commit (`git tag -d` + force-push) only if no downstream consumers have pulled; otherwise issue a `vX.Y.Z+1` patch | Operator |
| Wrapper-CLI test suite regressed in CI on the tag | `tests/helix-cli.sh` fails on the tag in CI | Revert the offending change in a follow-up tag; do not silently amend the released tag | Operator |
| Critical artifact-reference page renders empty | A `HELIX_REAL_EXAMPLES_PUBLISHABLE` slug ships with a missing example | Patch release that flips the slug back off in `scripts/generate-reference.py` | Operator |

### Go or No-Go Decision

- Decision: [Go / Hold / Roll Back]
- Decision time: [ISO-8601 timestamp]
- Notes: Capture any deferred checks, exceptions, or known follow-up beads
  here. Reference the release-notes commit and the tag SHA so the decision
  is reconstructable from the tracker.
