---
title: Who it's for
weight: 4
---

HELIX is built for a specific shape of work. It rewards some teams and
overburdens others. Knowing which side you're on saves time.

## You should use HELIX if

**You're using AI agents on non-trivial software work.** HELIX is
designed for the case where agents are real participants in the work — not
autocomplete inside an IDE, but agents that read specs, claim beads, write
code, and submit reviews. If you have ever watched an agent loop without
making progress because it was re-deriving requirements from existing
code, HELIX is for you.

**Your project has more than one person — or more than one agent — over
time.** Knowledge that lives in one head doesn't survive turnover. HELIX's
artifact graph keeps intent durable across humans rotating in and out and
across model upgrades that make the previous agent obsolete.

**You care about coherence as the project grows.** Some projects can run
on memory and momentum until they ship. Others need to stay aligned across
months or years of incremental change. HELIX is built for the second case
— it pays a small upfront tax in artifacts to prevent the much larger tax
of drift.

**You want supervised autonomy, not full autonomy.** If you want an agent
that runs all night and reports a fait accompli, HELIX is the wrong tool.
The control system is designed around explicit human decision points.
That is the feature, not a limitation we plan to remove.

**You think in documents.** HELIX assumes that writing down intent, in a
form your collaborators can read and amend, is worth doing. Teams that
treat documentation as a chore will fight the system. Teams that treat
documentation as engineering will find HELIX is mostly already how they
think.

## You should not use HELIX if

**You're writing a one-off script.** A scratch utility doesn't need an
artifact graph. The smallest sufficient action is to write the script.

**You're prototyping a new idea where coherence doesn't matter yet.**
Throwaway prototypes are throwaway by design. HELIX optimizes for
projects that need to stay coherent past the first ship; it doesn't
optimize for projects you intend to throw away.

**You don't use AI agents.** A team writing all of its own code without
agentic assistance can adopt parts of HELIX (the artifact discipline, the
authority order) and benefit from them. But the framework's load-bearing
features — `helix run`, the bead/agent loop, cross-model review — assume
agents are part of the work. Without that, you're paying for machinery
you aren't using.

**You need to ship in a strictly regulated environment where AI cannot
write code.** Some industries forbid the very pattern HELIX is built
around. The framework is honest about being designed for AI-assisted
work; it does not retrofit cleanly to environments that cannot accept
that.

**You want a methodology to follow rather than a control system to
operate.** HELIX is not a process you check boxes against. It is a system
you run, with state, gates, and decisions. If your team prefers a
methodology document and quarterly retrospectives, traditional agile
frameworks will fit better. HELIX assumes you want to run something, not
just believe in something.

## What you give up to use it

HELIX has costs. Every team adopting it pays:

- **Up-front artifact discipline.** A one-paragraph idea won't run; you
  need at least a vision, a requirements outline, and a first feature
  spec to start the autopilot. For small projects this can feel heavy.
- **Tracker discipline.** Beads, dependencies, gates, and labels are not
  optional. The autopilot reads tracker state to decide what to do; a
  sloppy tracker produces a sloppy autopilot.
- **Document maintenance.** Artifacts drift. Cross-cutting concerns
  evolve. Specs need amendments. HELIX gives you tools (`helix evolve`,
  `helix align`) to keep things consistent, but the work is real.

In return, you get a system where AI agents do meaningful work without
losing the plot, where institutional knowledge survives turnover, and
where the next change is easy to make because the last change was
properly recorded. Whether that trade is worth it depends on the project.

If you're not sure, the cheapest experiment is to try HELIX on a single
non-trivial feature. The framework is designed to be adopted incrementally
— see [Getting Started](/use/getting-started) for the minimal first
build.
