---
title: "Opportunity Canvas"
slug: opportunity-canvas
phase: "Discover"
weight: 0
generated: true
aliases:
  - /reference/glossary/artifacts/opportunity-canvas
---

## What it is

Synthesis document validating problem-solution fit.
Final artifact before go/no-go decision on proceeding to Frame.

## Activity

**[Discover](/reference/glossary/activities/)** — Validate that an opportunity is worth pursuing before committing to a development cycle.

## Output location

`docs/helix/00-discover/opportunity-canvas.md`

## Relationships

### Requires (upstream)

- [Product Vision](../product-vision/)
- [Business Case](../business-case/)
- [Competitive Analysis](../competitive-analysis/)

### Enables (downstream)

_None._

### Informs

- [Prd](../prd/)
- [User Stories](../user-stories/)
- [Feature Specification](../feature-specification/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Opportunity Canvas Prompt

Create an opportunity canvas that validates problem-solution fit before proceeding to Frame.

## Storage Location

Store at: `docs/helix/00-discover/opportunity-canvas.md`

## Purpose

Answers: **Is this the right problem to solve?** Keep the canvas to one page and centered on the decision.

## Key Principles

- **Start with the problem** - validate customer pain before proposing a solution.
- **Be specific about customers** - name exact segments and alternatives.
- **Define clear success** - use measurable metrics with realistic timelines.

## Quality Checklist

- [ ] Problem is validated
- [ ] Customer segments are specific
- [ ] Unique value is differentiated
- [ ] Solution addresses the stated problem
- [ ] Metrics are measurable
- [ ] Unfair advantage is honest
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Opportunity Canvas

## Problem Statement

| Aspect | Description |
|--------|-------------|
| Problem | [What problem are you solving?] |
| Who | [Who has this problem?] |
| Impact | [What is the cost/pain of this problem?] |
| Evidence | [How do you know this is real?] |

**Problem Hypothesis**: [One sentence describing the core problem]

## Customer Segments

| Segment | Priority | Size | Characteristics | Current Solution |
|---------|----------|------|-----------------|------------------|
| [Primary] | P0 | [Size] | [Key traits] | [What they use now] |
| [Secondary] | P1 | [Size] | [Key traits] | [What they use now] |

**Early Adopters**: [Who will use this first and why?]

## Unique Value

| Value Proposition | Customer Benefit | Proof Point |
|-------------------|------------------|-------------|
| [Value 1] | [Why it matters] | [Evidence] |
| [Value 2] | [Why it matters] | [Evidence] |

**Elevator Pitch**: [2 sentences max describing the unique value]

## Solution Concept

| Capability | Problem Addressed | Priority |
|------------|-------------------|----------|
| [Capability 1] | [Which problem aspect] | P0/P1/P2 |
| [Capability 2] | [Which problem aspect] | P0/P1/P2 |

**NOT in Scope**: [What this solution will NOT do]

## Key Metrics

| Metric | Type | Target | Timeline |
|--------|------|--------|----------|
| [Success metric 1] | Outcome | [Target] | [When] |
| [Leading indicator 1] | Leading | [Target] | [When] |

**North Star Metric**: [Single most important metric]

## Unfair Advantage

| Advantage Type | Our Position | Sustainability |
|----------------|--------------|----------------|
| [Type 1] | [Description] | H/M/L |

**Honest Assessment**: [What we have vs. what we need to build]

## Go/No-Go Decision

**Decision**: Go | Pivot | No-Go

**Rationale**: [2-3 sentences explaining decision]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
