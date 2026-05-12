---
title: "Feature Specification"
linkTitle: "Feature Specification"
slug: feature-specification
phase: "Frame"
artifactRole: "core"
weight: 13
generated: true
---

## Purpose

A feature spec defines the **scope and requirements** for one major
capability. It sits between the PRD (which defines what the product needs)
and user stories (which define vertical slices for implementation). The
feature spec owns requirements; user stories own the user journey.

## Authoring guidance

- **Future state before current pain** — describe the desired user-visible
  outcome before optimizing around today's broken surface. The problem statement
  explains why the change is needed; it should not be the only organizing frame.
- **Scope, not solution** — describe what the feature must do, not how to
  build it. Implementation details belong in design docs.
- **One feature, one spec** — if a spec covers two independent capabilities,
  split it.
- **Functional areas before requirements** — when a feature spans multiple
  surfaces, user modes, workflow stages, or domain objects, name those areas
  before writing requirements. Group requirements by area instead of producing
  one flat list.
- **Separate similar domain objects** — if readers might confuse two things,
  define them separately before requirements. For example, "Artifacts" are
  project-specific instances; "Artifact Types" are reusable methodology
  definitions.

_Additional guidance continues in the full prompt below._

<details>
<summary>Quality checklist from the prompt</summary>

After drafting, verify every item. If any blocking check fails, revise before
committing.

### Blocking

- [ ] Overview links to a specific PRD requirement
- [ ] Ideal Future State is present for broad product-surface, workflow, IA, or documentation features
- [ ] Functional Areas is present when the feature spans multiple surfaces, workflows, user modes, or domain objects
- [ ] Similar domain objects are separated before requirements are written
- [ ] Functional requirements are grouped by area when a flat list would mix unrelated scopes
- [ ] Every functional requirement is testable
- [ ] Non-functional requirements have specific numeric targets
- [ ] User stories are referenced by ID (not duplicated inline)
- [ ] Dependencies name specific feature IDs and external systems
- [ ] No `[NEEDS CLARIFICATION]` markers remain

### Warning

- [ ] Problem statement quantifies the pain
- [ ] At least one feature-level edge case documented
- [ ] Success metrics are feature-specific (not product-level)
- [ ] Out of scope excludes something plausible

</details>

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/features/</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/frame/user-stories/">User Stories</a><br><a href="/artifact-types/design/solution-design/">Solution Design</a><br>Api Contracts<br><a href="/artifact-types/test/test-plan/">Test Plan</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/01-frame/features/FEAT-002-helix-cli.md"><code>docs/helix/01-frame/features/FEAT-002-helix-cli.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Feature Specification Generation Prompt

Create a feature specification that is precise enough to support design,
user story creation, and test planning.

## Storage Location

Store at: `docs/helix/01-frame/features/FEAT-NNN-&lt;name&gt;.md`

## Purpose

A feature spec defines the **scope and requirements** for one major
capability. It sits between the PRD (which defines what the product needs)
and user stories (which define vertical slices for implementation). The
feature spec owns requirements; user stories own the user journey.

## Key Principles

- **Future state before current pain** — describe the desired user-visible
  outcome before optimizing around today&#x27;s broken surface. The problem statement
  explains why the change is needed; it should not be the only organizing frame.
- **Scope, not solution** — describe what the feature must do, not how to
  build it. Implementation details belong in design docs.
- **One feature, one spec** — if a spec covers two independent capabilities,
  split it.
- **Functional areas before requirements** — when a feature spans multiple
  surfaces, user modes, workflow stages, or domain objects, name those areas
  before writing requirements. Group requirements by area instead of producing
  one flat list.
- **Separate similar domain objects** — if readers might confuse two things,
  define them separately before requirements. For example, &quot;Artifacts&quot; are
  project-specific instances; &quot;Artifact Types&quot; are reusable methodology
  definitions.
- **Stories by reference** — list user story IDs, don&#x27;t duplicate story
  content. Stories are separate files with their own lifecycle.
- **Testable requirements** — every functional requirement should be
  verifiable. If you can&#x27;t describe how to test it, it&#x27;s too vague.
- **Leave unknowns explicit** — use Open Questions at the bottom rather than
  inventing detail you don&#x27;t have.

## Section-by-Section Guidance

### Overview
Connect this feature to a specific PRD requirement. &quot;This feature implements
PRD P0-3&quot; is better than &quot;This feature improves the user experience.&quot;

### Ideal Future State
Describe the target state in user-visible terms. A good future state answers:

- What can the user understand, decide, or accomplish?
- What does the product surface make clear?
- How should the feature feel when it is working well?

For IA, documentation, onboarding, workflow, or product-surface features, this
section is mandatory. It should lead the spec toward the desired experience,
not merely away from the current failure mode.

### Problem Statement
Same standard as the PRD: describe the failure mode, not the absence of your
feature. Quantify where possible. Keep it subordinate to the future state; do
not let the spec become a list of current complaints.

### Functional Areas
Use this section whenever a feature has more than one surface, reader mode,
workflow stage, or domain object. The area map should make clear what belongs
where before requirements are written.

Examples:

- Home, Why, Use, Artifact Types, Artifacts, Concerns, Reference, Navigation
- Intake, Planning, Execution, Review, Reporting
- Admin, Operator, End user, Auditor
- API contract, CLI surface, generated docs, validation

### Functional Requirements
Number each requirement for traceability. Group requirements by functional
area when the feature spans multiple areas. Use stable prefixes that make the
scope clear (`NAV-01`, `TYPE-01`, `ART-01`) or use plain `FR-01` for narrow
single-area features.

Each requirement should be independently testable. These are what the feature
must do — user stories describe how users interact with these capabilities.

If a requirement mentions two areas joined by &quot;and&quot;, split it unless the
relationship between those areas is itself the requirement.

### Non-Functional Requirements
Every NFR needs a specific target. &quot;Must be fast&quot; is not a requirement.
&quot;95th percentile response under 200ms&quot; is. Only include NFRs relevant to
this specific feature, not product-wide NFRs from the PRD.

### User Stories
Reference by ID and title with a relative link. Do not duplicate story
content — the story file is the source of truth. If stories haven&#x27;t been
written yet, list placeholders with `[TODO: create story]` and note it in
Open Questions.

### Edge Cases and Error Handling
Feature-level edge cases that span multiple stories. If an edge case is
specific to one story, it belongs in that story&#x27;s file.

### Success Metrics
Feature-specific metrics, not product-level metrics from the PRD. How do
you know this specific feature is working as intended?

### Dependencies
Name specific feature IDs, external APIs, and PRD requirement numbers.
&quot;Depends on auth&quot; is too vague. &quot;Depends on FEAT-002 (auth middleware)
and the OAuth2 provider API&quot; is specific.

### Out of Scope
Each item should prevent a plausible scope question during implementation.
&quot;Not a replacement for the database&quot; is only useful if someone might think
it is.

## Quality Checklist

After drafting, verify every item. If any blocking check fails, revise before
committing.

### Blocking

- [ ] Overview links to a specific PRD requirement
- [ ] Ideal Future State is present for broad product-surface, workflow, IA, or documentation features
- [ ] Functional Areas is present when the feature spans multiple surfaces, workflows, user modes, or domain objects
- [ ] Similar domain objects are separated before requirements are written
- [ ] Functional requirements are grouped by area when a flat list would mix unrelated scopes
- [ ] Every functional requirement is testable
- [ ] Non-functional requirements have specific numeric targets
- [ ] User stories are referenced by ID (not duplicated inline)
- [ ] Dependencies name specific feature IDs and external systems
- [ ] No `[NEEDS CLARIFICATION]` markers remain

### Warning

- [ ] Problem statement quantifies the pain
- [ ] At least one feature-level edge case documented
- [ ] Success metrics are feature-specific (not product-level)
- [ ] Out of scope excludes something plausible</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Feature Specification: FEAT-XXX — [Feature Name]

**Feature ID**: FEAT-XXX
**Status**: [Draft | Specified | Approved]
**Priority**: [P0 | P1 | P2]
**Owner**: [Team/Person]

## Overview

[What this feature is and why it exists. 2-3 sentences connecting this feature
to a specific PRD requirement.]

## Ideal Future State

[Describe the future product behavior once this feature is working well. Focus
on what users can understand, decide, or accomplish. For broad product-surface,
workflow, IA, or documentation features, this section should come before the
problem framing so requirements are pulled toward the desired outcome instead
of only reacting to current pain.]

## Problem Statement

- **Current situation**: [What exists now — be specific]
- **Pain points**: [What is not working and for whom]
- **Desired outcome**: [What success looks like — measurable]

## Functional Areas

[For features that span more than one surface, user mode, workflow stage, or
domain object, map the areas before writing requirements. This prevents
unrelated requirements from collapsing into one list. Omit only when the
feature is a single narrow capability.]

| Area | User question or job | Feature responsibility |
|------|----------------------|------------------------|
| [Area] | [What the user needs to know or do] | [What this feature must provide] |

## Requirements

### Functional Requirements by Area

[Each requirement should be testable. Group requirements by functional area
when the feature has multiple areas. Use stable prefixes that make the scope
clear, such as `HOME-01`, `TYPE-01`, `NAV-01`, or `FR-01` for narrow features.]

#### [Area Name]

[PREFIX-01]. [Requirement]
[PREFIX-02]. [Requirement]

### Non-Functional Requirements

- **Performance**: [Specific target, e.g., &quot;95th percentile response &lt; 200ms&quot;]
- **Security**: [Specific requirement, not &quot;must be secure&quot;]
- **Scalability**: [Specific target, e.g., &quot;handles 10k concurrent users&quot;]
- **Reliability**: [Specific target, e.g., &quot;99.9% uptime&quot;]

## User Stories

[List the user stories that implement this feature. Each story is a separate
file in `docs/helix/01-frame/user-stories/`. Reference by ID — do not
duplicate story content here.]

- [US-XXX — Story title](../user-stories/US-XXX-slug.md)
- [US-XXX — Story title](../user-stories/US-XXX-slug.md)

## Edge Cases and Error Handling

[Feature-level edge cases that span multiple stories. Story-specific edge
cases belong in the story file.]

- **[Condition]**: [Expected behavior]

## Success Metrics

[How do we know this feature is working? Metrics specific to this feature,
not the product-level metrics from the PRD.]

- [Metric with target]

## Constraints and Assumptions

- [Constraint or assumption specific to this feature]

## Dependencies

- **Other features**: [FEAT-XXX if this feature depends on another]
- **External services**: [APIs, libraries, or systems this feature requires]
- **PRD requirements**: [Which P0/P1/P2 requirements this addresses]

## Out of Scope

[What this feature explicitly does not cover. Each item should prevent a
plausible scope question.]

## Review Checklist

Use this checklist when reviewing a feature specification:

- [ ] Overview connects this feature to a specific PRD requirement
- [ ] Ideal future state describes the desired user-visible outcome, not only current problems
- [ ] Problem statement describes what exists now and what is broken — not just what is wanted
- [ ] Functional areas are mapped when the feature spans multiple surfaces, workflows, or domain objects
- [ ] Requirements are grouped by functional area when a flat list would mix unrelated scopes
- [ ] Domain objects that sound similar are explicitly separated (for example, artifact instances vs artifact types)
- [ ] Every functional requirement is testable — you can write an assertion for it
- [ ] Non-functional requirements have specific numeric targets, not &quot;must be fast&quot;
- [ ] Edge cases cover realistic failure scenarios, not just happy paths
- [ ] Success metrics are specific to this feature, not product-level metrics
- [ ] Dependencies reference real artifact IDs (FEAT-XXX, external APIs)
- [ ] Out of scope excludes things someone might reasonably assume are in scope
- [ ] No implementation details (&quot;use X library&quot;, &quot;create Y table&quot;) — specify WHAT not HOW
- [ ] Feature is consistent with governing PRD requirements
- [ ] No `[NEEDS CLARIFICATION]` markers remain unresolved for P0 features</code></pre></details></td></tr>
</tbody>
</table>
