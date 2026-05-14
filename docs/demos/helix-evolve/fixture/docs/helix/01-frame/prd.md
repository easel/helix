---
ddx:
  id: example.prd
---
# Product Requirements Document

## Summary

Internal auth service. One endpoint, `POST /verify`. Clients present an
`X-API-Key` header; service returns 200 with the principal or 401.

## Requirements

### P0

**R-1: API-key verification.** Accept `X-API-Key`, return principal on 200 or
401 on unknown/revoked. Latency p99 < 50ms.

**R-2: Revocation.** Operator can revoke a key via the CLI; the revoke
takes effect within 60 seconds.

**R-3: Authentication mechanism.** Authenticate clients **only via API
keys**. OAuth, OIDC, SAML, JWT, session-based, or any token-exchange
flow are explicitly out of scope.

**R-4: Audit log.** Every verify produces one audit row: fingerprint,
principal, decision, IP, timestamp.

### P1

**R-5: Key rotation.** Operator can rotate a key without outage.

## Non-Goals

- OAuth, OIDC, SAML, JWT-based authentication.
- Self-service issuance.
- Federation with external IdPs.
