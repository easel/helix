---
title: "Feature Registry"
slug: feature-registry
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/feature-registry
---

## What it is

Central registry tracking all features, their status, dependencies,
and ownership throughout the project lifecycle. Single source of
truth for feature identification and tracking.

## Activity

**[Frame](/reference/glossary/activities/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/feature-registry.md`

## Relationships

### Requires (upstream)

- [PRD](../prd/)
- [Feature specifications](../feature-specification/) *(optional)*

### Enables (downstream)

_None._

### Referenced by

- Project Dashboard
- [Release Notes](../release-notes/)
- Progress Reports

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Feature Registry Generation Prompt
Maintain the feature registry as the source of truth for IDs, status, dependencies, ownership, and traceability.

## Focus
- Assign new FEAT-XXX IDs sequentially.
- Keep status changes and dependencies explicit.
- Preserve traceability to stories, designs, contracts, tests, and code.

## Completion Criteria
- Entries are brief and complete.
- IDs are unique and never reused.
- The registry stays easy to scan.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Feature Registry

**Status**: [Active | Archived]
**Last Updated**: [Date]

## Active Features

| ID | Name | Description | Status | Priority | Owner | Updated |
|----|------|-------------|--------|----------|-------|---------|
| FEAT-001 | [Name] | [Brief description] | [Status] | P0 | [Owner] | [Date] |

## Status Definitions

- **Draft**: Requirements being gathered
- **Specified**: Feature spec complete (Frame done)
- **Designed**: Technical design complete (Design done)
- **In Test**: Tests being written
- **In Build**: Implementation in progress
- **Deployed**: Released to production
- **Deprecated**: Scheduled for removal

## Dependencies

| Feature | Depends On | Type | Notes |
|---------|------------|------|-------|
| FEAT-002 | FEAT-001 | Required | [Why] |

## Feature Categories

### [Category Name]
- FEAT-XXX: [Feature Name]

## ID Rules

1. Sequential numbering: FEAT-XXX (zero-padded 3 digits)
2. Never reuse IDs, even for cancelled features
3. Optionally reserve ranges for teams/categories

## Deprecated/Cancelled

| ID | Name | Status | Reason | Date |
|----|------|--------|--------|------|
| FEAT-XXX | [Name] | [Cancelled/Deprecated] | [Why] | [Date] |
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
