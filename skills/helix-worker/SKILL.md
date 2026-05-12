---
name: helix-worker
description: Launch a HELIX operator loop in the background and monitor progress.
argument-hint: '[--agent codex|claude] [--max-cycles N] [helix run options...]'
---

# Worker

Launch the HELIX operator loop as a background process and monitor progress.
Use this skill when the user wants HELIX work to proceed while they continue
working interactively.

The worker is for background control of the runtime's existing execution loop.
It should not replace managed execution with a custom agent loop.

## When to Use

- the user wants HELIX work to run in the background
- long-running execution would waste interactive context
- the user wants to monitor progress without blocking the conversation
- the user says "run helix", "start working", or "grind through the queue"

## When Not to Use

- the user wants live adjustments between cycles; use `helix-run`
- a single issue needs implementing; use `helix-build`
- the user wants status only; use the project's status surface

## Methodology

1. Launch the operator loop with concise progress output enabled.
2. Capture stdout, stderr, process ID, and log location.
3. Monitor progress from summary lines rather than dumping full logs.
4. On failure or blockage, read only the indicated log range.
5. After completion, inspect ready and blocked work through the project tracker.
6. Report completed, skipped, blocked, and failed work clearly.

## Running with DDx

`helix run` remains a compatibility controller over `ddx agent execute-loop --once`
plus HELIX supervisory routing.

Launch:

```bash
cd <target-repo> && helix run --agent claude --summary --max-cycles 10 2>&1
```

Key flags:

- `--summary` (required) — routes verbose output to log file, emits concise progress lines
- `--agent codex|claude` — which agent to dispatch
- `--model <model>` — specific model, such as `gpt-5.3-codex-spark`
- `--max-cycles N` — stop after N completed build passes
- `--review-every N` — run fresh-eyes review every N cycles
- `--no-auto-align` — skip periodic alignment checks
- `--no-auto-review` — skip post-build reviews

Environment override:

```bash
HELIX_AGENT_TIMEOUT=1800
```

Summary output looks like:

```text
helix: [14:24:01] cycle 1: hx-42 (5 ready)
helix: [14:24:35] codex complete (rc=0, 34s, 892 tokens) - log L12-L340 in .helix-logs/helix-...log
helix: [14:24:36] cycle 1: hx-42 -> COMPLETE (1/3 done, 892 tokens)
helix: === run complete: 3 attempted, 2 completed, 1 skipped, 2400 tokens ===
```

When a cycle fails or blocks, read the log range:

```bash
sed -n '500,800p' .helix-logs/helix-20260402-142401.log
```

After completion:

```bash
helix status
ddx bead ready --execution
ddx bead blocked --json
```

Legacy wrapper blocker reports under `.helix-logs/blockers-*.md` may still
exist during the migration, but the durable contract is the DDx tracker.

Examples:

```bash
helix run --agent claude --summary --max-cycles 10 2>&1
HELIX_AGENT_TIMEOUT=1800 helix run --agent codex --model gpt-5.3-codex-spark --summary 2>&1
helix status
cat .helix-logs/helix-*.log | tail -50
```
