# Proof of Concept: Bounded Queue-Drain via `ddx agent execute-loop --once`

**PoC ID**: POC-001 | **Lead**: HELIX maintainers | **Time Budget**: 3 days | **Status**: Completed

> Example scenario reconstructed from the integration work that preceded ADR-001 and CONTRACT-001. The authoritative architecture record is in `docs/helix/02-design/architecture.md`; this PoC is illustrative.

## Objective

**Primary Question**: Does `ddx agent execute-loop --once` provide bounded execution semantics sufficient for HELIX's supervisory contract — i.e., does it claim and run exactly one ready bead, return control with an actionable outcome, and let HELIX make all post-cycle decisions itself?

**Success Criteria**:
- **Functional**: `--once` claims, executes, and lands or preserves a single bead, then exits with a parseable JSON outcome that names the executed bead, its status, and base/result revisions.
- **Performance**: One cycle completes in time bounded by the agent's own runtime — DDx adds no unbounded waits.
- **Integration**: HELIX wrapper code can run a cycle, parse the outcome, and proceed to post-cycle bookkeeping without inspecting DDx-internal state.
- **Failure-mode coverage**: Bead failure (`execution_failed`), preserved-with-conflict (`land_conflict`), post-run check failure, and "no claimable work" each return distinct, well-formed status values.
- **Concurrency safety**: A second `helix run` invocation against the same project does not race the first into double-claiming a bead.

**In Scope**: `--once` semantics, JSON outcome shape, single-bead claim/execute/close cycle, evidence-capture surface visible to HELIX.

**Out of Scope**: Multi-bead drain modes, polling intervals, harness-specific behavior (Claude vs OpenRouter vs MLX), HELIX-side review/alignment injection, performance benchmarking beyond "doesn't deadlock."

## Approach

**Architecture Pattern**: Delegate execution mechanics to DDx; HELIX wraps with supervisory policy only.

**Key Technologies**:
- **Primary**: `ddx agent execute-loop --once --json`, Bash + jq orchestration in `scripts/helix`.
- **Integration**: `.ddx/beads.jsonl` tracker, isolated worktrees managed by DDx, agent harnesses dispatched by DDx.

## Implementation

### Architecture Overview
```
helix run (Bash)
  └─ ddx agent execute-loop --once --json
       ├─ ReadyExecution() → pick one bead
       ├─ checkpoint dirty tree → isolated worktree
       ├─ dispatch agent (harness-resolved)
       ├─ post-run checks
       ├─ rebase + fast-forward land  OR  preserve under hidden ref
       └─ emit JSON: {attempts, successes, failures, results[]}
  └─ jq: extract results[].bead_id, status, result_rev
  └─ HELIX post-cycle: cycle counter, review/alignment injection,
                        context refresh, escalation policy
```

### Core Components

#### `helix run` orchestrator (HELIX-side)
- **Purpose**: Apply supervisory policy across cycles. Decide when to inject review/alignment, when to refresh context, when to escalate.
- **Implementation**: Bash + jq, ~200 lines of pipeline over `ddx` CLI JSON output. No claim/close logic; no `git checkout -- .`; no retry/backoff.

#### `ddx agent execute-loop --once` (DDx-side, observed only)
- **Purpose**: Bounded queue-drain primitive. Owns claim/execute/close mechanics for one bead.
- **Implementation**: Go binary; HELIX treats it as a black box and validates only the documented outcome surface.

### Integration Points

| Integration | Type | Status | Notes |
|-------------|------|--------|--------|
| `ddx agent execute-loop --once --json` | CLI + JSON | Working | Returns the documented `{attempts, successes, failures, results[]}` shape |
| `ddx bead blocked` | CLI | Working | Surfaces `retry-after` cooldowns DDx sets on failed attempts |
| `.ddx/beads.jsonl` | File-backed tracker | Working (DDx owns writes) | HELIX reads only via `ddx bead` commands |
| Isolated worktree lifecycle | Filesystem | Working | DDx owns creation, cleanup, orphan recovery |

## Results

### Test Scenarios

| Scenario | Result | Status |
|----------|--------|--------|
| One ready bead, agent succeeds, fast-forward lands | `results[0].status = success`, `result_rev` is the landed SHA | Pass |
| One ready bead, agent fails non-zero | `status = execution_failed`, attempt preserved under hidden ref, no tracker mutation | Pass |
| One ready bead, rebase conflict during landing | `status = land_conflict`, attempt preserved, `retry_after` set | Pass |
| One ready bead, post-run check fails | `status = post_run_check_failed`, attempt preserved | Pass |
| No ready beads in queue | `attempts = 0`, `results = []`, exit 0 | Pass |
| Two `helix run` invocations against same project | Second invocation either picks a different bead or sees no claimable work; no double-claim | Pass |
| Bead with malformed frontmatter | `status = structural_validation_failed`, no execution attempted | Pass |
| Concurrent operator edits to a bead during a cycle | Cycle completes against the version DDx claimed; HELIX detects drift at next `helix check` | Pass (per ADR-002 expectations) |

### Findings

- **FINDING 1**: `--once` returns control to HELIX after exactly one bead, regardless of outcome.
  - **Evidence**: All eight scenarios above terminate the DDx process and emit a single JSON object on stdout.
  - **Implications**: HELIX's supervisory contract from ADR-001 is preserved. There is no need for a HELIX-owned execution loop.

- **FINDING 2**: The JSON outcome shape carries enough evidence for HELIX post-cycle bookkeeping with no DDx-internal inspection.
  - **Evidence**: `results[].bead_id`, `status`, `base_rev`, `result_rev`, `session_id`, `retry_after` cover every post-cycle decision HELIX needs to make: cycle counting, closing-SHA sync, retry suppression handoff, evidence-link surfacing.
  - **Implications**: HELIX can delete its own retry/backoff, blocker tracking, and orphan worktree recovery code.

- **FINDING 3**: HELIX must not pre-select a bead.
  - **Evidence**: Setting `HELIX_SELECTED_ISSUE` had no effect — DDx ignores it. When HELIX assumed the bead it pre-selected matched `results[0].bead_id`, and DDx had picked a different ready bead, post-cycle bookkeeping closed the wrong issue in an early attempt.
  - **Implications**: HELIX must use `results[].bead_id` from the actual cycle for all post-cycle work. Queue curation (via `execution-eligible`, `dep-ids`, `superseded-by`) is the right control surface, not pre-selection.

- **FINDING 4**: A `preserved` outcome is not a HELIX physics-level conflict.
  - **Evidence**: A `land_conflict` returned `status = land_conflict` and a `retry_after` hint. HELIX treated it as a workflow-interpretation point: continue with another bead, escalate, or create a follow-on bead. None of those required HELIX to reach into DDx state.
  - **Implications**: The HELIX conflict taxonomy (resolvable vs physics-level) is separable from the DDx execution outcome (merged vs preserved). Confusing the two pushes platform concerns into HELIX.

### Risks

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| DDx silently changes the JSON outcome shape | Medium | High | Pin schema in CONTRACT-001; add a HELIX integration test that fails fast on schema drift |
| HELIX wrappers re-introduce claim/close logic to "fix" edge cases | Medium | High | Validation checklist in CONTRACT-001 forbids parallel claim mechanics |
| Operators expect HELIX-side retry behavior and are confused by `retry-after` | Low | Low | Surface DDx cooldowns through `ddx bead blocked`; document the ownership transfer |

## Analysis

**Overall Assessment**: VIABLE

**Rationale**: `--once` provides exactly the supervisory primitive HELIX needs. Every test scenario terminated cleanly, returned a parseable outcome, and required no HELIX-side execution mechanics. The remaining risks are interface-stability risks, not feasibility risks.

## Recommendations

1. Adopt `ddx agent execute-loop --once --json` as the single execution lane for `helix run`. -- Eliminates a parallel substrate; aligns with ADR-001 supervisory model. -- Next planning cycle.
2. Codify the JSON outcome shape as a contract in CONTRACT-001, including all `status` values and the outcome-to-status mapping. -- Drift-detection contract. -- Same cycle.
3. Delete HELIX-side retry/backoff, blocker tracking, orphan worktree recovery, and `git checkout -- .` cleanup. -- These now belong to DDx; keeping them creates two competing implementations. -- Same cycle.
4. Add a HELIX integration test that fails fast on schema drift in `--once --json`. -- Makes future DDx changes loud rather than silent. -- Same cycle.

### Follow-up
- [ ] ADR-001 to ratify the supervisory delegation model.
- [ ] CONTRACT-001 to ratify the boundary including JSON schema.
- [ ] TD update for `helix run` describing the post-cycle bookkeeping pipeline against `results[]`.
- [ ] Tracker-write-safety PoC (separately) against ADR-002 to confirm concurrent local refinement does not corrupt the JSONL tracker.
