#!/usr/bin/env node
const [, , direction, valueRaw] = process.argv;
const value = Number(valueRaw);
if (Number.isNaN(value)) {
  console.error("usage: convert <c-to-f|f-to-c> <number>");
  process.exit(2);
}
if (direction === "c-to-f") {
  console.log(value * 9 / 5 + 32);
} else if (direction === "f-to-c") {
  console.log((value - 32) * 5 / 9);
} else {
  console.error(`unknown direction: ${direction}`);
  process.exit(2);
}
