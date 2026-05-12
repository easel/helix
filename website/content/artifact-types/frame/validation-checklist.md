---
title: "Validation Checklist"
linkTitle: "Validation Checklist"
slug: validation-checklist
phase: "Frame"
artifactRole: "supporting"
weight: 25
generated: true
---

## Purpose

Comprehensive checklist to validate Frame phase completeness, quality,
and readiness for Design phase. Ensures all deliverables meet standards
and stakeholders are aligned.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/validation-checklist.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Validation Checklist Generation Prompt
Create the checklist that decides whether Frame is ready to move forward.

## Focus
- Check only the gates that matter: completeness, consistency, traceability, and stakeholder approval.
- Keep the pass/fail criteria concrete.
- Avoid duplicating the content already covered by source artifacts.

## Completion Criteria
- The checklist is short and actionable.
- Blocking gaps are easy to spot.
- Cross-references are verified.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
[Assessment and any conditions]</code></pre></details></td></tr>
</tbody>
</table>
