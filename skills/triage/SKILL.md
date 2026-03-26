---
name: triage
description: Review issue queue against repo state, improve issue quality, and fill gaps. Use when issues need cleanup, prioritization, or gap analysis.
disable-model-invocation: true
---

# Triage

Review the issue queue against the current state of the repository. Improve
issue quality and fill gaps.

## Steps

1. **Survey the queue** — list all open issues. Understand their priorities,
   dependencies, labels, and governing artifacts.

2. **Compare to repo state** — check whether the planning stack, implementation,
   and test coverage have evolved since issues were created. Identify issues that
   are now stale, already done, or no longer relevant.

3. **Improve unclaimed issues** — for issues that are unclear, underspecified, or
   poorly scoped:
   - Sharpen the description and acceptance criteria
   - Set or correct spec-id references
   - Fix dependency chains
   - Split issues that are too large
   - Merge issues that overlap

4. **Identify gaps** — look for work that should exist as issues but doesn't:
   - Untested acceptance criteria
   - Implementation that has drifted from specs
   - Missing deployment or iterate-phase follow-up
   - Quality concerns without tracking

5. **Create missing issues** — for each gap, create an issue with:
   - Clear description and acceptance criteria
   - Correct labels and spec-id
   - Appropriate dependencies

6. **Report** — summarize what changed: issues improved, issues created, issues
   closed as stale, and the resulting queue health.
