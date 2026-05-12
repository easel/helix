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

## Activity

**[Iterate](/reference/glossary/activities/)** — Measure, align, and improve. Close the feedback loop back into the planning strand.

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

This example is HELIX's actual security metrics, sourced from [`docs/helix/06-iterate/security-metrics.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/06-iterate/security-metrics.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Security Metrics — HELIX 2026-Q2 (post-`v0.3.3`)

> Illustrative example using representative measurements taken from the
> live HELIX repo around the `v0.3.3` release window. Exact counts reflect
> a single sampling period and will drift; the posture report's
> structure and decision logic are the canonical part. HELIX is a
> developer-local methodology framework, not a hosted service, so several
> traditional security-metric categories report N/A by design.

**Review Window**: 2026-04-01 → 2026-04-30
**Authority**: [`security-architecture.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/security-architecture.md),
[`security-owasp` concern](https://github.com/DocumentDrivenDX/helix/blob/main/workflows/concerns/security-owasp),
[`CONTRACT-001`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md).

### Incident Response

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Mean Time to Detect (MTTD) | N/A — operator-driven detection | N/A | Stable |
| Mean Time to Respond (MTTR) | < 1 cycle (operator stops the run) | < 1 cycle | Stable |
| Incidents resolved within SLA | 0 / 0 incidents this period | 100% when applicable | N/A |
| False-positive alert rate | N/A — no automated paging | N/A | Stable |

**Incident Summary**

- Total incidents this period: 0
- Critical (required immediate response): 0
- Fully resolved: 0

**Root Causes** (critical and high only)

| Root Cause | Count | Mitigation Status |
|------------|-------|-------------------|
| (none this period) | 0 | N/A |

### Vulnerability Management

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Open critical vulnerabilities (direct deps) | 0 | 0 | Stable |
| Open high vulnerabilities (direct deps) | 0 | 0 | Stable |
| MTTR for critical vulns | N/A — none open | < 7 days when applicable | Stable |
| Patch compliance rate (HELIX direct deps) | 100% (all pinned via `go.mod` / `package.json`) | 100% | Stable |

HELIX direct dependency surface is small: Hugo (pinned in
`.github/workflows/pages.yml`), Hextra (`website/go.mod`), Playwright
(`website/package.json`), DDx (operator-installed, version-pinned). The
project does not run a continuous SCA scan; vulnerability tracking is
manual and bound to dependency-update beads.

### Application Security

| Metric | Value | Trend |
|--------|-------|-------|
| SAST findings (new this period) | 0 | Stable |
| DAST findings (new this period) | N/A — no hosted service | N/A |
| Dependency vulnerabilities (direct) | 0 | Stable |
| Security review coverage | All commits gated by `lefthook` pre-commit (`check-workflow-paths`, secret-pattern scan) | Stable |
| Secret-pattern matches in commits | 0 | Stable |
| Bare `workflows/` references in docs (forbidden by hook) | 0 (enforced by `check-workflow-paths`) | Stable |

### Compliance Status

| Requirement | Status | Open Gaps | Target Resolution |
|-------------|--------|-----------|-------------------|
| Boundary contract (CONTRACT-001) honored | Compliant | None — every doc audited 2026-05-01 references the post-DDx-migration substrate after the AR-2026-05-01 follow-ups | Sustained via the `helix review` discipline |
| `security-owasp` concern coverage | Compliant on the developer-local surface; not applicable to hosted-service controls (no hosted service) | None | N/A |
| No secrets in repo | Compliant | None this period | Sustained via pre-commit secret scan |

### Security Posture Trend

- **Overall risk level**: Low — Trend: Stable
- **Summary**: HELIX is a developer-local framework; the active security
  surface is the operator's own model-provider key handling and the
  pre-commit guards that prevent secrets from being committed. Both held
  steady across the 2026-Q2 window. The largest residual risk is operator-
  introduced secrets in bead bodies, which is a contract-level concern,
  not a service-level one.

### Recommendations

| Recommendation | Priority | Rationale | Expected Impact |
|----------------|----------|-----------|-----------------|
| Add a continuous secret-pattern scan in CI (in addition to pre-commit) | Med | Pre-commit can be skipped (`--no-verify`); CI is the durable backstop | Catches any operator-bypassed secret leaks before they reach the public site |
| Wire a lightweight SCA scan (e.g. `govulncheck` for Go, `npm audit` for the website) into CI for the HELIX direct dep surface | Med | Vulnerability discovery is currently manual; small surface but worth automating | Earlier signal on Hextra / Hugo / Playwright vulns before they age |
| Document the `OPENROUTER_API_KEY` rotation cadence in the runbook | Low | Currently the runbook only describes how to react to auth failures, not preventive rotation | Reduces credential-age risk for long-lived operator setups |
| Add a deterministic test that asserts `ddx-server` binds to `127.0.0.1:7743` and refuses non-loopback bind without an explicit flag | Med | Security-architecture says this; nothing today tests it | Regression-protects the loopback-default posture |
