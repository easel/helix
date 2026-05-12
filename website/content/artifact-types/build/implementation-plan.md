---
title: "Implementation Plan"
linkTitle: "Implementation Plan"
slug: implementation-plan
phase: "Build"
artifactRole: "core"
weight: 10
generated: true
---

## Purpose

Build-phase plan that decomposes approved design into implementation slices,
sequencing, ownership, validation gates, and evidence expectations.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Build</strong></a> — Implement against the specs and tests. Capture the implementation plan that scopes the work.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/04-build/implementation-plan.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/deploy/release-notes/">Release Notes</a><br><a href="/artifact-types/deploy/deployment-checklist/">Deployment Checklist</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/04-build/implementation-plan.md"><code>docs/helix/04-build/implementation-plan.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Build Plan Generation Prompt

Create the canonical build plan for the Build phase. Keep it short, but preserve the sequencing, issue boundaries, and verification rules needed to execute implementation against the test plan and technical designs.

## Storage Location

`docs/helix/04-build/implementation-plan.md`

## Required Inputs

- `docs/helix/03-test/test-plan.md` and `docs/helix/03-test/test-plans/TP-*.md`
- `docs/helix/02-design/technical-designs/TD-*.md`
- project-level design constraints

## Include

- scope and governing artifacts
- build order and dependencies
- issue decomposition rules
- quality gates and closeout criteria
- risks that should refine upstream artifacts

## Template

`.ddx/plugins/helix/workflows/phases/04-build/artifacts/implementation-plan/template.md`
For tracker conventions see `ddx bead --help`.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Build Plan

## Scope

**Governing Artifacts**:
- [docs/helix/01-frame/...]
- [docs/helix/02-design/...]
- [docs/helix/03-test/...]

## Shared Constraints

- [Constraint from requirements, design, architecture, or security]

## Build Sequencing

| Order | Story / Area | Governing Artifacts | Depends On | Notes |
|------|---------------|---------------------|------------|-------|
| 1 | [US-XXX or area] | [TP/TD refs] | None | [Why first] |
| 2 | [US-XXX or area] | [TP/TD refs] | [Dependency] | [Why next] |

## Issue Decomposition

Story-level work is tracked via `ddx bead` in `.ddx/beads.jsonl`.

**Per-issue requirements**:
- Labels: `helix`, `phase:build`, `kind:build`, `story:US-{story-id}`
- References: user story, technical design, story test plan, this build plan
- `spec-id` pointing at the nearest governing artifact
- Blockers as dependency links

| Story / Area | Goal | Dependencies |
|--------------|------|--------------|
| [US-XXX] | [Outcome] | [Deps] |

## Quality Gates

- [ ] Failing tests exist before implementation starts
- [ ] All required tests pass before closing a build issue
- [ ] Behavior changes update canonical documents
- [ ] Code review is complete before phase exit

## Risks

| Risk | Impact | Response |
|------|--------|----------|
| [Risk] | [H/M/L] | [Action] |

## Exit Criteria

- [ ] Build issue set is defined with sequence and dependencies
- [ ] Shared constraints are documented
- [ ] Verification expectations are explicit

## Review Checklist

Use this checklist when reviewing an implementation plan:

- [ ] Governing artifacts are listed and exist on disk
- [ ] Shared constraints trace back to requirements, design, or architecture
- [ ] Build sequence has a justified ordering — not just arbitrary
- [ ] Dependencies between build steps are explicit
- [ ] Each story/area references its governing artifacts (TP, TD)
- [ ] Issue decomposition follows tracker conventions (labels, spec-id, deps)
- [ ] Quality gates are specific and enforceable, not aspirational
- [ ] Risks have concrete responses (&quot;we do X&quot;), not vague strategies
- [ ] Plan is consistent with governing test plan and technical designs</code></pre></details></td></tr>
</tbody>
</table>
