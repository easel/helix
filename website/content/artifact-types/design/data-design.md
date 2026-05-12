---
title: "Data Design"
linkTitle: "Data Design"
slug: data-design
phase: "Design"
artifactRole: "supporting"
weight: 15
generated: true
---

## Purpose

Design-level data architecture covering entities, stores, access patterns,
constraints, and migration strategy.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Design</strong></a> — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/02-design/data-design.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/technical-design/">Technical Design</a><br><a href="/artifact-types/test/test-plan/">Test Plan</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/data-design.md"><code>docs/helix/02-design/data-design.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Data Design Generation Prompt
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
  implementation and tests.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
- Backfill or cleanup: [If needed]</code></pre></details></td></tr>
</tbody>
</table>
