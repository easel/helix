# HELIX + DDx — Pitch Narrative

Source of truth for how we talk about HELIX and DDx. The microsite, the
README, the slide decks, and the demo voiceovers all draw from this
document. If any of them tells the story differently, this one is
authoritative.

Captured from a working sales call on 2026-05-13 with Stephen Sklarew (DDx
Helix pitch), Vince DiMascio (prospect), Erik LaBianca (HELIX/DDx author),
and Tim Oates. Refined for written delivery.

## One-line positioning

> **Day one, vibe-coded code ships. Day two, when you refactor, it dies.
> HELIX and DDx are the document discipline and the runtime that get you
> from day one to day n without losing the thread.**

## The three-line elevator pitch

> AI agents are now writing production code. Two problems show up
> immediately: the orchestration of multiple agents collapses under its
> own weight, and the code itself becomes unmaintainable because no one —
> human or AI — has a specification to defend it against. **HELIX is a
> document discipline that gives the agent context it can trust; DDx is
> the runtime that turns that context into bounded, evidence-backed
> work.** The result is software you can still refactor on day two.

## The pain arc (use in long-form conversation)

The pitch arc that actually lands, in order:

1. **The copy-paste activity.** You sat there with an LLM, copying code in
   and pasting code out. Then you got tired of being the copy-paste
   b****. Claude Code and Codex solved that.
2. **The orchestration sprawl.** Then you had two windows. Then four.
   They started stepping on each other — git conflicts, contradicting
   each other's work. You started writing files for them to communicate.
3. **The vibe-code collapse.** If you vibe-coded long enough, you ended
   up with a million lines of code that no one understands, including the
   LLM. There's no specification to defend the code against.
4. **The insight.** You can't *not* use these tools — they're too
   powerful. But you also can't ship without structure. So you need
   document discipline plus a runtime that respects it.

> *"And the other thing that happens is if you sit there and you vibe
> code long enough, eventually you'll have a million lines of code that
> no one understands. The LLM included."*

## The Day-1-vs-Day-2 frame (anchor)

This is the strongest positioning sentence in the pitch. Use everywhere.

> **Day one, you can vibe code real well. Day two, when you have to go
> in and refactor and clean it up, you need structure — because the LLM
> will start going off into corners and stop sticking to the task.**

HELIX and DDx are not what gets you to day one. They're what makes day n
survivable.

## The Karpathy slider (visual anchor)

Reference: Andrej Karpathy's "human-agentic slider." Sometimes you want
the agent fully autonomous. Sometimes you want every line by hand. Most
real work lives in the middle.

> **HELIX gives you the lever to move along the slider. With aligned
> artifacts, you can one-shot a prompt and let it propagate through the
> document stack — or you can painstakingly walk every section by hand.
> Same documents, different autonomy.**

This is the UX promise: artifacts as the substrate that makes the slider
work.

## What HELIX is (and isn't)

**Is:**
- A methodology for AI-assisted software development.
- A catalog of ~32 artifact types — vision, PRD, principles, feature
  specs, technical designs, test plans, ADRs, alignment reviews,
  implementation plans — with templates, prompts, and quality criteria.
- A single skill the agent invokes to keep those artifacts coherent.
- Portable: runs on Claude Code, Codex, Databricks Genie, Cursor, or any
  runtime that reads and writes markdown.

**Isn't:**
- A CLI you install.
- A tracker. (DDx provides that.)
- A platform you join. It's content you adopt.

> *"They never invoked a HELIX command, because there isn't one. They
> invoked their agent, and the agent invoked HELIX's skill."*

## What DDx is (and isn't)

**Is:**
- The reference runtime for HELIX-governed work.
- Manages plugins, artifacts, the document graph, and an opinionated
  bead tracker (better Jira-for-agents than Steve Yegge's Gas Town beads,
  which had the right idea but unstable implementation).
- Ships **FZO**, a routing agent that automatically picks the optimal
  provider for each task — balancing your Claude/Codex subscriptions
  today, running on local GPUs tomorrow.
- Owns the execution loop: git worktrees, deterministic acceptance
  criteria, cross-model adversarial review, evidence capture.

**Isn't:**
- The methodology. HELIX is the methodology.
- Lock-in. You can hand a HELIX-governed project to a different runtime
  and the artifacts come with you.

## The token-economics differentiator

Most "AI dev tools" today are token-max competitions: whoever burns more
GPU wins. This is a bad bet.

- Demand for tokens is going to outpace the supply curve for years.
- Power is the real constraint. Data centers are now measured in
  gigawatts; new transmission lines are being planted next to people's
  houses to feed them.
- "We're gonna leaderboard who spends the most tokens" is a really dumb
  idea. All you have to do is put two wires together and you can burn
  infinite power.

**FZO is DDx's bet on the other direction**: route every task to the
right model at the right cost, mix local + hosted inference, use the
cheapest model that can do the job. The same loop runs on a $20/month
Claude subscription, on your $200 Max plan, or on the GPUs in your
basement.

## The proof point: healthcare claims pipeline

A mid-size US healthcare provider had failed several attempts to
rewrite their claims-processing pipelines. They came to us against a
six-week deadline. Stephen and Erik took it on with DDx/Helix in
iteration two or three of the tooling — messy, but the principles were
in place.

**What we did:**
- Overengineered a fully declarative YAML pipeline covering ingest,
  dedup, enrichment, validation, candidacy, survivorship, reporting.
- Used Claude to populate the YAML specifications directly from the
  semi-structured Excel sheets the payers sent us.
- Delivered a working pipeline on day one — having never seen the
  production data.

**The validation:**
- Six months later, the product is still functional.
- It survived its first refactor.
- We're now extending it to other pipelines at a rate the rest of the
  company is, in the team's words, "boggled" by.

The lever isn't speed-to-v1 (lots of tools do that). The lever is the
ability to *react to change* at v2, v3, v4 without losing coherence.

## The exit ramp (buyer insurance)

The single most important sentence for risk-averse buyers:

> **At any time, you can pull the LLM out entirely.**

Because HELIX-governed projects are anchored in human-authored
specifications, anything generated against them is auditable, reviewable,
and replaceable. There is no "I can't read this code anymore" failure
mode. The artifacts are the contract; the code is the implementation.

## The "wonder" moment (close)

Stephen built **Liquid Marble** — a three-tier data platform spanning 45
sources across fisheries and geology in Washington, Oregon, and Utah,
feeding three user-facing apps (citizen-scientist dashboard, fly-fishing
trip-quality predictor, rockhound paleontology trip planner). All in
production on GCP with auto-generated Terraform. A month, off the side of
his desk.

> *"I couldn't have imagined building three apps sitting on top of a
> three-tier data warehouse myself."*

This is what the leverage actually feels like, once the discipline is in
place.

## Where to start

For a new team, the adoption path is:

1. **Install the skill.** `ddx install helix` puts the artifact catalog
   and alignment skill into your agent's reach.
2. **Frame the brief.** Author vision → PRD → concerns → first feature
   spec from the templates. The agent guides the interview.
3. **Check alignment.** As you make changes, run the alignment skill.
   It walks the artifact graph and reports drift.
4. **Plan + execute.** When you're ready to ship code, let DDx
   decompose the plan into beads and execute them with FZO-routed
   models.

The whole stack is incremental. You can stop at step 2 if you only
wanted the discipline; you can stop at step 3 if your runtime is
something other than DDx; you only get the full pipeline if you opt in.

## Audience map — which beats land for which reader

| Reader | Beats that land |
|--------|-----------------|
| Engineering IC | Pain arc, Day-1-vs-Day-2, slider, exit ramp |
| Tech lead / EM | Slider, what-HELIX-is, proof point, exit ramp |
| CTO / VP Eng | Proof point, token-economics, exit ramp, where to start |
| Sales / GTM | One-liner, wonder moment, proof point |
| Investor | Token-economics, FZO, proof point, where-to-start |
| Skeptic / regulated-industry buyer | Exit ramp, proof point, what-HELIX-isn't |

## Voice and tone

- **Plain.** No marketing language. The pitch works because it reads
  like a colleague explaining what hurt them, not a brochure.
- **Specific.** Use real numbers, real timelines, real failure modes.
  "Six weeks", "45 data sources", "200-foot transmission towers".
- **Self-aware.** Acknowledge that some of this is in flux — FZO is
  still maturing, the slider isn't fully built out, the pricing model is
  shifting under everyone's feet. Earn trust by admitting it.

## What this artifact governs

The microsite, the README, the demo session-record narrations
(`docs/demos/*/session.jsonl`), the slide deck, the public talks, and
any future GTM material. If a downstream surface contradicts this doc,
update this doc first (with a justification), then propagate.
