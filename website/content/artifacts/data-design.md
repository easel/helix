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

This example is HELIX's actual data design, sourced from [`docs/helix/02-design/data-design.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/data-design.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Data Design — HELIX Bead Tracker

**Scope**: The `.ddx/beads.jsonl` issue tracker that anchors HELIX execution.
**Status**: Complete

### Data Summary

- Scope: The bead tracker — HELIX's only durable execution-state store. Beads
  are work units (issues, tasks, epics, planning notes) governed by upstream
  artifacts and consumed by `ddx agent execute-bead` / `ddx agent execute-loop`.
- Storage systems: Append-friendly JSON Lines file (`.ddx/beads.jsonl`) with
  per-record locking enforced by the `ddx bead` CLI. No database, no daemon
  required for reads.
- Main concerns: Concurrent writer safety (operator and supervisor may both
  mutate during a live `helix run`), stale-claim recovery, deterministic
  ready/blocked queries, append history preserved in `events`, and forward-
  compatible schema evolution without breaking existing tooling.
- Authority: [CONTRACT-001](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md)
  (`ddx bead` and `.ddx/beads.jsonl` belong to DDx; HELIX consumes via the
  CLI), [ADR-002](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/adr) (tracker write safety model — referenced where
  available), and [API-001](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/contracts/API-001-helix-tracker-mutation.md)
  (HELIX-side mutation surface).

### Entities and Stores

| Entity or Store | Purpose | Key Fields | Volume / Growth | Notes |
|-----------------|---------|------------|-----------------|-------|
| `beads.jsonl` (record per line) | Durable issue/work-unit state | `id`, `title`, `description`, `status`, `priority`, `issue_type`, `labels[]`, `parent`, `dependencies[]`, `acceptance`, `spec-id`, `events[]`, claim metadata, `created_at`, `updated_at` | Hundreds to low thousands of records over a project lifetime; one file per repo | Append/rewrite via `ddx bead`; never edit by hand during a live run |
| `events[]` (embedded array per bead) | Append-only audit trail of state transitions and execution attempts | `event_type`, `timestamp`, `actor`, `payload` | 10s–100s per bead over its lifetime | Bounded by execution count; older events may be summarized but never silently truncated |
| Claim metadata (embedded fields) | Single-writer guard for active execution | `claimed-at` (ISO-8601 UTC), `claimed-pid`, `claimed-machine`, `owner` | One slot per in-progress bead | Cleared by `--unclaim`, `close`, or orphan-recovery sweep |
| Execution-eligibility metadata | Distinguishes execution-ready beads from refinement/superseded ones | `execution-eligible`, `superseded-by`, `replaces` | Sparse — most beads do not need it | Drives `ddx bead list --execution-ready` |

### Relationships

| From | To | Type | Cardinality | On Delete |
|------|----|------|-------------|-----------|
| Bead | Bead (`parent`) | epic-child | N:1 (optional) | RESTRICT — close epics only after children resolve |
| Bead | Bead (`dependencies[]`) | depends-on | N:M (optional) | RESTRICT — closing a dep does not auto-close dependents; readiness recomputes |
| Bead | Governing artifact (`spec-id`) | governed-by | N:1 (optional path string) | No delete propagation — `spec-id` is a path, not a foreign key; drift is surfaced via review |
| Bead | Bead (`superseded-by` / `replaces`) | supersession | N:1 (optional) | Supersession redirects readiness queries; original bead remains for audit |

### Access Patterns and Constraints

| Access Pattern | Frequency | Performance Need | Supporting Index or Cache |
|----------------|-----------|------------------|---------------------------|
| `ddx bead list --status open --json` (full read) | Every supervisor cycle | Sub-second on thousand-record stores | Sequential scan of JSONL — acceptable at this scale |
| `ddx bead ready` (filter open + deps satisfied + not superseded) | Every supervisor cycle | Sub-second | Computed in-memory after full read |
| Single-bead update (`update`, `claim`, `close`) | Every build cycle (many per `helix run`) | Strict atomicity — no torn writes | Exclusive file lock around read-modify-rewrite; `events[]` append captures intent before status changes |
| Orphan-recovery sweep (claims older than `HELIX_ORPHAN_THRESHOLD`, default 7200s) | Periodic during long runs | Bounded; touches only stale claims | Filter on `claimed-at` age + dead-PID check |
| `helix status` snapshot (counts by status, focused-epic view) | Operator-initiated, ad hoc | Sub-second | Reuses the open-list scan |

### Validation and Security

| Field or Data Type | Rules / Classification | Protection or Error Handling |
|--------------------|------------------------|------------------------------|
| `id` | Required; opaque (`helix-<8hex>`); unique within file | Generator rejects duplicates; corrupt IDs surface as parse failures |
| `status` | Enum: `open`, `in_progress`, `blocked`, `closed`, `superseded` | Mutations validated by `ddx bead`; raw JSONL edits during a live run risk torn state |
| `claimed-at` | ISO-8601 UTC; cleared on `--unclaim` and `close` | Orphan recovery uses age threshold + dead-PID check before clearing |
| `claimed-pid`, `claimed-machine` | Free-form identifiers | Dead-PID check is part of orphan recovery; recovery never destroys unrelated worktree state |
| `labels[]` | Free-form strings; `helix`, `phase:*`, `kind:*`, `area:*`, `story:US-*` are conventional | Convention enforced by HELIX skills; tracker accepts any label |
| `description`, `acceptance`, `title` | Free-form text — may include rendered context digests | No secret-bearing fields by contract; the tracker is checked into the repo by default. Operators must keep secrets out of bead bodies. |
| `events[]` payloads | Append-only history | Never rewritten by HELIX; corruption is recoverable from git history |
| File-level access | Repo-relative; readable by anyone with repo read access | Treat as public-ish: do not store secrets, customer data, or credentials |

### Migration Strategy

- Tooling: `ddx bead` is the only sanctioned writer. Schema evolution is
  managed downstream in DDx; HELIX consumes through the published CLI
  contract per CONTRACT-001.
- Approach: Additive fields land first (new optional metadata is ignored by
  older readers). Status enum extensions require a coordinated reader update
  before the new value is emitted. Removed fields go through a deprecation
  cycle — the writer stops emitting first, then a later major version drops
  read tolerance.
- Backfill or cleanup: Historical migration from the legacy `.helix/issues.jsonl`
  store is captured in `docs/helix/02-design/plan-2026-03-27-supervisory-concurrency.md`
  and the surrounding planning beads. The migration was a one-shot rewrite
  with the legacy file retired; no live rollback path is supported.
- Rollback: Because the file is plain JSONL under git, any unintended schema
  drift is recoverable by reverting the offending commit. Live tracker writes
  during a `helix run` are audited via `events[]` so a torn write can be
  reconstructed without fully reverting the file.
