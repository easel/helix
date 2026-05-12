---
title: "Security Tests"
slug: security-tests
phase: "Test"
weight: 300
generated: true
aliases:
  - /reference/glossary/artifacts/security-tests
---

## What it is

_(security-tests — description not yet captured in upstream `meta.yml`.)_

## Activity

**[Test](/reference/glossary/activities/)** — Define how we know it works. Plans, suites, and procedures that bind specs to implementation.

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

_None._

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Security Tests Generation
Create concise, project-specific security tests that map threats and security requirements to executable checks.

## Focus
- Cover the highest-risk threats first.
- Use a small threat-to-test matrix rather than broad prose.
- Include only the fixtures, setup, tooling, and controls that this stack actually needs.

## Completion Criteria
- Relevant threat coverage is explicit.
- Expected failures and pass criteria are clear.
- The output is usable in the Red phase.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Security Test Suite

**Project**: [Project Name]
**Date**: [Creation Date]

## Coverage Summary

- Threats covered: [Threat IDs or control names]
- Required setup: [Environments, accounts, fixtures]
- Out of scope: [What this suite does not test]

## Security Test Categories

- Authentication: [authn controls to verify]
- Authorization: [authz controls to verify]
- Input validation: [injection and tampering checks]
- Data protection: [encryption, masking, logging rules]
- Session management: [token and lifecycle checks]

## Threat Matrix

| Threat / Control | Test | Expected Result | Pass Criteria |
|------------------|------|-----------------|---------------|
| [Threat] | [Test case] | [Expected behavior] | [What proves it passes] |

## Automated Security Testing

```yaml
sast:
  tool: [tool]
  trigger: [when it runs]
dast:
  tool: [tool]
  target: [environment]
dependency_scan:
  tool: [tool]
```

## Key Test Cases

### SEC-TC-001: [Name]
**Steps**: [Minimal reproducible steps]
**Expected**: [Expected result]

### SEC-TC-002: [Name]
**Steps**: [Minimal reproducible steps]
**Expected**: [Expected result]

## Compliance and Abuse Cases

- [ ] [Regulatory or policy check]
- [ ] [Abuse or rate-limit check]
- [ ] [Audit/logging check]

## Done

- [ ] High-risk threats mapped to tests
- [ ] Applicable controls covered
- [ ] Tests are executable and deterministic
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
