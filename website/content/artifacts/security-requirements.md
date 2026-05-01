---
title: "Security Requirements"
slug: security-requirements
phase: "Frame"
weight: 100
generated: true
aliases:
  - /reference/glossary/artifacts/security-requirements
---

## What it is

Comprehensive security requirements definition for the project.
Covers security user stories, compliance mapping, risk assessment,
and testable acceptance criteria for security controls.

## Phase

**[Phase 1 — Frame](/reference/glossary/phases/)** — Define what the system should do, for whom, and how success will be measured.

## Output location

`docs/helix/01-frame/security-requirements.md`

## Relationships

### Requires (upstream)

- [Product Requirements Document](../prd/)
- [User Stories](../user-stories/)

### Enables (downstream)

- [Solution Design (security sections)](../solution-design/)

### Informs

- [Solution Design](../solution-design/)
- [Threat Model](../threat-model/)
- [Compliance Requirements](../compliance-requirements/)

### Referenced by

- [Test Plan](../test-plan/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Security Requirements Generation Prompt
Document the security requirements the project must satisfy before design and build.

## Focus
- Cover authentication, authorization, data protection, privacy, validation, and logging.
- Turn requirements into concrete controls and tests where possible.
- Keep compliance and risk notes brief but explicit.

## Completion Criteria
- Required controls are identified.
- Risks and assumptions are visible.
- The result is specific enough to guide design.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Security Requirements

**Project**: [Project Name]
**Date**: [Creation Date]
**Security Champion**: [Name]

## Overview
[Brief description of security scope and key protection goals]

## Required Controls

### Authentication
- [Control]

### Authorization
- [Control]

### Data Protection
- [Control]

### Privacy
- [Control]

### Input Validation
- [Control]

### Logging and Audit
- [Control]

## Compliance Requirements
**Applicable Regulations**: [List]
**Applicable Standards**: [List]
- [Required control or obligation]

## Security Risks
### High-Risk Areas
1. **[Area]**: [Description and mitigation]

## Security Architecture Requirements
- [ ] Network segmentation
- [ ] Application security testing
- [ ] Dependency vulnerability scanning
- [ ] Server hardening
- [ ] Patch management
- [ ] Backup and recovery tested

## Security Testing Requirements
- [ ] Penetration testing
- [ ] Vulnerability assessments
- [ ] Security code review
- [ ] Automated security scanning

## Assumptions and Dependencies
- [Assumption or dependency]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
