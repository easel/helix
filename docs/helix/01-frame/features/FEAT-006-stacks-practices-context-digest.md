---
dun:
  id: FEAT-006
  depends_on:
    - helix.prd
    - FEAT-003
---
# Feature Specification: FEAT-006 — Stacks, Practices, and Context-Digest Beads

**Feature ID**: FEAT-006
**Status**: Draft
**Priority**: P1
**Owner**: HELIX maintainers

## Overview

HELIX agents make technology choices and follow conventions inconsistently
because nothing in the workflow encodes what stack the project uses, what
practices follow from that stack, or how to summarize the full governing
context into an implementation-ready bead. This feature introduces stacks
(composable technology selections), best practices (conventions that activate
per-stack), and context digests (compact authority summaries assembled into
beads at triage time so implementing agents rarely need to read upstream
files).

This feature extends the cross-cutting injection model established by
FEAT-003 (principles). Where principles guide **judgment**, stacks guide
**choices** and practices guide **conventions**.

## Problem Statement

- **Current situation**: Beads carry `spec-id`, `acceptance`, `description`,
  and `design` — but none of these systematically include the active
  technology stack, tooling conventions, relevant ADR decisions, or governing
  principles. Implementing agents must reconstruct the full authority context
  by reading 5-10 upstream files. They frequently skip files, read stale
  versions, or make choices inconsistent with prior ADRs and stack decisions.
- **Pain points**:
  1. Stack drift — one agent chooses Jest, another chooses Vitest, because
     nothing declares the project's testing framework.
  2. Convention inconsistency — agents don't know to use Biome instead of
     Prettier, or clippy instead of manual linting, because tooling choices
     aren't injected.
  3. Context reconstruction cost — every implementation pass spends tokens
     reading upstream docs that could have been summarized once at triage.
  4. ADR amnesia — architecture decisions are made via spikes and ADRs but
     never flow into the beads that should honor them.
  5. Engineering principles (tests first, fake data, local-first UX) have no
     home — they're too concrete for the vision but too universal for a
     stack definition.
- **Desired outcome**: A bead created by triage or evolve is a self-contained
  execution unit. The implementing agent can work from the bead alone without
  reading upstream files in the common case. Stacks, practices, principles,
  and relevant ADRs are summarized into a compact context digest assembled at
  bead creation and refreshed at polish time.

## Design

### Cross-cutting concerns taxonomy

HELIX recognizes three layers of cross-cutting context:

| Layer | What it is | Scope | Example |
|-------|-----------|-------|---------|
| **Principles** | Values that guide judgment | Universal (project-wide) | "Design for simplicity", "Tests first", "Local-first UX" |
| **Stacks** | Composable technology selections | Per-project, from library | "TypeScript strict + Bun", "Rails 8 + Postgres 16" |
| **Practices** | Conventions that follow from a stack | Per-stack, overridable | "Use Biome, not Prettier", "Use clippy --all-targets" |

Principles are governed by FEAT-003. This feature governs stacks, practices,
and the context digest that wires all three into beads.

Engineering principles ("tests first", "fake data over fixtures", "prefer
stubs to mocks", "cloud native", "local-first UX") live in the principles
document alongside design principles. They are the same artifact type — just
more concrete. FEAT-003's size ceiling (warn at 8, nudge at 12, prune at 15+)
applies to the combined set.

### Stacks

A stack is a composable, named set of technology selections. Stacks live in
a library and are selected by the project:

```
workflows/stacks/              # HELIX default library
  typescript-bun/
    stack.md
    practices.md
  rails-postgres/
    stack.md
    practices.md
  gcp-cloud-run/
    stack.md
    practices.md
  python-uv/
    stack.md
    practices.md
```

A `stack.md` declares:

```markdown
# Stack: TypeScript + Bun

## Components
- **Language**: TypeScript (strict mode)
- **Runtime**: Bun 1.x
- **Package manager**: Bun (not npm, not yarn)

## Constraints
- All code must pass `tsc --noEmit` with strict config
- Use Bun-native APIs where available (Bun.serve, Bun.file)
- No Node.js compatibility shims unless unavoidable

## When to use
Projects that need fast startup, built-in test runner, and TypeScript-first
tooling without the Node.js ecosystem overhead.
```

Stacks are composable. A project selects multiple stacks that cover different
concerns (runtime, data, infra):

```markdown
# Project Stack (docs/helix/01-frame/stack.md)

## Active Stacks
- typescript-bun (runtime + language)
- postgres (data)
- gcp-cloud-run (infra)

## Project Overrides
- Testing: use Vitest instead of bun:test (bun:test lacks coverage)
```

### Practices

Each stack ships a `practices.md` with conventions that follow from the
technology choices:

```markdown
# Practices: TypeScript + Bun

## Linting & Formatting
- Linter: ESLint with @typescript-eslint/strict-type-checked
- Formatter: Biome (not Prettier)
- Run: `bunx biome check --write .`

## TypeScript Config
- strict: true
- noUncheckedIndexedAccess: true
- exactOptionalPropertyTypes: true
- verbatimModuleSyntax: true

## Testing
- Framework: bun:test (built-in)
- Prefer stubs to mocks (from principles)
- Use Bun.mock() for module mocking
- Fake data with @faker-js/faker, not static fixtures

## Imports
- Use Bun-native imports, not Node compat
- Prefer explicit file extensions in imports
```

Practices are advisory, not enforced — they guide agent choices. Project
overrides in `docs/helix/01-frame/stack.md` take precedence over library
practices.

### Relationship between stacks, spikes, ADRs, and POCs

Stacks, spikes, ADRs, and POCs interact at specific points in the workflow:

| Artifact | Role | Relationship to Stacks |
|----------|------|----------------------|
| **Stack** | Declares what technology to use | The selection itself |
| **Spike** | Investigates uncertainty before a stack decision | A spike may recommend adopting, rejecting, or modifying a stack. Spike findings inform stack selection. |
| **ADR** | Records a structural decision with rationale | An ADR may ratify a stack choice ("we chose Postgres over DynamoDB because..."), add constraints to a stack ("Postgres with pgvector for embeddings"), or override a stack practice ("we use connection pooling via PgBouncer, not the ORM's built-in pool"). |
| **POC** | Validates feasibility of a specific approach | A POC may prove that a stack combination works (or doesn't) before the project commits to it. |

The typical flow:

1. **Spike** or **POC** investigates a technology question
2. **ADR** records the decision with rationale and alternatives
3. **Stack selection** in `docs/helix/01-frame/stack.md` references the ADR
4. **Practices** activate for the selected stack
5. **Context digest** in beads summarizes the stack + practices + ADR rationale

ADRs that modify stack behavior should be cited in the project's stack
overrides section. When an ADR supersedes a stack practice, the override
should reference the ADR:

```markdown
## Project Overrides
- Connection pooling: PgBouncer external pool, not ORM pool (see ADR-005)
```

This ensures the context digest includes the ADR rationale alongside the
overridden practice.

### Context digest

The context digest is a compact summary of everything an implementing agent
needs to stay consistent. It is assembled automatically at bead creation
(triage, evolve) and refreshed at bead refinement (polish).

#### Contents

A context digest includes:

1. **Active principles** — the full principles list (design + engineering),
   compact enough to include verbatim (~500 tokens)
2. **Stack summary** — active stacks and any project overrides (~300 tokens)
3. **Stack practices** — merged practices from all active stacks, with
   project overrides applied (~300 tokens)
4. **Relevant ADRs** — decision + rationale for ADRs that affect the bead's
   area. Not the full ADR document — just the decision statement and key
   rationale (~200 tokens per relevant ADR)
5. **Governing spec context** — key requirements and acceptance criteria
   from the bead's `spec-id` target (~300 tokens)

Target size: **1000-1500 tokens**. Less than one file read, better signal
than reading 5 files.

#### What stays as a pointer

The digest does not include:
- Full PRD (too large — pointer via spec-id chain)
- Full design documents (reference by section)
- ADR alternatives and exploration (just the decision)
- Test plan details (pointer to TP-XXX)
- Full feature spec (extract key requirements only)

#### Assembly algorithm

At bead creation:

1. Load `docs/helix/01-frame/principles.md` (or HELIX defaults)
2. Load `docs/helix/01-frame/stack.md` — resolve active stacks
3. For each active stack, load `practices.md` from the library
4. Apply project overrides on top of library practices
5. Find ADRs relevant to the bead's scope:
   - Match by `area:*` labels on the bead
   - Match by feature reference (ADR's `Related` field matches bead's
     spec-id chain)
6. Load the governing spec (`spec-id` target) and extract key requirements
   and acceptance criteria relevant to this bead
7. Assemble into a structured digest
8. Write to the bead's `context` field (new field) or prepend to
   `description`

At polish time:

1. Re-run the assembly algorithm against current upstream state
2. Diff against the existing digest
3. If material changes exist, update the digest and note what changed

#### Digest format

The digest is prepended to the bead's `description` field using XML tags.
This avoids schema changes, is machine-parseable, and keeps the
human-written description cleanly separated below:

```xml
<context-digest>
<principles>Design for simplicity · Tests first · Fake data over fixtures ·
Local-first UX · Prefer reversible decisions</principles>
<stack>TypeScript strict + Bun | Postgres 16 | GCP Cloud Run</stack>
<practices>Biome (not Prettier) · ESLint strict · bun:test · Bun-native
imports · strict tsconfig · @faker-js/faker for test data</practices>
<adrs>ADR-003 event sourcing for audit trail · ADR-005 PgBouncer for
connection pooling (not ORM pool)</adrs>
<governing>FEAT-007 §3.2 — user notification preferences must support
email, push, and in-app channels with per-channel opt-out</governing>
</context-digest>

Implement user notification preferences per FEAT-007 Section 3.2.
Governing: FEAT-007, SD-007, TP-007.
```

`helix polish` locates the `<context-digest>` block by tag and replaces it
in-place, preserving the human-written description below. If no digest
exists yet, it is prepended.

### Injection points

| Consumer | What's injected | When |
|----------|----------------|------|
| `helix triage` | Assembles full context digest into new bead | At bead creation |
| `helix evolve` | Assembles context digest for beads it creates/modifies | At bead creation |
| `helix polish` | Refreshes context digest against current upstream | At refinement |
| `helix build` | Reads context digest from bead (no upstream reads needed) | At implementation |
| `helix review` | Reads context digest to verify implementation consistency | At review |
| `helix frame` | Stack selection and principles are available for scoping | At framing |
| `helix design` | Stack constraints and practices inform architecture | At design |

The key insight: **triage and polish are the write points, build and review
are the read points**. The context digest is written once (at triage) and
refreshed when needed (at polish), so implementation agents get pre-assembled
context without paying the read cost.

## Requirements

### Functional Requirements

1. HELIX must support a library of composable, named technology stacks in
   `workflows/stacks/`.
2. Each stack must declare its components, constraints, and associated
   practices in a `stack.md` and `practices.md`.
3. Projects must be able to select multiple stacks and declare overrides
   in `docs/helix/01-frame/stack.md`.
4. Project overrides must take full precedence over library practices.
5. `helix triage` and `helix evolve` must assemble a context digest into
   every bead they create, summarizing active principles, stack, practices,
   relevant ADRs, and governing spec context.
6. `helix polish` must refresh the context digest against current upstream
   state and flag material changes.
7. `helix build` and `helix review` must read the context digest from the
   bead rather than reconstructing context from upstream files.
8. The context digest must be compact enough (~1000-1500 tokens) that
   including it in the bead does not materially increase prompt cost.
9. ADR decisions that affect a bead's scope must be included in the context
   digest with their rationale.
10. Spike and POC findings that led to stack selections should be traceable
    through the ADR that ratified the decision.
11. HELIX must ship a small set of reference stacks as defaults in the
    library.
12. Stack practices and project overrides must reference governing ADRs when
    an override departs from the library default.

### Non-Functional Requirements

- **Consistency**: The same stack, practices, and principles must appear in
  every bead for a given scope — no agent should derive its own implicit
  technology choices.
- **Efficiency**: The context digest must reduce total tokens consumed per
  implementation pass compared to reading upstream files.
- **Maintainability**: Adding a new stack to the library should not require
  modifying any action prompt or skill.
- **Composability**: Stacks must be independently selectable and must not
  conflict at the practice level without explicit project resolution.

## User Stories

### US-001: Select a technology stack [FEAT-006]
**As a** HELIX operator starting a new project
**I want** to select from a library of known-good technology stacks
**So that** my project has consistent technology choices from the start

**Acceptance Criteria:**
- [ ] Given a HELIX library with stacks, when the user runs `helix frame`,
  then available stacks are presented for selection.
- [ ] Given the user selects "typescript-bun" and "gcp-cloud-run", when the
  selection completes, then `docs/helix/01-frame/stack.md` records both.
- [ ] Given selected stacks, when any downstream skill runs, then it has
  access to the active stack configuration.

### US-002: Override stack practices [FEAT-006]
**As a** HELIX operator with project-specific needs
**I want** to override specific practices from my selected stacks
**So that** I can customize conventions without forking the stack definition

**Acceptance Criteria:**
- [ ] Given the typescript-bun stack recommends bun:test, when the project
  overrides to Vitest, then all downstream context uses Vitest.
- [ ] Given an override references an ADR, when the context digest is
  assembled, then the ADR rationale appears in the digest.

### US-003: Self-contained implementation beads [FEAT-006]
**As a** HELIX operator running `helix run` in the background
**I want** implementation beads to contain enough context that the agent
  rarely reads upstream files
**So that** implementation is faster, cheaper, and more consistent

**Acceptance Criteria:**
- [ ] Given `helix triage` creates a bead, when the bead is created, then
  it contains a context digest with principles, stack, practices, relevant
  ADRs, and governing spec context.
- [ ] Given an implementing agent reads the context digest, when it
  implements the bead, then it makes technology choices consistent with the
  stack and follows the declared practices.
- [ ] Given the context digest is ~1000-1500 tokens, when compared to
  reading 5 upstream files, then total token usage per implementation pass
  decreases.

### US-004: Refresh context on polish [FEAT-006]
**As a** HELIX operator who changed a stack selection or ADR
**I want** existing beads to get updated context digests
**So that** implementing agents don't work from stale context

**Acceptance Criteria:**
- [ ] Given the project stack changes, when `helix polish` runs, then
  affected beads get refreshed context digests.
- [ ] Given an ADR is added or modified, when `helix polish` runs, then
  beads in the ADR's scope get the updated ADR summary in their digest.

### US-005: Stack decisions traced through ADRs and spikes [FEAT-006]
**As a** HELIX operator reviewing architecture
**I want** stack selections to reference the ADRs and spikes that justified
  them
**So that** the rationale for technology choices is traceable

**Acceptance Criteria:**
- [ ] Given a spike recommends adopting Postgres, when an ADR ratifies the
  decision, then the project stack references the ADR.
- [ ] Given the context digest includes an ADR summary, when a reviewer
  reads it, then they can trace back to the full ADR for details.

## Edge Cases and Error Handling

- **No stack selected**: If `docs/helix/01-frame/stack.md` does not exist,
  the context digest omits stack and practices sections. No error — the
  project simply has no declared stack.
- **Conflicting stacks**: If two selected stacks declare conflicting
  practices (e.g., "use Jest" vs "use bun:test"), the assembly algorithm
  must flag the conflict and require a project override to resolve it.
- **Very large digest**: If the context digest exceeds 2000 tokens (many
  ADRs, many stacks), the assembly algorithm should prioritize: principles
  first, then stack/practices, then ADRs by relevance, then spec context.
  Truncate ADR summaries before dropping them.
- **Stale ADR in digest**: If a referenced ADR is superseded after the
  digest is assembled, `helix polish` must detect the supersession and
  update the digest.
- **No relevant ADRs**: The ADR section is omitted from the digest. No
  error.
- **Stack practice overridden without ADR reference**: The assembly
  algorithm should warn (not block) that the override lacks rationale.

## Success Metrics

- Implementation beads contain context digests in >90% of cases.
- Implementing agents make stack-consistent technology choices (measured by
  review findings for stack drift).
- Total token usage per implementation pass decreases compared to baseline
  (agents reading 5+ upstream files).
- Stack selections are traceable to ADRs and spikes through the project
  stack file.

## Constraints and Assumptions

- The context digest is a static snapshot, not a live query. It is assembled
  at triage and refreshed at polish — not recomputed at build time.
- Stack definitions are markdown files in a library directory — no runtime
  infrastructure, no schema enforcement beyond convention.
- The library ships with HELIX but projects can add custom stacks alongside
  the defaults (in their own `workflows/stacks/` or a project-level
  directory).
- FEAT-003 (principles) must land first — the context digest depends on the
  principles resolution mechanism.

## Dependencies

- **FEAT-003**: Principles — the context digest includes active principles
- **FEAT-001**: Supervisory control — triage and polish are dispatched by
  the run loop
- **FEAT-002**: CLI — triage, polish, and evolve commands assemble digests
- **helix.prd**: PRD requirements for tracker-first execution
- **ADR template**: ADRs must have a stable "Decision" section that can be
  extracted for the digest

## Out of Scope

- Stack enforcement in CI (stacks guide choices, they're not lint rules)
- Stack marketplace or remote registry (library is local to the repo)
- Automatic stack detection from existing code (project declares stacks
  explicitly)
- Stack versioning beyond what the library files contain
- Per-bead stack overrides (stacks are project-level, not issue-level)

## Open Questions

- ~~Should the context digest be a new bead field or in `description`?~~
  **Decided**: XML tags prepended to `description`. No schema changes.
- How should practice conflicts between stacks be detected — simple string
  matching on practice categories, or a more structured approach?
- Should `helix build` ever fall back to reading upstream files when the
  digest is present, or should it trust the digest completely? (Proposed:
  trust the digest, rely on polish to keep it current.)
- What reference stacks should HELIX ship? Candidates: typescript-bun,
  python-uv, rails-postgres, rust-cargo, gcp-cloud-run, aws-lambda,
  next-vercel.
