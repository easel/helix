---
dun:
  id: helix.workflow.execution
  depends_on:
    - helix.workflow
    - helix.workflow.beads
---
# HELIX Execution Guide

This guide covers operator-facing HELIX execution flow: how to run bounded work
passes, how to decide whether more work remains, and how to automate the queue
for Codex or Claude Code.

For upstream Beads integration, labels, `spec-id`, and raw `bd` conventions,
see [BEADS.md](BEADS.md).

## Scope

This document owns HELIX execution behavior.

- Follow this file for queue guards, loop shape, and `NEXT_ACTION` handling.
- Follow the bounded action prompts under `workflows/helix/actions/` for
  action-specific behavior.
- Treat examples elsewhere in `workflows/helix/` as supportive summaries, not
  alternate execution contracts.

## Core Actions

HELIX uses four top-level execution actions:

- `helix implement`
  Executes one ready execution bead end-to-end, then exits.
- `helix check`
  Determines whether the next step is implementation, alignment, backfill,
  waiting, guidance, or stopping.
- `helix align <scope>`
  Runs a top-down reconciliation review and can emit follow-up execution beads.
- `helix backfill <scope>`
  Reconstructs missing HELIX docs conservatively from current evidence.

## Execution Model

Use a two-stage control loop:

1. Guard on true ready work with `bd ready`, not `bd list --ready`
2. Run the bounded `implementation` action while ready work exists
3. When the queue drains, run the bounded `check` action once
4. Follow `check` to either implement again, align, backfill, wait, ask for
   guidance, or stop

`bd ready` is blocker-aware. `bd list --ready` is not equivalent and should not
control an autonomous execution loop.

## Queue Guard

These examples assume `jq` is available.

```bash
helix_ready_count() {
  bd ready --json | jq 'length'
}
```

## Manual Loop

This is the minimal safe operator loop:

```bash
while [ "$(helix_ready_count)" -gt 0 ]; do
  helix implement
done

helix check
```

Interpret `check` as follows:

- `NEXT_ACTION: IMPLEMENT`
  More safe ready work exists; continue.
- `NEXT_ACTION: ALIGN`
  Run `reconcile-alignment` for the indicated scope.
- `NEXT_ACTION: BACKFILL`
  Run `backfill-helix-docs` for the indicated scope.
- `NEXT_ACTION: WAIT`
  Stop and wait for blockers or other in-progress work to resolve.
- `NEXT_ACTION: GUIDANCE`
  Stop and get user or stakeholder input.
- `NEXT_ACTION: STOP`
  No actionable work remains for the current scope.

## Agent Loops

The examples below assume a trusted local repository.

- Codex is intentionally run with `--dangerously-bypass-approvals-and-sandbox`
  and `--progress-cursor`.
- If the agent runtime cannot reach localhost Dolt sockets, force Beads direct
  mode with `BEADS_DOLT_SERVER_MODE=0`.

### Codex

```bash
while [ "$(helix_ready_count)" -gt 0 ]; do
  codex --dangerously-bypass-approvals-and-sandbox exec --progress-cursor -C "$PWD" --ephemeral <<'EOF'
Use the HELIX implementation action at workflows/helix/actions/implementation.md.
Execute one ready HELIX execution bead end-to-end.
Follow the action exactly.
EOF
done

codex --dangerously-bypass-approvals-and-sandbox exec --progress-cursor -C "$PWD" --ephemeral <<'EOF'
Use the HELIX check action at workflows/helix/actions/check.md.
Return the required NEXT_ACTION line and the exact next command.
Follow the action exactly.
EOF
```

### Claude Code

```bash
while [ "$(helix_ready_count)" -gt 0 ]; do
  claude -p \
    --permission-mode bypassPermissions \
    --dangerously-skip-permissions \
    --no-session-persistence <<'EOF'
Use the HELIX implementation action at workflows/helix/actions/implementation.md.
Execute one ready HELIX execution bead end-to-end.
Follow the action exactly.
EOF
done

claude -p \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  --no-session-persistence <<'EOF'
Use the HELIX check action at workflows/helix/actions/check.md.
Return the required NEXT_ACTION line and the exact next command.
Follow the action exactly.
EOF
```

## `helix run`

This repo also provides a small wrapper CLI at `scripts/helix`.

To expose it on your `PATH` locally:

```bash
scripts/install-local-skills.sh
```

That installer now also links `~/.local/bin/helix` to this repo's wrapper.

Main commands:

- `helix run`
- `helix implement`
- `helix check`
- `helix align`
- `helix backfill`

`helix run`:

- loops only while true ready HELIX execution work exists
- runs one bounded implementation pass at a time
- runs `check` when the queue drains
- can trigger `reconcile-alignment` every `N` cycles or when `check` returns
  `ALIGN`
- stops on `WAIT`, `GUIDANCE`, or `STOP`
- uses `codex --dangerously-bypass-approvals-and-sandbox exec
  --progress-cursor` when `--agent codex` is selected
- keeps wrapper and child Beads calls in direct mode when
  `BEADS_DOLT_SERVER_MODE=0` is set

Examples:

```bash
helix run
helix run --agent claude
helix run --review-every 5
helix check repo
helix align auth
```

## Reproducible Testing

The wrapper should be tested with deterministic command stubs rather than live
Codex or Claude sessions.

Run:

```bash
bash tests/helix-cli.sh
```

This harness:

- creates temporary git workspaces
- stubs `bd`, `codex`, and `claude`
- drives exact ready-queue and `NEXT_ACTION` sequences
- verifies `helix run`, periodic alignment, auto-alignment, dry-run output, and
  installer behavior

## Pre-Execution Pipeline

Before the implementation loop, the recommended sequence for new work is:

1. `helix plan [scope]` — create a comprehensive design document through
   iterative refinement (recommended for new features or major work)
2. `helix polish [scope]` — refine beads against the plan: deduplication,
   coverage verification, acceptance criteria sharpening (recommended after
   bead creation)
3. `helix run` — execute the bounded implementation loop

These steps are optional for small changes but strongly recommended for any
scope that will produce more than a handful of beads.

## Graph-Aware Routing

When `bv` is available, `helix implement` injects dependency graph metrics
(PageRank, betweenness centrality) into the agent prompt to inform Phase 2
candidate ranking:

- High PageRank + High Betweenness = critical bottleneck (prioritize)
- Low PageRank + Low Betweenness = leaf work (safe to parallelize)

When `bv` is absent, the existing `bd ready` ranking applies unchanged.

`helix next` prints the recommended next bead without spawning an agent:

```bash
helix next          # uses bv if available, falls back to bd ready
```

## Fresh-Eyes Review

After implementing a bead, `helix review` performs 1-3 self-review passes
looking for bugs, integration issues, and security concerns with fresh
perspective:

```bash
helix review                  # review last commit
helix review bd-abc123        # review changes for a specific bead
helix review src/auth/        # review specific files
```

## Swarm Execution

`helix spawn` launches multiple agents in tmux sessions via `ntm`:

```bash
helix spawn                       # 2 agents, 30s stagger (default)
helix spawn --count 3 --stagger 45  # 3 agents, 45s apart
```

- Staggered starts (default 30s apart) avoid thundering herd contention
- All agents share the same `bd` tracker
- Bead claiming via `bd update --claim` provides advisory locking
- Agents are fungible — any agent picks any bead
- Graceful fallback to single-agent `helix run` when `ntm` is absent

## Experiment Loop

`helix experiment` runs a single iteration of a metric-optimization loop for
`phase:iterate` beads. Each invocation: hypothesize → edit → test → benchmark →
keep/discard → log → exit.

The loop is driven externally by the `/ddx:experiment` skill (analogous to how
`/ddx:grind` drives repeated `implement` calls) or by the operator re-invoking
the command. This preserves the bounded-action model.

Experiments are operator-invoked only — `helix check` does not produce a
`NEXT_ACTION: EXPERIMENT` code. The operator chooses `helix experiment` instead
of `helix implement` for optimization work.

The experiment action requires a clean worktree. The CLI prompts the user to
commit uncommitted changes before proceeding.

The optimization target is a HELIX metric definition at
`docs/helix/06-iterate/metrics/<name>.yaml`. If one exists, the experiment
reads it; if not, the experiment creates one during setup. This connects
experiments to ratchets and monitoring through a shared metric definition.

Session artifacts (`autoresearch.*`, `experiments/`) are untracked local files,
gitignored on the experiment branch. At session close (`helix experiment
--close`), the action squash-merges the experiment branch back to produce a
single commit and records the result in the bead close comment. Experiments
are execution-layer work tracked by beads, not canonical HELIX docs.

`--close` is unique to the experiment command — it directs the action to
execute session close (squash-merge, ratchet update, bead close) instead of
running another iteration.

Experiments validate governing artifacts at session setup and close (not
per-iteration). Per-iteration guardrails are: scoped files, mandatory test
passage, and the experiment's own constraints. All existing tests must pass
after every kept iteration.

## Practical Rules

- Keep execution bounded to one bead per implementation pass.
- Do not use an unconditional `while true` loop.
- Treat `check` as the queue-drain decision point, not `reconcile-alignment`.
- Use alignment to expose or refine the next work set, not as the default work
  picker.
- Do not auto-run backfill unless you are intentionally reconstructing missing
  canonical docs.
