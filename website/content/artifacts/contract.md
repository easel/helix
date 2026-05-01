---
title: "Contract"
slug: contract
phase: "Design"
weight: 200
generated: true
aliases:
  - /reference/glossary/artifacts/contract
---

## What it is

Normative interface and schema contract that another team can implement
against directly, including API, CLI, protocol, event, and data contracts.

## Phase

**[Phase 2 — Design](/reference/glossary/phases/)** — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.

## Output location

`docs/helix/02-design/contracts/CONTRACT-{id}-{name}.md`

## Relationships

### Requires (upstream)

- [Architecture](../architecture/) *(optional)*
- [Solution Design](../solution-design/) *(optional)*
- [Technical Design](../technical-design/) *(optional)*
- [ADR](../adr/) *(optional)*

### Enables (downstream)

_None._

### Informs

- [Test Plan](../test-plan/)
- [Technical Design](../technical-design/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Contract Generation Prompt
Document the normative interface or schema that another team can implement
against directly.

## Focus
- State the contract scope and boundaries clearly.
- Specify exact commands, fields, types, units, enums, ranges, and requiredness
  where relevant.
- Define precedence, ordering, compatibility, and versioning rules explicitly.
- Define failure modes, error codes, retry behavior, and recovery expectations.
- Include concrete examples and a validation checklist.
- Keep the document normative and implementation-independent; rationale belongs
  in ADRs and broader approach belongs in solution or technical designs.

## Completion Criteria
- The contract is specific enough for an independent implementation.
- Normative surface details are explicit rather than implied.
- Error semantics and compatibility rules are documented.
- Tests can be derived directly from the contract.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
dun:
  id: contract
  depends_on:
    - architecture
---
# Contract

**Contract ID**: [CONTRACT-XXX | API-XXX]
**Type**: [boundary | HTTP API | CLI | library | protocol | event | schema]
**Status**: [draft | complete]
**Related**: [ADR / SD / TD / FEAT references]

## Purpose

[Why this contract exists and what it governs.]

## Scope and Boundaries

- In scope:
- Out of scope:
- Owning system or team:

## Normative Surface

| Element | Type / Shape | Required | Rules | Notes |
|---------|---------------|----------|-------|-------|
| [field, command, message, endpoint] | [type] | [yes/no] | [units, enum, constraints] | [notes] |

## Precedence and Compatibility

- Versioning:
- Ordering or precedence:
- Backward-compatibility rules:

## Error Semantics

| Condition | Error / Outcome | Retry | Recovery Expectation |
|-----------|------------------|-------|----------------------|
| [condition] | [error] | [yes/no] | [recovery] |

## Examples

```text
[Example request / response / payload / invocation]
```

## Validation Checklist

- [ ] Normative fields and rules are explicit.
- [ ] Compatibility and precedence rules are explicit.
- [ ] Error handling is explicit.
- [ ] At least one executable test can be derived from this contract.
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
