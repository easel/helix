---
title: Getting Started
weight: 1
prev: /docs
next: /docs/workflow
---

Get HELIX installed and running your first supervised build session.

## DDx and HELIX

[DDx](https://github.com/DocumentDrivenDX/ddx) (Document-Driven Development
eXperience) is the platform — it provides the document library, artifact graph,
tracker (`ddx bead`), agent harness (`ddx agent`), and execution framework
(`ddx exec`). HELIX is the methodology that runs on top of DDx — it defines
the phases (Frame → Design → Test → Build → Deploy → Iterate), the authority
order, the bounded execution loop, and the skills that drive AI agents through
structured delivery. You install DDx first, then install HELIX as a DDx package.

## Install

```bash
ddx install helix
```

This installs the HELIX skills, CLI, and shared workflow resources via the
[DDx](https://github.com/DocumentDrivenDX/ddx) package manager.

**Requirements:** [ddx](https://github.com/DocumentDrivenDX/ddx), `claude` or
`codex` CLI, bash, jq, git.

## Initialize a Project

```bash
cd your-project
ddx init                    # Set up DDx document library
helix frame                 # Create vision, PRD, feature specs
```

HELIX uses DDx for document management and issue tracking. `helix frame`
starts the planning process by creating the governing artifacts that drive
everything downstream.

## Run the Autopilot

```bash
helix run
```

`helix run` is HELIX's supervisory autopilot. It reads the tracker, selects
the highest-leverage next action, executes it, and repeats until human input
is needed or no work remains.

Key flags:

```bash
helix run --agent claude        # Use Claude as the agent
helix run --summary             # Concise output for background monitoring
helix run --max-cycles 10       # Stop after 10 completed build cycles
helix run --review-every 5      # Periodic alignment review
```

## Run Individual Commands

You can also drive HELIX interactively:

```bash
helix design auth               # Design the auth system
helix build                     # One bounded build pass
helix review                    # Fresh-eyes review of recent work
helix check                     # What should happen next?
helix align                     # Top-down reconciliation audit
helix evolve "add OAuth"        # Thread a requirement through the stack
helix triage "Fix login bug"    # Create a well-structured tracker issue
helix status                    # Lifecycle snapshot
```

## Monitor a Background Run

```bash
# Launch in the background
helix run --agent claude --summary --max-cycles 10 &

# Check progress
helix status

# Read failure details
cat .helix-logs/helix-*.log | tail -50
```

## Next Steps

- Read about the [HELIX workflow](../workflow) and how phases work
- See the full [CLI reference](../cli)
- Watch the [demo](../demos) of a complete HELIX lifecycle
