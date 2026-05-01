---
title: The Thesis
weight: 3
---

HELIX is the **methodology layer** for AI-assisted software delivery —
seven phases, a graph of artifacts, and a set of cross-cutting concerns
that travel with the work. It runs on [DDx](https://github.com/easel/ddx),
the platform substrate that owns agent execution, the bead/tracker
primitives, and the bounded queue-drain loop. The two together give you
supervised autonomy: AI agents that do real work, on artifacts you can
audit, with human judgment exactly where it matters.

## Three structural commitments

### Phases and artifacts give the work its shape

A HELIX project moves through [seven
phases](/reference/glossary/phases/): Discover, Frame, Design, Test,
Build, Deploy, Iterate. Each phase produces a specific set of
[artifacts](/artifacts/) — vision documents in Discover, PRDs and
feature specs in Frame, ADRs and contracts in Design, test plans in
Test, code in Build, runbooks in Deploy, alignment reviews in Iterate.

Forty-three artifact types in total, each with a defined role, a generation
prompt, a template, and a place in the [authority
order](/why/principles/#3-authority-order-governs-reconciliation). When
an artifact is missing or stale, HELIX knows which phase produces it. When
two artifacts disagree, the higher-authority one wins.

### Concerns inject standards across phases

[Cross-cutting concerns](/concerns/) — accessibility requirements, the
project's tech stack, observability strategy, security posture — are
declared once and propagated into every relevant bead via a *context
digest*. An agent claiming a bead inherits the active concerns
automatically. Stack drift, convention drift, and quality-attribute
amnesia stop being problems an operator has to remember to fix.

This is HELIX's answer to "every project needs consistency" without
forcing any specific tech stack on the framework itself. The standards
are project-owned. The injection mechanism is universal.

### Supervision wraps DDx's execution loop

`helix run` wraps DDx's `agent execute-loop` with supervisory behavior.
DDx claims ready beads, dispatches agents, captures execution evidence,
and closes work on merge. HELIX decides which beads are ready, which is
the highest leverage to claim next, when to stop for a human decision,
and which model to assign. The platform is the engine; HELIX is the
operator.

When something requires human judgment that the system cannot make for
itself — authority missing, ambiguity beyond automation, a product
question only the team can answer — the loop halts and tells the
operator exactly what is needed and why.

## What this shape buys you

- **Coherence at scale.** The artifact graph grows with the project.
  Agents joining (or replacing earlier agents) inherit full context, not
  partial recollection.
- **Durable knowledge.** Documents survive sessions, model upgrades, and
  team turnover. Institutional memory lives in the repository, not in
  someone's head.
- **Steerable autonomy.** The autopilot does work; the human steers via
  tracker state and gate decisions. The slider between manual and
  autonomous is per-task — set per bead, per phase, per project.
- **Compounding feedback.** Every bead leaves execution evidence. Every
  review leaves findings. Every change updates downstream artifacts. The
  knowledge that produces good work next time is captured by the work
  that happened this time.

## Read more

The eight load-bearing ideas behind these commitments are documented in
[Principles](/why/principles/). The full artifact catalog is in
[Artifacts](/artifacts/). The cross-cutting standards layer is in
[Concerns](/concerns/). When you're ready to build, [Use
HELIX](/use/) walks through installing, defining your project's first
artifacts, and running your first supervised build.
