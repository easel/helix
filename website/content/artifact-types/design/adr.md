---
title: "Architecture Decision Record"
linkTitle: "ADR"
slug: adr
phase: "Design"
artifactRole: "core"
weight: 11
generated: true
---

## Purpose

An ADR documents a significant architectural decision: the context that drove
it, the alternatives considered, the chosen approach, and the consequences.
Each ADR covers exactly one decision. ADRs are immutable once accepted; new
decisions that revise them create a new ADR marked as superseding the old one.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Design</strong></a> — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/02-design/adrs/ADR-{id}-{name}.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/solution-design/">Solution Design</a><br><a href="/artifact-types/design/technical-design/">Technical Design</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/adr/ADR-001-supervisory-control-model.md"><code>docs/helix/02-design/adr/ADR-001-supervisory-control-model.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Architecture Decision Record (ADR) Generation Prompt
Write a compact ADR that captures one decision, the alternatives, and the consequences.

## Focus
- State the context and decision plainly.
- Keep alternatives and tradeoffs honest but brief.
- Note validation and references only if they affect the decision.

## Completion Criteria
- The decision is unambiguous.
- Alternatives are compared clearly.
- Consequences are explicit.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
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

If this decision affects the project&#x27;s active concerns or overrides a
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

- [ ] Context names a specific problem — not &quot;we need to decide about X&quot;
- [ ] Decision statement is actionable — &quot;we will&quot; not &quot;we should consider&quot;
- [ ] At least two alternatives were evaluated
- [ ] Each alternative has concrete pros and cons, not vague assessments
- [ ] Selected option&#x27;s rationale explains why it wins over the best alternative
- [ ] Consequences include both positive and negative impacts
- [ ] Negative consequences have documented mitigations
- [ ] Risks are specific with probability and impact assessments
- [ ] Validation section defines how we&#x27;ll know if the decision was right
- [ ] Review triggers define conditions for reconsidering the decision
- [ ] Concern impact section is complete (or explicitly marked as no impact)
- [ ] ADR is consistent with governing feature spec and PRD requirements</code></pre></details></td></tr>
</tbody>
</table>
