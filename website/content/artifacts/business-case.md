---
title: "Business Case"
slug: business-case
phase: "Discover"
weight: 0
generated: true
aliases:
  - /reference/glossary/artifacts/business-case
---

## What it is

Investment justification with market sizing, ROI projections,
and risk assessment. Informs go/no-go decision.

## Phase

**[Phase 0 — Discover](/reference/glossary/phases/)** — Validate that an opportunity is worth pursuing before committing to a development cycle.

## Output location

`docs/helix/00-discover/business-case.md`

## Relationships

### Requires (upstream)

- [Product Vision](../product-vision/)

### Enables (downstream)

- [Opportunity Canvas](../opportunity-canvas/)

### Informs

- [Opportunity Canvas](../opportunity-canvas/)
- [Prd](../prd/)
- Resource Planning

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Business Case Prompt

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
- [ ] Strategic fit is explicit
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
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
- [Condition 2]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
