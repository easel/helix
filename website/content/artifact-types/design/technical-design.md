---
title: "Technical Design"
linkTitle: "Technical Design"
slug: technical-design
phase: "Design"
artifactRole: "core"
weight: 14
generated: true
---

## Purpose

Story-specific technical design that details HOW to implement a single
user story within the context of the broader solution architecture.
This enables vertical slicing by providing implementation details for
one story at a time.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Design</strong></a> — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/02-design/technical-designs/TD-{id}-{name}.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/test/test-plan/">Test Plan</a><br><a href="/artifact-types/build/implementation-plan/">Implementation Plan</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/technical-designs/TD-002-helix-cli.md"><code>docs/helix/02-design/technical-designs/TD-002-helix-cli.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Technical Design for User Story Prompt
Create a concise technical design for one user story.

## Focus
- Create a story-level artifact named `docs/helix/02-design/technical-designs/TD-XXX-[name].md`.
- Map each acceptance criterion to component changes, interfaces, data, security, and tests.
- Stay on the vertical slice for the story.
- Assume the broader architecture is already set by the parent solution design.
- Do not expand into a feature-wide or system-wide design; that belongs in a
  solution design (`SD-XXX-*`).
- Keep implementation sequence and rollout or migration notes only when they affect execution.

## Completion Criteria
- The story is implementable.
- Key interfaces, changes, and test coverage are explicit.
- The design stays compact.
- The output is clearly story-level and disambiguated from a solution design.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Technical Design: TD-XXX-[story-name]

**User Story**: [[US-XXX]] | **Feature**: [[FEAT-XXX]] | **Solution Design**: [[SD-XXX]]

## Scope

- Story-level design artifact
- Use for one vertical slice or one bounded implementation story
- Must inherit the broader approach from the parent solution design
- Do not redefine cross-component architecture here; that belongs in `SD-XXX`

## Acceptance Criteria

1. **Given** [precondition], **When** [action], **Then** [expected outcome]
2. **Given** [precondition], **When** [action], **Then** [expected outcome]

## Technical Approach

**Strategy**: [Brief description]

**Key Decisions**:
- [Decision]: [Rationale]

**Trade-offs**:
- [What we gain vs. lose]

## Component Changes

### Modified: [Component Name]
- **Current State**: [What exists]
- **Changes**: [What changes]

### New: [Component Name]
- **Purpose**: [Why needed]
- **Interfaces**: Input: [receives] / Output: [produces]

## API/Interface Design

```yaml
endpoint: /api/v1/[resource]
method: POST
request:
  type: object
  properties:
    field1: string
response:
  type: object
  properties:
    id: string
    status: string
```

## Data Model Changes

```sql
-- New tables or schema modifications
CREATE TABLE [table_name] (
    id UUID PRIMARY KEY,
    [columns]
);
```

## Integration Points

| From | To | Method | Data |
|------|-----|--------|------|
| [Source] | [Target] | [REST/Event/Direct] | [What data] |

### External Dependencies
- **[Service]**: [Usage] | Fallback: [If unavailable]

## Security

- **Authentication**: [Required auth level]
- **Authorization**: [Required permissions]
- **Data Protection**: [Encryption/masking]
- **Threats**: [Specific threats and mitigations]

## Performance

- **Expected Load**: [Requests/sec, data volume]
- **Response Target**: [Milliseconds]
- **Optimizations**: [Caching, indexing, etc.]

## Testing

- [ ] **Unit**: [What to test]
- [ ] **Integration**: [What integrations to test]
- [ ] **API**: [Endpoints to test]
- [ ] **Security**: [Security scenarios]

## Migration &amp; Rollback

- **Backward Compatibility**: [Strategy]
- **Data Migration**: [Required migrations]
- **Feature Toggle**: [Enable/disable mechanism]
- **Rollback**: [Steps to reverse]

## Implementation Sequence

1. [What to build first] -- Files: `[paths]` -- Tests: `[paths]`
2. [What to build next]
3. [Integration and verification]

**Prerequisites**: [Dependencies that must be complete first]

## Risks

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Strategy] |

## Review Checklist

Use this checklist when reviewing a technical design:

- [ ] Acceptance criteria use Given/When/Then format and are verifiable
- [ ] Technical approach inherits from the parent solution design — no contradictions
- [ ] Key decisions have documented rationale
- [ ] Trade-offs are explicit — what we gain and what we lose
- [ ] Component changes clearly describe current state vs. changes
- [ ] API/interface design includes request and response schemas
- [ ] Data model changes include migration SQL
- [ ] Integration points specify fallback behavior for external dependencies
- [ ] Security section addresses authentication, authorization, and data protection
- [ ] Performance targets are numeric with specific metrics
- [ ] Testing section covers unit, integration, API, and security scenarios
- [ ] Migration and rollback strategy is documented
- [ ] Implementation sequence is ordered with file paths and test paths
- [ ] Design is consistent with governing solution design and feature spec</code></pre></details></td></tr>
</tbody>
</table>
