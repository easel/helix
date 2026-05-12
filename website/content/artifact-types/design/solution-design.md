---
title: "Solution Design"
linkTitle: "Solution Design"
slug: solution-design
phase: "Design"
artifactRole: "core"
weight: 13
generated: true
---

## Purpose

Feature-level solution design that explains the chosen approach for a
feature or cross-component capability. It maps requirements to a concrete
system shape, evaluates alternatives, and defines the decomposition that
story-level technical designs should inherit.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Design</strong></a> — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/02-design/solution-designs/SD-{id}-{name}.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/technical-design/">Technical Design</a><br><a href="/artifact-types/test/test-plan/">Test Plan</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/solution-designs/SD-001-helix-supervisory-control.md"><code>docs/helix/02-design/solution-designs/SD-001-helix-supervisory-control.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Solution Design Generation Prompt
Create a solution design that maps requirements to a concrete approach.

## Focus
- Create a feature-level artifact named `docs/helix/02-design/solution-designs/SD-XXX-[name].md`.
- Show the main options and why the chosen one wins.
- Keep the domain model, decomposition, and tradeoffs concise.
- Cover cross-component system behavior and feature-level structure.
- Do not collapse into story-level implementation details; those belong in a
  technical design (`TD-XXX-*`).
- Preserve only the decisions needed by build and test.

## Completion Criteria
- Requirements are mapped.
- Tradeoffs are explicit.
- The chosen approach is clear.
- The output is clearly feature-level and disambiguated from a technical
  design.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Solution Design

**Feature**: [[FEAT-XXX]] | **Artifact**: `docs/helix/02-design/solution-designs/SD-XXX-[name].md`

## Scope

- Feature-level design artifact
- Use for cross-component behavior, main alternatives, domain model, and
  decomposition
- Do not use for one-story implementation details; those belong in `TD-XXX`

## Requirements Mapping

### Functional Requirements

| Requirement | Technical Capability | Component | Priority |
|------------|---------------------|-----------|----------|
| [Business requirement] | [Technical implementation] | [Component] | P0/P1/P2 |

### NFR Impact on Architecture

| NFR | Requirement | Architectural Impact | Design Decision |
|-----|------------|---------------------|-----------------|
| Performance | [Metric] | [What this requires] | [How achieved] |
| Security | | | |
| Scalability | | | |

## Solution Approaches

### Approach 1: [Name]
**Description**: [Overview]
**Pros**: [Advantages]
**Cons**: [Disadvantages]
**Evaluation**: [Selected/Rejected: why]

### Approach 2: [Name]
[Same structure]

**Selected Approach**: [Which and why]

## Domain Model

```mermaid
erDiagram
    %% [Define entities with attributes and relationships]
```

### Business Rules
1. [Rule]: [Description and implementation impact]

## System Decomposition

### Component: [Name]
- **Purpose**: [What it does]
- **Responsibilities**: [List]
- **Requirements Addressed**: [Which requirements]
- **Interfaces**: [How it communicates]

### Component Interactions
```mermaid
graph TD
    %% [Show component relationships]
```

## Technology Rationale

| Layer | Choice | Why | Alternatives Rejected |
|-------|--------|-----|----------------------|
| Language | [Choice] | [Reason] | [Others] |
| Framework | [Choice] | [Reason] | [Others] |
| Database | [Choice] | [Reason] | [Others] |
| Infrastructure | [Choice] | [Reason] | [Others] |

## Traceability

| Requirement ID | Component | Design Element | Test Strategy |
|---------------|-----------|----------------|---------------|
| FR-001 | [Component] | [How addressed] | [How tested] |

### Gaps
- [ ] [Requirement not fully addressed]: [Mitigation]

## Concern Alignment

If the project has active concerns (`docs/helix/01-frame/concerns.md`), confirm
this design is consistent with them:

- **Concerns used**: [Which active concerns does this design rely on?]
- **Constraints honored**: [Any concern constraints that shaped this design?]
- **ADRs referenced**: [Concern-related ADRs that govern design choices here]
- **Departures**: [Any design choices that depart from concern practices? If so,
  an ADR should justify the departure.]

## Constraints &amp; Assumptions

- **Constraints**: [Technical constraints and their design impact]
- **Assumptions**: [What we assume, risk if wrong]
- **Dependencies**: [External systems, libraries]

## Risks

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Strategy] |

## Review Checklist

Use this checklist when reviewing a solution design:

- [ ] Requirements mapping covers all P0 functional requirements from the governing spec
- [ ] NFR impact section shows how the architecture satisfies each non-functional requirement
- [ ] At least two solution approaches were evaluated with concrete pros/cons
- [ ] Selected approach rationale explains why alternatives were rejected
- [ ] Domain model captures all entities and their relationships
- [ ] Business rules are specific enough to implement
- [ ] System decomposition assigns every requirement to at least one component
- [ ] Component interfaces are defined — not just names, but how they communicate
- [ ] Technology rationale explains why each choice was made, not just what was chosen
- [ ] Traceability table maps every requirement to a component and test strategy
- [ ] Gaps section lists any requirements not fully addressed with mitigation plans
- [ ] Concern alignment verifies consistency with active project concerns
- [ ] Design is consistent with governing feature spec and PRD</code></pre></details></td></tr>
</tbody>
</table>
