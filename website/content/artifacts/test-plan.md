---
title: "Test Plan"
slug: test-plan
phase: "Test"
weight: 300
generated: true
aliases:
  - /reference/glossary/artifacts/test-plan
---

## What it is

The project-level test plan defines the testing strategy for the full
project: test levels and scope, framework choices, coverage targets,
critical paths, test data strategy, infrastructure requirements, and
sequencing. It drives failing tests before implementation begins and
provides traceability from requirements to test execution.

## Phase

**[Phase 3 — Test](/reference/glossary/phases/)** — Define how we know it works. Plans, suites, and procedures that bind specs to implementation.

## Output location

`docs/helix/03-test/test-plan.md`

## Relationships

### Requires (upstream)

- [Technical Design](../technical-design/) — tests validate design
- [User Stories](../user-stories/) — tests verify acceptance criteria
- [Security Requirements](../security-requirements/) — informs security tests *(optional)*

### Enables (downstream)

- [Test Suites](../test-suites/) — actual test implementation

### Informs

- [Test Suites](../test-suites/)
- [Implementation Plan](../implementation-plan/)

### Referenced by

- [Test Suites](../test-suites/)
- [Implementation Plan](../implementation-plan/)
- [Security Tests](../security-tests/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Test Plan Generation Prompt

Create the project-level test plan for the Test phase. Keep it concise, but include the minimum structure needed to drive failing tests before implementation.

## Storage Location

`docs/helix/03-test/test-plan.md`

## What to Include

- test levels and scope
- framework choices only where they matter
- coverage targets and critical paths
- test data strategy
- sequencing, dependencies, and infrastructure needs
- risks that can block test execution

## Keep In Mind

- tests are the executable specification
- every test should trace to a requirement or story
- do not add generic testing doctrine that the template already implies

Use template at `.ddx/plugins/helix/workflows/phases/03-test/artifacts/test-plan/template.md`.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
---
ddx:
  id: helix.test-plan
  depends_on:
    - helix.architecture
---
# Test Plan

## Testing Strategy

**Goals**: [Primary objective] | [Quality gates]
**Out of Scope**: [Excluded areas]

### Test Levels

| Level | Coverage Target | Priority |
|-------|-----------------|----------|
| Contract | [Target] | P0/P1 |
| Integration | [Target] | P0/P1 |
| Unit | [Target] | P0/P1 |
| E2E | [Target] | P0/P1 |

### Frameworks

| Type | Framework | Reason |
|------|-----------|--------|
| Contract | [Framework] | [Why] |
| Integration | [Framework] | [Why] |
| Unit | [Framework] | [Why] |
| E2E | [Framework] | [Why] |

## Test Data

| Type | Strategy |
|------|----------|
| Fixtures | [Static data approach] |
| Factories | [Dynamic generation] |
| Mocks | [External service mocking] |

## Coverage Requirements

| Metric | Target | Minimum | Enforcement |
|--------|--------|---------|-------------|
| Line | 80% | 70% | CI blocks |
| Critical | 100% | 100% | Required |

### Critical Paths (P0)

1. [Auth flow]
2. [Core transaction]
3. [Data persistence]
4. [Error handling]

### Secondary Paths (P1-P2)

- P1: [Secondary features] | P2: [Edge cases, rare scenarios]

## Implementation Order
1. [What must be written first and why]
2. [What follows]
3. [What can wait]

## Infrastructure

| Requirement | Specification |
|-------------|---------------|
| CI Tool | [Tool, version] |
| Test DB | [Type, seeding, cleanup] |
| Services | [Required services] |

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Flaky tests | High | Retry logic, isolation |
| Slow execution | Med | Parallelize |

**Known Gaps**: [Limitations and accepted risks]

## Build Handoff

**Commands**: `[test command]` | `[coverage command]`
**Priority**: [Recommended order]

## Review Checklist

Use this checklist when reviewing a test plan:

- [ ] Test levels cover contract, integration, unit, and E2E with coverage targets
- [ ] Framework choices are justified and consistent with project concerns
- [ ] Critical paths (P0) are identified and have 100% coverage requirements
- [ ] Test data strategy covers fixtures, factories, and mocks
- [ ] Coverage requirements have both targets and minimums with enforcement rules
- [ ] Implementation order is justified — what must be tested first and why
- [ ] Infrastructure requirements are specific (tool versions, service deps)
- [ ] Risks include flaky test mitigation and slow execution strategies
- [ ] Known gaps are documented with accepted risk rationale
- [ ] Build handoff commands are concrete and runnable
- [ ] Test plan traces back to acceptance criteria from governing feature specs
- [ ] No untested P0 requirement — every P0 acceptance criterion has a test
``````

</details>

## Example

This example is HELIX's actual test plan, sourced from [`docs/helix/03-test/test-plans/TP-002-helix-cli.md`](https://github.com/DocumentDrivenDX/helix/blob/main/docs/helix/03-test/test-plans/TP-002-helix-cli.md). It shows how this artifact is used in a live methodology project; it may include project-specific context.

## Test Plan: TP-002-helix-cli

**Status**: backfilled
**Backfill Date**: 2026-03-25

### Test Objective

Protect the wrapper CLI contract with deterministic shell tests that exercise
queue control, tracker semantics, prompt construction, installer behavior, and
command-specific safety rules.

### Primary Verification Command

```bash
bash tests/helix-cli.sh
```

### Covered Behaviors

#### Tracker (`ddx bead` over `.ddx/beads.jsonl`)

- issue creation and display
- dependency-aware ready and blocked queries
- claim flow setting `in_progress` and assignee
- `--claim` records `claimed-at` (ISO-8601 UTC) and `claimed-pid` metadata
- `--unclaim` restores `open` status and clears claim metadata
- claimed work remains owned until it is explicitly released or closed
- tracker update coverage for execution metadata fields including
  `execution-eligible`, `superseded-by`, and `replaces`
- tracker status summary
- lock timeout reports the recorded owner and fails closed
- execution-safe ready queries exclude refinement and superseded work

#### Wrapper Help and Dry-Run Output

- `help` lists supported commands and key options
- `check --dry-run` prints the expected agent invocation and action reference
- `backfill --dry-run` includes writable-session and trailer requirements
- `design`, `polish`, `review`, and `experiment` dry-runs include their scoped
  prompt details
- `build --dry-run` and `triage` surfaces reflect the converged command and
  tracker-validation contract
- `align --dry-run` and `align` behavior reflect the bead-governed alignment
  contract rather than an ad hoc standalone review path

#### Loop, Queue, and Cycle Control

- `run` stops after the queue drains
- `check` can emit `DESIGN` and `POLISH` when design or issue refinement must happen before execution resumes
- `run` dispatches bounded `design` and `polish` passes from queue-drain `NEXT_ACTION` results, then re-checks before build resumes
- `run --review-every N` triggers periodic alignment
- `run` auto-aligns once after `NEXT_ACTION: ALIGN`
- `run` surfaces alignment failures
- `align` acquires or creates the governing `kind:planning,action:align` bead
  before it writes reports or follow-on issues
- `run` treats `NEXT_ACTION: WAIT` as terminal and does not attempt an unblock build pass
- `run` surfaces `NEXT_ACTION: BACKFILL` as a distinct terminal branch rather than collapsing it into `WAIT` or `STOP`
- `run --max-cycles N` counts successful build completions, not failed attempts
- failed implementation attempts do not advance completed-cycle counters or periodic alignment timing
- Codex token accounting captures the `tokens used` footer when Codex emits it
  on stderr
- `.helix/context.md` is regenerated at run start, on epic switch, and every 5
  completed build cycles with Quick Reference build/test commands and current
  issue counts
- `run` revalidates selected work before claim and before close using tracker
  fingerprints (spec-id, parent, superseded-by, replaces)
- interactive refinement during a live run is surfaced as queue drift rather
  than stale claim/close behavior
- parent field changes during execution are detected as queue drift
- spec-id changes during execution are detected as queue drift
- supersession during execution is detected as queue drift and blocks a stale
  close
- `run` stays focused on an active epic until its child work finishes or a
  blocker releases focus
- `run` retries difficult issues with bounded exponential backoff
  (`min(5 * 2^(attempt-1), 40)` seconds, 4 attempts max) before blocking
- backoff delay formula produces correct values (5, 10, 20, 40s cap)
- intractable child blocks the parent epic during epic focus
- `run` expands batch selection to shared `area:*` labels when parent and
  `spec-id` metadata do not produce siblings
- `run` emits blocker reports, cycle timing, and token-usage observability
  data for `helix status`

#### Backfill Contract

- `backfill` fails when `BACKFILL_REPORT` is missing
- `backfill` succeeds only when the declared report file exists

#### Recovery and Review

- orphan recovery reclaims stale issues when PID is dead and claim age exceeds
  `HELIX_ORPHAN_THRESHOLD` (default 7200s)
- orphan recovery skips issues with fresh `claimed-at` timestamps
- orphan recovery does not destroy unrelated worktree changes
- orphan recovery does not unclaim legitimately active work without sufficient evidence
- recovery is issue-scoped and non-destructive by default
- failed or timed-out implementation attempts leave the worktree clean for the
  next retry or stop with an explicit blocker instead of retrying atop stale
  local state
- failed or timed-out implementation attempts release stale claims via
  `--unclaim` before a fresh retry path resumes
- `run` invokes post-implementation review when enabled
- `run --review-agent <other-agent>` switches review to a second model for
  cross-model verification (tested in live run, not just dry-run)
- `REVIEW_STATUS: CLEAN` allows the loop to continue
- `REVIEW_STATUS: ISSUES_FOUND` with `ISSUES_COUNT` and `FINDINGS_FILED`
  trailers is parsed and the loop continues
- review findings are surfaced and redirect or stop the loop rather than being ignored
- epic closure triggers a scoped post-epic review

#### Summary Mode

- `--summary` flag is accepted and implies `--quiet`
- summary output contains concise cycle lines with issue IDs and completion
  status
- verbose detail (tool calls, prompt echo, gate results) goes to log file only
- summary output includes log-file line-range pointers for diagnostics
- `--summary` is listed in help output

#### BUILD Loop Breaker

- consecutive empty BUILD cycles (check returns BUILD, no issue selectable)
  stop after 2 iterations
- orphan recovery is attempted before stopping
- if recovery frees issues, the loop continues

#### Commit

- `commit` fails with nothing to commit
- `commit <issue-id>` stages, runs build gate, commits with issue title,
  and closes the tracker issue
- `commit` without issue ID generates a summary from changed filenames
- `commit` auto-stages unstaged modifications when nothing is staged

#### Issue Selection Priority

- `run` prefers non-epic tasks with execution metadata (spec-id, acceptance,
  or design) over epics when selecting from the ready queue

#### Utility Commands

- `next` returns the first ready issue or `no ready issues`
- `experiment` requires a clean worktree
- `experiment --close` includes close-session guidance
- `status` reports persisted run-controller state and blocker summaries
- `triage` enforces required create fields instead of allowing partially
  specified HELIX issues
- installer creates the local `helix` launcher

### Test Method

- Create isolated temporary git workspaces
- Inject mock `codex` and `claude` binaries
- Seed `.ddx/beads.jsonl` (the `ddx bead` tracker store) with known issue graphs
- Assert exact stdout or stderr fragments and filesystem side effects

### Test Count

133 deterministic tests verified by `bash tests/helix-cli.sh`.

### Port Safety

The test harness is implementation-language-agnostic. To verify a port to
another language, change the `run_helix()` helper to invoke the new binary
instead of `bash scripts/helix`. All mock agents, tracker JSONL assertions,
and stderr output checks work unchanged.

### Known Gaps

- The current harness validates prompt shape and loop behavior, not live remote
  agent correctness.
- The harness should be extended if `check` grows additional machine-readable
  trailers beyond `NEXT_ACTION` that affect loop control.
- The harness should be extended when `helix status` begins exposing richer
  lifecycle history than the initial run-controller snapshot contract.

### Evidence

- `docs/helix/01-frame/features/FEAT-002-helix-cli.md`
- `docs/helix/02-design/technical-designs/TD-002-helix-cli.md`
- `workflows/EXECUTION.md`
- `workflows/TRACKER.md`
- `tests/helix-cli.sh`
