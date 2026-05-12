---
title: "Security Tests"
linkTitle: "Security Tests"
slug: security-tests
phase: "Test"
artifactRole: "supporting"
weight: 12
generated: true
---

## Purpose

Security-focused test coverage for authentication, authorization, input
handling, dependency risk, data protection, and abuse cases.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Test</strong></a> — Define how we know it works. Plans, suites, and procedures that bind specs to implementation.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/03-test/security-tests.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/test/test-plan/">Test Plan</a><br><a href="/artifact-types/iterate/security-metrics/">Security Metrics</a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Security Tests Generation
Create concise, project-specific security tests that map threats and security requirements to executable checks.

## Focus
- Cover the highest-risk threats first.
- Use a small threat-to-test matrix rather than broad prose.
- Include only the fixtures, setup, tooling, and controls that this stack actually needs.

## Completion Criteria
- Relevant threat coverage is explicit.
- Expected failures and pass criteria are clear.
- The output is usable in the Red phase.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

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
- [ ] Tests are executable and deterministic</code></pre></details></td></tr>
</tbody>
</table>
