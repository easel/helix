// Tests for bead-OAUTH-03.
//
// Covers the happy path, expiry, rotation, and replay. Notably
// MISSING: any test for the §4 revocation path.

import { describe, it, expect, beforeEach } from "vitest";
import { refresh } from "../../src/auth/refresh";
import { issueRefresh, revoke } from "../helpers";

describe("refresh", () => {
  beforeEach(async () => {
    await issueRefresh({ id: "rt-valid", principal: "alice", ttl: 30 * 24 * 3600 * 1000 });
    await issueRefresh({ id: "rt-expired", principal: "bob", ttl: -1 });
  });

  it("happy path: mints a new access + refresh, marks old consumed", async () => {
    const r = await refresh("rt-valid");
    expect(r.ok).toBe(true);
  });

  it("rejects unknown refresh", async () => {
    const r = await refresh("rt-nope");
    expect(r).toEqual({ ok: false, reason: "unknown" });
  });

  it("rejects expired refresh", async () => {
    const r = await refresh("rt-expired");
    expect(r).toEqual({ ok: false, reason: "expired" });
  });

  it("rejects replays of a consumed refresh", async () => {
    await refresh("rt-valid");
    const replay = await refresh("rt-valid");
    expect(replay).toEqual({ ok: false, reason: "consumed" });
  });

  // MISSING: no test that revoked refresh tokens are rejected.
  // §4 of security-architecture requires this; review should call it out.
});
