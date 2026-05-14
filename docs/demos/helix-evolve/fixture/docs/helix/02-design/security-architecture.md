# Security Architecture

## Authentication

The service authenticates incoming requests by validating an
`X-API-Key` header against the issued-keys table and rejecting any
fingerprint in the revoked-keys table. Keys are 256-bit opaque tokens,
stored hashed-at-rest.

## Threat model (current)

- **API-key theft.** Mitigated by mandatory TLS, rotation policy, and
  audit log alerting on cross-region usage.
- **Brute force.** Mitigated by per-IP rate limit; verify endpoint is
  capped at 30 req/s/IP.
- **Revocation lag.** Mitigated by the 60s revocation SLO and a
  cache-bust on the revoke command.

## Token lifecycle

API keys are long-lived until the operator rotates or revokes them.
No refresh tokens, no session tokens, no JWTs — by design.
