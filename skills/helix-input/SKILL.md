---
name: helix-input
description: Convert sparse user intent into governed HELIX work items.
argument-hint: '"<natural language request>" [--autonomy low|medium|high]'
disable-model-invocation: true
---

# Input

Accept sparse user intent, traverse the artifact stack to identify affected
work, and create or update governed work items so the rest of the HELIX process
can execute the intent.

If a specific request or autonomy level is given, use: $ARGUMENTS

## Use This Skill When

- the user provides a natural language request that should become work items
- intent is sparse or incomplete and needs to be mapped to governed artifacts
- the user specifies an autonomy level (`low`, `medium`, or `high`)
- the request should enter the durable planning and execution system rather than remain conversational

## Autonomy Levels

- `low`: ask the user before proceeding at each step; do not infer unconfirmed scope
- `medium` (default): create deterministic non-conflict artifacts; pause when ambiguity blocks progress
- `high`: create downstream artifacts without prompts unless blocked by physical or policy constraints; mark assumptions explicitly

## Methodology

1. **Parse the intent** — extract the core request, affected artifact layer, and
   explicit constraints or references.
2. **Traverse the artifact stack** — search for existing governing work,
   features, specs, and designs the request touches. Identify the blast radius.
3. **Create or update work items** — shape new work with phase, kind, area,
   governing artifact reference, deterministic acceptance, and compact context.
4. **Detect conflicts** — check for contradictions with higher-authority
   artifacts or duplicate open work. Report conflicts; with high autonomy,
   create explicit escalation work instead of blocking silently.
5. **Output a structured report** — include status, work created, work updated,
   autonomy level, conflicts, and next action.

## Authority Order

When artifacts disagree, prefer:

1. Product Vision
2. Product Requirements
3. Feature Specs / User Stories
4. Architecture / ADRs
5. Solution / Technical Designs
6. Test Plans / Tests
7. Implementation Plans
8. Source Code / Build Artifacts

## Running with DDx

Full action detail is in:

- `.ddx/plugins/helix/workflows/actions/input.md`

DDx-specific workflow:

- Search for existing governing beads, features, specs, and designs.
- Use `ddx bead create` for new work and `ddx bead update <id>` to refine existing items.
- Set appropriate labels such as `helix`, `phase:build`, `kind:implementation`, and `area:*`.
- Set `spec-id` to the governing artifact.
- For `high` autonomy, label speculative beads `kind:speculative`.
- After creating a bead, assemble its `<context-digest>` per `.ddx/plugins/helix/workflows/references/context-digest.md`; if the repo ships `scripts/refresh_context_digests.py`, use it instead of hand-editing digest XML.

DDx trailer format:

```text
INPUT_STATUS: COMPLETE | NEEDS_CLARIFICATION | BLOCKED
BEADS_CREATED: N
BEADS_UPDATED: N
AUTONOMY_LEVEL: low|medium|high
CONFLICTS: <description or "none">
NEXT_ACTION: helix run | helix check | <clarification question>
```
