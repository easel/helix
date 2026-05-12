---
title: "Project Concerns"
linkTitle: "Project Concerns"
slug: concerns
phase: "Frame"
artifactRole: "core"
weight: 12
generated: true
---

## Purpose

Declares the project's active cross-cutting concerns (tech stacks,
quality attributes, conventions) and any project-specific overrides.
Concerns are composable selections from the library at
.ddx/plugins/helix/workflows/concerns/. Each concern declares area scope and associated
practices that flow into context digests on beads.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/concerns.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/01-frame/concerns.md"><code>docs/helix/01-frame/concerns.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Concerns Selection Prompt

Guide the user through selecting project concerns from the library and
declaring any project-specific overrides.

## Approach

1. List available concerns from `.ddx/plugins/helix/workflows/concerns/` grouped by category:
   - **Tech stack**: typescript-bun, python-uv, rust-cargo
   - **Accessibility**: a11y-wcag-aa
   - **Observability**: o11y-otel
   - **Internationalization**: i18n-icu

2. For each category, ask the user:
   - Tech stack: &quot;What language, runtime, and package manager does this
     project use?&quot;
   - Data: &quot;What database or data layer?&quot;
   - Infrastructure: &quot;Where will this deploy?&quot;
   - Quality: &quot;Do you need accessibility (a11y), internationalization (i18n),
     or observability (o11y) support?&quot;

3. For each selected concern:
   - Check if the user wants to override any library practices
   - If overriding, ask for the governing ADR or create one
   - Ask if an ADR exists that justified this concern selection

4. Declare the project&#x27;s area labels — which `area:*` labels will beads use?
   The default set is: `ui`, `api`, `data`, `infra`, `cli`.

5. Check for practice conflicts between selected concerns and flag them.

6. Write `docs/helix/01-frame/concerns.md`.

## Key Rules

- Concerns are composable — selecting multiple is normal and expected.
- Project overrides take full precedence over library practices.
- Every override should reference a governing ADR when possible.
- The area taxonomy declared here controls which concerns are injected
  into which beads via `&lt;context-digest&gt;`.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: concerns
---

# Project Concerns

## Active Concerns

&lt;!-- Select from .ddx/plugins/helix/workflows/concerns/ or add custom entries.
     Each line: concern-name (category) — ADR reference that justified selection.
     The ADR ref is how the concern/ADR/spike chain stays traceable. --&gt;

- [concern-name] ([category]) — ADR-NNN: [one-line rationale]

## Project Overrides

&lt;!-- Override specific library practices. Cite the governing ADR. --&gt;

- [Practice]: [override] (see [ADR-NNN])

## Area Labels

This project uses the following area labels for concern scoping:

&lt;!-- Declare which area labels your beads use. Concerns are injected into
     beads based on matching these labels against each concern&#x27;s `areas` field. --&gt;

- `area:ui` — user-facing interfaces
- `area:api` — backend services and endpoints
- `area:data` — database, storage, data pipeline
- `area:infra` — deployment, CI/CD, infrastructure
- `area:cli` — command-line tools</code></pre></details></td></tr>
</tbody>
</table>
