---
title: "Architecture Decision Record"
slug: adr
phase: "Design"
weight: 200
generated: true
aliases:
  - /reference/glossary/artifacts/adr
---

## What it is

An ADR documents a significant architectural decision: the context that drove
it, the alternatives considered, the chosen approach, and the consequences.
Each ADR covers exactly one decision. ADRs are immutable once accepted; new
decisions that revise them create a new ADR marked as superseding the old one.

## Phase

**[Phase 2 — Design](/reference/glossary/phases/)** — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.

## Output location

`docs/helix/02-design/adrs/ADR-{id}-{name}.md`

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

_None._

### Informs

- [Solution Design](../solution-design/)
- [Technical Design](../technical-design/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Architecture Decision Record (ADR) Generation Prompt
Write a compact ADR that captures one decision, the alternatives, and the consequences.

## Focus
- State the context and decision plainly.
- Keep alternatives and tradeoffs honest but brief.
- Note validation and references only if they affect the decision.

## Completion Criteria
- The decision is unambiguous.
- Alternatives are compared clearly.
- Consequences are explicit.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: ADR-XXX
  depends_on:
    - helix.prd
    - helix.architecture
---
# ADR-[NUMBER]: [Title]

| Date | Status | Deciders | Related | Confidence |
|------|--------|----------|---------|------------|
| [YYYY-MM-DD] | [Proposed/Accepted/Deprecated/Superseded] | [Names] | [FEAT-XXX] | [High/Med/Low] |

## Context

| Aspect | Description |
|--------|-------------|
| Problem | [Specific problem] |
| Current State | [Existing situation] |
| Requirements | [Key requirements driving this] |

## Decision

We will [decision statement].

**Key Points**: [Point 1] | [Point 2] | [Point 3]

## Alternatives

| Option | Pros | Cons | Evaluation |
|--------|------|------|------------|
| [Option 1] | [Advantages] | [Disadvantages] | [Rejected: reason] |
| [Option 2] | [Advantages] | [Disadvantages] | [Rejected: reason] |
| **[Selected]** | [Advantages] | [Disadvantages + mitigations] | **Selected: reason** |

## Consequences

| Type | Impact |
|------|--------|
| Positive | [Good outcomes] |
| Negative | [Trade-offs, technical debt] |
| Neutral | [Side effects] |

## Risks

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| [Risk 1] | H/M/L | H/M/L | [Strategy] |

## Validation

| Success Metric | Review Trigger |
|----------------|----------------|
| [Metric 1] | [Condition for reconsideration] |

## Concern Impact

If this decision affects the project's active concerns or overrides a
library practice, note the impact here:

- **Concern selection**: [Does this ADR select, change, or constrain a concern?]
- **Practice override**: [Does this ADR override a library concern practice? If so,
  update `docs/helix/01-frame/concerns.md` Project Overrides with this ADR ref.]
- **No concern impact**: [Delete this section if the ADR has no concern relevance.]

## References

- [PRD section link]
- [Related ADRs]

## Review Checklist

Use this checklist when reviewing an ADR:

- [ ] Context names a specific problem — not "we need to decide about X"
- [ ] Decision statement is actionable — "we will" not "we should consider"
- [ ] At least two alternatives were evaluated
- [ ] Each alternative has concrete pros and cons, not vague assessments
- [ ] Selected option's rationale explains why it wins over the best alternative
- [ ] Consequences include both positive and negative impacts
- [ ] Negative consequences have documented mitigations
- [ ] Risks are specific with probability and impact assessments
- [ ] Validation section defines how we'll know if the decision was right
- [ ] Review triggers define conditions for reconsidering the decision
- [ ] Concern impact section is complete (or explicitly marked as no impact)
- [ ] ADR is consistent with governing feature spec and PRD requirements
``````

</details>

## Example

This example is HELIX's actual architecture decision record, sourced from [`docs/helix/02-design/adr/ADR-001-supervisory-control-model.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/adr/ADR-001-supervisory-control-model.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## ADR-001: HELIX Supervisory Control Model

| Date | Status | Deciders | Related | Confidence |
|------|--------|----------|---------|------------|
| 2026-03-27 | Proposed | HELIX maintainers | `helix-run`, skills, workflow contract | High |

### Context

| Aspect | Description |
|--------|-------------|
| Problem | HELIX currently reads too much like a set of mirrored commands. That makes the system behave literally unless the user already knows the method and manually steers each phase transition. |
| Current State | `helix-run` is documented mostly as a bounded operator loop over ready implementation work. Companion skills and commands are described as direct wrappers around individual actions. The repo does not yet clearly define how requirement changes should trigger design work, how spec changes should trigger issue refinement, how concurrent interactive refinement should affect a live run, or when autopilot should stop and ask for input. |
| Requirements | HELIX must preserve bounded execution, authority order, tracker-first work management, and direct interactive operation. It must also reduce orchestration burden by autonomously selecting the least-powerful sufficient next action when authority is available. |

### Decision

We will treat HELIX as a supervisory control system whose primary autonomous
entrypoint is `helix-run`.

`helix-run` will own end-to-end forward progress for HELIX-managed work. It
will continuously select the highest-leverage next bounded action that can be
taken safely without human input. Companion commands and skills such as
`align`, `plan`, `polish`, `implement`, `review`, `check`, and `backfill` will
be treated as triggered subroutines inside that control loop while remaining
available as direct interactive entrypoints.

Supervision must remain live to concurrent local operator activity. A running
`helix-run` session must treat tracker and governing-artifact changes as new
control input at safe boundaries. It may not assume that the selected issue is
still valid at claim time or close time just because it was valid earlier in
the loop.

**Key Points**: `helix-run` is supervisory autopilot | companion actions are subroutines plus intervention points | least-power escalation governs next-step selection

### Alternatives

| Option | Pros | Cons | Evaluation |
|--------|------|------|------------|
| Keep `helix-run` as a narrow implementation loop and leave higher-order transitions to the user | Simpler local implementation and fewer implicit transitions | Forces the user to remember HELIX constantly, increases orchestration burden, and weakens the product promise | Rejected: does not satisfy the product goal |
| Make every skill and command a peer, with no supervisory controller | Easy to describe as a command set | Produces a fragmented UX and no principled default behavior for autonomous progress | Rejected: no coherent control model |
| **Make `helix-run` the supervisor and treat companion actions as triggered subroutines** | Preserves direct control while enabling autopilot, aligns with least-power progression, and gives a clear model for user escalation | Requires clearer trigger rules, stronger documentation, and broader tests | **Selected: best fit for the product vision and PRD** |

### Consequences

| Type | Impact |
|------|--------|
| Positive | HELIX gains one coherent operating model for both interactive and autonomous use. |
| Positive | Users no longer need to restate the HELIX method to get correct downstream behavior. |
| Positive | Skills can be documented in terms of activation triggers and handoffs, not just literal command equivalence. |
| Negative | The workflow contract, skill descriptions, and tests will need substantial updates to encode transition rules explicitly. |
| Negative | `helix-run` becomes a broader supervisory surface, so ambiguity boundaries must be defined carefully to avoid overreach. |
| Neutral | Direct commands remain available, but their role becomes more clearly subordinate to the supervisory control model. |

### Risks

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Supervisory behavior remains underspecified and agents continue acting literally | H | H | Encode trigger rules and escalation boundaries in workflow docs and skill descriptions |
| The system overreaches into product judgment instead of bounded workflow progression | M | H | Preserve least-power rules and explicit stop-for-guidance conditions |
| The runner executes stale work while an operator is refining specs or issues in another session | M | H | Define queue-drift, revalidation, and supersession behavior explicitly before implementation |
| Implementation drifts from the new model because legacy docs and tests still describe a narrower loop | H | M | Follow this ADR with contract updates, skill updates, and deterministic test coverage |

### Validation

| Success Metric | Review Trigger |
|----------------|----------------|
| `helix-run` is described and implemented as supervisory autopilot across product, design, workflow, and skill docs | Any doc or implementation still treating `run` as only a wrapper around implementation queue execution |
| Requirement changes route to reconciliation/planning before implementation when appropriate | A representative scenario requires the user to manually name `align` or `plan` for correct behavior |
| Spec changes with open issues route to `polish` before implementation resumes | Issue refinement continues to depend on the user explicitly remembering the command |
| Concurrent interactive refinement causes `helix-run` to re-check rather than claim or close stale work | The wrapper claims or closes an issue whose governing tracker/spec state materially changed during the run |
| Direct use of companion commands still works without breaking the supervisory model | Interactive commands create a separate mental model or inconsistent tracker behavior |

### References

- [Product Vision](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/00-discover/product-vision.md)
- [PRD](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/01-frame/prd.md)
- [HELIX Supervisory Control Solution Design](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/solution-designs/SD-001-helix-supervisory-control.md)
- [HELIX CLI Technical Design](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/technical-designs/TD-002-helix-cli.md)
