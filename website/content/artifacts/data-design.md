---
title: "Data Design"
slug: data-design
phase: "Design"
weight: 200
generated: true
aliases:
  - /reference/glossary/artifacts/data-design
---

## What it is

Design-level data architecture covering entities, stores, access patterns,
constraints, and migration strategy.

## Phase

**[Phase 2 — Design](/reference/glossary/phases/)** — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.

## Output location

`docs/helix/02-design/data-design.md`

## Relationships

### Requires (upstream)

- [Architecture](../architecture/)
- [Solution Design](../solution-design/) *(optional)*
- [Technical Design](../technical-design/) *(optional)*
- [Security Architecture](../security-architecture/) *(optional)*

### Enables (downstream)

_None._

### Informs

- [Technical Design](../technical-design/)
- [Test Plan](../test-plan/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Data Design Generation Prompt
Document the data model and access patterns needed to support the design.

## Focus
- Name the main entities, stores, and key fields.
- Make relationships, lifecycle, and integrity constraints explicit.
- Capture the main access patterns and their performance or consistency needs.
- Note privacy, classification, retention, and protection consequences where they
  materially shape the design.
- Define migration and rollback expectations for schema or storage changes.
- Avoid drifting into implementation-specific query or ORM code.

## Completion Criteria
- The model is understandable to another engineer without reading code.
- Key data decisions and constraints are explicit.
- Access patterns and migration strategy are concrete enough to guide
  implementation and tests.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Data Design

## Data Summary

- Scope: [What feature, subsystem, or workflow this data design supports]
- Storage systems: [Database, queue, cache, object store]
- Main concerns: [Consistency, scale, retention, privacy, migration]

## Entities and Stores

| Entity or Store | Purpose | Key Fields | Volume / Growth | Notes |
|-----------------|---------|------------|-----------------|-------|
| [Name] | [What it represents] | [Important fields] | [Expected scale] | [Business rules or constraints] |

## Relationships

| From | To | Type | Cardinality | On Delete |
|------|----|------|-------------|-----------|
| [Entity1] | [Entity2] | [1:N, N:M] | [Required/Optional] | [CASCADE/RESTRICT/SET NULL] |

## Access Patterns and Constraints

| Access Pattern | Frequency | Performance Need | Supporting Index or Cache |
|----------------|-----------|------------------|---------------------------|
| [Read or write path] | [Rate] | [Latency or throughput target] | [Index, partition, cache] |

## Validation and Security

| Field or Data Type | Rules / Classification | Protection or Error Handling |
|--------------------|------------------------|------------------------------|
| [Field] | [Constraints or classification] | [Masking, encryption, validation, retention] |

## Migration Strategy

- Tooling: [Migration framework]
- Approach: [Schema rollout and rollback strategy]
- Backfill or cleanup: [If needed]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
