# HELIX Action: Implementation

You are performing one bounded HELIX execution pass against the built-in
tracker (`helix tracker`).

Your goal is to choose one ready execution issue, implement it completely
without drifting from the authoritative planning stack, satisfy all applicable
project quality gates, create any necessary follow-on issues, commit the work
with explicit issue traceability, close the issue, and exit.

This action is intentionally single-run. It must never loop internally or claim
multiple issues in one invocation. External supervisors may invoke it
repeatedly, but each run handles at most one issue. When the ready queue drains,
the external supervisor should run `workflows/actions/check.md` instead
of continuing blindly.

## Action Input

You may receive:

- no argument
- an explicit issue ID
- a scope selector such as `US-042`, `FEAT-003`, `area:auth`, or `phase:deploy`

Examples:

- `helix implement`
- `helix implement <id>`
- `helix implement US-042`
- `helix implement area:auth`

If no argument is given, choose the best ready HELIX execution issue.

## Authority Order

When artifacts disagree, use this order:

1. Product Vision
2. Product Requirements
3. Feature Specs / User Stories
4. Architecture / ADRs
5. Solution Designs / Technical Designs
6. Test Plans / Tests
7. Implementation Plans
8. Source Code / Build Artifacts

Rules:

- Higher layers govern lower layers.
- Tests govern build execution but do not override requirements or design.
- Source code reflects current state but does not redefine the plan.
- If an issue conflicts with its governing artifacts, do not implement the drift.
- Prefer aligning code and docs to plan. Only propose plan changes when the
  evidence is strong and the governing artifacts are stale or incomplete.

## Tracker Rules

Use the built-in tracker only. Follow:

- `workflows/TRACKER.md`

Issues are stored in `.helix/issues.jsonl`.

This action works only on execution issues. Exclude review issues by default.

Eligible issues are ready (no unresolved blockers) and represent execution work
rather than review work.

Do not claim or implement `phase:review` issues with this action.

## Core Principle

Select the smallest ready issue that unlocks meaningful forward progress and has
enough governing context to execute safely.

Do not pick work just because it is ready. Issues with weak authority, unclear
scope, or missing verification must be refined before implementation.

## PHASE 0 - Bootstrap

0. **Context Recovery**: Re-read AGENTS.md so project instructions are fresh
   in your working memory. After long sessions, context compaction may have
   dropped critical project rules. This step is cheap insurance against drift.
1. Verify the built-in tracker is available.
   - If `helix tracker status` fails, stop immediately.
2. Inspect the current git worktree.
   - Do not revert unrelated changes.
   - If unrelated changes create commit risk, isolate your issue changes rather
     than cleaning the tree destructively.
3. Load project quality and completeness gates.
   - Read relevant HELIX guidance such as `workflows/phases/04-build/enforcer.md`
     and any repo-specific CI, lint, test, security, or release rules.
   - Load ratchet floor fixtures if the project has adopted quality ratchets
     (see `workflows/ratchets.md`). Note the current floors so Phase 7
     can compare against them.

## PHASE 1 - Candidate Discovery

Determine the candidate set:

1. If the input is an explicit issue ID:
   - inspect only that issue
2. If the input is a scope selector:
   - search ready HELIX execution issues matching the selector
3. If no input is given:
   - inspect ready HELIX execution issues, excluding `phase:review`

Use tracker commands such as:

- `helix tracker ready`
- `helix tracker show <id>`
- `helix tracker dep tree <id>`

## PHASE 2 - Candidate Ranking

Rank candidates deterministically.

Prefer, in order:

1. explicit user-selected issue
2. unblocked issue with the clearest governing artifacts
3. issue on or near the critical path because other issues depend on it
4. issue whose acceptance criteria are specific and locally verifiable
5. smallest coherent slice likely to finish cleanly in one run

De-prioritize or reject issues when:

- governing artifacts are missing or contradictory
- acceptance criteria are vague
- required verification is undefined
- the issue is a hidden planning or decision task in execution clothing
- the issue would require broad speculative refactoring to complete

If no candidate is safe to execute, do not claim one. Report the reason and
open a refinement or decision issue if appropriate. Exit cleanly so the
supervisor can run the queue-health check.

## PHASE 3 - Claim And Context Load

For the selected issue:

1. claim it with `helix tracker update <id> --claim`
2. inspect:
   - issue fields and labels
   - `spec-id`
   - parent epic or parent issue
   - dependency tree
   - acceptance text
   - related story, feature, or area labels
3. load the governing artifacts referenced by:
   - `spec-id`
   - issue description
   - parent issue or epic
   - linked user story, feature, design, or test artifacts
4. determine the work phase from labels:
   - `phase:build`
   - `phase:deploy`
   - `phase:iterate`

## PHASE 4 - Pre-Execution Validation

Before editing code or docs, validate:

- the issue is still ready and unblocked
- the governing artifacts are sufficient to execute
- the acceptance criteria match upstream intent
- the verification method is concrete
- there is no upstream contradiction that should be resolved first

If the issue is underspecified or divergent:

- stop implementation
- document the gap
- create the needed follow-on issue such as `decision`, `doc`, or `design`
- leave the current issue open unless it is genuinely invalid

## PHASE 5 - Phase-Appropriate Execution

### `phase:build`

Follow Build-phase discipline strictly:

- implement only what is needed to satisfy the governing tests and artifacts
- do not change test expectations just to make the issue pass
- do not add unspecified features
- keep changes scoped to the issue
- refactor only after verification is green

### `phase:deploy`

Follow Deploy-phase discipline strictly:

- execute rollout, release, monitoring, and runbook work only within the issue scope
- do not expand product behavior or sneak in implementation changes unrelated to deployment safety
- verify rollback and observability expectations where required

### `phase:iterate`

Follow Iterate-phase discipline strictly:

- limit changes to documented cleanup, lessons, backlog, or metrics work
- do not turn iterate work into hidden feature implementation
- capture concrete follow-on execution issues when new work is discovered

## PHASE 6 - Follow-On Issue Capture

If execution reveals additional work:

- create a new issue immediately
- make it atomic and deterministic
- set `spec-id` to the nearest governing artifact
- add the correct HELIX labels
- encode blockers with `helix tracker dep add`

Create follow-on issues when:

- remaining work is outside the current issue scope
- a new bug or cleanup item is discovered
- governing docs must change before more code should land
- deployment or iterate work is exposed by build completion

Do not silently absorb follow-on work into the current issue.

## PHASE 7 - Verification

Run all verification required by the issue and the project.

At minimum, verify:

- the issue acceptance criteria are satisfied
- relevant tests pass
- no previously passing required checks now fail
- lint, type, format, or static analysis gates pass if defined by the project
- docs/config/runbooks are updated where required
- any build, deploy, or iterate phase exit conditions touched by the work are still valid
- ratchet enforcement commands pass if the project has adopted quality ratchets
  (see `workflows/ratchets.md`). If a ratchet auto-bump is triggered,
  include the updated floor fixture in the issue commit.

If the repository defines canonical verification wrappers or proof lanes, use
those wrappers for closure evidence. Narrower package or file commands are for
debugging after the canonical lane fails; they do not replace the maintained
closure surface.

If verification fails:

- fix the problem within the issue scope, or
- leave the issue open with a precise status note and follow-on issues if needed

Do not commit broken work as a completed issue.

If a canonical verification run contradicts a previously closed issue, do not
leave that issue green. Reopen it immediately or create a linked regression issue
that records the exact contradictory command, date, exit status, and reviewed
artifacts.

## PHASE 7.5 - Self-Review

Before committing, perform one quick fresh-eyes review:

1. Re-read the issue acceptance criteria.
2. Re-read the complete diff you are about to commit.
3. For each changed function, ask: "If I were reviewing this code for the
   first time, what would I flag?"
4. Check for: unclosed resources, missing error handling, hardcoded values
   that should be configuration, TODO comments that should be follow-on issues,
   test assertions that are too loose or tautological.

If issues are found, fix them before proceeding to Phase 8.

## PHASE 8 - Commit And Close

If the issue is complete:

1. review the diff for scope discipline
2. create a comprehensive commit that references the issue ID
3. include in the commit message:
   - issue ID
   - concise summary
   - governing artifact references where helpful
   - verification summary
4. close the issue with `helix tracker close <id>`

If the worktree contains unrelated changes, commit only the files that belong to
the issue. Never revert unrelated work just to simplify the commit.

## PHASE 9 - Output

Report:

1. Selected Issue
2. Why It Was Chosen
3. Governing Artifacts
4. Work Completed
5. Follow-On Issues Created
6. Verification Performed
7. Commit Created
8. Final Issue Status
9. Open Risks Or Decisions

Be precise and deterministic.
