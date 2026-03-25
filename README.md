# HELIX

A test-driven development workflow for AI-assisted software development.

HELIX enforces specification-first, test-first discipline through a structured
phase approach where tests are written BEFORE implementation. Human creativity
and AI capabilities collaborate throughout, with tests serving as the contract
between design and implementation.

## Quick Start

```bash
# Install skills and CLI
scripts/install-local-skills.sh

# Run the execution loop
helix run --agent claude

# Or run individual commands
helix implement
helix check
helix plan auth
helix experiment --close
```

## Phases

0. **Discover** (optional) — Validate the opportunity
1. **Frame** — Define the problem and establish context
2. **Design** — Architect the solution approach
3. **Test** — Write failing tests that define behavior
4. **Build** — Implement code to make tests pass
5. **Deploy** — Release to production with monitoring
6. **Iterate** — Learn and improve for the next cycle

## CLI Commands

| Command | Purpose |
|---------|---------|
| `helix run` | Loop: implement ready beads, check, decide, repeat |
| `helix implement [bead]` | Execute one ready bead end-to-end |
| `helix check [scope]` | Decide next action (IMPLEMENT/ALIGN/BACKFILL/WAIT/STOP) |
| `helix align [scope]` | Top-down reconciliation review |
| `helix backfill [scope]` | Reconstruct missing HELIX docs |
| `helix plan [scope]` | Create design document through iterative refinement |
| `helix polish [scope]` | Refine beads before implementation |
| `helix next` | Show recommended next bead (uses bv if available) |
| `helix review [scope]` | Fresh-eyes post-implementation review |
| `helix experiment [bead]` | One metric-optimization iteration |
| `helix spawn` | Launch multi-agent swarm (requires ntm) |

## Skills

Installed as Claude Code skills (invocable as `/helix:<name>`):

- `helix` — Main workflow execution
- `helix-alignment-review` — Drift analysis and traceability
- `execute` — Single bead end-to-end
- `grind` — Continuous queue execution
- `review` — Critical review for errors
- `triage` — Queue health analysis
- `handoff` — Review changes from other agents
- `plan` — Design document creation
- `polish` — Bead refinement
- `experiment` — Metric-driven optimization loop

## Beads Integration

HELIX uses [Beads](https://github.com/steveyegge/beads) (`bd`) for execution
tracking. Run `bd onboard` to get started.

## Documentation

- [Workflow Overview](workflows/helix/README.md)
- [Execution Guide](workflows/helix/EXECUTION.md)
- [Beads Integration](workflows/helix/BEADS.md)
- [Reference Card](workflows/helix/REFERENCE.md)
- [Quality Ratchets](workflows/helix/ratchets.md)
- [Conventions](workflows/helix/conventions.md)

## Origin

HELIX is the reference implementation of Document-Driven Development (DDx).
Originally developed in [ddx-library](https://github.com/easel/ddx-library),
it was extracted to its own repository to reflect the reality that HELIX is
the primary value and warrants its own identity.
