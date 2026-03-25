# Secure Coding Guidelines

## Required Inputs
- `docs/helix/01-frame/security-requirements.md` - Security requirements
- `docs/helix/02-design/security-architecture.md` - Security architecture
- Technology stack documentation

## Produced Output
- `docs/helix/04-build/secure-coding.md` - Secure coding guidelines

## Prompt

You are creating secure coding guidelines for the project. Your goal is to prevent security vulnerabilities during implementation.

Document guidelines for:

1. **Input Validation**
   - Validation approaches
   - Sanitization requirements
   - Allow-list vs deny-list
   - Common patterns

2. **Output Encoding**
   - Context-specific encoding
   - XSS prevention
   - Injection prevention

3. **Authentication & Session**
   - Credential handling
   - Session management
   - Token security

4. **Data Protection**
   - Sensitive data handling
   - Encryption usage
   - Logging restrictions

5. **Error Handling**
   - Error message content
   - Exception handling
   - Failure modes

6. **Language-Specific Guidelines**
   - Framework security features
   - Common vulnerabilities
   - Secure patterns

Use the template at `workflows/helix/phases/04-build/artifacts/secure-coding/template.md`.

## Completion Criteria
- [ ] All major vulnerability categories covered
- [ ] Guidelines are specific and actionable
- [ ] Code examples provided
- [ ] Review checklist included
