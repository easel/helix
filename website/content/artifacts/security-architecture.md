---
title: "Security Architecture"
slug: security-architecture
phase: "Design"
weight: 200
generated: true
aliases:
  - /reference/glossary/artifacts/security-architecture
---

## What it is

Design-level security architecture that maps trust boundaries, controls,
and security decisions to implementation and testing.

## Phase

**[Phase 2 — Design](/reference/glossary/phases/)** — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.

## Output location

`docs/helix/02-design/security-architecture.md`

## Relationships

### Requires (upstream)

- [Security Requirements](../security-requirements/)
- [Threat Model](../threat-model/)
- [System Architecture](../architecture/)

### Enables (downstream)

_None._

### Informs

- [Technical Design](../technical-design/)
- [Test Plan](../test-plan/)
- [Security Tests](../security-tests/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Security Architecture Generation Prompt
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
- The document is specific enough to guide implementation and testing.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: security-architecture
  depends_on:
    - security-requirements
    - threat-model
    - architecture
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

- [Test or validation that proves the control exists]
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
