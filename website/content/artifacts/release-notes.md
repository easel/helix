---
title: "Release Notes"
slug: release-notes
phase: "Deploy"
weight: 500
generated: true
aliases:
  - /reference/glossary/artifacts/release-notes
---

## What it is

Release-scoped communication artifact that summarizes shipped user-visible
and operator-visible changes, required actions, and known caveats for one
rollout.

## Phase

**[Phase 5 — Deploy](/reference/glossary/phases/)** — Ship to users with appropriate operational support, monitoring, and rollback plans.

## Output location

`docs/helix/05-deploy/release-notes.md`

## Relationships

### Requires (upstream)

- [Feature Registry](../feature-registry/) *(optional)*
- [Implementation Plan](../implementation-plan/) *(optional)*
- [Deployment Checklist](../deployment-checklist/) *(optional)*
- [Runbook](../runbook/) *(optional)*

### Enables (downstream)

_None._

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Release Notes Prompt

Create release-specific notes for one shipped rollout.

## Required Inputs
- release scope, version, and date
- shipped features, fixes, and operator-visible changes
- breaking changes, migrations, or rollout caveats
- known issues and support or rollback guidance
- links to deeper docs such as feature docs, deployment checklist, or runbook

## Produced Output
- `docs/helix/05-deploy/release-notes.md`

## Focus

Keep the document tightly scoped to what actually shipped in this release.
Write for readers who need to understand impact quickly: what changed, who is
affected, and what action they need to take.

Differentiate release notes from adjacent surfaces:

- `deployment-checklist` decides whether rollout can proceed
- `runbook` explains operator response procedures
- `CHANGELOG.md` records repository history
- `release-notes` communicate the release itself to users and operators

Lead with the most important highlights, then make required actions, breaking
changes, migrations, and known issues explicit. If no action is required or no
breaking changes exist, say that clearly.

Do not produce roadmap filler, a GTM plan, or a cross-functional launch
checklist. Launch coordination belongs in linked `phase:deploy` tracker work
plus the adjacent deploy artifacts (`deployment-checklist`, `monitoring-setup`,
and `runbook`), not inside release notes.

## Completion Criteria
- [ ] Release scope, audience, and channels are explicit
- [ ] Highlights and change summaries are limited to what actually shipped
- [ ] Required user or operator actions are explicit, or the document states none
- [ ] Breaking changes, migration guidance, and known issues are clear when relevant
- [ ] References point readers to deeper docs or support paths when needed

Use the template at `.ddx/plugins/helix/workflows/phases/05-deploy/artifacts/release-notes/template.md`.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Release Notes - [Release / Version]

## Release Scope

- Release identifier or version: [tag, version, or name]
- Release date: [YYYY-MM-DD]
- Rollout window or environment: [production, staged rollout, region]
- Release owner: [name or role]
- Source commit or build: [SHA, image tag, or build link]

## Audience and Channels

| Audience | Why they care | Delivery channel |
|----------|---------------|------------------|
| [end users] | [impact] | [email, docs, in-app, status page] |
| [operators or support] | [impact] | [runbook, team channel, incident channel] |
| [internal stakeholders] | [impact] | [release post, team update] |

## Highlights

- [highest-value shipped change]
- [second important change]
- [critical fix or operational improvement]

## Changes and Fixes

### New or Improved

| Area | What changed | Who is affected |
|------|--------------|-----------------|
| [feature or workflow] | [summary] | [users, operators, admins] |
| [feature or workflow] | [summary] | [users, operators, admins] |

### Fixes

| Issue or symptom | Resolution | User or operator impact |
|------------------|------------|-------------------------|
| [bug or failure mode] | [what is fixed] | [why it matters] |
| [bug or failure mode] | [what is fixed] | [why it matters] |

## Breaking Changes and Required Actions

If there are no breaking changes or required actions, state that explicitly.

| Change | Impact | Required action | Deadline or trigger |
|--------|--------|-----------------|---------------------|
| [breaking change] | [who is affected] | [migration or config step] | [before upgrade, after rollout] |

## Migration or Rollback Guidance

### Upgrade or Migration

1. [step one]
2. [step two]
3. [validation step]

### Rollback or Hold Guidance

- Pause rollout when: [condition]
- Roll back using: [runbook entrypoint or command]
- Ask for help in: [channel, team, or support path]

## Known Issues and Support

| Issue | Who is affected | Workaround or next step |
|------|------------------|-------------------------|
| [known issue] | [audience] | [workaround, mitigation, or ETA] |
| [known issue] | [audience] | [workaround, mitigation, or ETA] |

## References

- Deployment checklist: [link]
- Runbook: [link]
- Feature docs or changelog: [link]
- Support or escalation path: [link]
``````

</details>

## Example

This example is HELIX's actual release notes, sourced from [`docs/helix/05-deploy/release-notes.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/release-notes.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Release Notes — HELIX v0.3.3

### Release Scope

- Release identifier or version: `v0.3.3`
- Release date: 2026-04 (operator-driven; tag commit `0db3ea8`)
- Rollout window or environment: HELIX plugin (consumed by users via repo
  tag) and the public website at `https://documentdrivendx.github.io/helix/`
- Release owner: HELIX maintainer cutting the tag
- Source commit or build: `0db3ea8` (tag `v0.3.3`)

### Audience and Channels

| Audience | Why they care | Delivery channel |
|----------|---------------|------------------|
| HELIX plugin users | New CI behavior and review-threshold knob affect day-to-day `helix run` output | Plugin repo tag; release notes in `docs/helix/05-deploy/release-notes.md` |
| Website readers | Public docs at `documentdrivendx.github.io/helix/` updated to the tag | GitHub Pages rebuild; release-notes page |
| HELIX maintainers | Test-suite stability changes need to be folded into local development practice | Repo issues and the `helix-commit` workflow |

### Highlights

- **CI stability**: `tests/helix-cli.sh` now filters spurious DDx update
  notices that were causing intermittent CI red without indicating a real
  regression.
- **Review-threshold knob**: A configurable threshold gates how aggressively
  `helix run --review-every N` triggers periodic alignment, giving operators
  more control over review cadence on long-running queues.
- **Plugin manifest correctness**: A dangling hooks reference in
  `.claude-plugin/plugin.json` was removed; fresh plugin installs no longer
  emit a manifest-validation warning.

### Changes and Fixes

#### New or Improved

| Area | What changed | Who is affected |
|------|--------------|-----------------|
| CLI / wrapper | `--review-threshold` accepted on `helix run` to tune periodic-alignment cadence | Operators running long `helix run` sessions |
| CI | `tests/helix-cli.sh` filters DDx update notices from harness output before assertions | HELIX maintainers and contributors |
| Tracker / forge | Forge-agent discovery tracker issue added to capture follow-up work | HELIX maintainers |

#### Fixes

| Issue or symptom | Resolution | User or operator impact |
|------------------|------------|-------------------------|
| Intermittent CI red on `tests/helix-cli.sh` from DDx update banners | Banner filter applied before stdout assertions | Stable green CI; no operator action |
| Manifest validation warning on plugin install | Dangling hooks reference removed from `.claude-plugin/plugin.json` | Fresh installs are clean |

### Breaking Changes and Required Actions

There are no breaking changes in `v0.3.3`. No operator action is required.

### Migration or Rollback Guidance

#### Upgrade or Migration

1. Pull the new tag: `git fetch --tags && git checkout v0.3.3` in your
   HELIX checkout (or repoint your plugin install at the new tag).
2. Re-run `bash scripts/install-local-skills.sh` to refresh the local
   skill installation.
3. No tracker or schema migration is required — `.ddx/beads.jsonl` is
   forward-compatible.

#### Rollback or Hold Guidance

- Pause rollout when: a downstream consumer reports `--review-threshold`
  parsing errors, or when `tests/helix-cli.sh` regresses against the new
  tag in CI.
- Roll back using: `git checkout v0.3.2` and re-run
  `bash scripts/install-local-skills.sh`. The previous tag is fully
  compatible with the current `.ddx/beads.jsonl` schema.
- Ask for help in: the HELIX repo issue tracker.

### Known Issues and Support

| Issue | Who is affected | Workaround or next step |
|------|------------------|-------------------------|
| Forge-agent discovery is tracked as a follow-up bead but not yet implemented | Operators wanting auto-discovery of forge agents | Continue using explicit agent configuration; track the linked tracker issue |

### References

- Deployment checklist: [`deployment-checklist.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/deployment-checklist.md)
- Runbook: [`runbook.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/runbook.md)
- Plugin manifest: `.claude-plugin/plugin.json`
- Support or escalation path: HELIX repo issue tracker
