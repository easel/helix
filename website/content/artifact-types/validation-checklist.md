---
title: "Validation Checklist"
slug: validation-checklist
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/validation-checklist
---

## What it is

Comprehensive checklist to validate Frame phase completeness, quality,
and readiness for Design phase. Ensures all deliverables meet standards
and stakeholders are aligned.

## Activity

**[Frame](/reference/glossary/activities/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/validation-checklist.md`

## Relationships

### Requires (upstream)

- All Frame artifacts
- Exit gates criteria

### Enables (downstream)

_None._

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Validation Checklist Generation Prompt
Create the checklist that decides whether Frame is ready to move forward.

## Focus
- Check only the gates that matter: completeness, consistency, traceability, and stakeholder approval.
- Keep the pass/fail criteria concrete.
- Avoid duplicating the content already covered by source artifacts.

## Completion Criteria
- The checklist is short and actionable.
- Blocking gaps are easy to spot.
- Cross-references are verified.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Frame Phase Validation Checklist

**Status**: [ ] Not Started | [ ] In Progress | [ ] Complete
**Validated By**: [Name]
**Date**: [Date]
**Result**: [ ] Pass | [ ] Conditional Pass | [ ] Fail

## Go / No-Go Gates
- [ ] Problem, goals, and success metrics are clear enough to judge outcomes.
- [ ] P0 scope is identified, prioritized, and separated from non-goals.
- [ ] Features and stories are traceable through IDs and links.
- [ ] Acceptance criteria are testable.
- [ ] Major risks, dependencies, and external constraints are explicit.
- [ ] Frame artifacts do not contradict each other.
- [ ] Required stakeholders have reviewed the plan.

## Result
- [ ] **PASS**: Ready for Design phase
- [ ] **CONDITIONAL PASS**: Proceed with noted conditions
- [ ] **FAIL**: Address blocking issues first

**Conditions/Notes**:
[Assessment and any conditions]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
