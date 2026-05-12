---
title: "Stakeholder Map"
linkTitle: "Stakeholder Map"
slug: stakeholder-map
phase: "Frame"
artifactRole: "supporting"
weight: 23
generated: true
---

## Purpose

Comprehensive identification and analysis of all project stakeholders,
their influence, interests, and engagement strategies. Includes RACI
matrix for clear accountability.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/stakeholder-map.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/frame/prd/">PRD</a><br><a href="/artifact-types/frame/risk-register/">Risk Register</a><br>Communication Plan</td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Stakeholder Map Generation Prompt
Map the stakeholders who matter most to the project and how to engage them.

## Focus
- Identify primary and secondary stakeholders.
- Keep influence, interest, and communication needs clear.
- Note escalation paths without overexplaining them.

## Completion Criteria
- Stakeholders are named and categorized.
- Communication is actionable.
- The map stays compact.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Stakeholder Map

**Status**: [Draft | Review | Approved]
**Last Updated**: [Date]

## Primary Stakeholders (High Influence, High Interest)

### [Stakeholder Name/Role]
- **Role**: [Position/title]
- **Interest**: [What they care about]
- **Influence**: [Power to affect project]
- **Concerns**: [Main worries]
- **Success Criteria**: [What success looks like to them]
- **Communication**: [Preferred engagement method]

## Secondary Stakeholders (Variable Influence/Interest)

### [Stakeholder Name/Role]
- **Role**:
- **Interest**:
- **Influence**:
- **Engagement Level**: [Inform | Consult | Collaborate]

## RACI Matrix

| Activity/Decision | [Stakeholder 1] | [Stakeholder 2] | [Stakeholder 3] |
|-------------------|-----------------|-----------------|-----------------|
| Project Vision | A | R | C |
| Requirements | A | R | C |
| Technical Decisions | I | C | R/A |
| Budget Approval | A | C | I |
| Release Decision | A | R | C |

**R** = Responsible | **A** = Accountable | **C** = Consulted | **I** = Informed

## Power/Interest Grid

```
High Power  | Keep Satisfied      | Manage Closely
            | - [Stakeholder]     | - [Stakeholder]
            |---------------------|-------------------
Low Power   | Monitor             | Keep Informed
            | - [Stakeholder]     | - [Stakeholder]
            Low Interest          High Interest
```

## Communication Plan

| Stakeholder Group | Channel | Frequency | Content | Owner |
|-------------------|---------|-----------|---------|-------|
| [Group] | [Channel] | [Frequency] | [What] | [Who] |

### Escalation Path
1. [Team Lead] -&gt; [PM] -&gt; [Sponsor] -&gt; [Executive]</code></pre></details></td></tr>
</tbody>
</table>
