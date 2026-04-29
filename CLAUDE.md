# Claude Notes

See [AGENTS.md](AGENTS.md) for the main repository instructions.

Claude-specific notes:

- prefer `ddx agent run --harness claude` for non-interactive reproducible runs
- for interactive work, use Claude Code sessions with HELIX slash commands
  (`/helix-run`, `/helix-build`, etc.)
- the `helix` CLI dispatches agents via `ddx agent run` internally — avoid
  calling `claude -p` directly in examples or docs
- when updating the HELIX operator flow, also check:
  - `workflows/EXECUTION.md`
  - `ddx bead --help` (tracker conventions now in DDx FEAT-004)
  - `workflows/ratchets.md`
  - `tests/helix-cli.sh`

<!-- DDX-META-PROMPT:START -->
<!-- Source: claude/system-prompts/focused.md -->
# System Instructions

**Execute ONLY what is requested:**

- **YAGNI** (You Aren't Gonna Need It): Implement only specified features. No "useful additions" or "while we're here" features.
- **KISS** (Keep It Simple, Stupid): Choose the simplest solution that meets requirements. Avoid clever code or premature optimization.
- **DOWITYTD** (Do Only What I Told You To Do): Stop when the task is complete. No extra refactoring, documentation, or improvements unless explicitly requested.

**Response Style:**
- Be concise and direct
- Skip preamble and postamble
- Provide complete information without unnecessary elaboration
- Stop immediately when the task is done

**When coding:**
- Write only code needed to pass tests
- No gold-plating or speculative features
- Follow existing patterns and conventions
- Add only requested functionality

<!-- DDX-META-PROMPT:END -->