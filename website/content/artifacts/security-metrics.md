---
title: "Security Metrics"
slug: security-metrics
phase: "Iterate"
weight: 600
generated: true
aliases:
  - /reference/glossary/artifacts/security-metrics
---

## What it is

Iteration-level security posture report covering incident response,
vulnerability management, application security, and compliance.

## Phase

**[Phase 6 — Iterate](/reference/glossary/phases/)** — Measure, align, and improve. Close the feedback loop back into the planning strand.

## Output location

`docs/helix/06-iterate/security-metrics.md`

## Relationships

### Requires (upstream)

_None._

### Enables (downstream)

_None._

### Informs

- [Improvement Backlog](../improvement-backlog/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Security Metrics Prompt

Create a security metrics report for one iteration.

## Required Inputs
- Security monitoring and incident data for the iteration period
- Vulnerability scan results (SAST, DAST, dependency scans)
- Compliance audit findings, if applicable
- Previous security metrics report for trend comparison

## Produced Output
- `docs/helix/06-iterate/security-metrics.md`

## Focus

Report on security posture across four areas: incident response, vulnerability
management, application security, and compliance. For each area, state the
current value, the target, and the trend. Do not repeat raw data in prose —
summarize what the numbers mean and what action they justify.

Trend comparison against the previous period is required. If no prior report
exists, note the baseline and set targets for the next iteration.

Every recommendation must be specific enough to become a tracker issue. Vague
recommendations ("improve security posture") are not acceptable.

## Completion Criteria
- [ ] All four metric areas populated with current data
- [ ] Trend column populated for each metric (or baseline set if first report)
- [ ] At least one recommendation per area that is actionable as a tracker issue
- [ ] Root cause included for any critical or high-severity incidents
- [ ] Report covers the same iteration period as `metrics-dashboard.md`

Use the template at `.ddx/plugins/helix/workflows/phases/06-iterate/artifacts/security-metrics/template.md`.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Security Metrics — [Iteration / Date Range]

## Incident Response

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Mean Time to Detect (MTTD) | | | |
| Mean Time to Respond (MTTR) | | | |
| Incidents resolved within SLA | | | |
| False-positive alert rate | | | |

**Incident Summary**

- Total incidents this period: [X]
- Critical (required immediate response): [X]
- Fully resolved: [X]

**Root Causes** (critical and high only)

| Root Cause | Count | Mitigation Status |
|------------|-------|-------------------|
| | | |

## Vulnerability Management

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Open critical vulnerabilities | | | |
| Open high vulnerabilities | | | |
| MTTR for critical vulns | | | |
| Patch compliance rate | | | |

## Application Security

| Metric | Value | Trend |
|--------|-------|-------|
| SAST findings (new this period) | | |
| DAST findings (new this period) | | |
| Dependency vulnerabilities (direct) | | |
| Security review coverage | | |

## Compliance Status

| Requirement | Status | Open Gaps | Target Resolution |
|-------------|--------|-----------|-------------------|
| | | | |

## Security Posture Trend

- **Overall risk level**: [Low / Medium / High] — Trend: [Improving / Stable / Declining]
- **Summary**: [One sentence on direction and primary driver]

## Recommendations

Each recommendation must be specific enough to create a tracker issue.

| Recommendation | Priority | Rationale | Expected Impact |
|----------------|----------|-----------|-----------------|
| | High / Med / Low | | |
``````

</details>

## Example

_No worked example captured yet. The prompt and template above describe the canonical structure._
