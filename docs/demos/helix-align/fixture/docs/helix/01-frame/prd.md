---
ddx:
  id: example.prd
---
# Product Requirements Document

## Summary

A small internal-auth service. One endpoint, `POST /verify`. Clients
present an `X-API-Key` header; the service returns 200 with the
associated principal or 401. Keys are issued out-of-band and rotated
manually by an operator using a one-shot CLI.

## Requirements

### P0

**R-1: API-key verification.** The service accepts an `X-API-Key`
header and returns the associated principal on a 200 or a 401 if the
key is unknown or revoked. Latency p99 < 50ms.

**R-2: Revocation.** An operator can mark a key revoked through a CLI
admin command. Revoked keys are rejected within 60 seconds of the
command's commit.

**R-3: Authentication mechanism.** The service authenticates clients
**only via API keys**. Sessions, OAuth, SAML, and any token-exchange
flow are out of scope for v1.

**R-4: Audit log.** Every verify attempt produces one row in the audit
log: key fingerprint, principal, decision, IP, timestamp.

### P1

**R-5: Key rotation.** Operators can rotate a key — issue a replacement
and revoke the original — without an outage for in-flight requests.

## Non-Goals

- OAuth, OIDC, SAML, JWT-based auth — explicitly out for v1.
- Self-service key issuance for end users.
- Federation with external identity providers.
