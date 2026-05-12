---
name: helix-triage
description: Shape HELIX work items with governing artifact references and deterministic acceptance criteria.
argument-hint: '"Title" [--type task|epic|bug|chore] [options...]'
---

# Triage: Shape Execution-Ready And Planning Issues

Triage turns requests, review findings, bugs, and follow-on ideas into durable
work items. Execution-ready implementation beads should enter the tracker ready to
execute; if the request is vague, route it to planning/polish or file it explicitly as a
not-execution-ready item until its success criteria are measurable.

## When to Use

- the user asks for work to be done, tracked, queued, or filed as an issue
- the user mentions bugs, tasks, or work items that need creating
- creating new implementation, design, or test issues
- decomposing an epic into child tasks
- recording blockers or follow-on work during implementation
- filing bugs discovered during review or testing
- batch-creating execution issues from alignment review gaps or gap registers
- any time work should enter the tracker rather than be listed as next steps

Trigger rule: If the user is asking for work and it is not a spec or
requirement change, default to triage. When in doubt between suggesting next
steps and filing issues, file the issues.

## Required Shape

Use these conventions so work remains executable and traceable:

| Field | Required For | What To Set |
|-------|-------------|-------------|
| Phase | All work | Frame, design, test, build, deploy, iterate, or review |
| Governing artifact | Tasks | Nearest authorizing artifact, such as a design, decision, or test plan |
| Acceptance | Tasks, epics | Deterministic completion and success-measurement criteria |
| Description | Recommended | Work contract: what to do, which files, governing artifact references |
| Design note | Recommended | Implementation approach: how to do it |

Additional taxonomy should capture work kind and affected product area when the
project has a declared concern or area model.

## Methodology

1. **Identify the governing artifact.** What spec, design, decision, or test
   plan authorizes this work?
2. **Write deterministic acceptance and success-measurement criteria.** The
   criteria should be verifiable by running a specific command, checking a
   specific condition, or observing an explicit end state. Bad: "system works
   correctly." Good: "the named test command passes and the relevant artifact
   records the active acceptance case."
3. **Choose type and taxonomy.** Use bounded tasks for most work, epics for
   collections of tasks, bugs for broken behavior, and chores for maintenance.
4. **Set parent and dependencies.** If this is part of a larger goal, attach it
   to that parent. If order matters, encode explicit dependencies.
5. **Assemble compact context.** Include active principles, concerns,
   practices, relevant decisions, and governing artifact context so the
   implementing agent can work from the item alone.
6. **Create the work item.** Triage must not create execution-ready implementation beads without
   measurable success criteria. If criteria cannot be made measurable, route
   the work back to planning/polish, or file it as a not-execution-ready item.
7. **Leave execution closure to DDx.** Shape beads so DDx-managed execution to close merged work with evidence
   can verify the result without re-reading the original conversation.

## Decomposition Pattern

When an epic or large task needs breakdown:

1. Read the parent's acceptance criteria.
2. Create child tasks that collectively cover every criterion.
3. Attach each child to the parent.
4. Add explicit dependency edges when child order matters.
5. Each child should be completable in one bounded implementation cycle.
6. If a task has multiple children, consider promoting it to an epic.

## Running with DDx

Tracker conventions: `ddx bead --help` (DDx FEAT-004)

Implementation action:

- `.ddx/plugins/helix/workflows/actions/implementation.md`

CLI help:

```bash
ddx bead create --help
```

DDx metadata conventions:

| Field | Required For | What To Set |
|-------|-------------|-------------|
| `--labels helix,phase:*` | All issues | `helix` + one of `phase:frame`, `phase:design`, `phase:test`, `phase:build`, `phase:deploy`, `phase:iterate`, `phase:review` |
| `--spec-id` | Tasks | Nearest governing artifact (e.g., `SD-001`, `ADR-048`, `TP-SD-014`) |
| `--acceptance` | Tasks, Epics | Deterministic completion and success-measurement criteria |
| `--description` | Recommended | Work contract: what to do, which files, governing artifact references |
| `--design` | Recommended | Implementation approach: how to do it |

Additional labels to include when applicable:

- `kind:build`, `kind:implementation`, `kind:testing`, `kind:documentation`
- `area:*` for the affected subsystem, using the taxonomy declared in `docs/helix/01-frame/concerns.md`

DDx context digest:

- Follow `.ddx/plugins/helix/workflows/references/context-digest.md` to build a compact summary.
- Prepend the `<context-digest>` XML block to the description.
- If the repo ships `scripts/refresh_context_digests.py`, use it after bead creation instead of hand-writing digest XML.
- The `<concerns>` field must list concern names, never area labels.

Example:

```bash
new_id="$(ddx bead create "Implement X" \
  --type task \
  --labels helix,phase:build,kind:implementation,area:wal \
  --spec-id SD-017 \
  --description "<context-digest>
<principles>Design for simplicity · Tests first · Fake data</principles>
<concerns>typescript-bun | postgres</concerns>
<practices>ESLint strict · Biome · bun:test</practices>
<adrs>ADR-050 event sourcing for audit</adrs>
<governing>SD-017 §3.2 — Y component must handle partial writes</governing>
</context-digest>

Implement the Y component per SD-017 Section 3.2. Governing: SD-017, TP-SD-017, ADR-050." \
  --acceptance "cargo test -p niflheim-wal test_y passes; AC-SD17-005 promoted to active" \
  --parent hx-epic-id)"

ddx bead dep add "$new_id" hx-dependency-id
```
