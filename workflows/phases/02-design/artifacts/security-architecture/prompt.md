# Security Architecture Generation

## Required Inputs
- `docs/helix/01-frame/threat-model.md` - Threat analysis
- `docs/helix/01-frame/security-requirements.md` - Security requirements
- `docs/helix/02-design/architecture.md` - System architecture

## Produced Output
- `docs/helix/02-design/security-architecture.md` - Security architecture design

## Prompt

You are creating a security architecture for a software system. Your goal is to design security controls that address the identified threats and meet security requirements.

Based on the threat model, security requirements, and system architecture, design:

1. **Security Architecture Principles**
   - Defense in depth implementation
   - Least privilege application
   - Zero trust considerations
   - Security by design patterns

2. **Security Control Architecture**
   For each layer (network, application, data):
   - Authentication mechanisms
   - Authorization controls
   - Encryption requirements
   - Monitoring and detection

3. **Identity and Access Management**
   - Identity providers
   - Authentication flows
   - Authorization model (RBAC, ABAC, etc.)
   - Session management
   - API security

4. **Data Protection Architecture**
   - Data classification
   - Encryption at rest and in transit
   - Key management
   - Data loss prevention

5. **Security Monitoring**
   - Logging architecture
   - Intrusion detection
   - Security alerting
   - Incident response integration

6. **Threat Mitigation Mapping**
   | Threat ID | Control | Implementation | Verification |
   |-----------|---------|----------------|--------------|
   | [From threat model] | [Security control] | [How implemented] | [How verified] |

Use the template at `workflows/helix/phases/02-design/artifacts/security-architecture/template.md`.

## Completion Criteria
- [ ] All high-risk threats have mitigating controls
- [ ] Security principles applied consistently
- [ ] Control implementation is specific and actionable
- [ ] No `[NEEDS CLARIFICATION]` markers remain
