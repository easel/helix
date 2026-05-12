---
title: "Competitive Analysis"
slug: competitive-analysis
phase: "Discover"
weight: 0
generated: true
aliases:
  - /reference/glossary/artifacts/competitive-analysis
---

## What it is

Market landscape mapping and differentiation strategy.
Identifies competitive positioning and sustainable advantages.

## Activity

**[Discover](/reference/glossary/activities/)** — Validate that an opportunity is worth pursuing before committing to a development cycle.

## Output location

`docs/helix/00-discover/competitive-analysis.md`

## Relationships

### Requires (upstream)

- [Product Vision](../product-vision/)

### Enables (downstream)

- [Business Case (market context)](../business-case/)
- [Opportunity Canvas](../opportunity-canvas/)

### Informs

- [Business Case](../business-case/)
- [Opportunity Canvas](../opportunity-canvas/)
- [Prd](../prd/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Competitive Analysis Prompt

Create a competitive analysis that maps the market landscape and establishes differentiation strategy.

## Storage Location

Store at: `docs/helix/00-discover/competitive-analysis.md`

## Purpose

Answers: **How do we win in this market?** Keep the comparison factual, compact, and focused on positioning.

## Key Principles

- **Cover direct and indirect competitors** - compare strengths, weaknesses, and target customers.
- **Find the angle** - identify gaps and defensible differentiation.
- **Stay objective** - base claims on facts, not wishes.

## Quality Checklist

- [ ] At least 3 competitors analyzed
- [ ] Direct and indirect competitors included
- [ ] Feature matrix is factual
- [ ] Differentiation is specific and defensible
- [ ] Sources cited for competitor data
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Competitive Analysis

## Market Landscape

| Attribute | Assessment |
|-----------|------------|
| Market Maturity | Emerging / Growing / Mature / Declining |
| Growth Rate | [X]% annually |
| Key Trends | [Trend 1], [Trend 2] |
| Entry Barriers | Low / Medium / High |

## Competitor Profiles

| Competitor | Positioning | Target Segment | Strengths | Weaknesses |
|------------|-------------|----------------|-----------|------------|
| [Competitor 1] | [Position] | [Segment] | [Strengths] | [Weaknesses] |
| [Competitor 2] | [Position] | [Segment] | [Strengths] | [Weaknesses] |

**Indirect Competitors**: [List alternative solutions and threat level]

## Feature Comparison

| Feature | Us | Comp 1 | Comp 2 |
|---------|----|--------|--------|
| [Feature 1] | [Status] | [Status] | [Status] |
| [Feature 2] | [Status] | [Status] | [Status] |

**Legend**: Full | Partial | Planned | None

## Differentiation Strategy

| Differentiator | Why It Matters | Defensibility |
|----------------|----------------|---------------|
| [Differentiator 1] | [Customer value] | H/M/L |
| [Differentiator 2] | [Customer value] | H/M/L |

**Positioning**: For [target customer] who [need], our [product] is a [category] that [key benefit]. Unlike [competitors], we [primary differentiator].

## Strategic Implications

- **Attack**: [Where to compete aggressively]
- **Defend**: [Where to protect position]
- **Avoid**: [Where not to compete]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
