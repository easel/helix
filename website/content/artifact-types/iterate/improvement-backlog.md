---
title: "Improvement Backlog"
linkTitle: "Improvement Backlog"
slug: improvement-backlog
phase: "Iterate"
artifactRole: "core"
weight: 12
generated: true
---

## Purpose

Prioritized improvement inventory derived from iteration learnings and
tracker-backed follow-up work.

## Reference

<table class="helix-reference-table">
<tbody>
<tr><th>Activity</th><td><a href="/reference/glossary/activities/"><strong>Iterate</strong></a> — Measure, align, and improve. Close the feedback loop back into the planning strand.</td></tr>
<tr><th>Default location</th><td><code>docs/helix/06-iterate/improvement-backlog.md</code></td></tr>
<tr><th>Requires</th><td><em>None</em></td></tr>
<tr><th>Enables</th><td><em>None</em></td></tr>
<tr><th>Informs</th><td>Tracker Issues</td></tr>
<tr><th>HELIX documents</th><td><a href="https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/06-iterate/improvement-backlog.md"><code>docs/helix/06-iterate/improvement-backlog.md</code></a></td></tr>
<tr><th>Generation prompt</th><td><details><summary>Show the full generation prompt</summary><pre><code># Improvement Backlog Generation Prompt
Document the prioritized improvement inventory produced from iteration learnings.

## Focus
- Turn the current iteration&#x27;s learnings into a ranked list of follow-up work.
- Prefer concrete tracker-backed items over vague TODOs.
- Use metrics, feedback, and retrospective findings as evidence.
- Make the next selection obvious by sorting by priority and impact.
- Link each item to the relevant bead, report, or supporting artifact.

## Completion Criteria
- The inventory is prioritized.
- Every item has an evidence source.
- The next iteration candidates are explicit.</code></pre></details></td></tr>
<tr><th>Template</th><td><details><summary>Show the template structure</summary><pre><code>---
ddx:
  id: &quot;[artifact-id]&quot;
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
- [ ] Ordering is deterministic</code></pre></details></td></tr>
</tbody>
</table>
