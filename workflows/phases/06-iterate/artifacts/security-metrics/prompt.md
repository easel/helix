# Security Metrics and Analysis Generation Prompt

Create a comprehensive security metrics report that measures security posture, tracks incident trends, evaluates control effectiveness, and identifies areas for improvement.

## Storage Location

Store the security metrics report at: `docs/helix/06-iterate/security-metrics.md`

## Purpose

The security metrics report ensures:
- Security posture is quantified and trackable over time
- Incident patterns are analyzed for root causes
- Control effectiveness is measured against targets
- Investment in security is justified with data
- Improvement priorities are evidence-based

## Key Requirements

### 1. Incident Response Metrics

Track and report:
- Mean time to detect (MTTD) — target: < 4 hours
- Mean time to respond (MTTR) — target: < 2 hours
- Mean time to recover — target: < 8 hours
- False positive rate — target: < 5%
- Incidents by category, severity, and root cause

### 2. Vulnerability Management Metrics

Track and report:
- Open critical and high vulnerabilities with MTTR
- Vulnerability scan coverage percentage
- Patch management compliance rate
- Dependency vulnerability counts and remediation status

### 3. Compliance Metrics

Track and report:
- Regulatory compliance scores per applicable regulation
- Audit findings: total, critical, remediated, overdue
- Data classification policy compliance
- Access review completion rates

### 4. Threat Landscape Analysis

Summarize:
- Attack patterns observed (phishing, malware, brute force, exfiltration)
- Indicators of compromise detected
- Relevant threat intelligence and industry trends
- Threat actor attribution where applicable

### 5. Security Culture Metrics

Track and report:
- Security training completion rates
- Phishing simulation click and reporting rates
- Security champion participation
- Security suggestion submissions

### 6. Trends and Recommendations

Provide:
- Overall security posture score and trend
- Key improvements this period
- Prioritized recommendations for next period with rationale and resource estimates
- Security improvement backlog (high, medium, future)

## Quality Checklist

Before the security metrics report is complete:
- [ ] All metric categories are populated with current data
- [ ] Trends are compared against previous periods
- [ ] Targets are defined for each metric
- [ ] Root cause analysis is included for incidents
- [ ] Recommendations are prioritized and actionable
- [ ] Report is reviewed by security team lead
