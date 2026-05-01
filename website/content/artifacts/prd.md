---
title: "Product Requirements Document"
slug: prd
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/prd
---

## What it is

The PRD is the foundational business document that defines the problem,
solution vision, success metrics, and requirements. It serves as the
single source of truth for what we're building and why.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/prd.md`

## Relationships

### Requires (upstream)

- [Product Vision](../product-vision/) — informs scope and direction *(optional)*
- [Business Case](../business-case/) — justifies investment *(optional)*

### Enables (downstream)

- [Feature Specifications](../feature-specification/) — breaks down into features
- [User Stories](../user-stories/) — derives actionable stories
- [Principles](../principles/) — establishes design principles

### Informs

- [Feature Specification](../feature-specification/)
- [User Stories](../user-stories/)
- [Principles](../principles/)
- [Solution Design](../solution-design/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# PRD Generation Prompt

Create a PRD that frames the problem, scope, priorities, and success criteria
clearly enough that someone could build the product without further
conversation.

## Storage Location

Store at: `docs/helix/01-frame/prd.md`

## Purpose

The PRD is the **authority document for what to build and why**. It sits
between the product vision (which defines direction) and feature specs (which
define detailed requirements). Every design decision and implementation choice
should trace back to a PRD requirement.

## Key Principles

- **Problem first** — the problem section should make someone feel the pain
  before they see the solution.
- **Decision-oriented** — every section should help someone make a build/skip
  decision. If a section doesn't inform a decision, it's filler.
- **Testable requirements** — every P0 requirement should be verifiable. If
  you can't describe how to test it, it's too vague.
- **Honest non-goals** — non-goals should exclude things someone might
  reasonably expect to be in scope. "Not a replacement for X" only matters if
  someone might assume it is.

## Section-by-Section Guidance

### Summary
Write this last. This section must work as a **standalone 1-pager**: what
we're building, who uses it, the problem, the solution approach, and the top
2-3 success metrics. Someone who reads only this section should understand the
product well enough to decide whether to invest time in the full PRD. Test:
could a new team member read this alone and explain the product to someone
else?

### Problem
Describe the failure mode, not the absence of your solution. "Users don't have
a X" is weak. "Users spend N hours/week doing Y manually because Z doesn't
exist, leading to W failures" is strong. Quantify where possible.

### Goals
Each goal should describe a state change, not an activity. "Build a dashboard"
is an activity. "Operators can see system health without SSH" is a state
change.

### Success Metrics
Every metric needs three things: what you're measuring, a numeric target, and
how you'll measure it. "User satisfaction" is not a metric. "NPS > 40 from
monthly survey of active users" is. Drop the Timeline column — success metrics
should define what success looks like, not when it happens.

### Non-Goals
Each non-goal should prevent scope creep on something plausible. "Not a
general-purpose AI" is only useful if someone might think it is. Test: would
someone on the team argue for including this? If not, it's not a useful
non-goal.

### Personas
Name them. Give them a role, goals, and pain points specific enough to
validate with a real person. "Alex the Developer" with generic goals is a
template, not a persona.

### Requirements (P0/P1/P2)
P0 = the product is broken without this. P1 = the product is weak without
this. P2 = the product is better with this. If you have more than 7 P0s,
you're not prioritizing.

### Functional Requirements
These are the detailed behavioral specs. Each one should be testable — someone
reading it should know how to write an acceptance test. Organize by subsystem
or user flow, not by priority.

### Acceptance Test Sketches
For each P0 requirement, write a concrete scenario: what the user does, what
input they provide, and what observable result they see. These aren't full test
cases — they're the minimum an implementer (human or agent) needs to verify
the requirement is met. An AI agent should be able to read a sketch and write
a passing test without asking clarifying questions.

### Technical Context
Name the stack, key dependencies with versions, API schemas, and platform
targets. Be specific enough that an implementer knows what to install and what
interfaces to code against. "React" is not enough — "React 18 with TypeScript
5.x and Vite 6" is. If there's an API schema (OpenAPI, GraphQL SDL), point to
it. This section exists because AI agents need concrete dependency and
interface information to produce correct implementations.

**Important**: This section records stack decisions — it does not make them.
Stack selection rationale belongs in ADRs (Architecture Decision Records). If
you're documenting a choice that doesn't have an ADR yet, note it in Open
Questions. If an existing ADR contradicts what you'd write here, the ADR
governs until it's superseded.

### Constraints
Name real constraints, not aspirational ones. "Must work on mobile" is a
constraint only if you'd otherwise skip it. Budget, compliance, and platform
constraints matter most.

### Assumptions
These are bets. When an assumption is wrong, the plan breaks. Name each one
so the team knows what to watch.

### Risks
Each risk needs a concrete mitigation, not "monitor closely." If the
mitigation is monitoring, say what you'll monitor and what triggers action.

### Open Questions
List unresolved items explicitly rather than leaving `[TBD]` markers
scattered through the document. Each question should name who can answer it
and what's blocked by it. This section is honest about what you don't know
yet — it's better to have a clear list of unknowns than a document that
pretends to be complete.

### Success Criteria
These are the acceptance criteria for the entire initiative. They should be
observable outcomes ("operators can do X without Y") not activities ("we
shipped Z").

## Quality Checklist

After drafting, verify every item. If any blocking check fails, revise before
committing.

### Blocking

- [ ] Problem section quantifies the pain or names a specific failure mode
- [ ] Every P0 requirement is testable (someone could write an acceptance test)
- [ ] Every P0 has an acceptance test sketch with inputs and expected outputs
- [ ] Success metrics have numeric targets and named measurement methods
- [ ] No `[TBD]`, `[TODO]`, or `[NEEDS CLARIFICATION]` markers in any section except Open Questions
- [ ] Non-goals exclude something a reasonable person might assume is in scope
- [ ] Personas are specific enough to validate with a real user

### Warning

- [ ] Summary works as a standalone 1-pager (problem, solution, metrics)
- [ ] Goals describe state changes, not activities
- [ ] Risk mitigations are concrete actions, not "monitor"
- [ ] P0 requirements number 7 or fewer
- [ ] Assumptions are falsifiable
- [ ] Functional requirements are organized by subsystem or flow, not priority
- [ ] Technical Context names specific versions, not just library names
- [ ] Open Questions name who can answer and what's blocked
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: helix.prd
---
# Product Requirements Document

## Summary

[This section should work as a standalone 1-pager. Include: what we're
building, who uses it, what problem it solves, the solution approach, and the
top 2-3 success metrics. Write this last — it should be a distillation of the
full PRD, not an introduction. Someone who reads only this section should
understand the product well enough to decide whether to read the rest.]

## Problem and Goals

### Problem

[What is broken or missing? Who is affected? Be specific about the failure
mode — not "users struggle with X" but "users spend N hours per week doing X
because Y doesn't exist."]

### Goals

1. [Primary goal — what changes for users]
2. [Secondary goal]

### Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| [Metric] | [Numeric target] | [Named tool or process] |

### Non-Goals

[What we are explicitly not trying to achieve. Each non-goal should exclude
something a reasonable person might assume is in scope.]

Deferred items tracked in `docs/helix/parking-lot.md`.

## Users and Scope

### Primary Persona: [Name]

**Role**: [Job title/function]
**Goals**: [What they want to achieve]
**Pain Points**: [Current frustrations — specific enough to validate]

### Secondary Persona: [Name]

[Same structure]

## Requirements

### Must Have (P0)

1. [Core capability — what must be true for the product to be usable]

### Should Have (P1)

1. [Important feature — valuable but not blocking launch]

### Nice to Have (P2)

1. [Enhancement — improves experience but can be deferred]

## Functional Requirements

[Detailed behavioral requirements organized by subsystem or user flow. Each
requirement should be testable — someone reading it should know how to verify
whether it's satisfied.]

## Acceptance Test Sketches

[For each P0 requirement, describe a concrete scenario with inputs and
expected outputs. These aren't full test cases — they're the minimum needed
for an implementer (human or agent) to verify the requirement is met.]

| Requirement | Scenario | Input | Expected Output |
|-------------|----------|-------|-----------------|
| [P0 requirement] | [What the user does] | [Specific input or state] | [Observable result] |

## Technical Context

[Stack, key dependencies with versions, API schemas, and platform targets.
Be specific enough that an implementer knows what to install and what
interfaces to code against. This section records current stack decisions — it
does not make them. Stack selection rationale belongs in ADRs. If a choice
here isn't backed by an ADR yet, note it in Open Questions.]

- **Language/Runtime**: [e.g., TypeScript 5.x, Node 20+]
- **Key Libraries**: [e.g., React 18, Tailwind CSS 4]
- **Data/Storage**: [e.g., PostgreSQL 16, Redis 7]
- **APIs**: [e.g., OpenAPI spec at docs/api/v2.yaml]
- **Platform Targets**: [e.g., Linux, macOS; browser: Chrome/Firefox/Safari latest]

## Constraints, Assumptions, Dependencies

### Constraints

- **Technical**: [Platform or technology limits]
- **Business**: [Budget, timeline, resource limits]
- **Legal/Compliance**: [Regulatory requirements]

### Assumptions

- [Key assumptions — what must be true for this plan to work]

### Dependencies

- [External systems, teams, or artifacts this work depends on]

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Concrete strategy, not "monitor"] |

## Open Questions

[Unresolved items that need answers before or during implementation. Each
should name who can answer it and what's blocked by it. Prefer explicit
questions here over `[TBD]` markers scattered through the document.]

- [ ] [Question] — blocks [what], ask [who]

## Success Criteria

[What must be true to call the initiative successful. These should be
observable outcomes, not activities.]

## Review Checklist

Use this checklist when reviewing a PRD artifact:

- [ ] Summary works as a standalone 1-pager — someone can decide whether to read the rest
- [ ] Problem statement describes a specific failure mode with concrete cost
- [ ] Goals are outcomes, not activities ("users can X" not "we build Y")
- [ ] Success metrics have numeric targets and named measurement methods
- [ ] Non-goals exclude things a reasonable person might assume are in scope
- [ ] Personas have specific pain points, not generic descriptions
- [ ] P0 requirements are necessary for launch — removing any one makes the product unusable
- [ ] P1/P2 requirements are correctly prioritized relative to each other
- [ ] Every P0 requirement has an acceptance test sketch
- [ ] Functional requirements are testable — each can be verified with specific inputs and expected outputs
- [ ] Technical context names specific versions and interfaces, not vague technology areas
- [ ] Risks have concrete mitigations ("we do X"), not vague strategies ("we monitor")
- [ ] Open questions name who can answer and what is blocked
- [ ] No contradictions between requirements sections
- [ ] PRD is consistent with the governing product vision
``````

</details>

## Example

<details>
<summary>Show a worked example of this artifact</summary>

``````markdown
# Product Requirements Document - DDx CLI Toolkit

**Version**: 1.0.0
**Date**: January 14, 2024
**Status**: Approved
**Author**: Product Team

## Executive Summary

DDx (Document-Driven Development eXperience) is a CLI toolkit designed to help development teams share templates, prompts, and patterns across projects using AI assistance. Following a medical differential diagnosis metaphor, DDx enables teams to "diagnose" project issues, "prescribe" solutions through templates and patterns, and share improvements back to the community.

The toolkit addresses the growing need for standardized, AI-assisted development workflows while maintaining flexibility for project-specific customizations. By leveraging git subtree for version control and providing a curated library of templates and prompts, DDx accelerates development while ensuring consistency and quality.

## Problem Statement

### The Problem
Development teams struggle with:
- **Inconsistent project setup**: Each project reinvents configuration and structure
- **Knowledge silos**: Best practices and patterns aren't shared effectively
- **AI integration complexity**: Difficulty leveraging AI tools consistently
- **Template maintenance**: No systematic way to update and share improvements

### Current State
Teams currently:
- Copy-paste configurations between projects (error-prone)
- Maintain private template repositories (fragmented)
- Write ad-hoc AI prompts (inconsistent results)
- Struggle with contribution workflows (changes don't flow back)

### Opportunity
- **Market timing**: AI-assisted development is becoming mainstream
- **Technology enabler**: Git subtree provides robust versioning
- **Community need**: Developers seek standardized AI workflows

## Goals and Objectives

### Business Goals
1. Accelerate project initialization by 80%
2. Reduce configuration errors by 90%
3. Build a community of 1,000+ active users

### Success Metrics
| Metric | Target | Measurement Method | Timeline |
|--------|--------|-------------------|----------|
| Time to project setup | <5 minutes | CLI telemetry | Q2 2024 |
| Template reuse rate | >70% | Usage analytics | Q3 2024 |
| Community contributions | 50+ PRs/month | GitHub metrics | Q4 2024 |
| User satisfaction | NPS >50 | Quarterly survey | Q4 2024 |

### Non-Goals
- Not a full IDE or development environment
- Not a project generator (uses existing templates)
- Not a package manager replacement

## Users and Personas

### Primary Persona: Alex the Senior Developer
**Role**: Senior Full-Stack Developer
**Background**: 7+ years experience, leads small team
**Goals**:
- Standardize team practices
- Reduce setup time for new projects
- Share knowledge effectively

**Pain Points**:
- Repeating setup for each project
- Training juniors on best practices
- Keeping configurations updated

**Needs**:
- Quick project initialization
- Customizable templates
- Easy contribution workflow

## Requirements Overview

### Must Have (P0)
1. **Template Management**: Apply templates with variable substitution
2. **Pattern Library**: Reusable code patterns for common scenarios
3. **AI Prompt Integration**: Claude-specific prompts for development tasks
4. **Version Control**: Git subtree for reliable updates
5. **Configuration Management**: .ddx.yml for project settings

### Should Have (P1)
1. **Project Diagnostics**: Analyze project health
2. **Community Contribution**: Share improvements upstream
3. **Multi-language Support**: Templates for various languages

### Nice to Have (P2)
1. **Web Dashboard**: Visual template browser
2. **Metrics Tracking**: Anonymous usage analytics
3. **Plugin System**: Extensible architecture

## Timeline and Milestones

### Phase 1: Core CLI (Q1 2024)
- Basic commands (init, apply, list)
- Template system
- Git subtree integration

### Phase 2: Community Features (Q2 2024)
- Contribution workflow
- Template marketplace
- Documentation

### Phase 3: Advanced Features (Q3 2024)
- Diagnostics system
- AI prompt optimization
- Analytics dashboard

---
*This PRD demonstrates the expected format and detail level for Frame phase documentation.*
``````

</details>
