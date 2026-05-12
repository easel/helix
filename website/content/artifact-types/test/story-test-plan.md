---
title: "Story Test Plan"
linkTitle: "Story Test Plan"
slug: story-test-plan
phase: "Test"
artifactRole: "core"
weight: 11
generated: true
---

## Purpose

The story test plan translates one bounded technical design into executable
verification intent before implementation starts. It maps story acceptance
criteria to concrete failing tests, names the required setup and data, and
gives Build a precise handoff for one story-sized slice.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Test</strong></a> — Define how we know it works. Plans, suites, and procedures that bind specs to implementation.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/03-test/test-plans/TP-{id}-{name}.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/test/test-suites/">Test Suites</a><br><a href="/artifact-types/build/implementation-plan/">Implementation Plan</a></td></tr>
<tr><th>Referenced by</th><td><a href="/artifact-types/design/technical-design/">Technical Design</a><br><a href="/artifact-types/build/implementation-plan/">Implementation Plan</a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Story Test Plan Generation Prompt

Create the canonical story-scoped test plan for one bounded story slice. This
artifact exists because the project-wide `test-plan.md` does not replace the
need for per-story acceptance-to-test traceability.

## Storage Location

`docs/helix/03-test/test-plans/TP-{id}-{name}.md`

## What to Include

- the governing `[[US-XXX-*]]` and `[[TD-XXX-*]]` references
- a tight scope statement plus explicit out-of-scope boundaries
- a matrix mapping each active acceptance criterion to concrete failing tests
- executable proof details: test file paths, commands, or named test cases
- setup, fixtures, seed data, mocks, and environment assumptions
- edge cases and error scenarios that the story must prove before build begins
- build handoff notes that help implementation sequence the work

## Minimum Quality Bar

- Stay story-scoped. Do not drift into feature-wide strategy or generic testing doctrine.
- Name runnable evidence, not just test categories.
- Prefer one compact mapping table over repeated prose.
- If an acceptance criterion is not being covered now, say why explicitly.

Use template at `.ddx/plugins/helix/workflows/phases/03-test/artifacts/story-test-plan/template.md`.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Story Test Plan: TP-XXX-[story-name]

## Story Reference

**User Story**: [[US-XXX-[story-name]]]
**Technical Design**: [[TD-XXX-[story-name]]]
**Related Solution Design**: [[SD-XXX-[feature-name]]] or N/A

## Scope and Objective

**Goal**: [What this story must prove before build starts]

**In Scope**
- [Bounded behavior this TP governs]

**Out of Scope**
- [Adjacent behavior intentionally left to another TP, feature, or future slice]

## Acceptance Criteria Test Mapping

| Acceptance Criterion | Failing Test(s) to Create or Run | Test Level | File or Command | Setup / Data | Notes |
|----------------------|----------------------------------|------------|-----------------|--------------|-------|
| [Given/When/Then criterion] | `[test_name]` | Unit / Integration / Contract / E2E | `tests/...` or `bash ...` | [Fixture, seed, mock] | [Edge case or sequencing note] |

## Executable Proof

### Primary Commands

```bash
[command that proves this TP]
```

### Planned Test Files

- `tests/...`
- `tests/...`

### Coverage Focus

- P0: [Must-pass behavior]
- P1: [Important secondary behavior]

## Data and Setup

| Need | Required For | Source / Strategy |
|------|--------------|-------------------|
| [Fixture / seed / mock / env var] | [Tests] | [Where it comes from] |

## Edge Cases and Failure Modes

- [Boundary value or empty-state handling]
- [Validation failure or invalid input]
- [Dependency failure, timeout, or permission edge]

## Build Handoff

**Implementation Order**
1. [What should be implemented first to turn the first red test green]
2. [What follows once the core path passes]

**Constraints**
- [Constraint inherited from requirements, design, concern, or contract]

**Done When**
- [ ] Every in-scope acceptance criterion has passing evidence
- [ ] Named commands or test files exist and run
- [ ] Out-of-scope coverage remains explicitly deferred rather than silently skipped

## Review Checklist

- [ ] References the governing story and technical design
- [ ] Every active acceptance criterion maps to concrete failing tests
- [ ] File paths, commands, or test identifiers are specific enough to execute
- [ ] Setup, fixtures, mocks, and seed data are explicit
- [ ] Edge cases cover real story risks rather than generic boilerplate
- [ ] Scope remains bounded to one story slice
- [ ] Build handoff gives implementation a usable sequence</code></pre></details></td></tr>
</tbody>
</table>
