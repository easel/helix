---
title: "Risk Register"
linkTitle: "Risk Register"
slug: risk-register
phase: "Frame"
artifactRole: "supporting"
weight: 21
generated: true
---

## Purpose

Comprehensive identification, assessment, and management of project risks.
Includes both threats and opportunities with mitigation strategies and ownership.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/risk-register.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td>Project Planning<br>Budget Planning<br>Contingency Planning</td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Risk Register Generation Prompt
Create a concise register of the project risks that matter.

## Focus
- Score risks clearly and consistently.
- Tie each risk to an owner and a mitigation.
- Include triggers and review cadence only where they change action.

## Completion Criteria
- Major risks are covered.
- Ownership and mitigation are explicit.
- The register is easy to scan.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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

**Probability**: Very High (5) &gt;80% | High (4) 60-80% | Medium (3) 40-60% | Low (2) 20-40% | Very Low (1) &lt;20%
**Impact**: Critical (5) &gt;30% overrun | High (4) 20-30% | Medium (3) 10-20% | Low (2) 5-10% | Negligible (1) &lt;5%
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

Escalate when: risk score reaches Critical (20+), mitigation fails, or risk impacts multiple projects.</code></pre></details></td></tr>
</tbody>
</table>
