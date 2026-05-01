# Research Plan: Principles Injection Strategy Effectiveness

**Research Lead**: HELIX maintainers
**Time Budget**: 1 day (~8 hours)
**Status**: Example

> Example scenario reconstructed as the *plan* that would have preceded the actual research recorded in `docs/helix/06-iterate/research-principles-injection-2026-04-05.md`. The research itself ran on 2026-04-05; this plan illustrates the artifact format.

## Research Objectives

### Primary Research Questions

1. **Question**: Does injecting the HELIX product principles into agent prompts measurably change the alignment of the agent's reasoning with those principles, compared to no injection?
   - **Why Important**: HELIX's `principles` skill (FEAT-003) injects a ~500-token preamble into many judgment-making prompts. If injection does not change behavior, the token cost is wasted. If it changes only framing without changing conclusions, the value is cosmetic and we should justify the cost differently.
   - **Success Criteria**: A measurable alignment-score delta (≥1 point on a 0–5 rubric) between baseline and full-doc injection on at least one realistic design-judgment task.

2. **Question**: Does selective injection (1–2 most relevant principles, ~150 tokens) preserve most of the alignment benefit while reducing cost, or does it produce principle-blind reasoning?
   - **Why Important**: For high-frequency mechanical skills (`check`, `backfill-helix-docs`), the per-run cost of full-doc injection accumulates. Selective injection is the candidate compromise; we need evidence that the compromise actually helps before adopting it as the default for those skills.
   - **Success Criteria**: Alignment score for selective injection compared to both baseline and full-doc, with a recommendation about which skill types should use which strategy.

3. **Question**: At what principle-set size does full-doc injection start to degrade output quality relative to selective?
   - **Why Important**: HELIX defaults to 5 principles today. The methodology may grow that list. A scale finding lets us preemptively route around regression.
   - **Success Criteria**: A documented threshold or "needs further research" verdict with token-overhead numbers at 5/8/12 principles.

### Knowledge Gaps

| Gap | Impact | Current Confidence |
|-----|--------|--------------------|
| Whether injection changes the agent's *conclusion* or only its *framing* | High — affects whether injection has substantive value | Low — anecdotal only |
| Whether selective injection produces principle-explicit or principle-implicit reasoning | Medium — affects auditability for design artifacts | Low — no prior measurement |
| Token-overhead scaling at larger principle sets | Medium — informs future principle authoring | Low — no measurement above 5 principles |

## Scope

**In Scope**:
- Three injection strategies: baseline (none), full-doc (all 5 HELIX defaults), selective (2 most relevant).
- One realistic design-judgment task that exercises at least two of the five HELIX principles.
- Single-model evaluation using Claude Haiku 4.5 via `ddx agent run --harness claude`.
- An alignment rubric scored 0–5 against the named principles (explicit / implicit / absent).
- Token-cost and elapsed-time capture via DDx session metrics.

**Out of Scope**:
- Multi-model alignment (whether different models react differently to the same injection).
- Multi-turn alignment persistence (whether injection in turn 1 carries to turn 5).
- Position experiments (preamble vs inline vs closing constraint).
- Automated end-to-end deployment of the resulting recommendation.
- Human-evaluated rubric scoring (the score is self-referential in this round).

**Assumptions**:
1. A single design-judgment task is sufficient to detect alignment-score deltas of ≥1 point. Smaller deltas would require a larger battery and are out of scope for this round.
2. DDx agent metrics (`session_id`, output tokens, cost, elapsed) are the authoritative source for cost data.
3. The 5 default HELIX principles are stable for the duration of the experiment.

## Research Methods

### Method 1: Comparative Prompt Experiment

- **Objective**: Addresses Questions 1 and 2.
- **Approach**: Run the same design-judgment task three times — once per variant — through `ddx agent run --harness claude --model claude-haiku-4-5-20251001`. Capture full agent output, output tokens, and session ID for each run.
- **Participants/Sources**: Single agent (Claude Haiku 4.5). Task: a realistic HELIX-flavored design question that exercises Simplicity and Reversible Decisions principles ("Should we add a `--config-file` flag to `scripts/helix`?").
- **Duration**: ~3 hours including prompt setup, three runs, evidence capture.
- **Deliverable**: Three logged sessions plus raw outputs committed to the research artifact.

### Method 2: Alignment Rubric Scoring

- **Objective**: Addresses Question 1 — quantifies the difference between variants.
- **Approach**: Score each output 0–5 against the five HELIX principles. Each principle scores 1 point if explicitly named, 1 point if clearly implicit, 0 points if absent.
- **Participants/Sources**: Self-scoring against the rubric in this plan. Raw outputs preserved for later peer review or human re-scoring.
- **Duration**: ~1 hour.
- **Deliverable**: A scoring table per variant with a per-principle breakdown.

### Method 3: Token-Cost Projection

- **Objective**: Addresses Question 3.
- **Approach**: Use the captured per-variant token counts to project overhead at 5 / 8 / 12 / 15 principles, assuming linear scaling of preamble length. Flag the projection as an upper bound — it does not measure quality regression at larger sets, only cost.
- **Participants/Sources**: Captured DDx metrics.
- **Duration**: ~1 hour.
- **Deliverable**: A projection table with explicit "cost only — quality regression unmeasured" caveat.

## Timeline

| Phase | Duration | Activities | Deliverables |
|-------|----------|------------|--------------|
| Planning | 1 hour | Finalize task wording, lock variants and rubric | Plan approved |
| Investigation | 3 hours | Run three variants, capture sessions and metrics | Raw outputs + DDx metrics |
| Analysis | 2 hours | Score alignment rubric, project token costs | Scoring table + cost table |
| Validation | 2 hours | Write up findings, peer review by a second maintainer | `research-principles-injection-<date>.md` artifact |

**Total Duration**: 1 day (~8 hours)

## Research Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Single-task scope produces a result that does not generalize | High | Medium | Explicitly limit conclusions to "design-judgment tasks of this shape"; flag generalization as further-research |
| Self-referential rubric scoring biases toward injection-favorable conclusions | Medium | Medium | Preserve raw outputs verbatim so a future human or different model can re-score |
| The chosen task does not actually exercise the named principles | Medium | High | Pre-vet the task wording against the principle list before running variants |
| Single-model result misleads about multi-model behavior | High | Low | Document the limitation; route a follow-up research bead for cross-model replication if findings are decision-relevant |
| Token-cost projection mistaken for a quality projection | Medium | Medium | Caveat the projection table inline; do not propagate the number into recommendations as a quality bound |

## Completion Criteria

- [ ] All three primary research questions answered with evidence (or explicitly deferred with rationale).
- [ ] Raw agent outputs and DDx session IDs captured in the research artifact for re-scoring.
- [ ] Alignment scoring table and token-cost projection committed.
- [ ] Recommendation about which skills should use full-doc vs selective injection, with rationale.
- [ ] At least one named follow-up research direction recorded for future work (multi-model, position, scale).
- [ ] Findings reviewed by a second HELIX maintainer; conclusions either accepted or contested in writing.
