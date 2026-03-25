---
name: triage
description: Review beads queue against repo state, improve bead quality, and fill gaps. Use when beads need cleanup, prioritization, or gap analysis.
disable-model-invocation: true
---

# Triage

Review the beads queue against the current state of the repository. Improve
bead quality and fill gaps.

## Steps

1. **Survey the queue** — list all open beads. Understand their priorities,
   dependencies, labels, and governing artifacts.

2. **Compare to repo state** — check whether the planning stack, implementation,
   and test coverage have evolved since beads were created. Identify beads that
   are now stale, already done, or no longer relevant.

3. **Improve unclaimed beads** — for beads that are unclear, underspecified, or
   poorly scoped:
   - Sharpen the description and acceptance criteria
   - Set or correct spec-id references
   - Fix dependency chains
   - Split beads that are too large
   - Merge beads that overlap

4. **Identify gaps** — look for work that should exist as beads but doesn't:
   - Untested acceptance criteria
   - Implementation that has drifted from specs
   - Missing deployment or iterate-phase follow-up
   - Quality concerns without tracking

5. **Create missing beads** — for each gap, create a bead with:
   - Clear description and acceptance criteria
   - Correct labels and spec-id
   - Appropriate dependencies

6. **Report** — summarize what changed: beads improved, beads created, beads
   closed as stale, and the resulting queue health.
