---
dun:
  id: helix.workflow.quickstart
  depends_on:
    - helix.workflow
---
# HELIX Workflow Quick Start Guide

Use this guide to start a repo on the current HELIX contract without learning
the whole workflow tree first.

## Start Here

Read these files in order when you need the canonical contract:

1. [README.md](README.md)
2. [EXECUTION.md](EXECUTION.md)
3. [BEADS.md](BEADS.md)

Use the bounded action prompts only when you are doing the corresponding work:

- [implementation.md](actions/implementation.md)
- [check.md](actions/check.md)
- [reconcile-alignment.md](actions/reconcile-alignment.md)
- [backfill-helix-docs.md](actions/backfill-helix-docs.md)

## Bootstrap A Repo

```bash
bd init
scripts/install-local-skills.sh
```

Notes:

- `bd init` creates the upstream Beads workspace in `.beads/`.
- `scripts/install-local-skills.sh` links the local `helix` wrapper into
  `~/.local/bin/helix`.
- The wrapper is optional but preferred for operator loops.

## Build The Canonical Planning Stack

Prompts and templates live under `workflows/helix/phases/<phase>/artifacts/`.
Use them to draft or refine the canonical docs under `docs/helix/`.

Typical order:

1. Optional discovery in `docs/helix/00-discover/`
   Capture product vision, business case, and opportunity context when needed.
2. Frame in `docs/helix/01-frame/`
   Write the PRD, feature specs, user stories, and supporting requirement docs.
3. Design in `docs/helix/02-design/`
   Define architecture, ADRs, contracts, solution designs, and technical
   designs.
4. Test in `docs/helix/03-test/` and `tests/`
   Write the test plan and failing tests before implementation.
5. Build in `docs/helix/04-build/` plus upstream `bd`
   Keep project build guidance in docs and story-level execution work in Beads.
6. Deploy in `docs/helix/05-deploy/` plus upstream `bd`
   Keep rollout docs canonical and rollout tasks in Beads.
7. Iterate in `docs/helix/06-iterate/`
   Capture backlog, lessons, reviews, and next-iteration planning.

## Create Execution Work

HELIX execution runs through upstream Beads, not HELIX-specific task files.

Build, deploy, and iterate execution work should:

- use native `bd` issues and dependencies
- carry `helix` plus one phase label
- cite the governing docs with `spec-id` and/or description
- stay small enough to close independently

See [BEADS.md](BEADS.md) for the mapping and examples.

## Run The Queue

Preferred wrapper commands:

```bash
helix run
helix implement
helix check repo
helix align repo
helix backfill repo
```

These are equivalent to direct action commands:

```bash
helix implement
helix check
helix align repo
helix backfill repo
```

Execution rules:

- Use `implementation` for one ready execution bead at a time.
- When the ready queue drains, run `check`.
- Run alignment only when the plan exists but the next work set is unclear.
- Run backfill only when the canonical stack is missing or too weak.
- Do not drive the queue with `bd list --ready`.

## Minimal Operator Loop

If you are not using `helix run`, use the bounded manual loop from
[EXECUTION.md](EXECUTION.md):

```bash
while [ "$(bd ready --json | jq 'length')" -gt 0 ]; do
  helix implement
done

helix check
```

## Common Next Steps

- Need artifact structure or naming rules:
  Read [conventions.md](conventions.md) and the relevant phase README.
- Need queue behavior:
  Read [EXECUTION.md](EXECUTION.md).
- Need `bd` labels or bead examples:
  Read [BEADS.md](BEADS.md).
- Need a top-down audit:
  Run alignment with [reconcile-alignment.md](actions/reconcile-alignment.md).
- Need missing docs reconstructed:
  Run backfill with [backfill-helix-docs.md](actions/backfill-helix-docs.md).

## Validation

When you change HELIX wrapper behavior or its contract docs, run:

```bash
bash tests/helix-cli.sh
git diff --check
```
