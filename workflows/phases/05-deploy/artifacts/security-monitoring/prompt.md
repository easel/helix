# Security Monitoring Setup Generation Prompt

Create a comprehensive security monitoring and alerting setup that provides continuous visibility into security events, threats, and compliance posture throughout the deployment and operation lifecycle.

## Storage Location

Store the security monitoring setup at: `docs/helix/05-deploy/security-monitoring.md`

## Purpose

The security monitoring setup ensures:
- Security events are detected and correlated in real time
- Threats are identified before they cause damage
- Compliance requirements for logging and auditing are met
- Incident response is supported with actionable data
- Security posture is continuously measured and improved

## Key Requirements

### 1. Security Event Collection

#### Authentication and Access Events
- Failed and successful login attempts
- Privilege escalation and administrative actions
- MFA bypass attempts and account lockouts
- Unusual access patterns (time, location, device)

#### Data Protection Events
- Large data exports or unusual query patterns
- Encryption key access outside normal patterns
- Data classification policy violations
- Backup and restore operations

#### Infrastructure Events
- Configuration changes to security controls
- Network traffic anomalies
- New service or application deployments
- Security tool status changes

### 2. SIEM Integration

#### Platform Configuration
- Data source onboarding and log ingestion
- Security rule and correlation logic
- Alert threshold calibration
- Retention policies for security events

#### Correlation and Analysis
- Cross-source event correlation
- Anomaly detection baselines
- Threat intelligence feed integration
- Automated triage for common patterns

### 3. Alert Configuration

#### Alert Categories
Define alerts for:
- Authentication anomalies (brute force, credential stuffing)
- Authorization violations (privilege escalation, unauthorized access)
- Data protection incidents (exfiltration, policy violations)
- Infrastructure threats (configuration drift, network anomalies)

#### Alert Routing
- Severity-based escalation matrix
- Security team notification channels
- Integration with incident response workflows
- On-call rotation for security operations

### 4. Compliance Monitoring

#### Audit Trail
- All user actions logged with timestamps and attribution
- Administrative changes tracked
- Data access events recorded with context
- Log integrity verification mechanisms

#### Regulatory Reporting
- Breach notification timelines (e.g., GDPR 72-hour requirement)
- Compliance dashboard with KPIs
- Evidence collection for audits
- Regular compliance report generation

### 5. Dashboards and Metrics

#### Security Operations Dashboard
- Active security incidents and their status
- Alert volumes, trends, and false positive rates
- System security health indicators
- Threat intelligence feed status

#### Key Performance Indicators
- Mean time to detect (MTTD) security incidents
- Mean time to respond (MTTR) to security alerts
- Security control effectiveness metrics
- Compliance posture scores

## Implementation Guide

### Quick Start
Essential security monitoring to implement first:
1. Authentication event logging and alerting
2. Administrative action audit trail
3. Critical security alerts (brute force, privilege escalation)
4. Basic security operations dashboard
5. Incident response integration

### Progressive Enhancement
Add depth over time:
1. Threat intelligence correlation
2. User behavior analytics (UBA)
3. Automated response playbooks
4. Advanced anomaly detection
5. Continuous compliance monitoring

## Quality Checklist

Before security monitoring is complete:
- [ ] All critical security events are collected
- [ ] SIEM rules are tuned and tested
- [ ] Alert thresholds minimize false positives
- [ ] Escalation matrix is documented and tested
- [ ] Compliance audit requirements are covered
- [ ] Incident response integration is validated
- [ ] Dashboard metrics are updating in real time
- [ ] Log retention meets regulatory requirements
- [ ] Security team is trained on tools and procedures
- [ ] Monitoring coverage is documented
