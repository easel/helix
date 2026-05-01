---
dun:
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
