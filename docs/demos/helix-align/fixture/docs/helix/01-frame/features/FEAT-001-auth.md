# FEAT-001 — API-key authentication

## Summary

The verify endpoint. Clients send `X-API-Key: <opaque>`; the service
checks the key against the issued/revoked tables and returns the
principal or 401.

## User stories

- **US-AUTH-1** — As an internal service I send my API key and learn
  the calling principal so my application can authorize the request.
- **US-AUTH-2** — As an operator I can revoke a leaked key from the
  CLI and have it rejected within a minute.

## Acceptance

- `POST /verify` with a valid `X-API-Key` returns `{principal, issued_at}`
  and status 200.
- `POST /verify` with an unknown or revoked key returns 401 with no
  principal leak.
- `auth-cli revoke <fingerprint>` causes subsequent verifies to fail
  within 60s.

## Out of scope

OAuth, sessions, JWTs — see ADR-002 (superseded ADR-001's plan to
include OAuth in v1).
