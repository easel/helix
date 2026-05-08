---
title: "PR-FAQ"
slug: pr-faq
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/pr-faq
---

## What it is

A working-backwards artifact pairing a launch-day press release with an
internal FAQ. The press release forces the team to commit to a concrete
customer outcome before any design or implementation; the FAQ surfaces the
hard questions — economics, feasibility, adoption, regulatory exposure —
that the PRD will then have to answer. HELIX uses the PR-FAQ as a focus
and validation step between the Product Vision and the PRD.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/pr-faq.md`

## Relationships

### Requires (upstream)

- [Product Vision](../product-vision/) — sets long-term direction; PR-FAQ narrows to a specific launch outcome within it
- [Opportunity Canvas](../opportunity-canvas/) — frames the customer problem and segment *(optional)*
- [Business Case](../business-case/) — informs the economic FAQs *(optional)*

### Enables (downstream)

- [PRD](../prd/) — press release outcome and FAQ open questions seed the PRD
- [Stakeholder Map](../stakeholder-map/) — internal FAQ surfaces who must be in the loop
- [Principles](../principles/) — customer commitments inform design principles

### Informs

- [Prd](../prd/)
- [Principles](../principles/)
- [Stakeholder Map](../stakeholder-map/)
- [Feature Specification](../feature-specification/)

### Referenced by

- [Prd](../prd/)
- [Solution Design](../solution-design/)
- [Feature Specification](../feature-specification/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# PR/FAQ Prompt
Synthesize the source material into a launch-day press release and FAQ using a working-backwards lens.

## Focus
- Keep the press release customer-centric and future-facing.
- Use the FAQ to surface adoption blockers, feasibility concerns, and validation needs.
- Call out assumptions and high-risk gaps instead of glossing over them.

## Completion Criteria
- The press release is readable on its own.
- The FAQ answers the likely hard questions.
- Next steps and experiments are explicit.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
ddx:
  id: helix.pr-faq
---
# PR-FAQ: [PRODUCT NAME]

<!--
This artifact has two halves: a launch-day press release (~350 words) and an
internal FAQ. Write it as if the product ships tomorrow. The press release is
customer-facing; the FAQ is internal and confronts the hard questions. If you
can't write a credible PR-FAQ, the team doesn't yet understand the problem.
-->

## Press Release

**FOR IMMEDIATE RELEASE — [CITY, COUNTRY] — [LAUNCH DATE]**

### Headline

[ONE-LINE VALUE PROPOSITION IN PLAIN ENGLISH. NO JARGON, NO ADJECTIVES LIKE "REVOLUTIONARY" OR "WORLD-CLASS". STATE WHAT THE PRODUCT DOES AND FOR WHOM.]

### Subhead

[ONE SENTENCE EXPANDING THE HEADLINE: WHO IT IS FOR, WHAT IT DOES, WHY IT MATTERS, WHEN IT IS AVAILABLE.]

### Summary

<!-- The lede. What is being announced, the customer outcome, and why now. 2-4 sentences. -->

[COMPANY NAME] today announced [PRODUCT NAME], [SHORT DESCRIPTION]. [PRODUCT NAME] helps [SPECIFIC CUSTOMER SEGMENT] [ACHIEVE SPECIFIC OUTCOME] by [HOW IT WORKS, ONE PHRASE]. It is available [WHERE/WHEN] starting [DATE].

### The Problem

<!-- Name the customer pain in their words. Not "users struggle" — "a 12-person bookkeeping firm spends 6 hours a week reconciling deposits by hand." -->

[CONCRETE PROBLEM, IN THE CUSTOMER'S TERMS, WITH A NUMBER OR FAILURE MODE THAT MAKES IT REAL.]

### The Solution

<!-- How the product solves the problem. Stay at the customer's level — what they do, not how the system is implemented. -->

[ONE PARAGRAPH DESCRIBING THE EXPERIENCE OF USING THE PRODUCT TO SOLVE THE PROBLEM ABOVE.]

### Quote from [LEADER NAME, TITLE]

> "[ONE PARAGRAPH IN THE COMPANY'S VOICE EXPLAINING WHY WE BUILT THIS. NAMES THE CUSTOMER, THE PROBLEM, AND THE COMMITMENT. NOT A SLOGAN.]"

### How It Works

<!-- 3-5 short steps from the customer's perspective. -->

1. [STEP ONE]
2. [STEP TWO]
3. [STEP THREE]

### Customer Quote

> "[ONE PARAGRAPH FROM THE IMAGINED CUSTOMER. IN THEIR VOICE. ABOUT THE OUTCOME THEY GOT, NOT THE FEATURES THEY USED. NAMES A SPECIFIC NUMBER, TIME SAVED, OR PROBLEM AVOIDED.]"
>
> — [CUSTOMER NAME, ROLE, COMPANY OR CONTEXT]

### Availability

[WHERE TO GET IT, WHAT IT COSTS, WHAT PLATFORMS, WHAT REGIONS, WHEN, HOW TO SIGN UP.]

---

## FAQ

<!--
Two halves. External FAQs are what a customer, journalist, or analyst would
ask. Internal FAQs are what an exec, engineer, lawyer, or finance partner
would ask in a review meeting. The internal FAQs should be the hardest
questions you can think of — not soft-balls.
-->

### External FAQs

#### How much does it cost?

[SPECIFIC PRICING. IF FREE, EXPLAIN HOW THE BUSINESS MODEL WORKS. IF NOT YET DECIDED, SAY SO AND NAME THE DECISION OWNER.]

#### How is this different from [EXISTING ALTERNATIVE]?

[NAME THE INCUMBENT OR ADJACENT PRODUCT. DESCRIBE THE SPECIFIC DIFFERENCE — WHO BENEFITS FROM THE DIFFERENCE AND WHEN.]

#### Who is this NOT for?

<!-- Forces honest scoping. -->

[SEGMENT OR USE CASE THAT IS BETTER SERVED BY AN ALTERNATIVE.]

#### What's not in v1?

[EXPLICIT LIST OF FEATURES OR USE CASES DELIBERATELY DEFERRED. EACH WITH A REASON.]

#### What platforms / regions / integrations are supported at launch?

[SPECIFIC LIST.]

#### When can I get it?

[DATE OR PHASED ROLLOUT.]

### Internal FAQs

<!--
Each question below should make at least one stakeholder uncomfortable to
answer. If they don't, the FAQ is too soft.
-->

#### What is the unit economics story? Is this profitable per customer?

[GROSS MARGIN ESTIMATE. ASSUMPTIONS. WHAT BREAKS THE MODEL.]

#### What is the riskiest technical assumption?

[NAME ONE SPECIFIC FEASIBILITY RISK. WHAT WOULD WE NEED TO BUILD OR PROVE TO DE-RISK IT.]

#### What experiments must run before we commit?

[LIST OF NAMED EXPERIMENTS WITH OWNERS AND DEADLINES. IF NONE — JUSTIFY WHY.]

#### What is the smallest viable launch?

[THE MINIMUM SHAPE OF V1 THAT VALIDATES THE THESIS.]

#### Who else has to ship something for this to work?

[EXTERNAL TEAMS, VENDORS, REGULATORY APPROVALS, OR CUSTOMERS. WHAT'S THE COMMITMENT STATUS.]

#### What regulatory or legal exposure does this create?

[LICENSING, DATA PROTECTION, FINANCIAL REGULATION, INDUSTRY-SPECIFIC RULES. NAME THE JURISDICTION.]

#### How does this scale? What breaks at 10x and 100x usage?

[SPECIFIC BOTTLENECKS. WHAT WE'D HAVE TO REBUILD.]

#### What are we choosing not to do, and why?

[EXPLICIT NON-GOALS WITH RATIONALE. PAIRS WITH THE PRD'S NON-GOALS SECTION.]

#### What would cause us to abandon this project?

<!-- Kill criteria. Concrete, observable. -->

[SPECIFIC SIGNAL — A METRIC TARGET MISSED, A COMPETITOR LAUNCH, A REGULATORY CHANGE — THAT WOULD MAKE US STOP.]

#### What does success look like 12 months after launch?

[QUANTITATIVE TARGETS THAT INFORM THE PRD'S SUCCESS METRICS.]

## Review Checklist

Use this checklist when reviewing a PR-FAQ artifact:

- [ ] Press release names a specific customer segment, not "users" or "teams"
- [ ] Press release reads as a real wire-service story — no marketing fluff
- [ ] Press release stays under ~350 words
- [ ] The Problem section uses the customer's words and names a specific failure mode with a number
- [ ] The Solution section describes the customer experience, not the implementation
- [ ] Customer quote describes an outcome the customer got, not features they used
- [ ] Availability names specific dates, prices, platforms, and regions
- [ ] External FAQ explicitly compares to existing alternatives
- [ ] External FAQ names who this is NOT for
- [ ] A FAQ explicitly lists what is out of scope for v1
- [ ] Internal FAQ surfaces at least one credible feasibility or technical risk
- [ ] Internal FAQ confronts unit economics or pricing plausibility
- [ ] Internal FAQ states explicit kill criteria
- [ ] Internal FAQ names experiments or validation steps required before commit
- [ ] No `[TBD]`, `[TODO]`, or `[NEEDS CLARIFICATION]` markers remain
- [ ] PR-FAQ is consistent with the governing Product Vision
``````

</details>

## Example

<details>
<summary>Show a worked example of this artifact</summary>

``````markdown
---
ddx:
  id: helix.pr-faq.example
---
# PR-FAQ: HELIX

> Example scenario: a working-backwards PR-FAQ written as if HELIX itself were launching today. Drawn from `docs/helix/00-discover/product-vision.md` and `docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md`. This is illustrative; the authoritative product description lives in those documents.

## Press Release

**FOR IMMEDIATE RELEASE — REMOTE — 2026-04-30**

### Headline

HELIX launches as an open-source supervisory autopilot for spec-driven AI software delivery.

### Subhead

HELIX runs on top of DDx and lets small software teams using AI agents move work from product intent to shipped code without becoming full-time agent dispatchers. It is available today as an open-source plugin and methodology repo.

### Summary

HELIX maintainers today released HELIX, a methodology layer and supervisory autopilot for AI-assisted software delivery. HELIX helps teams that already use AI coding agents stop hand-steering each step: it routes work across vision, requirements, design, tests, implementation, review, and metrics, and only stops when human judgment is actually needed. HELIX is available today on GitHub under an open-source license and runs on the DDx platform substrate.

### The Problem

Teams using AI coding agents repeatedly hit the same failure mode: the agent is technically capable, but the human is spending most of their day deciding what the agent should do next. Specs drift from code, the same review feedback gets re-discovered three sprints later, and a senior engineer ends up as a full-time prompt dispatcher instead of a decision-maker. In informal conversations across multiple teams, the recurring complaint is the same shape: "the agent works, but I'm tired of telling it what to work on."

### The Solution

HELIX provides a supervisory autopilot — `helix run` — that selects the highest-leverage next bounded action and advances it. When a feature spec is ambiguous, HELIX refines the spec before implementing. When implementation reveals a missing requirement, HELIX surfaces the artifact mismatch and reconciles it. When a test fails, HELIX fixes it; when a design question emerges, HELIX stops and asks. Operators steer through the tracker — creating beads, setting priorities, approving phase gates — while HELIX shapes workflow context and DDx drains execution-ready work through `ddx agent execute-loop`. The mental model is an autopilot you can grab the wheel from, not a command wrapper you must drive at every step.

### Quote from HELIX maintainers

> "HELIX exists because every team we know that has adopted AI coding agents has independently rediscovered the same problem: the agent isn't the bottleneck, the operator is. We built HELIX as a thin, supervisory layer that respects two ideas — that planning and execution are complementary strands that feed each other, and that the smallest sufficient next action is almost always the right one."

### How It Works

1. The team captures product intent in `docs/<project>/helix/` — vision, PRD, feature specs, design docs.
2. HELIX walks the artifact graph and writes machine-auditable beads to the DDx tracker.
3. `helix run` delegates execution to `ddx agent execute-loop`, which claims a ready bead, dispatches an agent, and lands or preserves the attempt with evidence.
4. HELIX interprets each cycle's outcome, injects review and alignment beads when warranted, and either continues or stops for human input.
5. The operator steers through the tracker; the artifact graph stays honest because every bead traces back to governing intent.

### Customer Quote

> "Before HELIX, I was spending most of my mornings babysitting an agent — re-stating what phase we were in, telling it which file to look at, redoing the same review feedback every other day. With HELIX I open the repo, look at what `helix run` did overnight, review the diffs, approve the gates, and make actual product calls. The first week I noticed I'd written more code review than prompts."
>
> — HELIX early-adopter operator, small product team

### Availability

HELIX is available today on GitHub under an open-source license. It is distributed as a DDx plugin (`.ddx/plugins/helix/`) bundling phase prompts, artifact templates, and concerns. HELIX requires DDx for tracker, agent execution, and graph indexing. Cost: free. Platforms: macOS and Linux. Onboarding path: clone the plugin, install via `ddx`, run `helix input`.

---

## FAQ

### External FAQs

#### How much does it cost?

HELIX is free and open-source. Operating costs come from the AI agent provider you choose (Anthropic API, OpenAI-compatible providers, local LM Studio / MLX) and from DDx itself, which is also open-source.

#### How is this different from working-backwards PR-FAQs, specification-driven development, or Cursor Rules?

Working-backwards is a *planning practice* — write the press release first. HELIX adopts that practice as one artifact among many but adds a durable execution lane that keeps the planning artifacts honest as code is written. Specification-driven development is the closest cousin; HELIX differs in that it is opinionated about the artifact graph (vision → PRD → specs → designs → tests → code) and ships the supervisory loop that keeps those layers reconciled. Cursor Rules and similar in-IDE conventions inject instructions into a single agent turn; HELIX maintains state across turns, sessions, and operators through the tracker and the artifact graph, so context survives turning the laptop off.

#### Who is HELIX NOT for?

HELIX is not for teams that want a single chat-only "build me X" experience without durable artifacts. It is not for teams that refuse to adopt DDx as the platform substrate — HELIX delegates execution mechanics to DDx by design and does not work standalone. It is not optimized for solo non-AI workflows; many of its mechanisms (tracker, supervisory loop, cross-model review) presume agent participation.

#### What's not in v1?

- Multi-project supervisory orchestration (HELIX runs per-repo today).
- A hosted control plane (HELIX is local-first, file-backed, git-tracked).
- A built-in VCS UI; HELIX uses your existing GitHub/GitLab.
- Non-Markdown artifact templates; everything is Markdown plus YAML frontmatter.

#### What platforms / regions / integrations are supported at launch?

macOS and Linux. Any agent harness DDx supports today: Claude (Anthropic API), OpenAI-compatible providers via OpenRouter, local LM Studio, MLX. GitHub and GitLab work via standard git remotes; no special integration is required.

#### When can I get it?

Today. The plugin and methodology repo are public on GitHub.

### Internal FAQs

#### What is the unit economics story?

HELIX is open-source and unmonetized. There are no per-customer unit economics. The sustainability question is maintainer time: HELIX is feasible only if the methodology layer remains thin enough that one to two maintainers can keep it healthy. Every feature that pulls workflow logic into a parallel substrate (e.g., re-implementing DDx graph primitives or execution mechanics) directly threatens that economy. CONTRACT-001 exists in part to keep maintenance costs bounded.

#### What is the riskiest technical assumption?

That the DDx/HELIX boundary is stable enough to delegate execution mechanics without HELIX needing escape hatches. Specifically, HELIX assumes `ddx agent execute-loop --once --json` returns a stable workflow-visible outcome surface (bead ID, status, base/result revisions, retry hints). If DDx changes that shape silently, every HELIX post-cycle path breaks. We mitigate by pinning the schema in CONTRACT-001 and adding HELIX-side integration tests that fail fast on drift.

#### What experiments must run before we commit?

(1) An end-to-end run of `helix run` against `ddx agent execute-loop --once` on a real project, validating that supervisory wrapping works without HELIX-side claim/close logic. (2) The principles-injection research (see `docs/helix/06-iterate/research-principles-injection-2026-04-05.md`) — does prompt injection actually change agent reasoning, and at what cost? (3) A queue-drift scenario: confirm that HELIX detects superseded beads at `helix check` time and prevents them from entering the DDx ready queue.

#### What is the smallest viable launch?

`helix input`, `helix run`, and a working artifact graph for a single project, with `helix check` for drift detection. Review/alignment beads, slider autonomy, and concerns/practices context digests can iterate post-launch.

#### Who else has to ship something for this to work?

DDx must hold its end of CONTRACT-001 — graph primitives, `execute-loop` semantics, evidence capture, runtime metrics. The agent harness providers (Anthropic, OpenAI-compatible vendors, LM Studio, MLX) must continue to expose the surfaces DDx wraps. Neither dependency is at material risk today, but the boundary contract makes the dependency explicit so a future drift is debuggable rather than mysterious.

#### What regulatory or legal exposure does this create?

Minimal. HELIX is a developer tool that orchestrates local agents and writes Markdown to the operator's repo. It does not move money, store customer data, or operate as a service. The most relevant exposure is open-source licensing of the plugin's `.ddx/plugins/helix/workflows/` content; this is handled at the repo level. Operators using HELIX with cloud agent providers inherit those providers' data-handling terms — HELIX does not change them.

#### How does this scale? What breaks at 10x and 100x usage?

Per-project usage is bounded by the agent provider, not by HELIX. The methodology scales operator attention, not throughput. The substrate scaling questions belong to DDx (tracker size, graph index size, execution evidence storage), not to HELIX. The HELIX-side scaling concern is artifact-graph navigability — if a project accumulates hundreds of feature specs, the supervisory loop's context-resolution time grows. We have not yet measured this at 10x scale and have flagged it as a future research direction.

#### What are we choosing not to do, and why?

We are not building a hosted control plane — HELIX is local-first by design. We are not absorbing DDx-owned execution mechanics — that is the explicit boundary in CONTRACT-001. We are not building a chat-only entrypoint that skips the artifact graph — the graph is the durable contract, not optional context. We are not adopting a generic "do everything" agent posture — least-power escalation is principle 3, not an aspiration.

#### What would cause us to abandon HELIX?

(1) If DDx absorbs HELIX workflow semantics — autonomy, escalation, prompt strategy — there is no methodology layer left to maintain. (2) If maintainer time required to track agent-tooling churn exceeds what one to two part-time maintainers can sustain, HELIX collapses into stale prompts. (3) If a credible alternative (e.g., a built-in agent IDE feature set) makes the supervisory loop redundant, the unique value evaporates.

#### What does success look like 12 months after launch?

A team adopting HELIX should report that they spend materially less time deciding what the agent should do next; that specs, designs, tests, and code remain mutually consistent across iterations; and that escalations occur at real product-judgment boundaries rather than because the workflow contract is underspecified. These targets seed the PRD's success metrics.
``````

</details>
