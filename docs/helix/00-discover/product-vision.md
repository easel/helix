# Product Vision

## Mission Statement

HELIX helps teams and agents turn product intent into shipped software through
a supervised autopilot that continuously advances the weakest ready layer of
the development stack until human input is actually needed.

HELIX combines collaborative planning with bounded autonomous execution so
human attention stays focused on judgment, tradeoffs, and approvals rather
than routine orchestration.

## Positioning

For software teams using AI agents for day-to-day development who lose too
much operator effort deciding what the agent should do next and keeping
planning artifacts aligned with implementation, HELIX is a supervisory
autopilot that continuously advances work across specs, designs, tests,
implementation, review, and metrics until human judgment is actually needed.
Unlike ad hoc prompting with manual agent steering, HELIX maintains a durable
control loop where requirements govern code, the tracker steers agents, and
every action traces back to governing intent.

## Vision

HELIX becomes the default control system for spec-driven agent software
delivery: a workflow where requirements, design, test, implementation, review,
and metric refinement advance with minimal human intervention, and where
multi-agent and single-agent teams alike adopt HELIX as the safe default for
carrying software from intent to production.

**North Star**: A team should be able to express intent once, collaborate where judgment matters, and let HELIX carry the rest of the workflow forward safely.

## User Experience

A developer opens their terminal with a backlog of work tracked in the repo.
They run `helix run`. HELIX picks the highest-leverage ready issue, dispatches
an agent to implement it, verifies the result against acceptance criteria, and
commits. When it finishes, it picks the next one. The developer checks in
periodically — reviewing diffs, approving gates, making product calls when
HELIX surfaces a genuine ambiguity. When they want to work on something
directly, they do — editing a spec, writing a test, closing an issue — and
HELIX picks up the rest. The mental model is a autopilot you can always grab
the wheel from.

## Target Market

| Attribute | Description |
|-----------|-------------|
| Who | Small to medium software teams using AI agents for day-to-day development |
| Pain | Too much operator effort deciding what the agent should do next and keeping planning artifacts aligned with implementation |
| Current Solution | Informal prompting, scattered TODOs, weak issue hygiene, and manual agent steering |
| Why They Switch | As codebases grow, ad hoc prompting breaks down — specs drift from code, agents loop without progress, and the human becomes a full-time dispatcher instead of a decision-maker |

## Key Value Propositions

| Value Proposition | Customer Benefit |
|-------------------|------------------|
| Supervisory autopilot | HELIX keeps work moving across specs, designs, tests, implementation, review, and metrics until human judgment is actually needed |
| Least-power execution | HELIX chooses the smallest sufficient next action instead of overreaching, reducing unnecessary churn and speculative changes |
| Authority-ordered reconciliation | When artifacts disagree, HELIX resolves the conflict by escalating to the governing source instead of guessing from code alone |
| Tracker as steering wheel | The tracker is the primary human interface for steering agents. Users create issues, set priorities, approve gates, and reject work through tracker state; agents read it and execute |
| Cross-model quality | Critical artifacts are reviewed by alternating AI models, catching blind spots that self-review misses |
| Interactive intervention points | Users can step into any layer of the workflow directly without losing the benefits of autopilot orchestration |

## Product Principles

1. **Autopilot by default**
   `helix run` is HELIX's supervisory autopilot. It continuously selects and
   executes the highest-leverage next bounded action that does not require
   human input.

2. **Human intervention by exception**
   HELIX should escalate only when ambiguity, missing authority, tradeoffs, or
   product judgment block safe forward progress. When it stops, it should tell
   the user exactly what decision is needed and why.

3. **Least powerful next action**
   HELIX should restore progress with the smallest sufficient action: refine a
   spec before redesigning a system, sharpen issues before implementing, and
   reconcile artifacts before inventing new ones.

4. **Authority before implementation**
   Requirements, designs, tests, and plans govern code. Implementation is
   evidence of current behavior, not the source of truth for what should exist.

5. **Tracker as the steering wheel**
   The tracker is the primary interface between humans and agents. Users steer
   by creating issues, setting priorities, approving phase gates, and rejecting
   work — all through tracker state. Agents read tracker state and execute.
   The mental model is: `User <-> Tracker <-> helix run (background)`.

6. **Do hard things**
   Agents should attack problems, not defer them. If the toolchain doesn't
   compile, try to fix it. If a spec is ambiguous, make the best-effort
   interpretation and document the reasoning. Only genuinely contradictory
   governing artifacts or intractable technical problems after escalating
   effort should result in stopping.

7. **Cross-model verification**
   Critical artifacts and implementations should be reviewed by a different AI
   model than the one that produced them. Different models have different blind
   spots; alternating reviewers catches errors that self-review misses.

8. **Interactive entry at any layer**
   The user should be able to work directly on vision, PRD, specs, tests,
   issues, implementation, review, or metrics while still benefiting from
   HELIX's overall control system.

9. **Continuous useful work**
   The system should always be making forward progress. When one issue is
   blocked, move to the next. When an epic's children are done, review the
   epic before moving on. Absorb small adjacent work instead of creating
   ticket churn. The goal is net progress, not activity.

## Success Definition

| Metric | Target |
|--------|--------|
| Autonomous forward progress | From an established vision and PRD, `helix run` advances the repo through downstream refinement and bounded execution until input is required |
| Reduced orchestration overhead | Users spend materially less time telling the agent what phase to enter next |
| Artifact alignment | Specs, issues, tests, implementation, and follow-on work remain traceable and mutually consistent after iterative changes |
| Safe escalation | HELIX asks for user input primarily at real judgment boundaries, not because the workflow contract is underspecified |

## Why Now

AI coding tools are already useful, but teams still lack a reliable supervisory
layer that keeps complex software work coherent over time. The repo already
contains the workflow method, tracker, CLI, and skill surfaces needed to make
the control loop explicit — the gap is connecting them into a single autopilot
that humans can trust and steer.

## Explicit Non-Goals

- HELIX is not a generic "do everything" agent that replaces product judgment.
- HELIX is not an unbounded autonomous coding loop.
- HELIX is not a chat-only prompt library disconnected from durable tracker
  state.
- HELIX should not force users to remain in autopilot mode when they want to
  intervene directly in a specific workflow layer.
