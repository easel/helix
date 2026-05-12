---
title: "Compliance Requirements"
slug: compliance-requirements
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/compliance-requirements
---

## What it is

Comprehensive regulatory and compliance requirements analysis.
Identifies applicable regulations, maps requirements to implementation
controls, and defines a compliance validation plan.

## Activity

**[Frame](/reference/glossary/activities/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/compliance-requirements.md`

## Relationships

### Requires (upstream)

- [Product Requirements Document](../prd/)
- [Security Requirements](../security-requirements/)
- [Stakeholder Map](../stakeholder-map/) *(optional)*

### Enables (downstream)

_None._

### Informs

- [Solution Design](../solution-design/)

### Referenced by

- [Test Plan](../test-plan/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Compliance Requirements Analysis Prompt
Document the compliance obligations for this project in the local template.

## Focus
- Identify only the regulations and standards that actually apply to this system.
- Map each obligation to its source, affected scope, concrete controls, owners, and timing.
- Keep the result concise and implementation-relevant.

## Completion Criteria
- Applicable requirements are identified.
- Controls, risks, owners, and deadlines are explicit.
- No generic filler is added.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Compliance Requirements

**Project**: [Project Name]
**Compliance Risk Level**: [Critical/High/Medium/Low]
**Date**: [Creation Date]

## Executive Summary

**Applicable Regulations**: [List of regulations that apply]
**Compliance Scope**: [What aspects of the system must comply]
**Key Requirements**: [Top 3-5 highest-impact requirements]

## Applicable Regulations

For each applicable regulation, document:

### [Regulation Name]
- **Jurisdiction**: [Where it applies]
- **Applicability**: [Why it applies to this project]
- **Key Requirements**: [Summary of main requirements]
- **Penalties**: [Potential fines/sanctions]
- **Timeline**: [Any specific deadlines]

### Industry Standards

#### [Standard Name]
- **Scope**: [What aspects are covered]
- **Certification Required**: [Yes/No]
- **Key Controls**: [Summary of main controls]

## Compliance Requirements Matrix

For each regulation, create a requirements table:

| Requirement | Reference | Description | Implementation | Owner | Status |
|-------------|-----------|-------------|----------------|-------|--------|
| [Requirement] | [Article/Section] | [What must be done] | [How] | [Who] | [Status] |

## Data Classification and Handling

| Data Type | Classification | Regulations | Handling Requirements |
|-----------|----------------|-------------|----------------------|
| [Type] | [Sensitivity level] | [Applicable regs] | [Required controls] |

### Data Retention

| Data Type | Retention Period | Legal Basis | Disposal Method |
|-----------|------------------|-------------|-----------------|
| [Type] | [Duration] | [Why] | [How] |

## Privacy Requirements

### Data Subject Rights (if applicable)

| Right | Implementation | Response Time |
|-------|----------------|---------------|
| [Right] | [How implemented] | [SLA] |

### Privacy Impact Assessment

For each data processing activity:
- **Data Types**: [What data]
- **Purpose**: [Why processed]
- **Legal Basis**: [Lawful basis]
- **Risk Level**: [High/Medium/Low]

## Incident Response and Reporting

### Breach Notification Requirements

| Regulation | Authority Notification | Individual Notification | Timeline |
|------------|----------------------|------------------------|----------|
| [Reg] | [Requirements] | [Requirements] | [Deadline] |

## Compliance Risk Assessment

| Risk | Impact | Likelihood | Risk Level | Mitigation |
|------|--------|------------|------------|------------|
| [Risk] | [Impact] | [Likelihood] | [Level] | [Action] |

## Implementation Plan

- [ ] Regulatory applicability analysis and gap assessment
- [ ] Data protection, access controls, audit logging
- [ ] Privacy mechanisms and data subject rights
- [ ] Vendor data processing agreements
- [ ] Compliance testing and audits
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
