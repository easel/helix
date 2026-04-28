<bead-review>
  <bead id="helix-00e2486f" iter=1>
    <title>Audit CONTRACT-001 DDx-owned items against actual DDx implementation</title>
    <description>
Walk CONTRACT-001's DDx-owned responsibility list (sections: Agent execution substrate, Execution and metric substrate, Git-context execution mechanics, Always-on runtime metrics, Post-Cycle HELIX Behavior table). For every DDx-owned item produce one of three terminal resolutions: (a) link to existing implementation file:line in ~/Projects/ddx/cli, (b) new DDx-side bead with deterministic acceptance filed in DDx's own tracker, or (c) HELIX-owned backport with LOE estimate and contract amendment diff.

Known gaps as of 2026-04-17 (verified by grep):
- ddx bead blocked only filters dep-blocked; no retry-after surfacing
- No build-gate implementation in ddx/cli/internal/agent/ (no lefthook/cargo-check/BuildGate match)
- No run-state writer in DDx source
- No structured event when HELIX injects a supervisory bead

Output: docs/helix/02-design/contracts/CONTRACT-001-audit.md matrix with one row per DDx-owned responsibility, terminal column filled. If audit materially amends CONTRACT-001 (changes ownership, removes a claimed DDx capability, or adds a new HELIX responsibility), file an amendment-notification bead that blocks helix-stuck / operator-status / integration-harness beads until their acceptance criteria are re-reviewed against the new matrix.
    </description>
    <acceptance>
docs/helix/02-design/contracts/CONTRACT-001-audit.md exists and has one row per DDx-owned item in CONTRACT-001 with a terminal resolution (code-link, new-DDx-bead, or HELIX-backport-with-LOE). No row left 'TBD' or 'investigating'. If any ownership or capability claim in CONTRACT-001 changes, an amendment-notification bead is filed that depends_on this bead and is depended_on by the operator-status, integration-harness, and helix-stuck beads before they may be closed.
    </acceptance>
    <labels>helix, phase:design, kind:spec, area:workflow, area:cli, phase-3-prep</labels>
  </bead>

  <governing>
    <ref id="docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md" path="docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md">
      <content>
# CONTRACT-001: DDx / HELIX Boundary Contract

**Status:** Draft  
**Owner:** HELIX maintainers  
**Related:** [Product Vision](../../00-discover/product-vision.md), [FEAT-011](../../01-frame/features/FEAT-011-slider-autonomy.md), [ADR-001](../adr/ADR-001-supervisory-control-model.md)

## Purpose

This contract defines the ownership boundary between **DDx** and **HELIX**.

- **DDx** is the platform substrate.
- **HELIX** is the workflow and methodology layer built on that substrate.

The goal is to keep execution/storage/platform concerns in DDx while keeping
workflow semantics, autonomy behavior, and prompt strategy in HELIX.

This contract exists to prevent two common failure modes:
1. HELIX re-implementing platform capabilities DDx already provides
2. DDx absorbing HELIX-specific workflow behavior and becoming methodology-bound

## DDx-Owned Substrate Responsibilities

HELIX expects DDx to provide these platform capabilities.

### 1. Graph primitives
- Document graph indexing
- `[[ID]]` body-link indexing in addition to frontmatter dependencies
- Upstream/downstream traversal primitives
- Reverse/dependent lookup primitives
- Discovery of graph-authored execution documents

### 2. Agent execution substrate
- `ddx agent run` as the general harness interface
- `ddx agent execute-bead <bead-id> [--from <rev>] [--no-merge]` as the
  canonical git-aware single-bead execution primitive
- `ddx agent execute-loop [--once] [--poll-interval <duration>]` as the
  canonical single-project queue-drain primitive that claims ready beads,
  runs `execute-bead`, and closes merged work with evidence
- Standard harness/model/effort/preset controls available through the DDx agent surface
- Session capture, transcript capture, and runtime evidence capture

### 3. Execution and metric substrate
- Graph-authored execution documents as authoritative definitions
- Immutable execution runs stored in the DDx execution substrate
- Metric projection over execution runs
- Required execution semantics sufficient to decide merge vs preserve
- Metric ratchet evaluation sufficient to decide merge vs preserve

### 4. Git-context execution mechanics
- Dirty-tree checkpointing before managed execution
- Isolated worktree execution
- Preserved hidden refs for non-landed attempts
- Rebase only to prepare fast-forward landing
- Fast-forward landing when merge-eligible
- Guaranteed worktree cleanup after landing or preservation

### 5. Always-on runtime metrics and provenance
For every managed execute-bead attempt, including attempts launched by
`ddx agent execute-loop`, DDx should capture runtime facts such as:
- harness
- model
- session ID
- elapsed duration
- token usage
- cost
- base revision
- result revision

### 6. Repo-local DDx configuration surfaces
- `.ddx/config.yaml`
- installed DDx skills/bootstrap assets
- preset/model resolution surfaces used by HELIX

## HELIX-Owned Workflow / Methodology Responsibilities

HELIX owns workflow behavior on top of the DDx substrate.

### 1. Autonomy semantics
HELIX defines what `low`, `medium`, and `high` autonomy mean behaviorally.
DDx does not own these semantics.

### 2. Workflow routing and supervision
HELIX owns:
- `helix input`
- `helix run`
- planning vs execution routing
- supervisory stop/continue behavior
- when to ask for human input
- when to delegate a current project queue to `ddx agent execute-loop`
- bead authoring rules for deterministic acceptance and success-measurement
  criteria so DDx-managed execution can close merged work without manual
  interpretation
- bead topology policy for parent-child relationships and dependencies when
  queue order matters (curation — ensures DDX's deterministic ordering is correct;
  HELIX does not predict which bead DDX will select)

### 3. Artifact-flow policy
HELIX owns:
- authority ordering across artifact layers
- change propagation policy through the artifact stack
- graph traversal policy beyond the primitive graph operations DDx exposes
- search fallback policy when declared links are incomplete

### 4. Conflict and escalation policy
HELIX owns:
- resolvable vs physics-level conflict classification
- the vocabulary and meaning of those conflict classes
- escalation behavior
- follow-on bead creation
- interpretation of preserved attempts for workflow continuation

The conflict taxonomy is HELIX-defined:
- **Resolvable**: workflow may continue with escalation, assumptions, or follow-on beads
- **Physics-level**: workflow must stop for human resolution because the governing intent is genuinely contradictory

DDx may return execution outcomes such as merged or preserved, but it does not define HELIX conflict classes.

HELIX interprets each bead as a governed workspace-state transformation:

- bead `B` defines the intended transition from workspace state `W` to
  successor workspace state `W'`
- the execution run is the attempt and evidence record for realizing `B : W -> W'`
- the execution outcome describes how that attempt landed
- the state delta is the realized material change between `W` and `W'`

### 5. Prompt and workflow strategy
HELIX owns:
- prompt design
- prompt engineering strategy
- stage-authored behavior stance for planning, execution, review, alignment,
  and related workflow stages
- bead prompt structure
- workflow wording and intervention policy
- execution-document authoring conventions for HELIX artifacts (see [CONTRACT-002](CONTRACT-002-helix-execution-doc-conventions.md))

HELIX does **not** expose stage personalities as a separate first-class
workflow configuration surface. The simpler contract is:

- HELIX bakes stage stance into the governing action prompt, skill wording, or
  execution-doc convention for that stage
- DDx still owns harness/model execution and any concrete model resolution
- if a stage needs a smarter, cheaper, slower, or faster lane, HELIX may ask
  for tier or harness constraints, but it must not turn stage stance into
  concrete model policy

The default HELIX stage stances are:

| Stage family | Stance owned by HELIX | Notes |
|---|---|---|
| Planning (`input`, `frame`, `design`, `evolve`, `triage`, `polish`) | exploratory, assumption-surfacing, artifact-authoring | widen context, expose ambiguity, prefer reversible shaping |
| Managed execution (`build`, `measure`, execution-ready bead work) | contract-following, bounded, anti-feature-creep | implement only the governed slice and prove it deterministically |
| Review (`review`, fresh-eyes passes) | adversarial, defect-seeking, risk-first | findings first; preserve merge/preserve evidence boundary |
| Alignment (`align`) | top-down, conservative, drift-seeking | compare lower layers against higher-authority artifacts |
| Supervisory/mechanical (`check`, `report`, queue steering) | concise, state-oriented, policy-applying | route work without inventing new product behavior |

These stances apply whether HELIX launches work through DDx-managed execution
or through a direct non-managed prompt such as `ddx agent run` for planning,
review, or alignment. The stage selects the stance; DDx resolves the execution
vehicle and concrete model policy.

## Shared Integration Objects

These objects are shared across the boundary and should keep stable meanings.

| Object | DDx role | HELIX role |
|---|---|---|
| **Bead** | tracker record + execution target | intended workspace-state transform (`B : W -> W'`) |
| **Workspace state** | execution substrate input/output surface | governed current/successor state under workflow interpretation |
| **State delta** | realized material diff between workspace states | workflow-visible change to inspect during measure/report |
| **Graph artifact** | indexed document node | governance/context layer |
| **Execution doc** | discovered executable validation definition | authored validation contract |
| **Execution run** | immutable evidence record | workflow input for measure/report/iteration |
| **Metric** | structured runtime observation | workflow signal |
| **Ratchet** | threshold/baseline evaluation | policy input for workflow decisions |
| **Preserved attempt** | non-landed managed execution result | experiment/review/iteration input |

## Workflow Handoff Points

### HELIX -> DDx
HELIX decides:
- what autonomy behavior should apply
- what workflow prompt/context to use
- what stage-authored stance should apply for the selected workflow step
- when implementation/verification should be dispatched
- whether to dispatch one bounded attempt with `ddx agent execute-bead` or
  hand a single-project ready queue to `ddx agent execute-loop`

HELIX then hands execution to DDx through managed agent/execution surfaces.

### DDx -> HELIX
DDx returns evidence, not workflow policy:
- execution outcome
- queue-drain result summaries when `execute-loop` is used
- required execution results
- ratchet results
- runtime metrics
- landed vs preserved outcome
- transcript/session/exec evidence locations

Minimum workflow-visible outcome surface from `ddx agent execute-loop --once --json`:

```json
{
  "project_root": "/path",
  "attempts": 1,
  "successes": 1,
  "failures": 0,
  "results": [
    {
      "bead_id": "hx-abc123",       "attempt_id": "...",
      "harness": "codex",           "status": "success",
      "detail": "...",              "session_id": "...",
      "base_rev": "sha",             "result_rev": "sha",
      "retry_after": "..."
    }
  ]
}
```

`results[].status` values:

| Status | Meaning |
|--------|---------|
| `success` | Bead merged or preserved with success |
| `no_changes` | Agent produced no tracked changes; worktree clean |
| `execution_failed` | Agent or harness exit non-zero |
| `land_conflict` | Attempt preserved: rebase failed or fast-forward not possible |
| `post_run_check_failed` | Attempt preserved: post-run checks failed |
| `structural_validation_failed` | Bead malformed or missing required fields |

Outcome-to-status mapping (internal to DDx):
- `outcome=merged` → `status=success`
- `outcome=no-changes` → `status=no_changes`
- `outcome=preserved`, reason in (rebase failed, ff-merge failed, ff-merge not possible) → `status=land_conflict`
- `outcome=preserved`, reason=post-run checks failed → `status=post_run_check_failed`
- `outcome=preserved`, other reason → `status=success`

HELIX uses `results[].bead_id` for all post-cycle bookkeeping (not a pre-selected bead).
HELIX uses `results[].result_rev` as the closing SHA candidate.
HELIX uses `results[].retry_after` for blocked/suspended bead surfaced via `ddx bead blocked`.

HELIX-authored execution beads must make success machine-auditable. In
practice this means deterministic acceptance and success-measurement criteria:
exact commands, named checks, concrete files or fields to inspect, and
observable end states. Vague success text such as "works correctly" is not a
sufficient contract for `ddx agent execute-bead` or `ddx agent execute-loop`.

When HELIX delegates queue draining to `ddx agent execute-loop`, DDx owns the
claim/execute/close mechanics for merged work in that loop. HELIX remains
responsible for deciding when loop delegation is appropriate and for
interpreting preserved, failed, or blocked outcomes.

A preserved outcome is an execution result from a bounded DDx-managed attempt. It is not, by itself, a HELIX physics-level conflict; it hands control back to HELIX for workflow interpretation.

HELIX then decides what to do next:
- continue
- escalate
- ask for input
- create follow-on beads
- revise prompts/workflow wording

## Anti-Drift Rules

### DDx must not absorb
- HELIX autonomy semantics
- HELIX workflow routing logic
- HELIX escalation policy
- HELIX prompt engineering strategy
- HELIX artifact decomposition policy

### HELIX must not build in parallel
- a second graph engine if DDx provides graph indexing/traversal
- a second execution store
- a second metrics/provenance store
- a separate prompt-version registry
- custom git execution mechanics that bypass the DDx managed execution flow
- a second single-project queue-drain loop once `ddx agent execute-loop`
  satisfies the required HELIX supervision contract

## Queue Curation Policy

HELIX owns queue curation. DDx owns bead selection and execution.

HELIX does not predict which bead DDx will select. Instead, HELIX ensures the
queue is in the correct state so DDx's deterministic `ReadyExecution()` ordering
produces the intended sequence.

| Queue mechanism | DDx behavior | HELIX responsibility |
|---|---|---|
| `dep-ids` | `ReadyExecution` waits for all deps to be `closed` | Set correctly on all beads; update when deps are added |
| `parent` hierarchy | DDx respects parent/child but does not enforce child execution order | Epic execution is separate from child execution; children enter ready queue independently |
| `execution-eligible` | `ReadyExecution` filters out `false`; defaults `true` if absent | Set `false` to temporarily suppress a bead without closing it |
| `superseded-by` | `ReadyExecution` filters out superseded beads | Set when a bead is superseded; do not leave superseded beads open |
| `execute-loop-retry-after` | `ReadyExecution` filters out beads on cooldown | DDx sets this on failed attempts; HELIX should not set it |

### Epic-focus queue curation

When HELIX enters epic-focus mode (stay on an epic until all children are done):

1. HELIX sets `execution-eligible: false` on all non-child open beads via `ddx bead update --set execution-eligible=false`.
2. DDx's `ReadyExecution` naturally picks only eligible children.
3. When the epic closes or switches, HELIX removes the `execution-eligible` suppression from remaining beads.
4. No DDX flag or special selection logic is required.

### Queue-drift ownership

Drift (superseded-by, parent change, spec-id change) is a **pre-execution** concern.
HELIX detects drift at `helix check` time and prevents stale beads from entering
the ready queue. DDx executes what it is given; it does not reopen beads after
close-with-evidence.

HELIX does not implement post-close reopen logic. If a bead was ready when DDx
picked it, the execution result stands.

## Queue-Injected Supervisory Beads

Review and alignment are **regular beads**, not post-cycle hooks. HELIX injects them
into the queue and lets DDx execute them through execute-loop:

| Bead type | Trigger | Acceptance |
|---|---|---|
| `review-finding` | Post-build or periodic | Agent finds 0 new drift violations |
| `alignment-review` | Every N completed passes | No governance drift detected |

When HELIX injects a review or alignment bead into the queue, DDx picks it up
like any other ready bead. The execution produces the same evidence bundle as
implementation beads, enabling performance analysis.

`--no-auto-review` and `--no-auto-align` control whether HELIX injects these beads
— they do not disable post-cycle hooks.

## Performance Metadata and Optimization

Every execute-bead attempt produces:

```
bead_id → { new_state, performance_metadata }
```

Performance metadata captured by DDx per attempt:
- model, harness, provider
- elapsed time
- token usage (input, output, total)
- cost
- base revision, result revision
- session ID, attempt ID

HELIX uses this for:
- **Prompt optimization**: did a simpler prompt produce the same result faster?
- **Model routing**: would a faster/cheaper model have sufficed? Would a smarter model have avoided the failure?
- **Process improvement**: why did this experiment fail? What assumption was wrong?

HELIX experiments use this infrastructure:
- Queue a batch of experiment beads with specific acceptance criteria
- DDx runs them all in order via execute-loop
- Each produces: new state + performance metadata
- Keep the ones that improve state; failed experiments leave a detailed record
  of what didn't work and why, enabling targeted improvement

This turns every bead execution into a measurable data point for continuous
process optimization.

## Post-Cycle HELIX Behavior

After `ddx agent execute-loop --once` returns, HELIX applies post-cycle
supervisory policy to the bead(s) in `results[].bead_id`.

| Behavior | Owner | Notes |
|---|---|---|
| Queue injection (review, alignment) | **HELIX** | Creates beads, DDx executes them |
| Epic promotion (task → epic when children appear) | **HELIX** | Post-cycle tracker mutation |
| Acceptance-failure filing | **HELIX** | Creates follow-on beads |
| Cycle counting | **HELIX** | Increments on `status=success` |
| Context refresh | **HELIX** | Every 5 cycles or on epic switch |
| Closing SHA sync | **DDx** | Uses `results[].result_rev` |
| Build gate (pre-merge check) | **DDx** | Runs before merge; reverts on failure |
| Retry suppression | **DDx** | Sets `execute-loop-retry-after` on cooldown |
| Orphan worktree recovery | **DDx** | Automatic after crashed runs |

Behaviors **deleted** from HELIX wrapper:
- HELIX retry/backoff logic (superseded by DDx `retry-after`)
- HELIX blocker tracking and reporting (superseded by `ddx bead blocked`)
- HELIX orphan tracker recovery (redundant with DDx worktree recovery)
- `git checkout -- .` cleanup (DDx worktrees are isolated)
- `safe_unclaim` after failed attempt (DDx handles claim lifecycle)
- `HELIX_SELECTED_ISSUE` env var (DDx never consumed it)

## Validation Checklist

The boundary is healthy when all of the following are true:

- [ ] HELIX uses DDx graph primitives instead of a parallel graph implementation for document indexing/traversal
- [ ] HELIX uses DDx-managed bead execution instead of directly inventing its own execution/provenance substrate
- [ ] HELIX parses `execute-loop --json` to find executed bead(s), applies post-cycle
  bookkeeping to those bead IDs rather than to a pre-selected bead
- [ ] HELIX does not pass `HELIX_SELECTED_ISSUE` or any bead selector to DDx execute-loop
- [ ] HELIX uses `execution-eligible` for epic-focus queue curation, not DDX flags
- [ ] HELIX injects review and alignment as regular beads into the queue, not as post-cycle hooks
- [ ] HELIX uses performance metadata from execute-bead results for prompt and model routing optimization
- [ ] HELIX experiments use execute-loop to run batched experiment beads with performance tracking
- [ ] HELIX does not implement retry/backoff or blocker tracking (DDx handles via `retry_after`)
- [ ] HELIX does not implement post-close reopen logic (drift is pre-execution)
- [ ] HELIX execution beads carry deterministic success criteria and
  measurement hooks precise enough for DDx-managed close-with-evidence
- [ ] DDx provides enough runtime evidence for HELIX to evaluate preserved attempts and landed runs
- [ ] HELIX autonomy behavior is documented in HELIX, not DDx
- [ ] DDx execution/metric/git semantics are documented in DDx, not redefined in HELIX
- [ ] Preserved attempts, execution runs, and runtime metrics have one authoritative home in DDx
- [ ] HELIX workflow docs describe how they consume DDx results rather than duplicating DDx implementation details

## References

- [Product Vision](../../00-discover/product-vision.md)
- [FEAT-011: Slider Autonomy Control](../../01-frame/features/FEAT-011-slider-autonomy.md)
- [ADR-001: HELIX Supervisory Control Model](../adr/ADR-001-supervisory-control-model.md)
- [API-001: HELIX Tracker Mutation Surface](API-001-helix-tracker-mutation.md)
- [CONTRACT-002: HELIX Execution-Document Conventions](CONTRACT-002-helix-execution-doc-conventions.md)
      </content>
    </ref>
  </governing>

  <diff rev="b466120efc390c77073ace31b23fcf54fc712de6">
commit b466120efc390c77073ace31b23fcf54fc712de6
Author: ddx-land-coordinator <coordinator@ddx.local>
Date:   Fri Apr 17 17:51:56 2026 -0400

    chore: add execution evidence [20260417T214435-]

diff --git a/.ddx/executions/20260417T214435-d2b95ace/manifest.json b/.ddx/executions/20260417T214435-d2b95ace/manifest.json
new file mode 100644
index 0000000..0aae807
--- /dev/null
+++ b/.ddx/executions/20260417T214435-d2b95ace/manifest.json
@@ -0,0 +1,82 @@
+{
+  "attempt_id": "20260417T214435-d2b95ace",
+  "bead_id": "helix-00e2486f",
+  "base_rev": "025a8dbdd2a3b443af9a2acfec21ef86e4dd6e99",
+  "created_at": "2026-04-17T21:44:36.190038146Z",
+  "requested": {
+    "harness": "codex",
+    "model": "gpt-5.4",
+    "prompt": "synthesized"
+  },
+  "bead": {
+    "id": "helix-00e2486f",
+    "title": "Audit CONTRACT-001 DDx-owned items against actual DDx implementation",
+    "description": "Walk CONTRACT-001's DDx-owned responsibility list (sections: Agent execution substrate, Execution and metric substrate, Git-context execution mechanics, Always-on runtime metrics, Post-Cycle HELIX Behavior table). For every DDx-owned item produce one of three terminal resolutions: (a) link to existing implementation file:line in ~/Projects/ddx/cli, (b) new DDx-side bead with deterministic acceptance filed in DDx's own tracker, or (c) HELIX-owned backport with LOE estimate and contract amendment diff.\n\nKnown gaps as of 2026-04-17 (verified by grep):\n- ddx bead blocked only filters dep-blocked; no retry-after surfacing\n- No build-gate implementation in ddx/cli/internal/agent/ (no lefthook/cargo-check/BuildGate match)\n- No run-state writer in DDx source\n- No structured event when HELIX injects a supervisory bead\n\nOutput: docs/helix/02-design/contracts/CONTRACT-001-audit.md matrix with one row per DDx-owned responsibility, terminal column filled. If audit materially amends CONTRACT-001 (changes ownership, removes a claimed DDx capability, or adds a new HELIX responsibility), file an amendment-notification bead that blocks helix-stuck / operator-status / integration-harness beads until their acceptance criteria are re-reviewed against the new matrix.",
+    "acceptance": "docs/helix/02-design/contracts/CONTRACT-001-audit.md exists and has one row per DDx-owned item in CONTRACT-001 with a terminal resolution (code-link, new-DDx-bead, or HELIX-backport-with-LOE). No row left 'TBD' or 'investigating'. If any ownership or capability claim in CONTRACT-001 changes, an amendment-notification bead is filed that depends_on this bead and is depended_on by the operator-status, integration-harness, and helix-stuck beads before they may be closed.",
+    "parent": "helix-e26584d7",
+    "labels": [
+      "helix",
+      "phase:design",
+      "kind:spec",
+      "area:workflow",
+      "area:cli",
+      "phase-3-prep"
+    ],
+    "metadata": {
+      "claimed-at": "2026-04-17T21:44:18Z",
+      "claimed-machine": "eitri",
+      "claimed-pid": "1437524",
+      "events": [
+        {
+          "actor": "ddx",
+          "body": "{\"resolved_provider\":\"lmstudio\",\"resolved_model\":\"qwen3.5-27b\",\"fallback_chain\":[]}",
+          "created_at": "2026-04-17T21:44:24.364151842Z",
+          "kind": "routing",
+          "source": "ddx agent execute-bead",
+          "summary": "provider=lmstudio model=qwen3.5-27b"
+        },
+        {
+          "actor": "ddx",
+          "body": "tier=cheap harness=lmstudio model=qwen3.5-27b probe=ok\nexec: no command",
+          "created_at": "2026-04-17T21:44:24.462600297Z",
+          "kind": "tier-attempt",
+          "source": "ddx agent execute-loop",
+          "summary": "execution_failed"
+        },
+        {
+          "actor": "ddx",
+          "body": "{\"resolved_provider\":\"script\",\"resolved_model\":\"/Users/erik/Projects/helix/.ddx/executions/20260417T214430-ccba6eda/prompt.md\",\"route_reason\":\"direct-override\",\"fallback_chain\":[]}",
+          "created_at": "2026-04-17T21:44:30.556603394Z",
+          "kind": "routing",
+          "source": "ddx agent execute-bead",
+          "summary": "provider=script model=/Users/erik/Projects/helix/.ddx/executions/20260417T214430-ccba6eda/prompt.md reason=direct-override"
+        },
+        {
+          "actor": "ddx",
+          "body": "tier=standard harness=script model=/Users/erik/Projects/helix/.ddx/executions/20260417T214430-ccba6eda/prompt.md probe=ok\nscript harness: unknown directive \"\u003cexecute-bead\u003e\" at index 0",
+          "created_at": "2026-04-17T21:44:30.652795518Z",
+          "kind": "tier-attempt",
+          "source": "ddx agent execute-loop",
+          "summary": "execution_failed"
+        }
+      ],
+      "execute-loop-heartbeat-at": "2026-04-17T21:44:18.401696721Z",
+      "spec-id": "docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md"
+    }
+  },
+  "governing": [
+    {
+      "id": "docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md",
+      "path": "docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md"
+    }
+  ],
+  "paths": {
+    "dir": ".ddx/executions/20260417T214435-d2b95ace",
+    "prompt": ".ddx/executions/20260417T214435-d2b95ace/prompt.md",
+    "manifest": ".ddx/executions/20260417T214435-d2b95ace/manifest.json",
+    "result": ".ddx/executions/20260417T214435-d2b95ace/result.json",
+    "checks": ".ddx/executions/20260417T214435-d2b95ace/checks.json",
+    "usage": ".ddx/executions/20260417T214435-d2b95ace/usage.json",
+    "worktree": "tmp/ddx-exec-wt/.execute-bead-wt-helix-00e2486f-20260417T214435-d2b95ace"
+  }
+}
\ No newline at end of file
diff --git a/.ddx/executions/20260417T214435-d2b95ace/prompt.md b/.ddx/executions/20260417T214435-d2b95ace/prompt.md
new file mode 100644
index 0000000..3bae4f4
--- /dev/null
+++ b/.ddx/executions/20260417T214435-d2b95ace/prompt.md
@@ -0,0 +1,19 @@
+<execute-bead>
+  <bead id="helix-00e2486f">
+    <title>Audit CONTRACT-001 DDx-owned items against actual DDx implementation</title>
+    <description>
+Walk CONTRACT-001&#39;s DDx-owned responsibility list (sections: Agent execution substrate, Execution and metric substrate, Git-context execution mechanics, Always-on runtime metrics, Post-Cycle HELIX Behavior table). For every DDx-owned item produce one of three terminal resolutions: (a) link to existing implementation file:line in ~/Projects/ddx/cli, (b) new DDx-side bead with deterministic acceptance filed in DDx&#39;s own tracker, or (c) HELIX-owned backport with LOE estimate and contract amendment diff.&#xA;&#xA;Known gaps as of 2026-04-17 (verified by grep):&#xA;- ddx bead blocked only filters dep-blocked; no retry-after surfacing&#xA;- No build-gate implementation in ddx/cli/internal/agent/ (no lefthook/cargo-check/BuildGate match)&#xA;- No run-state writer in DDx source&#xA;- No structured event when HELIX injects a supervisory bead&#xA;&#xA;Output: docs/helix/02-design/contracts/CONTRACT-001-audit.md matrix with one row per DDx-owned responsibility, terminal column filled. If audit materially amends CONTRACT-001 (changes ownership, removes a claimed DDx capability, or adds a new HELIX responsibility), file an amendment-notification bead that blocks helix-stuck / operator-status / integration-harness beads until their acceptance criteria are re-reviewed against the new matrix.
+    </description>
+    <acceptance>
+docs/helix/02-design/contracts/CONTRACT-001-audit.md exists and has one row per DDx-owned item in CONTRACT-001 with a terminal resolution (code-link, new-DDx-bead, or HELIX-backport-with-LOE). No row left &#39;TBD&#39; or &#39;investigating&#39;. If any ownership or capability claim in CONTRACT-001 changes, an amendment-notification bead is filed that depends_on this bead and is depended_on by the operator-status, integration-harness, and helix-stuck beads before they may be closed.
+    </acceptance>
+    <labels>helix, phase:design, kind:spec, area:workflow, area:cli, phase-3-prep</labels>
+    <metadata parent="helix-e26584d7" spec-id="docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md" base-rev="025a8dbdd2a3b443af9a2acfec21ef86e4dd6e99" bundle=".ddx/executions/20260417T214435-d2b95ace"/>
+  </bead>
+  <governing>
+    <ref id="docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md" path="docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md"/>
+  </governing>
+  <instructions>
+You are executing one bead inside an isolated DDx execution worktree. The bead&#39;s &lt;description&gt; and &lt;acceptance&gt; sections above are the completion contract — every AC checkbox must be provably satisfied by a specific piece of code, test, or file you can point to after your commit.&#xA;&#xA;## How to work&#xA;&#xA;1. Read first. If the bead description names files, read them to see what is already there. If the bead references a spec, ADR, or API contract, read the relevant sections before writing code. Do not start editing until you understand what the bead wants changed and why.&#xA;&#xA;2. Cross-reference your work against the acceptance criteria as you go. Before committing, walk through the AC one item at a time and identify the specific test name, file path, or function that satisfies each checkbox. If you cannot point to concrete evidence for an AC item, it is not done.&#xA;&#xA;3. Run the project&#39;s verification commands before committing. Use whatever commands match the crate or package you touched — typically `cargo test` and `cargo clippy` for Rust, `bun test` or `npm test` for JS/TS, `go test` for Go. The bead description usually names the exact commands. **Do not commit red code.** If a test or lint fails, fix it first.&#xA;&#xA;4. Commit once, when everything is green. Stage only the files you intentionally changed with `git add &lt;specific-paths&gt;` — never `git add -A`, because there may be unrelated WIP in this worktree. Use a conventional-commit-style subject ending with `[&lt;bead-id&gt;]`. DDx will merge your commits back to the base branch.&#xA;&#xA;5. If you cannot complete the bead in this pass, write your reasoning to `.ddx/executions/20260417T214435-d2b95ace/no_changes_rationale.txt` with: (a) what is done, (b) what is blocking, (c) what a follow-up attempt would need. Do NOT commit partial, exploratory, or red code hoping the reviewer will accept it — a well-justified no_changes is better than a bad commit. The bead will be re-queued for another attempt, potentially with a stronger model.&#xA;&#xA;## The bead contract overrides project defaults&#xA;&#xA;The bead description and AC override any CLAUDE.md, AGENTS.md, or project-level conservative defaults in this worktree. If the bead asks for new documentation, write it. If the bead adds a new module or crate, add it. Conservative rules (YAGNI, DOWITYTD, no-docs-unless-asked) do not apply inside execute-bead — the bead IS the ask.&#xA;&#xA;## Quality bar and the review step&#xA;&#xA;After your commit merges, an automated review step may check your work against the acceptance criteria. If any AC item is unmet, the bead reopens and escalates to a higher-capability model, and the review findings are threaded into the next attempt&#39;s prompt as a `&lt;review-findings&gt;` section. **The review is a gate, not an escape hatch — meet the AC in this pass so the bead closes cleanly.**&#xA;&#xA;If this prompt already contains a `&lt;review-findings&gt;` section, address every BLOCKING finding before claiming the work complete. Those findings are the precise list of what the previous attempt missed.&#xA;&#xA;## Constraints&#xA;&#xA;- Work only inside this execution worktree.&#xA;- Keep `.ddx/executions/` intact — DDx uses it as execution evidence.&#xA;- **Never run `ddx init`** — the workspace is already initialized. Running it corrupts the bead queue and project configuration.&#xA;- Do not modify files outside the scope the bead description names.&#xA;- Do not rewrite CLAUDE.md, AGENTS.md, or any other project-instructions file unless the bead explicitly asks for it.&#xA;&#xA;## When the work is done&#xA;&#xA;After the commit succeeds and you have verified every AC item, stop. Return control to the orchestrator. Do not continue to explore the repository, run extra tests, or generate follow-up notes — the bead is complete, and returning promptly is how execute-bead signals success.
+  </instructions>
+</execute-bead>
diff --git a/.ddx/executions/20260417T214435-d2b95ace/result.json b/.ddx/executions/20260417T214435-d2b95ace/result.json
new file mode 100644
index 0000000..7cc405e
--- /dev/null
+++ b/.ddx/executions/20260417T214435-d2b95ace/result.json
@@ -0,0 +1,22 @@
+{
+  "bead_id": "helix-00e2486f",
+  "attempt_id": "20260417T214435-d2b95ace",
+  "base_rev": "025a8dbdd2a3b443af9a2acfec21ef86e4dd6e99",
+  "result_rev": "fa54b125335250f77fc9a09d1c69f85cb4a8cb88",
+  "outcome": "task_succeeded",
+  "status": "success",
+  "detail": "success",
+  "harness": "codex",
+  "model": "gpt-5.4",
+  "session_id": "eb-0e2d33c4",
+  "duration_ms": 439850,
+  "tokens": 4969194,
+  "exit_code": 0,
+  "execution_dir": ".ddx/executions/20260417T214435-d2b95ace",
+  "prompt_file": ".ddx/executions/20260417T214435-d2b95ace/prompt.md",
+  "manifest_file": ".ddx/executions/20260417T214435-d2b95ace/manifest.json",
+  "result_file": ".ddx/executions/20260417T214435-d2b95ace/result.json",
+  "usage_file": ".ddx/executions/20260417T214435-d2b95ace/usage.json",
+  "started_at": "2026-04-17T21:44:36.190705646Z",
+  "finished_at": "2026-04-17T21:51:56.04103415Z"
+}
\ No newline at end of file
diff --git a/.ddx/executions/20260417T214435-d2b95ace/usage.json b/.ddx/executions/20260417T214435-d2b95ace/usage.json
new file mode 100644
index 0000000..be16c52
--- /dev/null
+++ b/.ddx/executions/20260417T214435-d2b95ace/usage.json
@@ -0,0 +1,8 @@
+{
+  "attempt_id": "20260417T214435-d2b95ace",
+  "harness": "codex",
+  "model": "gpt-5.4",
+  "tokens": 4969194,
+  "input_tokens": 4948309,
+  "output_tokens": 20885
+}
\ No newline at end of file
  </diff>

  <instructions>
You are reviewing a bead implementation against its acceptance criteria.

## Your task

Examine the diff and each acceptance-criteria (AC) item. For each item assign one grade:

- **APPROVE** — fully and correctly implemented; cite the specific file path and line that proves it.
- **REQUEST_CHANGES** — partially implemented or has fixable minor issues.
- **BLOCK** — not implemented, incorrectly implemented, or the diff is insufficient to evaluate.

Overall verdict rule:
- All items APPROVE → **APPROVE**
- Any item BLOCK → **BLOCK**
- Otherwise → **REQUEST_CHANGES**

## Required output format

Respond with a structured review using exactly this layout (replace placeholder text):

---
## Review: helix-00e2486f iter 1

### Verdict: APPROVE | REQUEST_CHANGES | BLOCK

### AC Grades

| # | Item | Grade | Evidence |
|---|------|-------|----------|
| 1 | &lt;AC item text, max 60 chars&gt; | APPROVE | path/to/file.go:42 — brief note |
| 2 | &lt;AC item text, max 60 chars&gt; | BLOCK   | — not found in diff |

### Summary

&lt;1–3 sentences on overall implementation quality and any recurring theme in findings.&gt;

### Findings

&lt;Bullet list of REQUEST_CHANGES and BLOCK findings. Each finding must name the specific file, function, or test that is missing or wrong — specific enough for the next agent to act on without re-reading the entire diff. Omit this section entirely if verdict is APPROVE.&gt;
  </instructions>
</bead-review>
