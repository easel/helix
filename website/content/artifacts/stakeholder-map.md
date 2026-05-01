---
title: "Stakeholder Map"
slug: stakeholder-map
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/stakeholder-map
---

## What it is

Comprehensive identification and analysis of all project stakeholders,
their influence, interests, and engagement strategies. Includes RACI
matrix for clear accountability.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/stakeholder-map.md`

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

_None._

### Informs

- [Prd](../prd/)
- [Risk Register](../risk-register/)
- Communication Plan

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Stakeholder Map Generation Prompt
Map the stakeholders who matter most to the project and how to engage them.

## Focus
- Identify primary and secondary stakeholders.
- Keep influence, interest, and communication needs clear.
- Note escalation paths without overexplaining them.

## Completion Criteria
- Stakeholders are named and categorized.
- Communication is actionable.
- The map stays compact.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
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
1. [Team Lead] -> [PM] -> [Sponsor] -> [Executive]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
