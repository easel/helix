# ADR-002 — Pivot to OAuth for v1 authentication

**Status:** proposed
**Date:** 2026-05-10
**Supersedes:** ADR-001 (API-key-only design)

## Context

Two of our new internal-tool consumers (Genie, the AI-ops platform) sent
clarifying questions on key rotation that revealed an underlying need
for short-lived tokens and per-user identity, not service-level shared
secrets. The platform-security team is also drafting a policy that
discourages bare API keys for new internal services starting Q3.

## Decision

Adopt OAuth 2.1 (authorization-code with PKCE for users, client-credentials
for services) as the v1 authentication mechanism. The existing
API-key path becomes a compatibility shim for legacy consumers and
will be deprecated by end of v1.

## Consequences

- Need to author a security-architecture artifact covering token
  lifecycle, refresh, and revocation.
- FEAT-001 user stories need to be re-cut for the OAuth flow; new
  stories for refresh and revoke.
- The current test plan tests only the API-key path; needs expansion.
- The PRD's R-3 ("authenticates **only via** API keys") becomes false
  and must be revised before this ADR can move to `accepted`.
