---
title: "Security Architecture"
linkTitle: "Security Architecture"
slug: security-architecture
phase: "Design"
artifactRole: "supporting"
weight: 17
generated: true
---

## Purpose

Design-level security architecture that maps trust boundaries, controls,
and security decisions to implementation and testing.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Design</strong></a> — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/02-design/security-architecture.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/design/technical-design/">Technical Design</a><br><a href="/artifact-types/test/test-plan/">Test Plan</a><br><a href="/artifact-types/test/security-tests/">Security Tests</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/security-architecture.md"><code>docs/helix/02-design/security-architecture.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Security Architecture Generation Prompt
Document the security architecture patterns, trust boundaries, controls, and
design-level security decisions that shape implementation and testing.

## Focus
- Start from security requirements and the threat model.
- Define trust boundaries, control points, identity, data protection, logging,
  monitoring, and residual risk.
- Map threats to controls and controls to tests.
- Keep the artifact at the design level; do not drift into code or deployment
  instructions.

## Completion Criteria
- Threats and controls are linked.
- Identity and access decisions are explicit.
- Data protection and monitoring decisions are explicit.
- The document is specific enough to guide implementation and testing.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
---

# Security Architecture

**Scope**: [system or subsystem]
**Status**: [draft | complete]

## Decision

[Summarize the security architecture approach and the main security controls.]

## Trust Boundaries

| Boundary | Assets | Trust Change | Control |
|----------|--------|--------------|---------|
| [name] | [asset] | [how trust changes] | [control] |

## Control Mapping

| Threat / Risk | Control | Implementation Surface | Verification |
|---------------|---------|-------------------------|--------------|
| [risk] | [control] | [component or interface] | [test or check] |

## Identity and Access

- Authentication:
- Authorization:
- Session or token handling:

## Data Protection

- Data at rest:
- Data in transit:
- Secrets and key handling:

## Logging and Monitoring

- Security events:
- Alerting:
- Audit trail:

## Residual Risk

- [Known risk and why it remains]

## Security Test Hooks

- [Test or validation that proves the control exists]</code></pre></details></td></tr>
</tbody>
</table>
