# Secure Coding Checklist

## Input Handling

- [ ] Inputs are validated server-side with an allowlist approach.
- [ ] SQL uses parameterized queries only.
- [ ] Output encoding matches the context.
- [ ] User-facing errors stay generic; details are logged securely.

## Authentication and Sessions

- [ ] Passwords are hashed with approved algorithms.
- [ ] Session tokens are secure and use `HttpOnly`, `Secure`, and `SameSite`.
- [ ] Sessions time out and invalidate on logout.

## Authorization

- [ ] Authorization is checked on every request.
- [ ] Access follows least privilege.
- [ ] Roles and permissions are explicit.

## Data Protection and Secrets

- [ ] Sensitive data is encrypted in transit and at rest.
- [ ] Secrets are externally managed.
- [ ] Sensitive data is not logged or cached.
- [ ] Secret rotation is documented where required.

## API Security

- [ ] Authentication and rate limiting are enforced where applicable.
- [ ] CORS and HSTS are configured where applicable.

## Logging and Monitoring

- [ ] Auth and admin actions are logged.
- [ ] Logs are protected from tampering.
- [ ] Security alerting is configured.

## Code Quality

- [ ] Security-focused review is complete.
- [ ] SAST findings are addressed.
- [ ] Dependencies are scanned for vulnerabilities.
- [ ] Debug info is disabled in production.
