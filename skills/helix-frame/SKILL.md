---
name: helix-frame
description: Create or refine HELIX product vision, requirements, feature specs, and user stories.
argument-hint: '[scope]'
---

# Frame: Define What to Build

Frame creates the highest-authority artifacts in the HELIX stack: the documents
that govern everything downstream. Use it when you need to define or refine
what the product should do before designing how.

## When to Use

- starting a new project from scratch
- adding a major new capability or feature area
- requirements are unclear or contradictory
- upstream authority is missing for requested work
- you want to write a product vision, requirements document, feature spec, or user story

## What It Produces

Frame-phase artifacts:

- **Product Vision** — mission, market, value propositions, principles, success metrics
- **PRD** — problem, goals, requirements, constraints, risks, success criteria
- **Feature Specs** — per-feature requirements, user stories, acceptance criteria
- **User Stories** — captured within feature specs or standalone artifacts

## Methodology

1. Read existing Frame-phase artifacts if they exist.
2. Read the relevant artifact templates and prompt guidance.
3. Create or update the appropriate documents using the templates.
4. Iteratively refine through multiple rounds: challenge assumptions, fill
   gaps, and sharpen requirements.
5. Validate all blocking quality checks declared by the artifact system before
   committing.
6. Create follow-up design work implied by the framing.

## Examples

```bash
helix frame                    # Frame the whole project
helix frame auth               # Frame the auth capability
helix frame "mobile payments"  # Frame a new feature area
```

## Running with DDx

When DDx supplies the HELIX runtime, use these packaged resources:

- Vision template: `.ddx/plugins/helix/workflows/phases/00-discover/artifacts/product-vision/`
- PRD template: `.ddx/plugins/helix/workflows/phases/01-frame/artifacts/prd/`
- Feature spec template: `.ddx/plugins/helix/workflows/phases/01-frame/artifacts/feature-specification/`
- Authority order: `.ddx/plugins/helix/workflows/actions/implementation.md`

If execution work is implied, create tracker issues after the framing artifacts
are coherent enough to govern design.
