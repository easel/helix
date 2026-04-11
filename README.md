# HELIX

A supervisory autopilot for AI-assisted software delivery. HELIX enforces
specification-first, test-first discipline through structured phases — framing
the problem, designing the solution, writing failing tests, building the
implementation, and iterating with real feedback. Humans set direction and make
judgment calls; AI agents do the heavy lifting under HELIX's supervision.

HELIX is built on [DDx](https://documentdrivendx.github.io/ddx/) (Document-Driven
Development eXperience), a platform for AI-assisted development. DDx
provides the foundation that HELIX runs on: a document library for governing
artifacts, a work tracker for issue management, an agent harness for dispatching
AI models, and an execution engine for recording what happened. HELIX adds the
methodology layer — the phases, the authority order, the bounded execution loop,
and the skills that turn governing documents into working software.

**[Documentation](https://documentdrivendx.github.io/helix/)** · **[Demo Reels](https://documentdrivendx.github.io/helix/docs/demos/)** · **[Getting Started](https://documentdrivendx.github.io/helix/docs/getting-started/)**

![HELIX Quickstart Demo](docs/demos/helix-quickstart/recordings/helix-quickstart.gif)

## Install

First, install [DDx](https://documentdrivendx.github.io/ddx/):

```bash
curl -fsSL https://raw.githubusercontent.com/DocumentDrivenDX/ddx/main/install.sh | bash
```

Then install HELIX:

```bash
ddx install helix
```

You'll also need [Claude Code](https://claude.ai/claude-code) (or another
agent CLI like `codex`), plus `bash` and `git`.

## Quick Start

Start by shaping sparse intent into governed HELIX work:

```bash
helix input "Build a REST API for managing bookmarks"
```

Then let DDx drain the execution-ready queue:

```bash
ddx agent execute-loop
```

`helix input` is the preferred intake surface for new work. `ddx agent execute-loop`
is the primary queue-drain command for execution-ready beads. `helix run` and
`helix build` remain available as compatibility wrappers for operators who
still want HELIX-owned execution entrypoints.

### Interactive commands

Inside a Claude Code session, HELIX skills are available as slash commands:

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

### CLI (automation and scripting)

For automation and scripting, prefer the DDx-managed queue-drain path:

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

## Phases

HELIX guides work through six phases. Each phase produces governing
artifacts that drive the next:

0. **Discover** (optional) — Validate the opportunity
1. **Frame** — Define the problem and establish context
2. **Design** — Architect the solution approach
3. **Test** — Write failing tests that define behavior
4. **Build** — Implement code to make tests pass
5. **Deploy** — Release to production with monitoring
6. **Iterate** — Learn and improve for the next cycle

## How it works

1. You shape intent into governed work with `helix input`
2. HELIX creates or updates governing artifacts (vision → requirements → design → tests)
3. The tracker breaks work into issues with acceptance criteria
4. `ddx agent execute-loop` drains execution-ready work from the queue
5. Reviews catch bugs that implementation blindness misses
6. The loop continues until the queue drains or human input is needed

The key insight: **documents drive the agents**. Requirements define what to
build. Designs define how. Tests define done. The tracker sequences the work.
HELIX orchestrates the agents to follow this chain — and stops them when they
drift.

## Workflow Contract

The HELIX methodology lives in `workflows/` and covers:

- [Workflow Overview](workflows/README.md) — phases, authority order, execution model
- [Execution Guide](workflows/EXECUTION.md) — operator flow, queue control, loop behavior
- [Reference Card](workflows/REFERENCE.md) — quick lookup for actions and concepts
- Tracker: `ddx bead --help` — issue management conventions

## DDx Platform

HELIX is built on [DDx](https://documentdrivendx.github.io/ddx/) — a
platform for AI-assisted development. DDx provides the document library, work
tracker, agent harness, and execution engine. HELIX provides the methodology,
phases, authority order, and supervisory skills.

See [DDx Methodology](workflows/DDX.md) for the artifact graph, authority
hierarchy, evolution model, and agent context model.
