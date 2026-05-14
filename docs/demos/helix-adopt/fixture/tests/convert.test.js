import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";

test("c-to-f 100 → 212", () => {
  const out = execFileSync("node", ["src/convert.js", "c-to-f", "100"]).toString().trim();
  assert.equal(out, "212");
});

test("f-to-c 212 → 100", () => {
  const out = execFileSync("node", ["src/convert.js", "f-to-c", "212"]).toString().trim();
  assert.equal(out, "100");
});
