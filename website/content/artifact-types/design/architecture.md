---
title: "Architecture"
linkTitle: "Architecture"
slug: architecture
phase: "Design"
artifactRole: "core"
weight: 10
generated: true
---

## Purpose

Captures the C4 views the team needs to build and review the system —
System Context, Container, Component (where helpful), Deployment, and
Data Flow — plus the quality attributes that constrain the design and
the architectural decisions that bind it. The architecture document is
the highest-authority structural artifact in the Design phase: solution
designs reference it, technical designs follow it, and operational
artifacts (runbook, monitoring, deployment) trace back to its quality
attributes.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Design</strong></a> — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/02-design/architecture.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/solution-design/">Solution Design</a><br><a href="/artifact-types/design/technical-design/">Technical Design</a><br><a href="/artifact-types/design/adr/">ADR</a><br><a href="/artifact-types/design/contract/">Contract</a><br><a href="/artifact-types/design/data-design/">Data Design</a><br><a href="/artifact-types/design/security-architecture/">Security Architecture</a></td></tr>
<tr><th>Referenced by</th><td><a href="/artifact-types/design/solution-design/">Solution Design</a><br><a href="/artifact-types/design/technical-design/">Technical Design</a><br><a href="/artifact-types/deploy/deployment-checklist/">Deployment Checklist</a><br><a href="/artifact-types/deploy/runbook/">Runbook</a><br><a href="/artifact-types/deploy/monitoring-setup/">Monitoring Setup</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/architecture.md"><code>docs/helix/02-design/architecture.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Architecture Documentation Generation Prompt
Document the architecture views that the team actually needs to build and review the system.

## Focus
- Include only the C4 views that add information; omit empty or duplicate views.
- Keep boundaries, deployment shape, data flow, and quality attributes visible.
- Annotate major tradeoffs or constraints directly on the relevant view or summary.
- Remove generic architecture commentary.

## Completion Criteria
- The views are understandable at a glance.
- Key boundaries and tradeoffs are visible.
- The document stays implementation-relevant.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
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
| Disaster Recovery | RTO: [target] / RPO: [target] | [Backup/Failover strategy] |</code></pre></details></td></tr>
</tbody>
</table>
