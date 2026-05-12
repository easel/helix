---
title: "Contract"
linkTitle: "Contract"
slug: contract
phase: "Design"
artifactRole: "core"
weight: 12
generated: true
---

## Purpose

Normative interface and schema contract that another team can implement
against directly, including API, CLI, protocol, event, and data contracts.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Design</strong></a> — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/02-design/contracts/CONTRACT-{id}-{name}.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td><a href="/artifact-types/test/test-plan/">Test Plan</a><br><a href="/artifact-types/design/technical-design/">Technical Design</a></td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md"><code>docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Contract Generation Prompt
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
- Tests can be derived directly from the contract.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
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
- [ ] At least one executable test can be derived from this contract.</code></pre></details></td></tr>
</tbody>
</table>
