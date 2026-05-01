---
title: "Threat Model"
slug: threat-model
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/threat-model
---

## What it is

Systematic identification and analysis of security threats using
STRIDE methodology. Maps threats to system components, assesses
risk, and defines mitigation strategies.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/threat-model.md`

## Relationships

### Requires (upstream)

- [Product Requirements Document](../prd/)
- [Security Requirements](../security-requirements/)
- [User Stories](../user-stories/)

### Enables (downstream)

_None._

### Informs

- [Solution Design](../solution-design/)
- [Test Plan](../test-plan/)

### Referenced by

- [Adr](../adr/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Threat Modeling Prompt
Document the project threat model with enough detail to drive mitigations.

## Focus
- Define boundaries, assets, and trust changes first.
- Analyze threats with STRIDE and map them to controls.
- Keep risk scoring and mitigation ownership explicit.

## Completion Criteria
- The threat surface is clear.
- Important threats are prioritized.
- Mitigations are concrete.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Threat Model

**Project**: [Project Name]
**Date**: [Creation Date]

## Executive Summary

**System Overview**: [Brief description]
**Key Assets**: [Primary assets needing protection]
**Primary Threats**: [Top 3-5 threats]
**Risk Level**: [Critical/High/Medium/Low]

## System Description

### Boundaries and Components
**In Scope**: [Systems, components, data flows included]
**Out of Scope**: [What is not covered]
**Trust Boundaries**: [Where trust levels change]

### Components
| Component | Description | Trust Level |
|-----------|-------------|-------------|
| [Component] | [Description] | [Level] |

### Data Flows
- **External Sources**: [Data entering the system]
- **Internal Processing**: [How data moves within]
- **External Destinations**: [Where data exits]

## Assets

### Data Assets
| Asset | Classification | Confidentiality | Integrity | Availability |
|-------|---------------|-----------------|-----------|--------------|
| [Asset] | [Level] | [Criticality] | [Criticality] | [Criticality] |

### System Assets
| Asset | Criticality | Dependencies |
|-------|-------------|--------------|
| [Asset] | [Level] | [Dependencies] |

## STRIDE Threat Analysis

For each STRIDE category (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege):

| ID | Threat | Impact | Likelihood | Risk | Mitigation |
|----|--------|--------|------------|------|------------|
| TM-X-001 | [Threat] | [Level] | [Level] | [Level] | [Control] |

ID prefix: S=Spoofing, T=Tampering, R=Repudiation, I=Information Disclosure, D=Denial of Service, E=Elevation of Privilege.

## Risk Assessment

**Scoring**: Impact (1-5) x Likelihood (1-5)
- **Critical (20-25)**: Immediate action required
- **High (15-19)**: Action within 30 days
- **Medium (10-14)**: Action within 90 days
- **Low (1-9)**: Monitor or accept

### Top Risks
| Risk ID | Threat | Impact | Likelihood | Score | Priority |
|---------|--------|--------|------------|-------|----------|
| [ID] | [Threat] | [1-5] | [1-5] | [Score] | [Level] |

## Mitigation Strategies

### [Risk ID] - [Title]
- **Controls**: [Preventive, detective, corrective actions]
- **Timeline**: [When to implement]
- **Owner**: [Who is responsible]

## Security Controls Summary

- **Preventive**: [Authentication, authorization, encryption, input validation]
- **Detective**: [Logging, monitoring, intrusion detection]
- **Corrective**: [Incident response, backup/recovery, patching]

## Assumptions and Dependencies
- [List assumptions and external dependencies]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
