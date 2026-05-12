---
title: "Project Principles"
linkTitle: "Project Principles"
slug: principles
phase: "Frame"
artifactRole: "core"
weight: 11
generated: true
---

## Purpose

Cross-cutting design principles that guide judgment calls across all HELIX
phases. Not workflow rules or process enforcement — these are lenses applied
when choosing between two valid options.

Two-layer model:
  Layer 1 (HELIX defaults): .ddx/plugins/helix/workflows/principles.md — sensible defaults
  Layer 2 (Project):        docs/helix/01-frame/principles.md — project-owned

If the project file exists, it is the sole active source.
If it does not exist, HELIX defaults are used.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/principles.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Principles Generation Prompt

Help the user create a project principles document that guides judgment calls
across all HELIX phases.

## Bootstrap Flow

1. **Check for existing principles**: If `docs/helix/01-frame/principles.md`
   already exists, load it and offer to refine rather than replace.

2. **Load HELIX defaults**: Read `.ddx/plugins/helix/workflows/principles.md` for the baseline
   design principles. Present them to the user as the starting point.

3. **Discovery conversation**: Ask the user three questions to surface
   project-specific values:
   - &quot;What does your project value most?&quot;
   - &quot;What trade-offs do you consistently lean toward?&quot;
   - &quot;What past mistakes should these principles help you avoid?&quot;

4. **Synthesize**: Combine the user&#x27;s input with the HELIX defaults to
   produce a project principles document. The user may keep, modify, or
   remove any HELIX default. Removed defaults stay removed — HELIX does
   not re-add them.

5. **Tension detection**: For each pair of principles in the result, evaluate
   whether they could pull in opposite directions for a realistic decision.
   Flag any unresolved tensions and ask the user for a resolution strategy.

6. **Write the file**: Output to `docs/helix/01-frame/principles.md` using
   the template from `template.md`. The user owns the file from this point.

## Principles Quality Criteria

Each principle must be:

- **Decision-changing**: It must change at least one real choice. If removing
  the principle would not change any decision, it is not a principle.
- **Actionable**: An agent or developer reading it should know which option
  to prefer in a concrete scenario.
- **Concise**: One sentence for the principle, one sentence for the
  rationale. If it needs a paragraph, it may be a policy, not a principle.

Reject or flag:

- Workflow rules (belong in enforcers or ratchets, not principles)
- Aspirational statements that do not change decisions
- Principles so broad they apply to every project (&quot;write good code&quot;)

## Size Thresholds

Monitor the number of principles and provide guidance:

- **At 8 principles**: &quot;Consider whether all of these are decision-changing.
  Can any be consolidated?&quot;
- **At 12 principles**: &quot;The Agile Manifesto has 12 and most teams can name
  maybe 4-5. Consider consolidating.&quot;
- **At 15+ principles**: &quot;This has grown beyond a decision framework into a
  wish list. Strongly recommend pruning to the principles that actually
  change decisions.&quot;

## Tension Detection

When evaluating a set of principles for tensions:

1. Parse each principle into a short semantic summary.
2. For each pair, ask: &quot;Is there a realistic decision where these two
   principles pull in opposite directions?&quot;
3. For each detected tension, check whether the tension resolution section
   already addresses it.
4. Flag unresolved tensions with a concrete example scenario.
5. Accept the user&#x27;s resolution strategy and add it to the tension
   resolution section of the document.

## Completion Criteria

- The principles document contains only decision-changing principles.
- No workflow rules are included (those belong in enforcers/ratchets).
- All identified tensions have resolution strategies.
- The document is within the size ceiling (ideally 5-8 principles).
- The user has reviewed and approved the final set.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Project Principles

These principles guide judgment calls across all HELIX phases. They are not
workflow rules or process enforcement — they are lenses applied when choosing
between two valid options.

This document was bootstrapped from HELIX defaults. You own it now — add,
modify, reorder, or remove any principle. The only constraint: principles
cannot negate HELIX mechanics (artifact hierarchy, phase gates, tracker
semantics).

## Principles

1. **Design for change** — Prefer structures that are easy to modify over
   structures that are easy to describe today.

2. **Design for simplicity** — Start with the minimal viable approach.
   Additional complexity requires justification.

3. **Validate your work** — Every change should be verified through the most
   appropriate means available (tests, type checks, manual verification).

4. **Make intent explicit** — Code, configuration, and documentation should
   make the *why* visible, not just the *what*.

5. **Prefer reversible decisions** — When uncertain, choose the option that
   is easiest to undo or change later.

## Tension Resolution

When principles pull in opposite directions, document the resolution strategy
here. Each entry should name the two principles, describe when they conflict,
and state how to decide.

*No tensions identified yet. As you add project-specific principles, use this
section to resolve any conflicts with existing principles.*</code></pre></details></td></tr>
</tbody>
</table>
