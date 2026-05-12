---
title: "Feature Registry"
linkTitle: "Feature Registry"
slug: feature-registry
phase: "Frame"
artifactRole: "supporting"
weight: 17
generated: true
---

## Purpose

Central registry tracking all features, their status, dependencies,
and ownership throughout the project lifecycle. Single source of
truth for feature identification and tracking.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/feature-registry.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Referenced by</th><td>Project Dashboard<br><a href="/artifact-types/deploy/release-notes/">Release Notes</a><br>Progress Reports</td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Feature Registry Generation Prompt
Maintain the feature registry as the source of truth for IDs, status, dependencies, ownership, and traceability.

## Focus
- Assign new FEAT-XXX IDs sequentially.
- Keep status changes and dependencies explicit.
- Preserve traceability to stories, designs, contracts, tests, and code.

## Completion Criteria
- Entries are brief and complete.
- IDs are unique and never reused.
- The registry stays easy to scan.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
| FEAT-XXX | [Name] | [Cancelled/Deprecated] | [Why] | [Date] |</code></pre></details></td></tr>
</tbody>
</table>
