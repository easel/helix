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

This example is HELIX's actual product requirements document, sourced from [`docs/helix/01-frame/prd.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/01-frame/prd.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Product Requirements Document

### Summary

HELIX is a development control system for AI-assisted software delivery. It
combines collaborative planning with a supervisory autopilot that keeps work
moving across requirements, specifications, designs, tests, implementation,
review, and metrics until human judgment is actually needed.

The primary product experience is not a bag of commands. It is a loop in which
the user can work interactively at any layer, often by talking directly to an
agent, while HELIX autonomously detects downstream implications, selects the
least-powerful sufficient next action, and advances the workflow without
requiring repeated manual orchestration. `helix run` is therefore an optional
convenience entrypoint to the supervisory loop, not the only valid way to
access it.

### Problem and Goals

#### Problem

AI-assisted development tools are good at producing local output, but weak at
maintaining coherent progress across a full software delivery stack. Users must
still tell the system what phase to enter next, remember when requirements
changes imply design updates, decide when stale issues need refinement, and
manually reconnect implementation work to governing artifacts.

That creates three failures:

1. Too much operator effort goes into orchestration instead of judgment.
2. Requirements, designs, tests, issues, and code drift out of alignment after
   iterative changes.
3. The agent behaves too literally unless the user remembers the HELIX method
   and explicitly restates it.

#### Goals

1. Make the HELIX supervisory loop the default autopilot for HELIX-managed
   work, whether entered through direct agent interaction or a thin
   compatibility surface such as `helix run`.
2. Ensure HELIX automatically advances the highest-leverage ready layer that
   does not require human input.
3. Make direct commands and skills available as intervention points inside the
   same loop, not as disconnected parallel interfaces.
4. Preserve bounded execution, authority order, and tracker-first discipline
   while making the system feel fluid in interactive use.

#### Success Metrics

| Metric | Target | Measurement Method | Timeline |
|--------|--------|-------------------|----------|
| Autopilot progression | `helix run` can advance from existing vision/requirements through downstream refinement and bounded execution without explicit phase instructions | End-to-end scenario tests and workflow walkthroughs | Year 1 |
| Reduced orchestration burden | Users rarely need to tell HELIX which phase to enter next when authority is sufficient | Qualitative operator evaluation and session review | Year 1 |
| Trigger correctness | Requirement changes, spec changes, and ready implementation work route to the expected HELIX actions | Deterministic tests and spec-driven examples | Year 1 |
| Safe escalation | HELIX asks for input mainly at real judgment boundaries, not because the control contract is underspecified | Review of intervention points in representative sessions | Year 2 |

#### Non-Goals

- Create an unbounded autonomous coding agent.
- Replace product, design, or prioritization judgment with guessed decisions.
- Require autopilot mode for all users or all tasks.
- Flatten all HELIX phases into one generic prompt.

### Users and Scope

#### Primary Persona: HELIX Operator
**Role**: Developer, tech lead, or staff engineer using AI as a day-to-day development partner  
**Goals**: Express product intent clearly, intervene where judgment matters, and let the system carry forward the rest of the workflow  
**Pain Points**: Too much manual orchestration, repeated re-explaining of workflow expectations, artifact drift after changes, and inconsistent issue quality

#### Secondary Persona: HELIX Maintainer
**Role**: Maintainer evolving the HELIX workflow, CLI, skills, and tracker  
**Goals**: Keep the workflow contract coherent across docs, skills, and implementation  
**Pain Points**: The product intent is easy to dilute when surface docs or skill descriptions become too command-literal

#### Tertiary Persona: New Team Member
**Role**: Developer or tech lead adopting HELIX for the first time without the creator present  
**Goals**: Understand the artifact hierarchy, create a first project, and become productive quickly  
**Pain Points**: The methodology is sophisticated and requires guided onboarding; without it, users may misuse HELIX as a prompt library or skip the planning artifacts entirely

### Requirements

#### Must Have (P0)

1. `helix run` acts as HELIX's supervisory autopilot rather than a narrow
   command wrapper.
2. `helix run` continuously selects the highest-leverage next bounded action
   that can be taken safely without user input.
3. HELIX applies the principle of least power when choosing the next action.
   It should refine or reconcile existing artifacts before escalating to larger
   changes.
4. HELIX detects downstream implications of user-driven changes.
   - A functionality change request triggers specification and design work when
     needed.
   - A specification or design change triggers issue refinement when open work
     already exists.
   - A specification or issue refinement made during a live `helix run`
     session must be observed at the next safe execution boundary rather than
     ignored until a later manual restart.
   - Ready execution work triggers bounded implementation.
5. HELIX escalates to the user when safe progress depends on missing authority,
   unresolved ambiguity, tradeoffs, prioritization, or approval.
6. Users can directly invoke any layer of the workflow interactively without
   breaking the overall control model.
7. Tracker state remains the durable execution layer for refinement, ordering,
   ownership, and completion of work.
8. Execution-ready beads must encode explicit parent-child relationships,
   dependencies, and deterministic success criteria so
   `ddx agent execute-loop` can drain work without hidden human ordering
   rules.
9. Alignment, review, measure, and report flows must capture every actionable
   result as properly ordered beads instead of leaving prose-only next steps.
10. `helix run` must support concurrent local operation where an automated
   session advances execution while an operator or another agent refines specs
   and tracker issues interactively.
11. `helix run` must revalidate issue state before claim and before close so
   concurrent refinement does not lead to stale execution or false completion.
12. HELIX must be distributed and installed as one skill pack, not as isolated
   standalone skills copied without their shared resources.
13. Resources shared by multiple HELIX skills must live in `workflows/`, while
   skill-specific resources must live with the corresponding skill under
   `skills/<skill>/`.
14. Plugin, enterprise, and local installations must preserve package-relative
    access from HELIX skills to the shared `workflows/` resource library.

#### Should Have (P1)

1. HELIX documents explicit trigger rules between `run`, `align`, `design`,
   `polish`, `build`, `review`, `check`, `evolve`, and `backfill`.
2. Skills describe not only what each command does, but when it should
   activate based on user intent and repo state.
3. The workflow contract makes it obvious where human attention is expected and
   where autopilot should proceed silently.
4. Deterministic tests cover the most important state transitions in the
   supervisory loop.
5. Packaging and installer rules make incomplete skill-only installs invalid
   rather than silently degrading shared-resource access.
6. Deterministic tests cover queue drift caused by concurrent interactive
   refinement while `helix run` is active.
7. `helix status` provides a structured lifecycle snapshot: run-controller
   state, current claimed work, blocked issues with reasons, pending human
   decisions, and next recommended action.
8. Cross-model review: when `--review-agent` is configured, reviews and plan
   critiques alternate between the implementation agent and the review agent
   to catch blind spots.
9. Epic focus mode: when `helix run` picks an epic, it stays focused —
   decompose into children, implement them, review the epic on close — before
   moving to the next scope.
10. First-class principles: HELIX ships a small set of default design
    principles and every judgment-making skill loads the active principles
    (project-specific if they exist, HELIX defaults otherwise) to guide
    design trade-offs, implementation choices, and review criteria
    consistently across phases. See [[FEAT-003]].
11. Plugin packaging: HELIX should be installable as a Claude Code plugin so
    that skills, the CLI, and shared workflow resources are discovered
    automatically via the plugin manifest — no manual symlink installation
    required. See [[FEAT-004]].
12. Concerns, practices, and context digests: HELIX ships a library of
    composable cross-cutting concerns (tech stacks, a11y, o11y, i18n) with associated practices. Beads
    created by triage and evolve must carry a compact context digest
    (~1000-1500 tokens) summarizing active principles, concerns, practices,
    relevant ADRs, and governing spec context — making beads self-contained
    execution units that rarely require upstream file reads. See [[FEAT-006]].
13. Artifact template quality: each artifact template (Vision, PRD, Feature
    Spec, Solution Design, Technical Design, ADR, Test Plan) must include
    clear instructions for what goes in each section, prompts for agents to
    generate drafts from higher-level artifacts, review checklists for
    adversarial review, and relationship declarations so the artifact graph
    can be constructed automatically. See [[FEAT-008]].
14. Team onboarding: HELIX must be teachable without its creator present.
    This includes a getting-started guide that walks through initializing a
    project, understanding the artifact hierarchy, creating a first bead,
    and running an agent; a guided first-project template; and
    self-documenting prompts that explain why each bead exists and what
    context it draws from. See [[FEAT-009]].
15. Testing strategy templates: HELIX should provide structured guidance on
    testing approaches — acceptance test generation from acceptance criteria,
    property-based testing patterns, integration/flow testing, and
    performance benchmarking templates. These are structured approaches and
    prompts, not test frameworks. See [[FEAT-010]].
16. Hypothesis-driven optimization: the `helix experiment` command must
    support metric definition, hypothesis generation, hypothesis testing
    (apply change, re-measure), selection (keep improvements, discard
    regressions), and iteration until target or diminishing returns. Each
    hypothesis is a bead. Failed hypotheses must roll back cleanly.

#### Nice to Have (P2)

1. Operator-facing examples show common transitions such as requirements change
   -> evolve -> polish -> build -> review.
2. The tracker supports richer lifecycle metadata: phase labels for all 6
   phases (`phase:frame`, `phase:test`), per-scope phase gates, and structured
   blocker descriptions.
3. Phase-aware `helix run` that drives the full lifecycle (Frame → Design →
   Test → Build → Deploy → Iterate) using explicit per-scope phase state
   rather than inference from labels and deps.
4. `helix frame`, `helix test`, and `helix deploy` as phase-specific commands
   for manual control over phases currently handled implicitly.
5. `helix reject` as a compound operation: structured rejection reason, mark
   execution-ineligible, create corrective follow-on issue.
6. Unstructured feedback routing: when a user provides unstructured feedback
   about a running system ("I don't like how this looks", "the ships should
   be green"), HELIX should determine which artifact layer the feedback
   applies to and generate the appropriate bead to address it.
7. Real-project feedback integration: lessons from validated HELIX projects
   should be captured and folded into improved templates, better prompts,
   new cross-cutting concerns, and updated getting-started materials.

### Phases

| Phase | Description | Key Activities |
|-------|-------------|----------------|
| **Discover** | Explore the problem space | Market analysis, competitive review, stakeholder research |
| **Frame** | Decompose the problem into structured artifacts | Vision, PRD, Feature Specs, Acceptance Criteria |
| **Plan** | Encode requirements as testable assertions | Convert acceptance criteria into executable tests |
| **Build / Iterate** | Red-green-refactor against tests | Implement code to pass tests, respecting cross-cutting concerns |
| **Polish** | Systematic optimization against metrics | Hypothesis-driven improvement, adversarial review, gap analysis |

### Command Surface

The command surface is organized around how users interact with HELIX:

#### Execution (how agents work)

- `helix run` — supervisory autopilot; reads tracker, selects the
  highest-leverage next action, delegates managed execution to DDx, and
  repeats until human input is needed or no work remains
- `helix worker` — launch `helix run` as a background process and monitor
  progress via summary output and log files
- `helix status` — structured lifecycle snapshot for human observation

Execution contract:
- HELIX owns supervisory routing, artifact-aware queue policy, review, and
  escalation decisions
- DDx owns managed execution primitives: `ddx agent execute-bead` for bounded
  single-bead work and `ddx agent execute-loop` as the default queue-drain
  contract
- HELIX CLI surfaces are convenience entrypoints and compatibility wrappers,
  not the durable owner of claim/execute/close mechanics
- retained `helix run` and `helix build` are compatibility wrappers and
  deprecation candidates once DDx exposes the remaining HELIX-visible routing
  and evidence hooks they currently bridge
- direct `ddx agent run` remains for non-managed prompts such as planning,
  review, and alignment

#### Steering (how humans direct agents)

The tracker is the primary steering interface. Users typically interact with
the tracker via an agent conversation while `helix run` grinds in the
background. Structured commands ensure artifact consistency:

- `ddx bead` — raw CRUD for issues (create, show, update, close, list,
  ready, blocked, dep, status)
- `helix evolve` — thread a requirement change through the artifact stack;
  updates governing docs and creates/modifies tracker issues
- `helix design` — create or extend the design stack (architecture, ADRs,
  solution designs, test strategy) through iterative multi-model refinement
- `helix review` — fresh-eyes review of recent work
- `helix align` — convenience entrypoint that creates or claims the governing
  alignment bead, then runs the stored alignment prompt to produce a durable
  report plus properly ordered follow-on beads
- `helix polish` — iterative issue refinement before implementation
- `helix experiment` — metric-driven optimization loop

Queue-shaping rules for DDx-managed execution:
- use parent-child relationships to keep related work grouped under an epic or
  governing planning bead
- use explicit dependencies for real ordering constraints instead of prose
- require machine-auditable acceptance and success criteria: exact commands,
  named checks, concrete files or fields, or observable repository states
- do not create execution-ready build beads when success criteria are still
  subjective or underspecified; route those back to planning or polish first
- alignment, review, and report outputs must become beads before the governing
  planning bead closes

#### Internal (dispatched by run, also directly invocable)

- `helix build` — one bounded implementation pass (currently: `implement`)
- `helix check` — queue-health decision: what action should run take next

#### Deferred (Phase 2 — requires tracker lifecycle primitives)

- `helix frame` — Phase 1: requirements, feature specs, user stories
- `helix test` — Phase 3: write failing tests from design artifacts (Red gate)
- `helix deploy` — Phase 5: release, monitoring, verification
- `helix reject` — compound rejection: structured reason, mark ineligible,
  create corrective follow-on
- Per-scope phase gates on tracker epics/scopes

#### Command naming principle

Commands that map to HELIX phases use the phase name: `frame`, `design`,
`test`, `build`, `deploy`. Commands that are control-plane verbs use their
verb: `run`, `status`, `evolve`, `review`, `align`, `polish`, `experiment`.

### Functional Requirements

#### Supervisory Run Loop

1. `helix run` must own autonomous forward progress and supervisory routing for
   HELIX-managed work.
2. `helix run` must treat DDx-managed execution as the implementation
   substrate, not as a detail to be reimplemented locally.
3. `helix run` must treat the companion HELIX actions as triggered subroutines
   inside the loop, while still allowing them to be invoked directly.
4. `helix run` must stop when human input is required rather than continuing
   through uncertainty.
5. `helix run` must support epic focus: when an epic is selected, stay on it
   (decompose → implement children → review on close) before moving on.
6. `helix run` must use exponential backoff on difficult issues rather than
   immediately skipping them. Only declare an issue intractable after
   escalating effort across multiple attempts.
7. `helix run` must absorb small adjacent work (same file, related manifest
   updates) into the current issue rather than creating separate tickets for
   every observation.
8. `helix run` must produce a structured blocker report when it finishes,
   identifying every skipped issue with its reason and marking them in the
   tracker for human triage.
9. The migration target is DDx-managed queue drain through `ddx agent execute-loop`;
   until that parity is complete, HELIX may keep a compatibility wrapper, but
   the governing contract must treat `execute-loop` as the destination rather
   than growing more wrapper-owned claim/close mechanics.

#### Trigger Rules

1. When the user asks for a functionality change, HELIX must evaluate whether
   existing requirements, feature specs, or designs need reconciliation or
   expansion before implementation work continues.
2. When requirements or design artifacts change and open issues already exist,
   HELIX must refine the issue queue before implementation resumes.
3. When issues are ready and adequately governed by upstream artifacts, HELIX
   must prefer bounded implementation over further speculative planning.
4. When tracker or governing-artifact state changes during a live run, HELIX
   must re-check at the next safe boundary instead of closing or claiming work
   from stale assumptions. Drift on a single issue should skip that issue,
   not stop the entire loop.
5. After implementation, HELIX must review the recent work using a different
   AI model than the one that implemented it when cross-model review is
   configured.
6. After an epic closes, HELIX must run a scoped review against the epic's
   governing spec to verify acceptance coverage and catch gaps.
7. When canonical artifacts are missing or too incomplete for safe progress,
   HELIX must stop for guidance or run a bounded reconstruction path rather
   than guessing.
8. When `helix evolve` invalidates in-flight work, it must use explicit
   tracker primitives (`superseded-by`, `execution-eligible=false`, or
   blocking deps on new design issues) rather than vague "re-evaluation"
   flags.

#### Interactive Operation

1. Users must be able to work directly in vision, PRD, specs, designs, issues,
   tests, implementation, review, or metrics.
2. Direct invocation of a single HELIX command or skill must not break the
   broader model that `helix run` uses to resume supervision later.
3. The typical interaction pattern is: user talks to an agent that manipulates
   the tracker and governing artifacts, while `helix run` supervises in the
   background and DDx-managed execution handles bounded work. The tracker is
   the shared state between the human-facing agent and the execution lane.

#### Observability

1. `helix run` must persist run-controller state (last check result, stop
   reason, current claimed issue, last action timestamp, cumulative token
   usage) to a structured state file.
2. `helix status` must surface this state file plus tracker health in a
   machine-readable format.
3. Long-running codex sessions must have timeout enforcement and periodic
   heartbeat output.
4. Each cycle must log elapsed time and token usage.
5. Every HELIX skill invocation that produces structured output must create a
   DDx execution run record linking the output to the governing artifact.
   See [[FEAT-005]].
6. `helix status` must be able to query recent execution history to report
   what actions were taken and their outcomes.

#### Quality Assurance

1. Tracker validation must enforce required fields (helix label, phase label,
   spec-id for tasks, acceptance criteria for tasks and epics) at issue
   creation time.
2. Design documents and critical artifacts should go through multi-round
   iterative refinement with convergence detection.
3. When cross-model review is configured, alternating AI models critique each
   other's work to catch implementation blindness.

#### Packaging and Resource Access

1. HELIX skills must be installed as one package that preserves both
   `skills/` and `workflows/`.
2. `workflows/` must be treated as the shared resource library for assets used
   by multiple HELIX skills.
3. Assets used by only one skill should live in that skill's directory instead
   of `workflows/`.
4. HELIX skills must reference shared resources through stable package-relative
   paths and must fail clearly if the shared library is missing.

### Constraints, Assumptions, Dependencies

#### Constraints

- **Technical**: HELIX must preserve bounded actions, authority-ordered
  decision-making, tracker-first execution, and package-relative access from
  skills to shared workflow resources.
- **Product**: The interface must stay comprehensible; new supervisory behavior
  cannot devolve into hidden magical state changes.
- **Testing**: The control loop should be explainable and testable through
  deterministic scenarios, not only anecdotal chat transcripts.

#### Assumptions

- Repositories using HELIX have or will produce a usable authority stack:
  vision, requirements, specs, designs, tests, and issues.
- Users want the ability to intervene anywhere in the workflow even when
  autopilot exists.
- The least-power heuristic can be documented tightly enough to avoid arbitrary
  agent behavior.

#### Dependencies

- Workflow contract documents under `workflows/`
- **DDx bead tracker** (`ddx bead`) as the canonical work-item backend. HELIX
  configures `bead.id_prefix: hx` and layers HELIX-specific labels/fields via
  validation hooks. HELIX no longer owns storage directly.
- **DDx agent service** (`ddx agent run`, `ddx agent execute-bead`,
  `ddx agent execute-loop`) for harness dispatch, managed bead execution,
  token tracking, and session logging. HELIX no longer implements its own
  execution substrate; it calls DDx.
- **DDx execution framework** (`ddx exec`) for durable, artifact-linked
  execution run records. HELIX skill outputs are captured as DDx execution
  runs. See DDx FEAT-010 and [[FEAT-005]].
- HELIX tracker conventions (labels, spec-id, queue semantics) remain
  HELIX-owned, enforced via DDx validation hooks, and operate on DDx beads.
- Skill surfaces under `skills/`
- CLI execution surface in `scripts/helix`
- Plugin packaging via `.claude-plugin/plugin.json` manifest that preserves
  the HELIX package layout (see [[FEAT-004]])
- Legacy installer (`scripts/install-local-skills.sh`) as development
  convenience

### Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Autopilot remains too vague and agents continue behaving literally | High | High | Define trigger rules and escalation boundaries explicitly in the PRD and workflow contract |
| The system overreaches and makes product decisions without authority | Medium | High | Preserve bounded actions, least-power rules, and escalation-on-ambiguity requirements |
| Interactive commands and autopilot drift into separate mental models | Medium | High | Define companion commands as intervention points inside one shared control system |
| Existing docs and skills lag behind the product contract | High | Medium | Follow the PRD with explicit workflow and skill-spec updates plus tracker issues |
| Testing and validation unsolved industry-wide | High | High | Progressive abstraction + TDD + hypothesis optimization; track Meta JIT testing and similar research |
| Documentation staleness (classic doc-driven failure) | Medium | High | Reconciliation beads, adversarial review, `helix align` |
| DDX/HELIX boundary confusion | Medium | Medium | Explicit separation: DDX owns platform (beads, agents, exec); HELIX owns methodology (phases, templates, concerns) |
| Transferability — new users can't adopt without creator | High | High | Team onboarding workflow ([[FEAT-009]]), guided first-project template, self-documenting prompts |
| Rate of change in agentic best practices | High | Medium | Flexible template system, concern library extensibility, no breaking changes to artifact shapes |

### Success Criteria

- `helix run` is defined as HELIX's supervisory autopilot in the product docs.
- The PRD makes clear when HELIX should continue autonomously and when it must
  stop for user input.
- The PRD defines the required transitions among requirement changes, design
  reconciliation, issue refinement, bounded implementation, and review.
- The PRD makes direct commands and skills subordinate to one coherent control
  model rather than describing them as isolated wrappers.
