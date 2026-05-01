---
title: Use HELIX
weight: 4
---

The how-to layer. Once you understand [why HELIX is shaped the way it
is](/why/), this section explains how to run it in practice — installing
the plugin, framing your project, designing solutions, building under
test, and steering the autopilot day to day.

## Start here

{{< cards >}}
  {{< card link="getting-started" title="Getting Started" subtitle="Install HELIX, set up DDx, and run your first supervised build session in under 10 minutes." icon="play" >}}
  {{< card link="workflow" title="The Workflow" subtitle="The seven lifecycle phases, the autopilot loop, gating, and how the system makes decisions about what to do next." icon="refresh" >}}
{{< /cards >}}

## How HELIX runs

Three patterns of use, depending on how much autonomy you want:

- **Manual.** You run individual phase commands (`helix frame`, `helix
  design`, etc.) and review every output before accepting it. HELIX
  enforces phase gates and validates artifacts; you make every decision.
- **Supervised.** You use `helix run` to advance the project
  continuously. The autopilot picks the highest-leverage next bead,
  dispatches an agent, captures evidence, and either closes the bead or
  surfaces a blocker. You step in when the loop stops at a human-judgment
  point.
- **Bounded autonomous.** For specific scopes (a feature, a phase, a
  sprint), `helix run --autonomy high` lets the loop go further between
  human gates — useful for routine implementation work where the design
  is settled.

The slider between these is per-task. The same project can run a critical
spec change in manual mode and a routine code change in bounded
autonomous mode.

## Cross-cutting concerns

When you frame a project, you select active [cross-cutting
concerns](/concerns/) — tech stack, accessibility, observability,
security posture. From that point forward, every bead the autopilot
creates inherits those concerns automatically. Agents make consistent
choices because the context digest tells them what the project values
before they start.

{{< cards >}}
  {{< card link="workflow/concerns" title="Cross-Cutting Concerns" subtitle="How concerns are declared, selected, propagated into beads, and used by agents during execution." icon="shield-check" >}}
{{< /cards >}}
