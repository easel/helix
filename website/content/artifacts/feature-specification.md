---
title: "Feature Specification"
slug: feature-specification
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/feature-specification
---

## What it is

Detailed specifications for each feature including functional and
non-functional requirements, constraints, and edge cases. Uses
[NEEDS CLARIFICATION] markers for ambiguous requirements.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/features/`

## Relationships

### Requires (upstream)

- [PRD](../prd/) — derives features from requirements

### Enables (downstream)

- [User Stories](../user-stories/) — stories implement feature slices

### Informs

- [User Stories](../user-stories/)
- [Solution Design](../solution-design/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Feature Specification Generation Prompt

Create a feature specification that is precise enough to support design,
user story creation, and test planning.

## Storage Location

Store at: `docs/helix/01-frame/features/FEAT-NNN-<name>.md`

## Purpose

A feature spec defines the **scope and requirements** for one major
capability. It sits between the PRD (which defines what the product needs)
and user stories (which define vertical slices for implementation). The
feature spec owns requirements; user stories own the user journey.

## Key Principles

- **Scope, not solution** — describe what the feature must do, not how to
  build it. Implementation details belong in design docs.
- **One feature, one spec** — if a spec covers two independent capabilities,
  split it.
- **Stories by reference** — list user story IDs, don't duplicate story
  content. Stories are separate files with their own lifecycle.
- **Testable requirements** — every functional requirement should be
  verifiable. If you can't describe how to test it, it's too vague.
- **Leave unknowns explicit** — use Open Questions at the bottom rather than
  inventing detail you don't have.

## Section-by-Section Guidance

### Overview
Connect this feature to a specific PRD requirement. "This feature implements
PRD P0-3" is better than "This feature improves the user experience."

### Problem Statement
Same standard as the PRD: describe the failure mode, not the absence of your
feature. Quantify where possible.

### Functional Requirements
Number each requirement for traceability. Each one should be independently
testable. These are what the feature must do — user stories describe how
users interact with these capabilities.

### Non-Functional Requirements
Every NFR needs a specific target. "Must be fast" is not a requirement.
"95th percentile response under 200ms" is. Only include NFRs relevant to
this specific feature, not product-wide NFRs from the PRD.

### User Stories
Reference by ID and title with a relative link. Do not duplicate story
content — the story file is the source of truth. If stories haven't been
written yet, list placeholders with `[TODO: create story]` and note it in
Open Questions.

### Edge Cases and Error Handling
Feature-level edge cases that span multiple stories. If an edge case is
specific to one story, it belongs in that story's file.

### Success Metrics
Feature-specific metrics, not product-level metrics from the PRD. How do
you know this specific feature is working as intended?

### Dependencies
Name specific feature IDs, external APIs, and PRD requirement numbers.
"Depends on auth" is too vague. "Depends on FEAT-002 (auth middleware)
and the OAuth2 provider API" is specific.

### Out of Scope
Each item should prevent a plausible scope question during implementation.
"Not a replacement for the database" is only useful if someone might think
it is.

## Quality Checklist

After drafting, verify every item. If any blocking check fails, revise before
committing.

### Blocking

- [ ] Overview links to a specific PRD requirement
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
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: FEAT-XXX
  depends_on:
    - helix.prd
---
# Feature Specification: FEAT-XXX — [Feature Name]

**Feature ID**: FEAT-XXX
**Status**: [Draft | Specified | Approved]
**Priority**: [P0 | P1 | P2]
**Owner**: [Team/Person]

## Overview

[What this feature is and why it exists. 2-3 sentences connecting this feature
to a specific PRD requirement.]

## Problem Statement

- **Current situation**: [What exists now — be specific]
- **Pain points**: [What is not working and for whom]
- **Desired outcome**: [What success looks like — measurable]

## Requirements

### Functional Requirements

[Each requirement should be testable. Number them for traceability.]

1. [Requirement]
2. [Requirement]

### Non-Functional Requirements

- **Performance**: [Specific target, e.g., "95th percentile response < 200ms"]
- **Security**: [Specific requirement, not "must be secure"]
- **Scalability**: [Specific target, e.g., "handles 10k concurrent users"]
- **Reliability**: [Specific target, e.g., "99.9% uptime"]

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
- [ ] Problem statement describes what exists now and what is broken — not just what is wanted
- [ ] Every functional requirement is testable — you can write an assertion for it
- [ ] Non-functional requirements have specific numeric targets, not "must be fast"
- [ ] Edge cases cover realistic failure scenarios, not just happy paths
- [ ] Success metrics are specific to this feature, not product-level metrics
- [ ] Dependencies reference real artifact IDs (FEAT-XXX, external APIs)
- [ ] Out of scope excludes things someone might reasonably assume are in scope
- [ ] No implementation details ("use X library", "create Y table") — specify WHAT not HOW
- [ ] Feature is consistent with governing PRD requirements
- [ ] No `[NEEDS CLARIFICATION]` markers remain unresolved for P0 features
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
