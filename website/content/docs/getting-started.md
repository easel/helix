---
title: Getting Started
weight: 1
prev: /docs
next: /docs/background
---

Get HELIX installed and running your first supervised build session.

## DDx and HELIX

HELIX is built on [DDx](https://documentdrivendx.github.io/ddx/) (Document-Driven
Development eXperience), a platform for AI-assisted development. DDx
provides the foundation: a **document library** for managing governing artifacts
like specs and designs, a **work tracker** (`ddx bead`) for issue management with
dependencies and claims, an **agent harness** (`ddx agent`) for dispatching AI
models with token tracking, and an **execution engine** (`ddx exec`) for recording
structured evidence of what happened.

HELIX adds the methodology on top — the development phases
(Frame → Design → Test → Build → Deploy → Iterate), the authority order that
resolves conflicts between artifacts, the bounded execution loop that decides
what to do next, and the skills that turn all of this into agent instructions.
You install DDx first, then install HELIX as a DDx package.

## Install

First, install DDx:

```bash
curl -fsSL https://raw.githubusercontent.com/DocumentDrivenDX/ddx/main/install.sh | bash
```

Then install HELIX:

```bash
ddx install helix
```

You'll also need [Claude Code](https://claude.ai/claude-code) (or another
agent CLI like `codex`), plus `bash` and `git`.

## Start Building

Start by shaping your request into governed HELIX work:

```bash
helix input "Build a REST API for managing bookmarks"
```

`helix input` is the preferred intake surface for new work. It turns sparse
intent into the governing artifacts and tracker beads that HELIX and DDx use
downstream.

## Understand the Artifact Hierarchy

After framing, your project has governing artifacts at different zoom levels:

```
Product Vision          "What is this and why?"
  └── PRD               "What must it do?"
       └── Feature Spec  "What exactly does this feature do?"
            └── Bead     "One unit of work to implement it"
```

Higher levels govern lower levels. If a feature spec contradicts the PRD,
the PRD wins. HELIX enforces this automatically — you don't need to remember
the hierarchy, but understanding it helps you steer effectively.

## Add Work to the Tracker

HELIX works from a tracker queue. After framing, you can add specific work
items:

```
> /helix-triage "Add user authentication with OAuth"
```

This creates a well-structured bead with acceptance criteria, spec references,
and a context digest that tells the implementing agent everything it needs to
know. You can also add beads directly:

```bash
ddx bead create "Add OAuth login flow" --type task \
  --labels helix,phase:build --set spec-id=FEAT-001 \
  --acceptance "OAuth login redirects to provider and returns a session token"
```

## Run the Autopilot

Once framing or triage has produced execution-ready beads, drain the queue with DDx:

```bash
ddx agent execute-loop
```

This is the primary execution path. DDx claims ready beads, executes the
bounded work, records evidence, and closes completed items. `helix run` and
`helix build` still exist as compatibility wrappers for operators who prefer
the older HELIX-owned entrypoints.

## Interactive Commands

Inside a Claude Code session, HELIX skills are available as slash commands.
You can invoke them at any time to steer the work:

| Command | What it does |
|---------|-------------|
| `/helix-input "build a bookmarks API"` | Shape sparse intent into governed HELIX work |
| `/helix-run` | Compatibility autopilot wrapper over DDx queue drain |
| `/helix-build` | Compatibility wrapper for one bounded implementation pass |
| `/helix-frame` | Create vision, PRD, and feature specs |
| `/helix-design auth` | Design a subsystem through iterative refinement |
| `/helix-review` | Fresh-eyes review of recent work |
| `/helix-evolve "add OAuth"` | Thread a new requirement through the artifact stack |
| `/helix-check` | What should happen next? |
| `/helix-align` | Top-down reconciliation review |
| `/helix-triage "Fix login bug"` | Create a well-structured tracker issue |
| `/helix-status` | Queue health and lifecycle snapshot |
| `/helix-experiment` | Metric-driven optimization loop |
| `/helix-polish` | Refine issues before implementation |

You can also just describe what you want in natural language — Claude
understands HELIX context and will invoke the right skills:

```
> The auth module needs OAuth support. Thread that through the specs and design.
> Review the last commit for security issues.
> What should we work on next?
```

## Background Execution (CLI)

For long-running work, CI integration, or scripting, prefer the DDx-managed
execution path:

```bash
helix input "Build a REST API for managing bookmarks"
ddx agent execute-loop                # Primary queue-drain surface
ddx agent execute-loop --once         # One bounded drain pass
```

Compatibility wrappers remain available:

```bash
helix run --agent claude --summary    # Compatibility autopilot wrapper
helix build                           # Compatibility bounded build wrapper
helix start                           # Daemon mode with PID file
helix status                          # Check progress
helix stop                            # Stop the daemon
```

Or run the queue-drain command directly:

```bash
ddx agent execute-loop                # Drain the ready queue until it stops
ddx agent execute-loop --once         # Stop after one bounded pass
```

## Next Steps

- Read about the [HELIX workflow](../workflow) and how phases work
- See the full [CLI reference](../cli) for automation and scripting
- Watch the [demo reels](../demos) of HELIX in action
