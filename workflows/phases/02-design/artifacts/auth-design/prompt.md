# Authentication Design Generation

## Required Inputs
- `docs/helix/01-frame/security-requirements.md` - Security requirements
- `docs/helix/02-design/architecture.md` - System architecture

## Produced Output
- `docs/helix/02-design/auth-design.md` - Authentication and authorization design

## Prompt

You are designing the authentication and authorization system. Your goal is to create a secure, usable identity management approach.

Design the following:

1. **Authentication Strategy**
   - Authentication methods (password, SSO, MFA, etc.)
   - Identity providers
   - Session management approach
   - Token strategy (JWT, sessions, etc.)

2. **Authorization Model**
   - Access control model (RBAC, ABAC, etc.)
   - Permission structure
   - Role definitions
   - Resource-level permissions

3. **Authentication Flows**
   - Login flow
   - Registration flow
   - Password reset
   - MFA enrollment and verification
   - Token refresh

4. **Security Considerations**
   - Credential storage
   - Brute force protection
   - Session security
   - Token security

Use the template at `workflows/helix/phases/02-design/artifacts/auth-design/template.md`.

## Completion Criteria
- [ ] All authentication methods documented
- [ ] Authorization model clearly defined
- [ ] Security controls specified
- [ ] No `[NEEDS CLARIFICATION]` markers remain
