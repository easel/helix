# HELIX

A supervisory autopilot for AI-assisted software delivery. Specification-first,
test-first discipline through structured phases where tests are written before
implementation. Humans and AI agents collaborate throughout.

**[Documentation](https://easel.github.io/helix/)** · **[Demo Reels](https://easel.github.io/helix/docs/demos/)** · **[Getting Started](https://easel.github.io/helix/docs/getting-started/)**

![HELIX Quickstart Demo](docs/demos/helix-quickstart/recordings/helix-quickstart.gif)

## Install

```bash
# Clone and install (skills + CLI)
git clone https://github.com/easel/helix.git
cd helix && scripts/install-local-skills.sh
```

Or load as a Claude Code plugin (no install step):

```bash
claude --plugin-dir /path/to/helix
```

**Requirements:** bash, jq, git, [ddx](https://github.com/DocumentDrivenDX/ddx), and `claude` or `codex` CLI.

## Quick Start

```bash
cd your-project
ddx init                    # Set up document library and tracker
helix frame                 # Create vision, PRD, feature specs
helix run                   # Autopilot: build → review → check → repeat
```

Or run individual commands:

```bash
helix build                 # One bounded build pass
helix check                 # What should happen next?
helix design auth           # Design a subsystem
helix review                # Fresh-eyes review
helix status                # Queue health and lifecycle snapshot
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
| `helix run` | Loop: implement ready issues, check, decide, repeat |
| `helix build [issue]` | Execute one ready issue end-to-end |
| `helix check [scope]` | Decide next action (BUILD/DESIGN/ALIGN/BACKFILL/WAIT/STOP) |
| `helix align [scope]` | Top-down reconciliation review |
| `helix backfill [scope]` | Reconstruct missing HELIX docs |
| `helix design [scope]` | Create design document through iterative refinement |
| `helix status` | Show tracker health and queue summary |
| `helix evolve [requirement]` | Thread requirement through the artifact stack |
| `helix triage [title]` | Create well-structured tracker issues |
| `helix polish [scope]` | Refine issues before implementation |
| `helix next` | Show recommended next issue |
| `helix review [scope]` | Fresh-eyes post-implementation review |
| `helix experiment [issue]` | One metric-optimization iteration |

## Skills

HELIX publishes its portable skill surface from the repo at
`./.agents/skills` and installs those same skills into the canonical user path
`~/.agents/skills`.

Temporary compatibility mirror:
- `~/.claude/skills`

Installed skill set:

- `helix-run` <-> `helix run`
- `helix-build` <-> `helix build`
- `helix-check` <-> `helix check`
- `helix-align` <-> `helix align`
- `helix-backfill` <-> `helix backfill`
- `helix-design` <-> `helix design`
- `helix-polish` <-> `helix polish`
- `helix-next` <-> `helix next`
- `helix-review` <-> `helix review`
- `helix-experiment` <-> `helix experiment`
- `helix-evolve` <-> `helix evolve`
- `helix-triage` <-> `helix triage`

The contract is strict: public skill names are `helix-<command>` and must
mirror the CLI subcommand exactly.

The `skills/` tree remains the implementation source for skill content and
shared references. The project-level package surface that agent clients should
consume is `./.agents/skills`.

Required skill metadata:

- every published `SKILL.md` must declare `name` and `description`
- skills whose mirrored CLI command accepts a trailing scope, selector, or goal
  must also declare `argument-hint`
- `name` must match the skill directory basename exactly

Deterministic validation:

```bash
bash tests/validate-skills.sh
```

This validator checks directory-name to skill-name alignment, required
frontmatter, and the canonical `.agents/skills -> skills/` symlink contract.

## Workflow Contract

The HELIX-specific operating contract lives in `workflows/` and covers:

- authority order and canonical documentation
- bounded actions such as `implement`, `check`, `align`, and `backfill`
- the built-in tracker and queue-control rules
- the `helix` wrapper CLI used to run those actions consistently

Start with:

- [Workflow Overview](workflows/README.md)
- [Execution Guide](workflows/EXECUTION.md)
- Tracker: `ddx bead --help` (conventions in DDx FEAT-004)
- [Reference Card](workflows/REFERENCE.md)

## Tracker

HELIX uses a built-in file-backed tracker for execution tracking. Canonical
issues live in `.ddx/beads.jsonl`. Run `ddx bead` to manage issues,
`ddx bead import` to pull compatible JSONL into the canonical store, and
`ddx bead export` to write JSONL for interop or recovery.

## Documentation

- [DDx — Document-Driven Development Experience](workflows/DDX.md)
- [Workflow Contract](workflows/README.md)
- [Quality Ratchets](workflows/ratchets.md)
- [Conventions](workflows/conventions.md)

## Document-Driven Development Experience (DDx)

HELIX is the reference implementation of DDx — the tooling and methodology
layer that keeps governing documents current and uses them to drive AI agents
through software development.

See [DDx Methodology](workflows/DDX.md) for the artifact graph, authority
hierarchy, evolution model, and agent context model.

Originally developed in [ddx-library](https://github.com/easel/ddx-library),
HELIX was extracted to its own repository because it is the primary value:
DDx is the methodology, HELIX is the machine that runs it.
