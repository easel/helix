---
name: helix-backfill
description: Reconstruct missing HELIX documentation from available evidence without inventing authority.
argument-hint: "[scope]"
disable-model-invocation: true
---

# Backfill

Backfill reconstructs missing or incomplete HELIX artifacts from evidence that
already exists. It is a documentation recovery action, not permission to invent
requirements or designs.

## Methodology

1. Use the provided scope when present.
2. Read the available evidence: existing artifacts, implementation, tests,
   release notes, and recorded decisions.
3. Separate confirmed facts from inference.
4. Reconstruct only what the evidence supports.
5. Mark uncertainty explicitly and create follow-up work for unresolved gaps.
6. Emit the required backfill status and report markers.

## Constraints

- Do not fabricate missing planning artifacts.
- Do not promote implementation accidents into requirements without evidence.
- Separate confirmed evidence from inference.
- Create follow-up work when gaps need human guidance.

## Output

- updated or created documentation artifacts within the requested scope
- explicit uncertainty notes where evidence is incomplete
- `BACKFILL_STATUS` and `BACKFILL_REPORT` markers
- follow-up work items for unresolved authority gaps

## Running with DDx

When DDx supplies the HELIX runtime, read and apply:

- `.ddx/plugins/helix/workflows/actions/backfill-helix-docs.md`

Use `$ARGUMENTS` as the scope when provided. Create follow-on tracker work when
gaps need human guidance.
