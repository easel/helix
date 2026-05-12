---
title: "Product Vision"
slug: product-vision
phase: "Discover"
weight: 0
generated: true
aliases:
  - /reference/glossary/artifacts/product-vision
---

## What it is

North star document defining mission, positioning, direction, target market,
and success criteria. First artifact in Discover phase.

## Activity

**[Discover](/reference/glossary/activities/)** — Validate that an opportunity is worth pursuing before committing to a development cycle.

## Output location

`docs/helix/00-discover/product-vision.md`

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

- [Business Case](../business-case/)
- [Competitive Analysis](../competitive-analysis/)
- [Opportunity Canvas](../opportunity-canvas/)

### Informs

- [Business Case](../business-case/)
- [Competitive Analysis](../competitive-analysis/)
- [Opportunity Canvas](../opportunity-canvas/)
- [Prd](../prd/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Product Vision Prompt

Create a concise product vision that aligns stakeholders on mission, direction, and value.

## Storage Location

Store at: `docs/helix/00-discover/product-vision.md`

## Purpose

A **north star document** that keeps direction, value, and success criteria
clear. Every downstream artifact — PRD, specs, designs, tests — traces back to
this document. If the vision is vague, everything built on it drifts.

## Key Principles

- **Be concise** — keep the mission to 1-2 sentences.
- **Be specific** ��� name target customers, name competitors, state measurable
  outcomes. Placeholders and hedging ("various users", "significant impact")
  are not acceptable.
- **Be compelling** — connect the vision to real customer pain and a concrete
  end state.
- **Be honest** — if you can't fill a section with substance, that's a signal
  the thinking isn't done yet. Flag it rather than filling with platitudes.

## Section-by-Section Guidance

### Mission Statement
Write it so someone outside the team understands what you do in one breath.
Test: could you say this in a single tweet?

### Positioning (Moore's Template)
Fill in every blank with a real noun. "For [target] who [need]" must name a
specific customer segment and a specific pain — not a category. "Unlike
[alternative]" must name an actual product or approach the customer uses today.
If you can't name the alternative, you don't understand the market yet.

### Vision
Describe the desired end state, not a timeline. What changes for users? What
changes in the market? Avoid "we will be the leading..." — describe what the
world looks like, not your position in it.

### User Experience
Walk through a concrete session. Use present tense. Name the actions the user
takes and what the system does in response. This should read like a usage
scenario, not marketing copy.

### Target Market
"Who" must be specific enough to find these people. "Software teams" is too
broad. "Teams of 3-15 engineers using AI coding agents daily who ship
weekly" is specific enough.

### Key Value Propositions
Each row must pass the "so what?" test. The customer benefit column should
describe what changes for the customer, not restate the capability.

### Success Definition
Every metric must be measurable with a tool or process you can name. "User
satisfaction" is not measurable. "NPS > 40 from monthly survey" is.

### Why Now
Ground this in an observable change — a technology shift, a market event, a
regulatory change, a behavioral trend. "AI is getting better" is too vague.
"Coding agents can now implement bounded tasks reliably but teams lack a
supervisory layer" is grounded.

## Quality Checklist

After drafting, verify every item. If any blocking check fails, revise before
committing.

### Blocking

- [ ] Positioning names a specific customer segment (not a category)
- [ ] Positioning names a specific competitor or alternative (not "existing solutions")
- [ ] Target market is specific enough to identify real people
- [ ] Every success metric has a numeric target or measurable outcome
- [ ] User experience section describes a concrete scenario (not abstract benefits)

### Warning

- [ ] Mission fits in a tweet (under 280 characters)
- [ ] Vision describes an end state, not a timeline or market position
- [ ] Why Now cites an observable change, not a general trend
- [ ] Value propositions pass the "so what?" test
- [ ] No section contains only placeholder text
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Product Vision

## Mission Statement

[One to two sentences: What we do + for whom + why it matters]

## Positioning

For [target customer] who [need or problem],
[product name] is a [category] that [key benefit].
Unlike [current alternative], [product name] [primary differentiator].

## Vision

[What does the world look like when this product succeeds? Describe the desired end state — not when it happens, but what changes for users and the market.]

**North Star**: [Single sentence describing ultimate success state]

## User Experience

[Describe what a typical session looks like when this product works as intended. Walk through a concrete scenario from the user's perspective — what do they do, what happens, how does it feel?]

## Target Market

| Attribute | Description |
|-----------|-------------|
| Who | [Specific customer type] |
| Pain | [Primary pain point] |
| Current Solution | [What they use today] |
| Why They Switch | [What makes the status quo untenable] |

## Key Value Propositions

| Value Proposition | Customer Benefit |
|-------------------|------------------|
| [Core capability] | [Why it matters to customer] |
| [Core capability] | [Why it matters to customer] |

## Success Definition

| Metric | Target |
|--------|--------|
| Primary KPI | [Specific measurable outcome] |
| [Supporting metric] | [Specific measurable outcome] |

## Why Now

[One paragraph: What has changed — in the market, technology, or user behavior — that makes this the right time to build this? Why would waiting be costly?]

## Review Checklist

Use this checklist when reviewing a product vision artifact:

- [ ] Mission statement is specific — names the user, the problem, and the approach
- [ ] Positioning statement differentiates from the current alternative
- [ ] Vision describes a desired end state, not a feature list
- [ ] North star is a single measurable sentence
- [ ] User experience section describes a concrete scenario, not abstract benefits
- [ ] Target market identifies specific pain points and switching triggers
- [ ] Value propositions map to customer benefits, not internal capabilities
- [ ] Success metrics are measurable and time-bound
- [ ] Why Now section names a specific change, not a vague opportunity
- [ ] No implementation details (technology choices, architecture) — those belong in design
``````

</details>

## Example

This example is HELIX's actual product vision, sourced from [`docs/helix/00-discover/product-vision.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/00-discover/product-vision.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Product Vision

### Mission Statement

HELIX is a methodology and artifact catalog for AI-assisted software teams. It
packages decades of document discipline — PRDs, design documents, test plans,
alignment reviews — as portable templates plus one skill that keeps everything
in sync as the work moves.

### Core Metaphor

The double helix of DNA has two strands wound around each other; neither
leads, neither follows. HELIX adopts that shape for software development. The
**document strand** holds intent, design, and tests. The **execution strand**
turns those into running code. HELIX is the discipline of the document
strand. A substrate — DDx, an agent runtime, anything that reads and writes
files — runs the execution strand.

### Positioning

For software teams using AI agents to build production systems but losing time
to inconsistent specifications, drifting designs, and ad-hoc prompting, HELIX
is a portable development methodology delivered as artifact templates and a
single planning skill. Unlike one-off prompt libraries or vendor-locked
workflow tools, HELIX is a methodology you adopt, not a platform you join — its
content runs on any agent runtime that reads and writes markdown.

#### What HELIX Is Not

- HELIX is **not a platform.** It is content (templates, prompts, methodology
  docs) plus one skill. It runs inside substrates (DDx, Databricks Genie,
  Claude Code, a plain agent shell).
- HELIX is **not a tracker, CLI, or execution engine.** Those are substrate
  concerns. HELIX produces aligned artifacts and plans; substrates execute
  them.
- HELIX is **not waterfall.** The seven activities (Discover, Frame, Design,
  Test, Build, Deploy, Iterate) name kinds of work, not steps in a sequence.
  Multiple activities run at once and feed each other through artifact updates.
- HELIX is **not prescriptive about tools.** Stack choices are project
  concerns.

### Vision

HELIX becomes the default discipline for AI-assisted software development.
Teams adopt it the way they adopted test-driven development: not because of a
tool, but because the practice produces durably better software. Agents
authoring against HELIX's templates produce specifications and designs at a
level human reviewers actually trust. The alignment skill keeps the governing
artifacts coherent as priorities and code evolve.

**North Star**: A team writes its product intent once, and the rest of the
governing artifacts — features, designs, tests, code — stay aligned with that
intent through every change, without the team rewriting documents by hand.

### The Methodology

HELIX names seven kinds of work in software development. Each owns a set of
artifact types, and the activities are connected by an authority order that
decides which artifact wins when two disagree. Work moves between activities
freely — a failing test surfaces a design gap, a production metric revises the
PRD, a vision change propagates downstream.

#### The Seven Activities

| Activity | Purpose | Primary Artifacts |
|---|---|---|
| **Discover** | Clarify the opportunity | Product vision, business case, competitive analysis, opportunity canvas |
| **Frame** | Define what to build | PRD, feature specs, user stories, principles, cross-cutting requirements |
| **Design** | Decide how to build it | Architecture, ADRs, solution designs, technical designs, contracts |
| **Test** | Encode the contract as executable specifications | Test plans, story test plans, security tests |
| **Build** | Implement to make tests pass | Implementation plan plus executed work (in the substrate's tracker) |
| **Deploy** | Make it observable in production | Deployment checklist, runbook, monitoring setup, release notes |
| **Iterate** | Close the loop with real signal | Metric definitions, metrics dashboard, improvement backlog |

#### Authority Order

The artifacts have a strict authority order. Higher-level artifacts govern
lower-level ones; conflicts resolve **up** the order, never down.

1. Product Vision
2. PRD
3. Feature Specifications and User Stories
4. Architecture and ADRs
5. Solution Designs and Technical Designs
6. Test Plans and Executable Tests
7. Implementation Plans
8. Source Code and Build Artifacts

When the implementation contradicts the test, the test wins. When the test
contradicts the design, the design wins. When the design contradicts the
feature spec, the feature spec wins. Source code is evidence of current
behavior, not the source of truth for what should exist.

#### How Changes Flow

Changes enter at any activity:

- **Top-down** — a vision revision propagates into PRD, features, designs, tests, code.
- **Bottom-up** — implementation reveals a missing requirement; the spec gets a refinement.
- **Middle-out** — a design exposes a conflict between two features; both specs update.
- **Lateral** — a deploy-time observability gap surfaces an ADR question.

The alignment skill keeps these flows coherent. It walks the artifacts when
invoked, identifies drift in any direction, and produces a plan to close it.

### User Experience

A team wants to add OAuth login. They describe the intent to their agent. The
agent invokes the HELIX alignment skill against the project's existing
governing artifacts.

The skill walks the artifacts and produces a structured finding: the new feature
affects three feature specs, two solution designs, and the security
architecture; one existing ADR conflicts with the OAuth pattern; four user
stories need to be added; one test plan must be revised before any of that.
Output is a plan ordered by authority — start with the security-architecture
revision, then update the affected feature specs, then create the stories,
then update the designs.

The team reviews the plan, adjusts scope, approves it. The substrate (DDx,
Databricks Genie, whatever they're using) creates work items from the plan.
As work happens, the alignment skill runs periodically against the artifacts to
catch drift before it accumulates.

The team never invoked a HELIX command, because there isn't one. They invoked
their agent, and the agent invoked HELIX's skill.

### Target Market

| Attribute | Description |
|-----------|-------------|
| Who | Software teams using AI agents (Claude Code, Cursor, Databricks Genie, Copilot Workspace) for non-trivial development |
| Pain | Artifact drift across sessions; agents make local decisions that conflict with global intent; specs and code diverge silently; reviews catch problems too late |
| Current Solution | Ad hoc prompting, manual document maintenance, hoping for the best |
| Why They Switch | HELIX gives agents and humans the same methodology — every change traces back to a governing artifact, and the alignment skill catches drift early |

### Key Value Propositions

| Capability | Customer Benefit |
|---|---|
| Authority-ordered artifact catalog | Every document has a clear governing relationship; changes propagate predictably |
| Single alignment skill | Catches drift early without walking the artifact tree by hand |
| Portable content | Run on any substrate that reads markdown — DDx, Databricks Genie, Claude Code, anything |
| Document-driven reviews | Audits work on artifacts, not chat transcripts |
| Methodology, not platform | Adopt incrementally; no vendor lock-in |

### Product Principles

1. **Authority is the resolver.** Conflicts between artifacts resolve up the
   authority order, never down. Source code never overrides specification.

2. **Documents are the contract.** Every consequential decision lands as an
   artifact update. If a decision is not in the documents, it does not exist.

3. **Alignment is continuous.** The loop runs always; drift is caught early,
   not in a quarterly audit. The alignment skill is the operator of this rule.

4. **Substrates are pluggable.** HELIX itself never executes code, manages
   queues, owns infrastructure, or assumes a runtime. The runtime is the
   substrate's concern.

5. **Less is more.** HELIX owns the methodology and one skill — not the
   toolbox. Every feature added to HELIX is weighed against "could this live
   in the substrate instead?"

6. **Work flows in every direction.** A test exposes a design gap; a metric
   revises a feature spec; a vision update propagates down. The activity
   names locate the kind of work, not its position in a sequence.

7. **Discipline over improvisation.** AI agents improvise well; the value of
   HELIX is the discipline that makes improvisation reviewable.

### Success Definition

| Metric | Target |
|--------|--------|
| Substrate breadth | 3 documented substrate deployments (DDx, Databricks Genie, one other) within 12 months |
| Adoption | 50+ public repos using HELIX templates as their artifact catalog within 18 months |
| Alignment quality | Healthy artifact sets average < 3 alignment findings per skill run |
| Authoring quality | PRDs and feature specs authored from HELIX templates pass first-pass review at measurably higher rates than free-form equivalents |
| Skill portability | Skill body contains zero substrate-specific commands; portability check passes on every release |

### Why Now

AI-assisted development has crossed from novelty to default practice. Most
professional developers ship AI-touched code daily. But the practice is
uneven: agents produce work that is locally good but globally inconsistent,
because the disciplines human teams developed over decades — PRDs, design
documents, test plans, alignment reviews — have not been packaged into
something agents can apply uniformly.

The agents are ready. The methodology has been ad hoc. The Genie / Cursor /
Claude Code era will have its TDD-equivalent practice. HELIX is the bet on
what it looks like: document-driven, agent-friendly, substrate-portable.

### Known Risks

1. **Methodology adoption is slow.** Teams resist process; "just write the
   code" is the durable default. *Mitigation*: keep HELIX minimal; the
   alignment skill must produce value on the first run.

2. **Substrate fragmentation.** If every agent runtime needs custom packaging,
   maintenance cost scales linearly. *Mitigation*: define a minimal runtime
   contract early; adapters are small wrappers, not forks.

3. **Skill quality.** The alignment skill is HELIX's primary product. Noisy
   or wrong findings collapse the value. *Mitigation*: the skill is the focus
   of HELIX's own development effort; everything else is content.

4. **DDx coupling lingers.** Earlier HELIX work assumed DDx; some surfaces
   still leak it. *Mitigation*: explicit decoupling beads; ratchet on "no
   substrate refs in skill body."

5. **Documentation staleness.** Classic failure mode of document-driven
   development. *Mitigation*: the alignment skill itself catches stale
   documents; HELIX dogfoods its own catalog.

6. **Transferability.** HELIX must be teachable without its creator present.
   *Mitigation*: onboarding doc is a P0 deliverable; new-teammate review is a
   release criterion.

### Explicit Non-Goals

- HELIX will not provide a CLI, a tracker, a queue, or an execution engine.
- HELIX will not impose technology choices or fork by language ecosystem.
- HELIX will not replace product, design, or architectural judgment. It
  packages the discipline of capturing those judgments; the judgments remain
  human.
- HELIX will not be a fully autonomous agent. The alignment skill produces
  plans; humans approve.
- HELIX will not flatten the seven activities into one generic prompt. The
  activity decomposition is load-bearing.
