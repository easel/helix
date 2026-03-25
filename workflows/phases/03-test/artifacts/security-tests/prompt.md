# Security Tests Generation

## Required Inputs
- `docs/helix/01-frame/threat-model.md` - Threat model
- `docs/helix/02-design/security-architecture.md` - Security architecture
- `docs/helix/01-frame/security-requirements.md` - Security requirements

## Produced Output
- `docs/helix/03-test/security-tests.md` - Security test plan
- Security test implementations

## Prompt

You are creating security tests for the system. Your goal is to verify that security controls are effective.

Based on the threat model and security architecture, create:

1. **Security Test Categories**
   - Authentication tests
   - Authorization tests
   - Input validation tests
   - Encryption verification
   - Session management tests
   - Error handling tests

2. **Threat-Based Tests**
   | Threat ID | Test | Expected Result | Pass Criteria |
   |-----------|------|-----------------|---------------|
   | [From threat model] | [Test description] | [Expected behavior] | [How to verify] |

3. **OWASP Top 10 Coverage**
   - Injection attacks
   - Broken authentication
   - Sensitive data exposure
   - XML external entities
   - Broken access control
   - Security misconfiguration
   - XSS
   - Insecure deserialization
   - Vulnerable components
   - Insufficient logging

4. **Security Test Implementation**
   - Static analysis (SAST) configuration
   - Dynamic analysis (DAST) approach
   - Penetration test scenarios
   - Fuzz testing targets

Use the template at `workflows/helix/phases/03-test/artifacts/security-tests/template.md`.

## Completion Criteria
- [ ] All high-risk threats have tests
- [ ] OWASP Top 10 covered
- [ ] Tests are implementable
- [ ] No `[NEEDS CLARIFICATION]` markers remain
