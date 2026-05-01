---
title: Concerns
weight: 4
generated: true
aliases:
  - /docs/glossary/concerns
  - /reference/glossary/concerns
---

**Cross-cutting concerns** are HELIX's mechanism for declaring shared standards once and propagating them everywhere agents work.

A concern bundles a description, components, constraints, and drift signals with per-phase practices. When an agent claims a bead, HELIX synthesizes a *context digest* that includes the active concerns — so the agent makes consistent technology choices, follows the project's conventions, and respects quality requirements without having to re-derive them from the codebase.

Concerns are how HELIX answers "every project needs this kind of consistency" without forcing any specific tech stack on the framework itself.

## Tech Stack

{{< cards >}}
  {{< card link="go-std" title="Go + Standard Toolchain" subtitle="all" >}}
  {{< card link="python-uv" title="Python + uv" subtitle="all" >}}
  {{< card link="react-nextjs" title="React + Next.js" subtitle="web, ui" >}}
  {{< card link="rust-cargo" title="Rust + Cargo" subtitle="all" >}}
  {{< card link="scala-sbt" title="Scala + sbt" subtitle="all" >}}
  {{< card link="typescript-bun" title="TypeScript + Bun" subtitle="all" >}}
{{< /cards >}}

## Quality Attributes

{{< cards >}}
  {{< card link="a11y-wcag-aa" title="Accessibility (WCAG 2.1 AA)" subtitle="ui, frontend" >}}
  {{< card link="e2e-kind" title="E2E Testing with Kind Clusters" subtitle="api, infra" >}}
  {{< card link="e2e-playwright" title="E2E Visual Testing (Playwright)" subtitle="ui, site" >}}
  {{< card link="i18n-icu" title="Internationalization (ICU MessageFormat)" subtitle="ui, frontend" >}}
  {{< card link="o11y-otel" title="Observability (OpenTelemetry)" subtitle="api, backend, infra" >}}
  {{< card link="testing" title="Testing" subtitle="all" >}}
  {{< card link="ux-radix" title="UX Interaction Patterns (Radix)" subtitle="ui, frontend" >}}
{{< /cards >}}

## Security & Compliance

{{< cards >}}
  {{< card link="security-owasp" title="Security (OWASP)" subtitle="all" >}}
{{< /cards >}}

## Infrastructure

{{< cards >}}
  {{< card link="k8s-kind" title="Kubernetes + kind" subtitle="infra" >}}
{{< /cards >}}

## Documentation & Demos

{{< cards >}}
  {{< card link="demo-asciinema" title="Demo Reels (Asciinema)" subtitle="all" >}}
  {{< card link="demo-playwright" title="Demo Reels (Playwright)" subtitle="ui, frontend" >}}
  {{< card link="hugo-hextra" title="Microsite (Hugo + Hextra)" subtitle="all" >}}
{{< /cards >}}
