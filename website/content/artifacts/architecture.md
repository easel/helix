---
title: "Architecture"
slug: architecture
phase: "Design"
weight: 200
generated: true
aliases:
  - /reference/glossary/artifacts/architecture
---

## What it is

_(architecture — description not yet captured in upstream `meta.yml`.)_

## Phase

**[Phase 2 — Design](/reference/glossary/phases/)** — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

_None._

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Architecture Documentation Generation Prompt
Document the architecture views that the team actually needs to build and review the system.

## Focus
- Include only the C4 views that add information; omit empty or duplicate views.
- Keep boundaries, deployment shape, data flow, and quality attributes visible.
- Annotate major tradeoffs or constraints directly on the relevant view or summary.
- Remove generic architecture commentary.

## Completion Criteria
- The views are understandable at a glance.
- Key boundaries and tradeoffs are visible.
- The document stays implementation-relevant.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: helix.architecture
  depends_on:
    - helix.prd
---
# Architecture Diagrams

## Level 1: System Context

```mermaid
graph TB
    %% [Add users, system, external dependencies]
```

| Element | Type | Purpose | Protocol |
|---------|------|---------|----------|
| [User/System] | User/External | [Interaction] | [HTTP/API/etc] |

## Level 2: Container Diagram

```mermaid
graph TB
    %% [Add containers: Web, API, DB, Cache, Queue, Worker]
```

| Container | Technology | Responsibilities | Communication |
|-----------|------------|------------------|---------------|
| [Name] | [Stack] | [What it does] | [Protocol/Format] |

## Level 3: Component Diagram

```mermaid
graph TB
    %% [Add components per container: Controller, Service, Repository, etc]
```

| Component | Purpose | Implementation Notes |
|-----------|---------|---------------------|
| [Name] | [Responsibility] | [Key decisions] |

## Deployment

```mermaid
graph TB
    %% [Add: LB, Web Tier, App Tier, Data Tier]
```

| Component | Infrastructure | Instances | Scaling |
|-----------|---------------|-----------|---------|
| [Name] | [Container/VM] | [Count] | [H/V] |

## Data Flow

```mermaid
sequenceDiagram
    %% [Add sequence for key use case]
```

## Architecture Summary

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Frontend | [Tech] | [Why] |
| Backend | [Tech] | [Why] |
| Database | [Tech] | [Why] |
| Infra | [Tech] | [Why] |

**Patterns**: [Pattern 1: usage] | [Pattern 2: usage]

## Quality Attributes

| Attribute | Strategy | Key Decisions |
|-----------|----------|---------------|
| Scalability | [H/V scaling] | [Approach] |
| Security | [Controls] | [Boundaries] |
| Observability | [Metrics/Logging/Tracing] | [Tools] |
| Disaster Recovery | RTO: [target] / RPO: [target] | [Backup/Failover strategy] |
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
