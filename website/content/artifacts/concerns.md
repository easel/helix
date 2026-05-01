---
title: "Project Concerns"
slug: concerns
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/concerns
---

## What it is

Declares the project's active cross-cutting concerns (tech stacks,
quality attributes, conventions) and any project-specific overrides.
Concerns are composable selections from the library at
.ddx/plugins/helix/workflows/concerns/. Each concern declares area scope and associated
practices that flow into context digests on beads.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/concerns.md`

## Relationships

### Requires (upstream)

- [PRD](../prd/) *(optional)*
- [Principles](../principles/) *(optional)*

### Enables (downstream)

- Context Digest

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Concerns Selection Prompt

Guide the user through selecting project concerns from the library and
declaring any project-specific overrides.

## Approach

1. List available concerns from `.ddx/plugins/helix/workflows/concerns/` grouped by category:
   - **Tech stack**: typescript-bun, python-uv, rust-cargo
   - **Accessibility**: a11y-wcag-aa
   - **Observability**: o11y-otel
   - **Internationalization**: i18n-icu

2. For each category, ask the user:
   - Tech stack: "What language, runtime, and package manager does this
     project use?"
   - Data: "What database or data layer?"
   - Infrastructure: "Where will this deploy?"
   - Quality: "Do you need accessibility (a11y), internationalization (i18n),
     or observability (o11y) support?"

3. For each selected concern:
   - Check if the user wants to override any library practices
   - If overriding, ask for the governing ADR or create one
   - Ask if an ADR exists that justified this concern selection

4. Declare the project's area labels — which `area:*` labels will beads use?
   The default set is: `ui`, `api`, `data`, `infra`, `cli`.

5. Check for practice conflicts between selected concerns and flag them.

6. Write `docs/helix/01-frame/concerns.md`.

## Key Rules

- Concerns are composable — selecting multiple is normal and expected.
- Project overrides take full precedence over library practices.
- Every override should reference a governing ADR when possible.
- The area taxonomy declared here controls which concerns are injected
  into which beads via `<context-digest>`.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Project Concerns

## Active Concerns

<!-- Select from .ddx/plugins/helix/workflows/concerns/ or add custom entries.
     Each line: concern-name (category) — ADR reference that justified selection.
     The ADR ref is how the concern/ADR/spike chain stays traceable. -->

- [concern-name] ([category]) — ADR-NNN: [one-line rationale]

## Project Overrides

<!-- Override specific library practices. Cite the governing ADR. -->

- [Practice]: [override] (see [ADR-NNN])

## Area Labels

This project uses the following area labels for concern scoping:

<!-- Declare which area labels your beads use. Concerns are injected into
     beads based on matching these labels against each concern's `areas` field. -->

- `area:ui` — user-facing interfaces
- `area:api` — backend services and endpoints
- `area:data` — database, storage, data pipeline
- `area:infra` — deployment, CI/CD, infrastructure
- `area:cli` — command-line tools
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
