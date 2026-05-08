---
title: "Improvement Backlog"
slug: improvement-backlog
phase: "Iterate"
weight: 600
generated: true
aliases:
  - /reference/glossary/artifacts/improvement-backlog
---

## What it is

Prioritized improvement inventory derived from iteration learnings and
tracker-backed follow-up work.

## Phase

**[Phase 6 — Iterate](/reference/glossary/phases/)** — Measure, align, and improve. Close the feedback loop back into the planning strand.

## Output location

`docs/helix/06-iterate/improvement-backlog.md`

## Relationships

### Requires (upstream)

- [Metrics Dashboard](../metrics-dashboard/)
- [Security Metrics](../security-metrics/)

### Enables (downstream)

_None._

### Informs

- Tracker Issues

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Improvement Backlog Generation Prompt
Document the prioritized improvement inventory produced from iteration learnings.

## Focus
- Turn the current iteration's learnings into a ranked list of follow-up work.
- Prefer concrete tracker-backed items over vague TODOs.
- Use metrics, feedback, and retrospective findings as evidence.
- Make the next selection obvious by sorting by priority and impact.
- Link each item to the relevant bead, report, or supporting artifact.

## Completion Criteria
- The inventory is prioritized.
- Every item has an evidence source.
- The next iteration candidates are explicit.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
ddx:
  id: improvement-backlog
  depends_on:
    - metrics-dashboard
---
# Improvement Backlog

**Iteration**: [iteration or release]
**Source Learnings**: [metrics, feedback, retrospective, incident review]

## Prioritization Rules

- [Rule for ordering work]
- [Rule for handling safety or risk]

## Backlog Items

| Priority | Item | Evidence | Tracker Ref | Why Now | Status |
|----------|------|----------|-------------|---------|--------|
| P1 | [item] | [metric or finding] | [bead ID] | [reason] | [open/blocked] |

## Selection for Next Iteration

- [Chosen item]
- [Why it wins the next slot]

## Review Checklist

- [ ] Each item cites evidence
- [ ] Tracker references are included
- [ ] Ordering is deterministic
``````

</details>

## Example

This example is HELIX's actual improvement backlog, sourced from [`docs/helix/06-iterate/improvement-backlog.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/06-iterate/improvement-backlog.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Improvement Backlog — HELIX 2026-Q2

**Iteration**: 2026-Q2 (post-`v0.3.3`)
**Source Learnings**: `docs/helix/06-iterate/alignment-reviews/AR-2026-05-01-public-examples.md`,
`docs/helix/06-iterate/metrics-dashboard.md`,
`docs/helix/06-iterate/security-metrics.md`,
recent `tests/helix-cli.sh` regression history,
the active concerns roster (`hugo-hextra`, `demo-asciinema`, `e2e-playwright`).

### Prioritization Rules

- Rank by **authority leverage**: items that shore up CONTRACT-001 alignment
  or fix authority-inversion risks rank above cosmetic improvements.
- Rank by **public-surface impact**: items that make the public website /
  artifact reference more accurate to readers rank above purely-internal
  cleanups.
- Items without tracker references stay at the bottom until they are
  filed — the backlog does not retain unsourced ideas.
- Safety / supply-chain risk items take priority over feature work. None
  are currently flagged in `security-metrics.md`.

### Backlog Items

| Priority | Item | Evidence | Tracker Ref | Why Now | Status |
|----------|------|----------|-------------|---------|--------|
| P1 | Author HELIX-real worked examples for the 12 descoped artifact slugs | AR-2026-05-01-public-examples.md "Follow-up beads to file" table | This iterate cycle is consuming them; one bead per slug | Public artifact reference currently shows a `Decision / Why It Exists` page where a worked example is expected, misleading readers | open |
| P1 | Restore the public-site Playwright proof lane to green | `e2e-playwright` concern; recent CI history | helix-438c8a07 (and successors under `area:site,area:testing`) | Site regressions are landing without test coverage; Playwright is the only deterministic site verification | open |
| P2 | Reconcile `helix-run` ↔ `helix run` cosmetic drift across PRD, ADR-001, SD-001, TD-002 | AR-2026-05-01-public-examples.md cross-cutting findings #7 | Filed as part of artifact-restoration work; covered by per-doc refresh beads | Published canonical examples should use the actual CLI invocation form; cosmetic but visible | open |
| P2 | Verify the `github.com/easel/ddx` repo URL in architecture.md vs the canonical org URL | AR-2026-05-01-public-examples.md cross-cutting findings #6 | Pending bead under `area:docs,area:artifacts` | Public links must resolve; org migration may have invalidated this link | open |
| P2 | Propagate context-digest concerns onto open beads under FEAT-006 | FEAT-006 status in implementation-plan-2026-04-11-snapshot ("DIVERGENT") | helix-674b1b42, helix-691d18c0, helix-d9f93a59 | Concern propagation is incomplete; beads claimed today may not see the right practices | open |
| P3 | Replace remaining hardcoded `/home/erik/...` paths in older docs | AR-2026-05-01-public-examples.md cross-cutting findings #4 | One bead per affected doc | Public-readability blocker for any doc flipped into `HELIX_REAL_EXAMPLES_PUBLISHABLE` later | open |
| P3 | Demo-recording inventory refresh under `demo-asciinema` | `demo-asciinema` concern; demos may have drifted from current CLI surface | helix-39fc1526 and successors | Public demos should match shipped behavior post-`v0.3.3` | open |
| P3 | Forge-agent discovery scaffolding | `eff9742` "chore: add forge agent discovery tracker issue" | The bead created in that commit | Listed as a known known-issue in `release-notes.md`; no current path to consume it | open |

### Selection for Next Iteration

- **Chosen item**: P1 — Author HELIX-real worked examples for the 12
  descoped artifact slugs. This iterate cycle is consuming them as the
  current work-unit; eight slugs are flipped on as of `v0.3.3`, and
  twelve more are pending per AR-2026-05-01.
- **Why it wins the next slot**: Highest authority leverage (CONTRACT-001
  alignment), highest public-surface impact (the artifact reference is the
  most-visited part of the site), and it unblocks all P3 items below by
  exercising the relocate-meta-decision-doc pattern that several other
  cleanups will reuse.

### Review Checklist

- [x] Each item cites evidence
- [x] Tracker references are included (or marked as "pending bead" where
      not yet filed)
- [x] Ordering is deterministic (priority + position within priority)
