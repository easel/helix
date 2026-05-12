---
title: "User Stories"
linkTitle: "User Stories"
slug: user-stories
phase: "Frame"
artifactRole: "core"
weight: 14
generated: true
---

## Purpose

User stories are **governing design artifacts**, not throwaway tickets. Each
story defines a complete vertical slice of the application that is
independently implementable and testable. Tracker issues reference stories;
stories don't reference tracker issues. Stories are more stable than the
implementation beads that fulfill them.

## Authoring guidance

- **One story, one vertical slice** — a story should trace a complete path
  from user action to outcome. If it can't be demonstrated end-to-end, it's
  not a story yet.
- **Stable reference** — stories will be referenced by multiple tracker issues
  across design, implementation, and testing. Write them to last.
- **Implementer-sufficient** — an implementer reading only this story and the
  parent feature spec should be able to build it without asking clarifying
  questions.
- **Test-first friendly** — acceptance criteria and test scenarios should be
  concrete enough to write tests before writing code.

<details>
<summary>Quality checklist from the prompt</summary>

After drafting, verify every item. If any blocking check fails, revise before
committing.

### Blocking

- [ ] Story names a specific persona from the PRD (not a generic role)
- [ ] "I want" describes a user action, not a system behavior
- [ ] "So that" names a measurable outcome, not a tautology
- [ ] Walkthrough traces a complete path from trigger to outcome
- [ ] Every acceptance criterion is independently testable (one Given/When/Then)
- [ ] Test scenarios include concrete values, not placeholders
- [ ] Story links to parent feature spec by ID

### Warning

- [ ] Context would be missed if removed (not generic filler)
- [ ] At least one edge case is documented
- [ ] Test scenarios cover both happy path and at least one edge case
- [ ] Out of scope excludes something plausible
- [ ] No compound acceptance criteria (split into separate items)

</details>

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/user-stories/</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/solution-design/">Solution Design</a><br>Test Cases<br>Tracker Issues</td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># User Story Generation Prompt

Create standalone user stories that serve as stable design artifacts — vertical
slices referenced throughout design, implementation, and testing.

## Storage Location

Store at: `docs/helix/01-frame/user-stories/US-NNN-&lt;slug&gt;.md` (one file per story)

## Purpose

User stories are **governing design artifacts**, not throwaway tickets. Each
story defines a complete vertical slice of the application that is
independently implementable and testable. Tracker issues reference stories;
stories don&#x27;t reference tracker issues. Stories are more stable than the
implementation beads that fulfill them.

## Key Principles

- **One story, one vertical slice** — a story should trace a complete path
  from user action to outcome. If it can&#x27;t be demonstrated end-to-end, it&#x27;s
  not a story yet.
- **Stable reference** — stories will be referenced by multiple tracker issues
  across design, implementation, and testing. Write them to last.
- **Implementer-sufficient** — an implementer reading only this story and the
  parent feature spec should be able to build it without asking clarifying
  questions.
- **Test-first friendly** — acceptance criteria and test scenarios should be
  concrete enough to write tests before writing code.

## Section-by-Section Guidance

### Story (As a / I want / So that)
The &quot;As a&quot; must name a specific persona from the PRD, not a generic role.
The &quot;I want&quot; must describe what the user does, not what the system does
internally. The &quot;So that&quot; must name a measurable outcome or business value —
&quot;so that I can use the feature&quot; is circular.

### Context
This is the background an implementer needs to make judgment calls. Why does
this story exist? What&#x27;s the user&#x27;s situation? What pain are they hitting?
2-4 sentences, not a paragraph of filler. Test: would removing this section
force the implementer to ask a question? If not, it&#x27;s too generic.

### Walkthrough
A step-by-step journey through the vertical slice. Present tense, concrete
actions. This is not a flowchart — it&#x27;s one specific path (the happy path)
from trigger to outcome. Branching and error cases go in Edge Cases.

Test: could a QA engineer use this walkthrough as a manual test script?

### Acceptance Criteria
Given/When/Then format. Each criterion must be independently testable — one
clear precondition, one action, one observable outcome. Avoid compound
criteria (&quot;Given A and B and C, when D, then E and F and G&quot;). Split those
into separate criteria.

### Edge Cases
What happens when the user does something unexpected, inputs are invalid,
or the system is in an unusual state? Each edge case names the condition and
the expected behavior. Don&#x27;t just list failure modes — specify what the system
should do.

### Test Scenarios
Concrete input/output pairs. An implementer should be able to copy these into
a test file with minimal modification. Include the happy path and at least one
edge case from the section above. Name specific values, not placeholders.

### Dependencies
Name other stories this one depends on (by ID), the parent feature spec,
and any external systems or APIs. If another story must be done first, say so.

### Out of Scope
What this story explicitly does not cover. Each item should exclude something
an implementer might reasonably try to include. This prevents scope creep
during implementation.

## Quality Checklist

After drafting, verify every item. If any blocking check fails, revise before
committing.

### Blocking

- [ ] Story names a specific persona from the PRD (not a generic role)
- [ ] &quot;I want&quot; describes a user action, not a system behavior
- [ ] &quot;So that&quot; names a measurable outcome, not a tautology
- [ ] Walkthrough traces a complete path from trigger to outcome
- [ ] Every acceptance criterion is independently testable (one Given/When/Then)
- [ ] Test scenarios include concrete values, not placeholders
- [ ] Story links to parent feature spec by ID

### Warning

- [ ] Context would be missed if removed (not generic filler)
- [ ] At least one edge case is documented
- [ ] Test scenarios cover both happy path and at least one edge case
- [ ] Out of scope excludes something plausible
- [ ] No compound acceptance criteria (split into separate items)</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# US-XXX: [Story Title]

**Feature**: [FEAT-XXX — Feature Name]
**Priority**: [P0 | P1 | P2]
**Status**: [Draft | Review | Approved]

## Story

**As a** [specific user type from PRD personas]
**I want** [specific functionality — what the user does, not what the system does]
**So that** [measurable business value or user outcome]

## Context

[Why this story matters. What&#x27;s the user&#x27;s situation before this works? What
problem are they hitting? This should be 2-4 sentences that give an
implementer enough background to make judgment calls without asking.]

## Walkthrough

[Step-by-step description of the user&#x27;s journey through this slice. Write in
present tense. Name concrete actions and system responses. This is the
vertical slice — it should cover one complete path from trigger to outcome.]

1. User [action]
2. System [response]
3. User [action]
4. System [response — the outcome]

## Acceptance Criteria

[Each criterion must be testable. Use Given/When/Then format. An implementer
should be able to write a passing test from each criterion alone.]

- [ ] Given [specific precondition], when [specific action], then [observable outcome]
- [ ] Given [specific precondition], when [specific action], then [observable outcome]

## Edge Cases

[What happens when things go wrong or inputs are unexpected? Each edge case
should name the condition and the expected system behavior.]

- **[Condition]**: [Expected behavior]
- **[Condition]**: [Expected behavior]

## Test Scenarios

[Concrete input/output pairs for the acceptance criteria. An implementer
should be able to copy these into a test file.]

| Scenario | Input / State | Action | Expected Result |
|----------|---------------|--------|-----------------|
| Happy path | [specific state] | [specific action] | [specific result] |
| [Edge case] | [specific state] | [specific action] | [specific result] |

## Dependencies

- **Stories**: [US-XXX if this story depends on another being done first]
- **Feature Spec**: [FEAT-XXX]
- **External**: [APIs, services, or data this story requires]

## Out of Scope

[What this story explicitly does not cover, to prevent scope creep during
implementation.]</code></pre></details></td></tr>
</tbody>
</table>
