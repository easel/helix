---
title: "Security Requirements"
linkTitle: "Security Requirements"
slug: security-requirements
phase: "Frame"
artifactRole: "supporting"
weight: 22
generated: true
---

## Purpose

Comprehensive security requirements definition for the project.
Covers security user stories, compliance mapping, risk assessment,
and testable acceptance criteria for security controls.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Frame</strong></a> — Define what the system should do, for whom, and how success will be measured.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/01-frame/security-requirements.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/solution-design/">Solution Design</a><br><a href="/artifact-types/frame/threat-model/">Threat Model</a><br><a href="/artifact-types/frame/compliance-requirements/">Compliance Requirements</a></td></tr>
<tr><th>Referenced by</th><td><a href="/artifact-types/test/test-plan/">Test Plan</a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Security Requirements Generation Prompt
Document the security requirements the project must satisfy before design and build.

## Focus
- Cover authentication, authorization, data protection, privacy, validation, and logging.
- Turn requirements into concrete controls and tests where possible.
- Keep compliance and risk notes brief but explicit.

## Completion Criteria
- Required controls are identified.
- Risks and assumptions are visible.
- The result is specific enough to guide design.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
- [Assumption or dependency]</code></pre></details></td></tr>
</tbody>
</table>
