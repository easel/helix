# Security Architecture

## §3 Token lifecycle

### §3.1 Issuance

Access tokens are signed JWTs, 15-minute TTL. Refresh tokens are
opaque, server-side-only, 30-day TTL, single-use.

### §3.2 Refresh

The refresh endpoint validates the refresh token, mints a new access
token AND a new refresh token (rotation), and marks the prior refresh
as consumed. Replays of consumed refresh tokens MUST be rejected.

## §4 Revocation

Every refresh and verify call MUST consult the revocation list. A
revoked token grants no access, regardless of expiry. The revocation
list is checked before any token-derived claim is honored.

The revocation event also unwinds any active access tokens issued
from the revoked refresh chain (best-effort; the access TTL caps the
exposure window).

## §5 Audit

Every refresh produces a row: prior-refresh-fingerprint,
new-refresh-fingerprint, principal, IP, timestamp, decision.
