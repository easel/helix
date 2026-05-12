---
title: "Technical Spike"
slug: tech-spike
phase: "Design"
weight: 200
generated: true
aliases:
  - /reference/glossary/artifacts/tech-spike
---

## What it is

Time-boxed technical investigation to explore unknowns, validate approaches,
or reduce technical risk before committing to implementation. Produces
concrete technical insights to inform architecture and design decisions.

## Activity

**[Design](/reference/glossary/activities/)** — Decide how to build it. Capture trade-offs, contracts, and architecture decisions.

## Output location

`docs/helix/02-design/spikes/`

## Relationships

### Requires (upstream)

- [Solution design context](../solution-design/) *(optional)*
- [Architecture principles](../principles/)

### Enables (downstream)

- [Architecture refinement](../architecture/)
- [Implementation approach](../implementation-plan/)
- [Risk mitigation](../adr/)

### Informs

- [Architecture](../architecture/)
- [Adr](../adr/)
- [Solution Design](../solution-design/)
- [Implementation Plan](../implementation-plan/)
- [Contract](../contract/)

## Generation prompt

The agent prompt that produces this artifact.

<details>
<summary>Show the full generation prompt</summary>

``````markdown
# Technical Spike Generation Prompt
Use the spike to answer one technical question with evidence.

## Focus
- State the question, hypothesis, and method.
- Keep the investigation small and measurable.
- End with findings, limitations, and a recommendation.

## Completion Criteria
- The uncertainty is reduced.
- Evidence is documented.
- The recommendation is actionable.
``````

</details>

## Template

<details>
<summary>Show the template structure</summary>

``````markdown
# Technical Spike: {{spike_title}}

**Spike ID**: {{spike_id}} | **Lead**: {{spike_lead}} | **Time Budget**: {{time_budget}} | **Status**: In Progress | Completed

## Objective

**Technical Question**: {{technical_uncertainty}}

**Goals**:
- [ ] [Specific goal 1]
- [ ] [Specific goal 2]

**Success Criteria**: Evidence gathered, recommendations with rationale, risks identified.

**Out of Scope**: Production implementation, comprehensive testing, optimization work.

## Hypothesis

**Primary**: [What we think we'll discover]
**Assumptions**: [Key assumptions]
**Expected Outcome**: [Anticipated result]

## Approach

**Method**: [Prototype | Benchmark | Literature Review | Comparative Analysis | Integration Testing]

**Activities**:
| Day | Activity | Objective |
|-----|----------|-----------|
| 1 | [Activity] | [Goal] |
| 2 | [Activity] | [Goal] |

## Findings

**FINDING 1**: [Discovery]
- **Evidence**: [Concrete proof/data]
- **Implications**: [What this means]

### Measurements
| Metric | Approach A | Approach B | Notes |
|--------|------------|------------|--------|
| [Metric] | [Value] | [Value] | [Context] |

## Analysis

**Hypothesis**: CONFIRMED | PARTIALLY CONFIRMED | REJECTED
**Rationale**: [Evidence]

### Risks
| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Strategy] |

## Conclusions

**Primary Conclusion**: [Clear answer to the technical question]
**Confidence**: High | Medium | Low
**Limitations**: [What could not be determined]

## Recommendations

**RECOMMENDATION**: [Specific, actionable recommendation]
- **Rationale**: [Why, based on evidence]
- **Next Steps**: [What needs to happen]
- **Concern Impact**: [Does this recommend adopting, rejecting, or modifying a
  concern? If so, an ADR should ratify the decision and the project concern
  document should be updated accordingly.]
``````

</details>

## Example

<details>
<summary>Show a worked example of this artifact</summary>

``````markdown
# Technical Spike: Bash vs Go for the `scripts/helix` Orchestrator

**Spike ID**: SPIKE-001 | **Lead**: HELIX maintainers | **Time Budget**: 2 days | **Status**: Completed

> Example scenario reconstructed from the implementation-language deliberations that informed `docs/helix/02-design/architecture.md`. The orchestrator is implemented in Bash today; this spike illustrates how that decision was rationalized.

## Objective

**Technical Question**: Should `scripts/helix` — HELIX's supervisory orchestrator — be implemented in Bash with `jq` over DDx CLI JSON output, or as a compiled Go binary that calls DDx as a library?

**Goals**:
- [x] Compare developer ergonomics for the dominant operation in `helix run`: dispatch a `ddx` command, parse JSON, branch on a status, dispatch the next.
- [x] Compare testability against the `tests/helix-cli.sh` harness shape HELIX already prefers.
- [x] Compare deployment overhead — does the operator need a compile/install step, or is a clone-and-run path possible?
- [x] Compare maintenance cost over the kinds of changes HELIX has actually made in the last quarter (new phase commands, new escalation rules, new bead-authoring conventions).

**Success Criteria**: Evidence gathered against each goal, a recommendation with rationale, risks identified, and a clear escape hatch in case the recommendation needs to be revisited.

**Out of Scope**: Production-grade error UX, performance optimization, packaging/distribution decisions, multi-language plugin embedding.

## Hypothesis

**Primary**: Bash + `jq` is the right choice because `helix run` is dominated by pipelines over `ddx` JSON output. The orchestrator's complexity is in policy (which bead, which prompt, when to escalate), not in algorithms.

**Assumptions**:
1. HELIX continues to delegate execution mechanics to DDx per CONTRACT-001 — the orchestrator does not need to do its own git mechanics, agent dispatch, or evidence capture.
2. The `tests/helix-cli.sh` harness shape (a deterministic CLI test in Bash with golden outputs) is the right testing model for supervisory logic.
3. Operators already have `bash` and `jq` on macOS and Linux; assuming a Go toolchain is a heavier ask.

**Expected Outcome**: Bash wins on ergonomics for the actual operation shape and on deployment, with a small testability gap that the existing CLI harness already closes. Go would win only if the orchestrator needed to do significant in-process logic that it does not.

## Approach

**Method**: Comparative Analysis with a representative-complexity sample.

**Activities**:
| Day | Activity | Objective |
|-----|----------|-----------|
| 1 | Implement a representative `helix run` cycle (`execute-loop --once --json` → parse `results[]` → post-cycle bookkeeping → cycle counter → escalation decision) in both Bash and Go | Concrete ergonomics comparison |
| 1 | Wire each implementation to a deterministic harness modeled on `tests/helix-cli.sh` | Concrete testability comparison |
| 2 | Time and document the developer-loop overhead for one realistic change ("add an escalation rule for `post_run_check_failed`") in each implementation | Maintenance cost evidence |
| 2 | Catalog the deployment shape: what does an operator clone/install/run for each? | Deployment comparison |

## Findings

**FINDING 1**: The dominant operation in `helix run` is pipeline-shaped; Bash + `jq` expresses it more directly than Go.
- **Evidence**: The post-cycle bookkeeping path is `ddx agent execute-loop --once --json | jq -r '.results[] | "\(.bead_id) \(.status) \(.result_rev)"' | while read ...`. The Go equivalent requires an `os/exec` call, a struct definition mirroring the JSON shape, an unmarshal, and a loop — three to five times as much code for the same observable behavior.
- **Implications**: For the actual operation shape HELIX performs, Bash is the more direct expression.

**FINDING 2**: Testability is comparable, with a slight Bash advantage in the existing harness shape.
- **Evidence**: `tests/helix-cli.sh` is already a Bash-driven golden-output harness. A Bash orchestrator drops into that harness with no impedance mismatch. A Go orchestrator would need to either expose a CLI surface that the same harness drives (in which case the test layer is unchanged) or grow a parallel `go test` suite for in-process logic.
- **Implications**: Bash matches the testing model HELIX already prefers. Go would either be neutral (CLI-tested) or strictly add a test surface (in-process tested) without removing the CLI harness.

**FINDING 3**: Deployment overhead is the most asymmetric factor.
- **Evidence**: Bash: clone the plugin, run `scripts/helix`. Go: install a toolchain, build for the operator's platform, distribute binaries for macOS/Linux × architectures, handle plugin-update flows. HELIX is distributed as a DDx plugin alongside Markdown content; adding a compile step to the methodology repo is a meaningful operator-facing cost.
- **Implications**: Bash has a near-zero install step. Go adds release infrastructure HELIX does not currently need.

**FINDING 4**: Maintenance cost favors Bash for the changes HELIX actually makes.
- **Evidence**: A representative recent change ("inject `alignment-review` beads every N successful cycles") was a 5-line edit to one Bash function. The equivalent in Go required a struct field, a counter, a config plumbing path, and a unit test — same observable behavior, three to four times the touchpoints.
- **Implications**: When the orchestrator's complexity is workflow policy rather than algorithms, Bash is the lower-friction surface for iterative methodology change.

**FINDING 5**: Bash carries genuine costs HELIX should plan around.
- **Evidence**: Error handling (`set -euo pipefail` discipline), portability (GNU vs BSD flag differences), and quoting are real failure modes. They have already produced bugs in `scripts/helix`.
- **Implications**: The choice is not free. The recommendation is contingent on rigorous Bash discipline (strict mode, jq for all JSON, integration test coverage for every supervisory branch) — not on Bash being effortless.

### Measurements

| Metric | Bash | Go | Notes |
|--------|------|-----|-------|
| Lines of code for representative cycle | ~70 | ~240 | Identical observable behavior |
| Touchpoints for "add new escalation rule" | 1 file, 5 lines | 3 files, ~30 lines | Recent real-world change shape |
| Operator install steps | 1 (clone) | 4 (toolchain + build + place binary + permissions) | macOS/Linux x86_64+arm64 |
| Test harness fit | Native (existing `tests/helix-cli.sh`) | Adjacent (CLI-driven golden tests still possible) | HELIX prefers golden-output harness |
| Risk: silent quoting/portability bugs | Higher | Lower | Bash needs strict mode + lint discipline |
| Risk: "rewrite trap" if logic outgrows shell | Higher | Lower | Mitigated by CONTRACT-001 keeping execution in DDx |

## Analysis

**Hypothesis**: CONFIRMED.
**Rationale**: For the actual operation shape — pipelines over `ddx` JSON output — Bash is more direct, lower-overhead to deploy, and matches the existing CLI test harness. Go would dominate only if HELIX absorbed execution mechanics, which CONTRACT-001 explicitly forbids.

### Risks

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| Bash quoting/portability bug corrupts a tracker write | Medium | High | All tracker mutations go through `ddx bead` (per ADR-002); orchestrator never edits JSONL directly. Strict-mode discipline + shellcheck in CI |
| Orchestrator outgrows Bash if HELIX absorbs more logic over time | Medium | Medium | CONTRACT-001 caps the surface: HELIX does not own execution mechanics. Re-evaluate language if and only if the orchestrator's complexity moves out of "policy over CLI JSON" |
| New maintainers find Bash orthogonal to the rest of their toolchain | Medium | Low | Document the strict-mode + jq conventions; keep functions small; rely on `tests/helix-cli.sh` for behavior contracts |

## Conclusions

**Primary Conclusion**: Implement `scripts/helix` in Bash with `jq` for JSON parsing. Go is the wrong tool for the operation shape HELIX actually performs.

**Confidence**: High.

**Limitations**: This conclusion is contingent on CONTRACT-001 holding — i.e., HELIX continues to delegate execution mechanics to DDx. If HELIX absorbs in-process logic that is not pipeline-shaped, the analysis must be re-run.

## Recommendations

**RECOMMENDATION**: Implement `scripts/helix` in Bash. Adopt strict mode (`set -euo pipefail`), require all JSON access through `jq`, forbid direct tracker JSONL edits (use `ddx bead`), and lock behavior contracts in `tests/helix-cli.sh`.

- **Rationale**: Best ergonomics for the dominant operation shape, lowest deployment overhead, native fit with the existing test harness, lowest maintenance cost for the changes HELIX actually makes.
- **Next Steps**: Land Bash implementation; add shellcheck to CI; document the strict-mode + jq conventions in `.ddx/plugins/helix/workflows/EXECUTION.md`; revisit this decision if and only if HELIX takes on in-process logic that is not pipeline-shaped over `ddx` JSON output.
- **Concern Impact**: Reinforces the existing "platform substrate vs methodology layer" separation in CONTRACT-001. No new ADR is required to adopt; an ADR would be required to *replace* Bash with another language, since that would imply a larger change to the orchestrator's role.
``````

</details>
