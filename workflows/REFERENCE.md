---
dun:
  id: helix.workflow.reference
  depends_on:
    - helix.workflow
---
# HELIX Quick Reference Card

## Canonical Docs

- [README.md](README.md): high-level model and authority order
- [EXECUTION.md](EXECUTION.md): queue control and operator loop
- [BEADS.md](BEADS.md): upstream `bd` mapping and labels
- [implementation.md](actions/implementation.md): one bounded execution pass
- [check.md](actions/check.md): queue-drain decision
- [reconcile-alignment.md](actions/reconcile-alignment.md): top-down review
- [backfill-helix-docs.md](actions/backfill-helix-docs.md): conservative reconstruction
- [plan.md](actions/plan.md): iterative design document creation
- [polish.md](actions/polish.md): bead refinement before implementation
- [fresh-eyes-review.md](actions/fresh-eyes-review.md): post-implementation review
- [experiment.md](actions/experiment.md): metric-driven optimization iteration
- [metric-definition.yaml](templates/metric-definition.yaml): shared metric definitions

## Phase Summary

| Phase | Primary Output | Main Location |
|---|---|---|
| Optional `00-discover` | vision and opportunity framing | `docs/helix/00-discover/` |
| `01-frame` | requirements and stories | `docs/helix/01-frame/` |
| `02-design` | architecture and design contracts | `docs/helix/02-design/` |
| `03-test` | test plans and failing tests | `docs/helix/03-test/`, `tests/` |
| `04-build` | project build guidance + execution beads | `docs/helix/04-build/`, `.beads/` |
| `05-deploy` | rollout docs + deploy beads | `docs/helix/05-deploy/`, `.beads/` |
| `06-iterate` | backlog, reports, follow-up planning | `docs/helix/06-iterate/` |

## Authority Order

1. Product Vision
2. Product Requirements
3. Feature Specs / User Stories
4. Architecture / ADRs
5. Solution / Technical Designs
6. Test Plans / Tests
7. Implementation Plans
8. Source Code / Build Artifacts

## Core Commands

### Bootstrap

```bash
bd init
scripts/install-local-skills.sh
```

### Execution Commands

```bash
helix run
helix implement
helix implement bd-abc123
helix check repo
helix align repo
helix backfill repo
```

### Planning and Quality Commands

```bash
helix plan [scope]                    # create design document
helix plan --rounds 8 auth            # more refinement rounds
helix polish [scope]                  # refine beads before implementation
helix polish --rounds 10              # more polish rounds
helix next                            # recommended next bead (uses bv if available)
helix review [scope]                  # fresh-eyes review of recent work
helix spawn                           # launch multi-agent swarm (requires ntm)
helix spawn --count 3 --stagger 45    # 3 agents, 45s apart
helix experiment [bead-id|goal]       # one experiment iteration
helix experiment --close              # squash-merge and close session
```

### Beads

```bash
bd ready --json              # or: br ready --json
bd update <id> --claim       # or: br update <id> --status in_progress
bd show <id>                 # or: br show <id>
bd dep tree <id>             # or: br dep add/remove/list
bd blocked --json
bd close <id>                # or: br close <id>
bd doctor
```

See [BEADS.md](BEADS.md) for the full bd/br comparison and setup guidance.

## Beads Labeling

Labels are organizational conventions for triage and traceability. They are
not required by the execution loop queue guard.

Recommended labels:
- `helix` — identifies HELIX-managed beads (recommended, not required by the queue guard).
- Phase labels: `phase:build`, `phase:deploy`, `phase:iterate`, `phase:review`.
- Kind labels: `kind:build`, `kind:deploy`, `kind:backlog`, `kind:review`.
- Traceability labels: `story:US-XXX`, `feature:FEAT-XXX`, `area:<name>`, `source:metrics`.

## Decision Guide

- Starting new work or a large scope:
  run `helix plan`, then `helix polish`, then `helix run`.
- Ready execution beads exist:
  run `implementation` or `helix run`.
- No ready execution bead, but the planning stack exists and next work is
  unclear:
  run alignment.
- Canonical docs are missing or too incomplete to execute safely:
  run backfill.
- Work exists but is blocked or already in progress:
  stop and wait.
- The queue drains:
  run `check`, not a blind loop and not `bd list --ready`.
- After implementing a bead:
  run `helix review` for fresh-eyes quality check.

## Artifact Inputs

Use the prompts and templates under:

- `workflows/phases/00-discover/artifacts/`
- `workflows/phases/01-frame/artifacts/`
- `workflows/phases/02-design/artifacts/`
- `workflows/phases/03-test/artifacts/`
- `workflows/phases/04-build/artifacts/`
- `workflows/phases/05-deploy/artifacts/`
- `workflows/phases/06-iterate/artifacts/`

Those artifact directories support the canonical docs under `docs/helix/`; they
do not replace the bounded execution contract.

## Output Reports

- Alignment reviews:
  `docs/helix/06-iterate/alignment-reviews/AR-YYYY-MM-DD[-scope].md`
- Backfill reports:
  `docs/helix/06-iterate/backfill-reports/BF-YYYY-MM-DD[-scope].md`

## Validation

When changing HELIX wrapper behavior or the execution contract:

```bash
bash tests/helix-cli.sh
git diff --check
```
