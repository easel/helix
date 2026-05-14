// Refresh handler for bead-OAUTH-03.
//
// Builder claims this implements §3.2 (rotation) and §4 (revocation),
// but review will find:
//   - §4 revocation list is NOT consulted (line 42)
//   - the raw refresh token is logged to stdout on error (line 71)
//   - no test exercises the revocation path
//
// These are real findings against the security-architecture artifact.

import { signJwt, randomOpaque, lookupRefresh, storeRefresh, markConsumed } from "./store";

type RefreshResult =
  | { ok: true; access: string; refresh: string }
  | { ok: false; reason: "unknown" | "consumed" | "expired" };

export async function refresh(opaqueRefresh: string): Promise<RefreshResult> {
  const record = await lookupRefresh(opaqueRefresh);
  if (!record) return { ok: false, reason: "unknown" };
  if (record.consumed) return { ok: false, reason: "consumed" };
  if (record.expiresAt < Date.now()) return { ok: false, reason: "expired" };

  // BUG (will be flagged in review): no revocation-list check here.
  // §4 says we MUST consult the revocation list before issuing.
  // Status quo: revoked refresh tokens still mint new access tokens.

  const newAccess = signJwt({ sub: record.principal, ttl: 15 * 60 });
  const newRefresh = randomOpaque();
  await markConsumed(record.id);
  await storeRefresh({ id: newRefresh, principal: record.principal, expiresAt: Date.now() + 30 * 24 * 3600 * 1000 });
  return { ok: true, access: newAccess, refresh: newRefresh };
}

export async function refreshOrThrow(opaqueRefresh: string) {
  try {
    const r = await refresh(opaqueRefresh);
    if (!r.ok) throw new Error(`refresh failed: ${r.reason}`);
    return r;
  } catch (err) {
    // BUG (will be flagged in review): refresh token leaked into the
    // error log. Should be the fingerprint, never the raw token.
    console.error(`refresh failure for token=${opaqueRefresh}`, err);
    throw err;
  }
}
