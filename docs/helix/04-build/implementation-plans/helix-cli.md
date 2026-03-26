# HELIX Implementation Plan: helix-cli

**Status**: backfilled
**Backfill Date**: 2026-03-25

## Implementation Boundaries

- Keep `scripts/helix` as the single wrapper entrypoint.
- Keep tracker mechanics in `scripts/tracker.sh`.
- Keep installation concerns in `scripts/install-local-skills.sh`.
- Keep wrapper verification in `tests/helix-cli.sh`.
- Treat `workflows/` action files as the source of truth for delegated action
  behavior.

## Build Sequencing

1. Update the governing HELIX specs first.
2. Update deterministic tests second.
3. Update the wrapper and tracker implementation third.
4. Update user-facing workflow docs last.

## Build Rules

1. Change `helix run` command routing, prompts, or loop behavior in
   `scripts/helix` only after the feature, design, and test plan describe the
   target contract.
2. Change tracker storage, ownership metadata, queue semantics, or claim
   recovery in `scripts/tracker.sh` only when the tracker contract is updated
   to match.
3. Add or update deterministic tests in `tests/helix-cli.sh` before or with
   any wrapper behavior change.
4. Change local setup behavior in `scripts/install-local-skills.sh` only when
   launcher or skill installation requirements change.
5. Update user-facing command docs and workflow docs when the CLI surface,
   queue contract, or safety contract changes.

## Contract Rules

- `WAIT` is terminal for `helix run` unless the governing spec explicitly says
  otherwise.
- `BACKFILL` is handled by stopping the loop and surfacing the exact
  `helix backfill <scope>` handoff command.
- Recovery must be non-destructive by default and must not revert unrelated
  work.
- Claim ownership must be explicit enough to distinguish active work from a
  stale claim.
- Review findings must have a defined effect on loop control, issue state, or
  follow-on issue creation.
- Completed-cycle accounting must count successful implementation passes, not
  failed attempts or recovery-only iterations.

## Required Validation

When wrapper behavior or the HELIX execution contract changes, run:

```bash
bash tests/helix-cli.sh
git diff --check
```

## Operational Notes

- Agent selection is runtime-configurable through `HELIX_AGENT`,
  `--agent`, `--claude`, and `--codex`.
- `HELIX_LIBRARY_ROOT` can redirect the workflow library root.
- `HELIX_TRACKER_DIR` can redirect the tracker directory.
- Session stderr is tee'd into `.helix-logs/`.

## Follow-On Expectations

- Any change that affects `backfill`, `check`, or `run` should preserve the
  machine-readable contracts consumed by automation.
- Any change that affects tracker readiness or ownership must preserve
  dependency-aware queue behavior and stable claim semantics.
- Any change that affects recovery must preserve unrelated working tree
  changes.
- Any change that affects review handling must keep review findings visible to
  the loop controller and follow-on issue flow.
- Any change that affects installation must preserve creation of
  `~/.local/bin/helix`.

## Evidence

- `scripts/helix:17-37`
- `scripts/helix:40-94`
- `scripts/helix:250-305`
- `scripts/helix:451-519`
- `scripts/tracker.sh:7-18`
- `scripts/tracker.sh:265-420`
- `scripts/install-local-skills.sh:35-67`
- `tests/helix-cli.sh:440-447`
- `tests/helix-cli.sh:637-665`
- `workflows/REFERENCE.md:149-154`
