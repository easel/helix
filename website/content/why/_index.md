---
title: Why HELIX
weight: 1
aliases:
  - /docs
  - /docs/background
---

HELIX is the **methodology layer** for AI-assisted software development.
It defines seven lifecycle phases, the artifacts that populate each, the
authority order that resolves their conflicts, and the cross-cutting
concerns that travel with the work. It runs on
[DDx](https://github.com/easel/ddx) — the platform substrate that owns
agent execution and the bounded queue-drain loop.

The premise is narrow but load-bearing: AI agents will do real software
work in the coming decade, and the work needs structure that survives
turnover, model upgrades, and the temptation to skip the parts that
don't feel like coding. HELIX is the structure.

This section makes the case in four pages.

{{< cards >}}
  {{< card link="the-problem" title="The Problem" subtitle="Why waterfall, agile, and vibe coding each fail in the era of AI-assisted development — and why a compromise of all three doesn't fix the failure." icon="exclamation-circle" >}}
  {{< card link="the-thesis" title="The Thesis" subtitle="HELIX as a methodology layer on the DDx platform — seven phases, an artifact graph, and concerns that propagate across phases." icon="academic-cap" >}}
  {{< card link="principles" title="Principles" subtitle="Eight load-bearing ideas behind the framework — the design choices that explain why HELIX is shaped the way it is." icon="light-bulb" >}}
  {{< card link="who-its-for" title="Who it's for" subtitle="The kinds of projects HELIX rewards, the kinds it overburdens, and the costs you pay to adopt it." icon="user-group" >}}
{{< /cards >}}

## What's actually in the framework

If you skip the prose and just want to see what HELIX provides:

- **[Forty-three artifact types](/artifacts/)** across seven phases —
  vision, PRDs, feature specs, ADRs, technical designs, test plans,
  runbooks, alignment reviews. Each with a description, the relationships
  to other artifacts, the generation prompt, the template, and (where
  available) a worked example.
- **[Eighteen cross-cutting concerns](/concerns/)** — tech stacks
  (TypeScript+Bun, Go, Rust, etc.), quality attributes (accessibility,
  observability, testing, i18n), security postures, infrastructure
  conventions. Each with components, constraints, and per-phase
  practices.
- **[Seven lifecycle phases](/reference/glossary/phases/)** — Discover,
  Frame, Design, Test, Build, Deploy, Iterate — with the artifacts they
  produce and the gates between them.
- **[Supervisory commands](/reference/glossary/actions/)** — `helix
  frame`, `helix design`, `helix run`, `helix align`, `helix evolve`,
  `helix review`. The verbs that drive the autopilot.

Once the *why* lands, [Use HELIX](/use/) shows you how to install the
framework, define your project's first artifacts, and run your first
supervised build.
