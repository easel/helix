---
name: helix-build
description: Execute one bounded HELIX implementation pass for a selected work item.
argument-hint: "[issue-id|scope]"
disable-model-invocation: true
---

# Build

Run one bounded implementation attempt for a selected execution-ready work item.

If a specific issue or scope is given, use: $ARGUMENTS

## Methodology

A build pass is intentionally narrow. It should implement one coherent slice of
work, preserve traceability to governing artifacts, and stop once the declared
acceptance criteria can be evaluated.

## Readiness Rules

Before starting implementation:

1. Ensure the selector resolves to one execution-ready work item.
2. Confirm the work item has deterministic acceptance and success-measurement
   criteria: exact commands, named checks, files, fields, or observable end
   state that can prove success.
3. Confirm the governing artifacts are clear enough to authorize the change.
4. If the work lacks that contract, route it to planning, refinement, or
   triage before implementation.

## Execution Rules

- Load the implementation contract and relevant governing artifacts before editing.
- Make the smallest change that satisfies the work item.
- Preserve authority order: upstream artifacts govern implementation choices.
- File follow-up work for newly discovered scope instead of silently expanding
  the current pass.
- Stop when the bounded work is complete or blocked.

## Running with DDx

`helix build` is currently a compatibility wrapper over the DDx managed
execution surface.

Use this surface for one explicit bead or selector:

```bash
helix build [issue-id|scope]
ddx agent execute-bead <bead-id> [--from <rev>] [--no-merge]
```

DDx-specific contract:

- resolve one execution-ready bead from the current queue or selector
- delegate the bounded attempt to `ddx agent execute-bead`
- keep HELIX authority-order and bead-shaping rules in force
- avoid substituting a direct `ddx agent run` prompt or a private claim/execute/close loop for managed execution work

Read before executing:

- `.ddx/plugins/helix/workflows/actions/implementation.md`
- `.ddx/plugins/helix/workflows/EXECUTION.md`
- the bead's governing artifacts via `spec-id`, parent, and context digest

Operator guidance:

- Use `helix build` when the operator wants one explicit bounded attempt.
- Use `ddx agent execute-loop` for queue drain.
- Use `helix run` only when the compatibility wrapper's supervisory routing is needed on top of DDx-managed execution.
