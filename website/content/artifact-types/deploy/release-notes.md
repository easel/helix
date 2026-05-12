---
title: "Release Notes"
linkTitle: "Release Notes"
slug: release-notes
phase: "Deploy"
artifactRole: "core"
weight: 11
generated: true
---

## Purpose

Release-scoped communication artifact that summarizes shipped user-visible
and operator-visible changes, required actions, and known caveats for one
rollout.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Deploy</strong></a> — Ship to users with appropriate operational support, monitoring, and rollback plans.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/05-deploy/release-notes.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/05-deploy/release-notes.md"><code>docs/helix/05-deploy/release-notes.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Release Notes Prompt

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

Use the template at `.ddx/plugins/helix/workflows/phases/05-deploy/artifacts/release-notes/template.md`.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
- Support or escalation path: [link]</code></pre></details></td></tr>
</tbody>
</table>
