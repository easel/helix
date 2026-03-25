# Claude Notes

See [AGENTS.md](AGENTS.md) for the main repository instructions.

Claude-specific notes:

- prefer `claude -p` for non-interactive reproducible runs
- for the HELIX execution loop, the documented high-permission form is:

```bash
claude -p \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  --no-session-persistence
```

- when updating the HELIX operator flow, also check:
  - `workflows/helix/EXECUTION.md`
  - `workflows/helix/BEADS.md`
  - `workflows/helix/ratchets.md`
  - `tests/helix-cli.sh`
