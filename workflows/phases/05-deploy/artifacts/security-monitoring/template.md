# Security Monitoring Setup

**Service**: [Project Name]
**Security Owner**: [Name]

## Detection Scope
- High-risk assets: [Accounts, secrets, sensitive data paths, admin surfaces]
- Data sources: [Application logs, auth logs, infra events, security tools]

## Alerts and Routing

| Category | Signals |
|----------|---------|
| Authentication | [Failed logins, MFA bypass, lockouts] |
| Authorization | [Privilege changes, denied access, tenant boundary violations] |
| Data protection | [Exports, sensitive reads, key access anomalies] |
| Infrastructure | [Security config drift, unusual traffic, tool failures] |

## Triage and Response

| Priority | Trigger | Route | Target Response |
|----------|---------|-------|-----------------|
| Critical | [Condition] | [PagerDuty / phone / incident bridge] | [Time] |
| High | [Condition] | [Channel] | [Time] |
| Medium / Low | [Condition] | [Channel] | [Time] |

## KPIs

- MTTD: [Target]
- MTTR: [Target]
- False positive rate: [Target]
- Security control coverage: [Target or notes]

## Operational Checks
- [ ] Log data flowing from all sources
- [ ] Alerts triggering appropriately
- [ ] Incident response procedures tested
