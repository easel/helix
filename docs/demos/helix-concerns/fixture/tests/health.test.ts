// DRIFT: imports vitest instead of bun:test.
// The typescript-bun concern requires bun:test; align should flag this.
import { describe, it, expect } from "vitest";

describe("GET /health", () => {
  it("placeholder — needs a real HTTP harness once server is fixed", () => {
    expect(1 + 1).toBe(2);
  });
});
