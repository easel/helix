---
title: "Risk Register"
slug: risk-register
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/risk-register
---

## What it is

Comprehensive identification, assessment, and management of project risks.
Includes both threats and opportunities with mitigation strategies and ownership.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/risk-register.md`

## Relationships

### Requires (upstream)

- [PRD](../prd/) *(optional)*
- [Stakeholder Map](../stakeholder-map/) *(optional)*

### Enables (downstream)

_None._

### Informs

- Project Planning
- Budget Planning
- Contingency Planning

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Risk Register Generation Prompt
Create a concise register of the project risks that matter.

## Focus
- Score risks clearly and consistently.
- Tie each risk to an owner and a mitigation.
- Include triggers and review cadence only where they change action.

## Completion Criteria
- Major risks are covered.
- Ownership and mitigation are explicit.
- The register is easy to scan.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Risk Register

**Status**: [Draft | Review | Approved]
**Last Updated**: [Date]
**Risk Owner**: [Name]

## Summary

- **Critical Risks**: [Number]
- **High Risks**: [Number]
- **Medium Risks**: [Number]
- **Low Risks**: [Number]
- **Overall Risk Level**: [Low | Medium | High | Critical]

## Risk Scoring

**Probability**: Very High (5) >80% | High (4) 60-80% | Medium (3) 40-60% | Low (2) 20-40% | Very Low (1) <20%
**Impact**: Critical (5) >30% overrun | High (4) 20-30% | Medium (3) 10-20% | Low (2) 5-10% | Negligible (1) <5%
**Risk Score** = Probability x Impact: Critical (20-25), High (12-19), Medium (6-11), Low (1-5)

## Active Risks

### RISK-001: [Risk Title]
**Category**: [Technical | Business | Resource | External | Compliance]
**Status**: [Open | Mitigating | Monitoring | Closed]
**Owner**: [Name]

**Description**: [Risk and its potential consequences]

**Assessment**:
- **Probability**: [1-5] - [Justification]
- **Impact**: [1-5] - [Justification]
- **Risk Score**: [P x I]

**Triggers**: [Early warning signs]

**Mitigation**:
- **Preventive**: [Actions to reduce probability]
- **Contingency**: [Actions if risk occurs]
- **Fallback**: [Alternative if mitigation fails]

**Review**: [Frequency] | **Next Review**: [Date]

---

### RISK-002: [Risk Title]
[Repeat structure]

## Closed Risks

| ID | Risk | Resolution | Date | Lessons Learned |
|----|------|------------|------|-----------------|
| RISK-XXX | [Title] | [How resolved] | [Date] | [Learnings] |

## Escalation Criteria

Escalate when: risk score reaches Critical (20+), mitigation fails, or risk impacts multiple projects.
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
