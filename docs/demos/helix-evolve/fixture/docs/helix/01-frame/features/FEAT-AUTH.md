# FEAT-AUTH — API-key authentication

## Summary

The `POST /verify` endpoint. Clients send `X-API-Key`; service answers
200 with the principal or 401.

## User stories

- **US-AUTH-1** — As an internal service, I send my API key and learn
  the calling principal so my app can authorize the request.
- **US-AUTH-2** — As an operator, I can revoke a leaked API key from
  the CLI within 60 seconds.

## Acceptance

- 200 with `{principal, issued_at}` for valid key.
- 401 for unknown/revoked key, no principal leak.
- Revoke takes effect within 60s of CLI commit.

## Out of scope

OAuth, sessions, JWTs — see PRD non-goals.
