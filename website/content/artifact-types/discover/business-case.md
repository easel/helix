---
title: "Business Case"
linkTitle: "Business Case"
slug: business-case
phase: "Discover"
artifactRole: "supporting"
weight: 11
generated: true
---

## Purpose

Answers: **Should we invest in this opportunity?** Keep the case short, quantified, and decision-oriented.

## Authoring guidance

- **Quantify the decision** - use numbers and ranges, not adjectives.
- **Be explicit about risk** - show impact and mitigations.
- **Show strategic fit** - connect to company goals and timing.

<details>
<summary>Quality checklist from the prompt</summary>

- [ ] Market sizing uses verifiable data sources
- [ ] Investment estimate is realistic
- [ ] ROI assumptions are documented
- [ ] Major risks identified with mitigations
- [ ] Strategic fit is explicit

</details>

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Discover</strong></a> — Validate that an opportunity is worth pursuing before committing to a development cycle.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/00-discover/business-case.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/discover/opportunity-canvas/">Opportunity Canvas</a><br><a href="/artifact-types/frame/prd/">PRD</a><br>Resource Planning</td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Business Case Prompt

Create a business case that justifies investment with market sizing, ROI, and risk assessment.

## Storage Location

Store at: `docs/helix/00-discover/business-case.md`

## Purpose

Answers: **Should we invest in this opportunity?** Keep the case short, quantified, and decision-oriented.

## Key Principles

- **Quantify the decision** - use numbers and ranges, not adjectives.
- **Be explicit about risk** - show impact and mitigations.
- **Show strategic fit** - connect to company goals and timing.

## Quality Checklist

- [ ] Market sizing uses verifiable data sources
- [ ] Investment estimate is realistic
- [ ] ROI assumptions are documented
- [ ] Major risks identified with mitigations
- [ ] Strategic fit is explicit</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Business Case

## Executive Summary

[2-3 sentences: Opportunity, investment ask, expected return]

## Opportunity Sizing

| Market Tier | Size | Calculation | Source |
|-------------|------|-------------|--------|
| TAM (Total) | $[X]M | [Methodology] | [Source] |
| SAM (Serviceable) | $[X]M | [Methodology] | [Source] |
| SOM (Obtainable) | $[X]M | [Methodology] | [Source] |

**Key Assumptions**: [List assumptions underlying these numbers]

## Investment Required

| Category | Year 1 | Year 2 | Year 3 |
|----------|--------|--------|--------|
| Development | $[X] | $[X] | $[X] |
| Infrastructure | $[X] | $[X] | $[X] |
| Go-to-Market | $[X] | $[X] | $[X] |
| Operations | $[X] | $[X] | $[X] |

## Expected ROI

| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Revenue/Value | $[X] | $[X] | $[X] |
| Costs | $[X] | $[X] | $[X] |
| Net | $[X] | $[X] | $[X] |

**Breakeven**: [Month/Year] | **3-Year ROI**: [X]%

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | H/M/L | H/M/L | [Strategy] |
| [Risk 2] | H/M/L | H/M/L | [Strategy] |

## Strategic Alignment

| Strategic Goal | How This Contributes |
|----------------|---------------------|
| [Company goal 1] | [Contribution] |
| [Company goal 2] | [Contribution] |

**Opportunity Cost**: [What we give up by doing this]

## Recommendation

**Decision**: Go | Conditional Go | No-Go

**Rationale**: [2-3 sentences supporting recommendation]

**Conditions** (if Conditional Go):
- [Condition 1]
- [Condition 2]</code></pre></details></td></tr>
</tbody>
</table>
