---
title: "Feasibility Study"
slug: feasibility-study
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/feasibility-study
---

## What it is

A systematic analysis of project viability across technical, business,
operational, and resource dimensions. Used to validate that a proposed
solution is achievable before committing significant resources.

## Activity

**[Frame](/reference/glossary/activities/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/feasibility-study.md`

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

- [Risk-adjusted project plan](../prd/)

### Informs

- [Prd](../prd/)
- [Principles](../principles/)
- [Risk Register](../risk-register/)
- [Stakeholder Map](../stakeholder-map/)
- [Feature Registry](../feature-registry/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Feasibility Study Generation Prompt
Assess whether the project is feasible and what it would take to proceed.

## Focus
- Separate technical, business, operational, and resource feasibility.
- State the recommendation clearly.
- Capture the main risks, constraints, and open questions.

## Completion Criteria
- The recommendation is unambiguous.
- Each feasibility dimension is summarized briefly.
- Assumptions and mitigations are explicit.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Feasibility Study: {{project_name}}

**Decision Deadline**: {{decision_deadline}}
**Status**: Draft

## Executive Summary

### Project Overview
[Brief description of the proposed project or solution]

### Recommendation
**Overall Assessment**: FEASIBLE | CONDITIONALLY FEASIBLE | NOT FEASIBLE
**Decision**: GO | CONDITIONAL GO | NO GO
**Rationale**: [2-3 sentences on the main factors]

## Feasibility Assessment

### Technical
- **Assessment**: FEASIBLE | HIGH RISK | NOT FEASIBLE
- **Key requirements**: [Brief list]
- **Main risks**: [Brief list]

### Business
- **Assessment**: FEASIBLE | HIGH RISK | NOT FEASIBLE
- **Market opportunity**: [Brief summary]
- **Value proposition**: [Brief summary]

### Operational
- **Assessment**: FEASIBLE | HIGH RISK | NOT FEASIBLE
- **Support and deployment needs**: [Brief summary]
- **Regulatory requirements**: [Brief summary]

### Resource
- **Assessment**: FEASIBLE | HIGH RISK | NOT FEASIBLE
- **Budget**: [Estimate]
- **Team and timeline**: [Estimate]

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Strategy] |

## Alternatives

### [Alternative Approach]
- **Pros**: [Brief]
- **Cons**: [Brief]
- **Feasibility**: [Brief]

## Next Steps
1. [Action]
2. [Action]
``````

</details>

## Example

<details>
<summary>Show a worked example of this artifact</summary>

``````markdown
# Feasibility Study: Delegate Bounded Queue-Drain to DDx

**Feasibility Lead**: HELIX maintainers
**Evaluation Timeframe**: 2 weeks
**Decision Deadline**: 2026-03-27
**Status**: Example

> Example scenario reconstructed from HELIX's CONTRACT-001 boundary deliberations. This is illustrative — the authoritative record of the decision lives in `docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md` and `docs/helix/02-design/adr/ADR-001-supervisory-control-model.md`.

## Executive Summary

### Project Overview
HELIX maintains a supervisory autopilot (`helix run`) that selects the next bounded action and progresses HELIX-managed work toward done. Until early 2026, HELIX owned its own queue-drain loop: claim a ready bead, dispatch an agent, run pre/post checks, land or revert, repeat. DDx now ships `ddx agent execute-loop`, a single-project queue-drain primitive that performs the same claim-execute-close cycle with isolated worktrees, evidence capture, and runtime metrics.

This study evaluates whether HELIX should retire its in-tree execution mechanics and delegate per-cycle execution to `ddx agent execute-loop --once`, retaining only supervisory wrapping above DDx's bounded primitive.

### Recommendation
**Overall Assessment**: FEASIBLE
**Decision**: GO
**Rationale**: DDx's `--once` semantics already return control to HELIX after each bead, preserving the supervisory contract from ADR-001. Delegation removes a parallel execution substrate and lets HELIX focus on workflow semantics: routing, escalation, artifact-flow policy. The remaining risk — drift between HELIX's expectations and DDx's behavior — is mitigated by codifying the boundary in CONTRACT-001 and by making `execute-loop --once --json` the workflow-visible outcome surface.

## Feasibility Assessment

### Technical
- **Assessment**: FEASIBLE
- **Key requirements**:
  - DDx exposes a bounded "drain at most one bead, then return" mode (`--once`).
  - DDx returns enough evidence per attempt for HELIX to make merge/preserve/escalate decisions: bead ID, status, base/result revisions, session ID, retry hints.
  - DDx owns dirty-tree checkpointing, isolated worktree execution, fast-forward landing, and worktree cleanup so HELIX never touches `git checkout -- .`.
- **Main risks**:
  - HELIX wrappers may continue to set selectors (`HELIX_SELECTED_ISSUE`) DDx never honors, producing the illusion of control.
  - Status semantics (`success` vs `land_conflict` vs `post_run_check_failed`) must stay stable; ad-hoc changes in DDx would break HELIX post-cycle bookkeeping.
  - Review and alignment behavior must be re-expressed as queue-injected beads, not as HELIX-only post-cycle hooks.

### Business
- **Assessment**: FEASIBLE
- **Market opportunity**: HELIX's positioning is a supervisory layer for spec-driven agent development. Owning a parallel execution substrate dilutes that positioning and slows adoption — every HELIX user pays for HELIX's git mechanics in addition to whatever their platform substrate provides.
- **Value proposition**: Delegation reinforces "HELIX owns workflow semantics; DDx owns execution mechanics." Operators get one execution lane to trust and reason about, and HELIX docs can point at DDx evidence rather than re-document equivalent internals.

### Operational
- **Assessment**: FEASIBLE
- **Support and deployment needs**: HELIX already requires DDx for tracker, graph, and agent execution. Adding `execute-loop` as a required dependency does not broaden the footprint. The `scripts/helix` orchestrator stays Bash+jq because the workflow logic is mostly pipelines over `ddx` JSON output.
- **Regulatory requirements**: None — both DDx and HELIX are local developer tools.

### Resource
- **Assessment**: FEASIBLE
- **Budget**: Maintainer time only. No new infrastructure.
- **Team and timeline**: Maintainers can codify the boundary contract and rewrite `helix run` against `--once` within one planning cycle. The deletion side of the change (HELIX retry/backoff, blocker tracking, orphan worktree recovery, manual unclaim, `git checkout -- .` cleanup) is larger than the addition side.

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| DDx drift in `execute-loop --once --json` outcome shape breaks HELIX post-cycle bookkeeping | Medium | High | Pin the JSON shape in CONTRACT-001; add a HELIX integration test that fails fast on schema drift |
| HELIX continues to "predict" which bead DDx will pick, leading to corrupt bookkeeping when the prediction is wrong | Medium | High | Forbid pre-selection; HELIX uses `results[].bead_id` from the cycle output for all post-cycle work |
| Review and alignment behavior gets re-implemented as HELIX-side hooks instead of queue-injected beads | High | Medium | Validation checklist in CONTRACT-001; reject any wrapper that mutates DDx claim/close behavior |
| Operators expect the old "HELIX schedules retries" behavior and are confused by `retry-after` cooldowns | Medium | Low | Document ownership transfer; surface DDx cooldown via `ddx bead blocked` instead of a HELIX retry log |
| DDx changes execution semantics (e.g., switches to multi-bead drain by default) without re-honoring `--once` | Low | High | Treat `--once` as a contract-level commitment; pin in CONTRACT-001 and call it out in DDx upgrade notes |

## Alternatives

### Alternative 1: Keep HELIX-owned queue-drain and treat DDx as a per-bead executor
- **Pros**: HELIX retains direct control over claim/close lifecycle; no boundary contract needed.
- **Cons**: Two execution substrates compete for ownership of git mechanics, retry policy, and evidence capture. Every DDx improvement must be mirrored in HELIX. Maintenance cost grows with every supported harness.
- **Feasibility**: Feasible but strategically wrong; preserves the failure mode this study is trying to retire.

### Alternative 2: Have DDx absorb HELIX supervisory behavior (autonomy semantics, escalation, artifact flow)
- **Pros**: One tool to operate.
- **Cons**: DDx becomes methodology-bound. HELIX's explicit non-goal — being a generic do-everything platform — is violated. The product vision's separation of "platform substrate" from "workflow methodology" collapses.
- **Feasibility**: Feasible technically, rejected on positioning grounds.

### Alternative 3: Delegate execute-loop but keep a HELIX-side claim shim "just in case"
- **Pros**: Gradual migration.
- **Cons**: Two claim paths means two code paths to keep correct. Concurrent local refinement (per ADR-002) becomes harder, not easier, because there are now two writers to the tracker.
- **Feasibility**: Possible but worse than committing to delegation.

### Recommendation Rationale
Delegation is the smallest sufficient change that keeps the supervisory promise of `helix run` while removing parallel execution mechanics. The technical primitive HELIX needs (`--once`) already exists in DDx. The only meaningful work is codifying the boundary so future drift is visible.

## Next Steps
1. Ratify CONTRACT-001 with the DDx-owned and HELIX-owned responsibility lists explicit, including shared-object meanings (bead, workspace state, execution run, ratchet).
2. Rewrite `helix run` against `ddx agent execute-loop --once --json`. Delete HELIX retry/backoff, blocker tracking, orphan worktree recovery, `safe_unclaim`, and `git checkout -- .` cleanup.
3. Move review and alignment from HELIX-side post-cycle hooks to queue-injected beads (`review-finding`, `alignment-review`).
4. Add a `helix check`-time queue-drift detector so superseded beads never enter DDx's ready queue (per CONTRACT-001 queue-drift ownership).
5. Land an integration test that fails when `execute-loop --once --json` schema drifts.
``````

</details>
