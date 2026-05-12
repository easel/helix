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

## Activity

**[Frame](/reference/glossary/activities/)** — Define what the system should do, for whom, and how success will be measured.

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
ddx:
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

This example is HELIX's actual product requirements document, sourced from [`docs/helix/01-frame/prd.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/01-frame/prd.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Product Requirements Document

### Summary

HELIX is a software development methodology and artifact catalog for
AI-assisted teams. It ships portable content (templates for ~32 artifact
types, authoring prompts, methodology documentation) plus a single skill
that keeps the governing artifacts aligned. The primary user experience is
invoking the alignment skill against a project's existing documents and
getting a plan for the changes needed to keep them coherent.

HELIX does not provide a CLI, a tracker, an execution loop, or any runtime
infrastructure. Those are substrate concerns. DDx is the reference substrate;
Databricks Genie and Claude Code are target substrates. HELIX is the
discipline; the substrate is the engine.

### Problem and Goals

#### Problem

AI-assisted software development is now the default practice, but the practice
itself is unpracticed. Teams using AI agents to write production code see three
failure modes:

1. **Artifact drift.** Specifications, designs, and tests fall out of sync with
   code because no one walks the artifacts between work sessions.
2. **Inconsistent agent behavior.** Without a shared methodology, agents make
   locally-good decisions that conflict with global intent — a feature gets
   built, but its design contradicts an earlier ADR; a refactor lands without
   updating the technical design that documented its predecessor.
3. **Lossy session boundaries.** Each new conversation re-improvises the same
   workflow. Specs that should be written are not; reviews that should happen
   do not. Context evaporates.

Human teams developed disciplines for these problems decades ago: PRDs, design
documents, test plans, alignment reviews. The agents that now write our code
have not been given that discipline in a portable, tool-agnostic form.

#### Goals

1. **Catalog.** Define a minimal, complete catalog of artifact types covering
   software development from intent through deployment to feedback. Each type
   carries a template, an authoring prompt, and quality criteria.
2. **Alignment skill.** Provide a single skill that any AI agent can run
   against a project's governing artifacts to identify drift, gaps, and
   contradictions, and produce a plan for closing them.
3. **Methodology spec.** Specify authority order, the seven-activity control
   loop, the artifact-type schema, and the alignment skill contract as a
   substrate-neutral document.
4. **Stay small.** HELIX is content + one skill. Not a tool, not a platform,
   not a CLI. Resist scope creep into substrate territory.

#### Success Metrics

| Metric | Target | Measurement Method | Timeline |
|---|---|---|---|
| Substrate breadth | 3 documented substrate deployments (DDx, Databricks Genie, one other) | Release audit | 12 months |
| Adoption | 50+ repos using HELIX templates as their artifact catalog | GitHub search; community survey | 18 months |
| Alignment quality | Healthy artifact sets average < 3 findings per skill run | Periodic sample across reference repos | Ongoing |
| Authoring quality | HELIX-template PRDs pass first-pass review at higher rates than free-form equivalents | Comparative review study | 12 months |
| Skill portability | Zero substrate-specific commands in skill body | Automated check on every release | Ongoing |

#### Non-Goals

- HELIX will not provide a CLI, tracker, queue, or execution engine.
- HELIX will not impose technology choices or fork by language ecosystem.
- HELIX will not replace product, design, or architectural judgment.
- HELIX will not be a fully autonomous coding agent.
- HELIX will not flatten the seven-activity loop into one generic prompt.

### Users and Scope

#### Primary Persona: HELIX Adopter

**Role**: Tech lead, staff engineer, or principal engineer guiding a team's
adoption of AI-assisted development.
**Goals**: Establish a methodology that produces durably reviewable software
output from agents. Reduce the cost of onboarding new team members or new
agent runtimes.
**Pain Points**: Inconsistent agent output across sessions; artifact drift;
the cost of writing a methodology from scratch for each project.

#### Secondary Persona: AI Agent

**Role**: Any AI runtime (Claude Code, Genie, Cursor, etc.) executing work
against a HELIX-governed artifact set.
**Goals**: Have a defined set of artifacts to read, a defined set to produce,
and a single skill to invoke for alignment.
**Pain Points**: Ambiguous context, drift between sessions, no standard for
"is this work complete."

#### Tertiary Persona: HELIX Maintainer

**Role**: Maintainer of the HELIX content catalog, the methodology spec, and
the alignment skill.
**Goals**: Keep the catalog tight; keep the methodology coherent; ship
substrate-portable improvements.
**Pain Points**: Resisting feature creep into substrate territory; pruning
legacy surfaces that crept across the boundary.

#### In Scope

- Artifact-type catalog (templates, prompts, quality criteria, examples)
- Methodology specification (authority order, seven-activity loop, principles)
- Single alignment skill (find drift; produce a plan)
- Substrate-portable packaging of all of the above (deployable adapters for
  DDx, Databricks Genie, Claude Code)
- HELIX's own self-application — its development artifacts in `docs/helix/`
  are themselves authored from HELIX templates

#### Out of Scope

- CLI, tracker, queue, execution loop, IDE integration
- Substrate-specific tooling beyond minimal packaging adapters
- Domain-specific extensions (HELIX is general-purpose)

### Requirements

#### Functional Requirements

##### P0

**R-1: Artifact-type catalog.** HELIX ships templates, prompts, and metadata
for every activity in the seven-activity loop. Each artifact type carries a
template (markdown skeleton), a prompt (authoring guidance), quality criteria,
and an example.

**R-2: Authority-ordered relationships.** Every artifact type declares its
position in the authority order. Higher-level artifacts govern lower-level
ones; conflicts resolve up.

**R-3: Alignment skill.** A single skill, deployable to any substrate that can
read and write markdown, takes an artifact root path plus an optional intent
and produces:
(a) a structured alignment report listing gaps, drift, and contradictions in
    the governing artifacts;
(b) a plan describing the artifact updates needed to close them, ordered by
    authority.

**R-4: Substrate-neutral content.** The catalog and skill body contain no
references to specific substrate commands, file layouts, or runtimes beyond
the minimal "read markdown, write markdown, search files" contract.

**R-5: Methodology specification.** A substrate-neutral specification document
defines the authority order, the seven-activity loop, the artifact-type
schema, and the alignment skill contract. New substrate consumers can
implement HELIX compliantly from this spec alone.

**R-6: Self-application.** HELIX's own development artifacts in `docs/helix/`
are authored from HELIX templates. The repo dogfoods its own catalog;
inconsistencies in the dogfood are themselves alignment findings.

##### P1

**R-7: Substrate adapters.** Packaging adapters wrap the HELIX content and
skill for known runtimes (DDx plugin, Databricks Genie skill, Claude Code
skill). Each adapter is a small repackaging, not a fork.

**R-8: Quality criteria as deterministic checks.** Where artifact quality
criteria are deterministic (regex patterns, section presence, word counts),
they are expressed in a form that substrates with prose-checker support
(notably DDx via `ddx doc prose`) can enforce.

**R-9: Per-artifact-type rule scoping.** Quality criteria attach to artifact
types; alignment skill applies type-scoped checks to instances based on ID
prefix or path. Requires upstream DDx feature (file separately on DDx queue).

##### P2

**R-10: Catalog versioning.** Artifact-type changes are reviewable; consumers
can pin to a known catalog version.

**R-11: Onboarding deliverable.** A guided first-project walkthrough usable
without the creator present. The new-teammate review is a release criterion.

#### Acceptance Test Sketches

**R-1 (catalog):** Given a fresh repo with no HELIX content, when HELIX
content is installed, then 7 activity directories exist under `workflows/
phases/`, each with at least one artifact-type directory; each artifact-type
directory contains `template.md`, `prompt.md`, `meta.yml`, and an example.

**R-3 (alignment skill):** Given a project with vision, PRD, feature specs,
but no design artifacts, when the alignment skill runs, then the output
report identifies the design gap and the plan describes which solution
designs to author, in what order, with traceability back to the affected
features.

**R-4 (substrate-neutral):** Given the alignment skill source, when grep is
run for substrate-specific commands (`ddx `, `helix `, `bead`, `.helix/`),
then zero hits in the skill's normative body. References are allowed only in
substrate-adapter packaging.

**R-6 (self-application):** Given the HELIX repo, when the alignment skill is
run against `docs/helix/`, then the resulting report has fewer findings than
on the same date one quarter prior — i.e. the dogfood improves over time.

#### Technical Context

HELIX content is authored in Markdown with YAML frontmatter using the `ddx:`
namespace (an open schema HELIX adopts; DDx happens to consume it). The
alignment skill is authored in Markdown with frontmatter compatible with
mainstream agent skill formats (Claude Code-compatible). Artifact templates
and prompts are plain Markdown.

Substrate adapters repackage the content for substrate-specific deployment:

- **DDx adapter**: `ddx install helix` makes the catalog and skill available
  under DDx's plugin mechanism.
- **Databricks Genie adapter**: bundles content + skill into Genie's skill
  packaging format.
- **Claude Code adapter**: ships content + skill as a Claude Code skill
  bundle.

HELIX does not impose a programming language, framework, or toolchain on the
projects that adopt it. The repo itself uses Markdown + YAML; substrate
adapters use whatever each substrate requires.

#### Constraints, Assumptions, Dependencies

**Constraints:**
- HELIX cannot assume any particular execution substrate is present at
  runtime. The skill must work given only "read file, write file, search
  files" as runtime primitives.
- The skill body cannot reference substrate-specific commands.
- The catalog cannot fork by language ecosystem.

**Assumptions:**
- AI agents capable of executing the alignment skill have file-read/write
  tools and reasonable context window for an governing artifacts (typically tens of
  files).
- Substrate adapters can package markdown content for their runtime; the
  packaging mechanics vary but the source content is uniform.

**Dependencies:**
- **DDx (reference substrate).** HELIX uses DDx for its own bead tracking
  and execution. This is HELIX-using-DDx, not HELIX-coupled-to-DDx — the
  relationship is the same one Databricks users would have with their own
  substrate.
- **Markdown/YAML toolchain.** No specialized parser beyond standard YAML
  frontmatter.

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Methodology adoption is slow because "just write the code" is the durable default | High | High | Keep HELIX minimal; the alignment skill must produce value on the first run; ship a strong getting-started narrative |
| Substrate fragmentation makes adapter maintenance unsustainable | Medium | High | Define minimal runtime contract early; small adapters, not forks; treat substrate breadth as a release-quality metric |
| Alignment skill produces noisy or wrong findings | Medium | High | Skill is HELIX's primary development focus; quality criteria in templates are explicit and testable; ratchets on finding precision |
| Old HELIX work leaks substrate coupling into new content | Medium | Medium | Decoupling beads in the queue; automated check on each release for substrate refs in skill body |
| Documentation staleness | Medium | Medium | The alignment skill itself catches stale documents; HELIX dogfoods its own catalog |
| Transferability — HELIX cannot be taught without its creator present | Medium | High | Onboarding doc is P1 deliverable; new-teammate review gates the next release |

### Open Questions

- What is the canonical name and location of the alignment skill? (Working
  name: `skills/helix-align/`. Could also be `helix-plan`. Single source of
  truth either way.)
- What is the minimal runtime contract for an alignment-capable substrate?
  (Probably: file read, file write, file search, optional shell exec. Needs
  written spec.)
- How does HELIX express type-scoped quality rules before DDx's prose-checker
  supports artifact-type scoping? Interim approach: prose guidance in
  `prompt.md`. Long-term: structured `rules:` block in `meta.yml` once DDx
  supports it.
- Which legacy FEATs are superseded by this PRD? Candidates:
  `FEAT-001-helix-supervisory-control`, `FEAT-002-helix-cli`,
  `FEAT-005-execution-backed-output`, parts of `FEAT-004-plugin-packaging`,
  parts of `FEAT-011-slider-autonomy`. Surviving FEATs: `FEAT-003-principles`,
  `FEAT-006-concerns-practices-context-digest`, `FEAT-008-artifact-template-quality`,
  `FEAT-009-team-onboarding`, `FEAT-010-testing-strategy-templates`.
- Does HELIX itself need any tooling beyond the alignment skill (e.g., a
  catalog validator, a release-time portability check)? If yes, where does
  that tooling live — in HELIX, or as a DDx contribution?

### Success Criteria

HELIX is successful when:

1. A new team can adopt the methodology by reading the vision, the PRD, and
   the methodology spec, and installing the content catalog via a substrate
   adapter — without further guidance from a HELIX maintainer.
2. The alignment skill runs against a real project's governing artifacts and
   produces a plan that a human can review and approve in under 10 minutes.
3. At least three substrates have working adapters; teams can pick the one
   that fits their environment.
4. HELIX's own `docs/helix/` is visibly authored from its own catalog — the
   dogfood is healthy by the alignment skill's own measure.
