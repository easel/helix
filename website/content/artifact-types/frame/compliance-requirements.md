---
title: "Compliance Requirements"
linkTitle: "Compliance Requirements"
slug: compliance-requirements
phase: "Frame"
artifactRole: "supporting"
weight: 15
generated: true
---

## Purpose

Comprehensive regulatory and compliance requirements analysis.
Identifies applicable regulations, maps requirements to implementation
controls, and defines a compliance validation plan.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/compliance-requirements.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/solution-design/">Solution Design</a></td></tr>
<tr><th>Referenced by</th><td><a href="/artifact-types/test/test-plan/">Test Plan</a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Compliance Requirements Analysis Prompt
Document the compliance obligations for this project in the local template.

## Focus
- Identify only the regulations and standards that actually apply to this system.
- Map each obligation to its source, affected scope, concrete controls, owners, and timing.
- Keep the result concise and implementation-relevant.

## Completion Criteria
- Applicable requirements are identified.
- Controls, risks, owners, and deadlines are explicit.
- No generic filler is added.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
- [ ] Compliance testing and audits</code></pre></details></td></tr>
</tbody>
</table>
