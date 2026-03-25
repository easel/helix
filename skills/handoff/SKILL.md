---
name: handoff
description: Review changes made by another agent or session. Use when picking up work from a prior session or another agent's output.
---

# Handoff Review

Another agent or session has made changes. Review them.

## Steps

1. **Identify what changed** — check recent commits, modified files, new or
   updated beads, and any new planning artifacts.

2. **Assess quality** — for each change:
   - Does it align with the governing specs and planning stack?
   - Are tests passing?
   - Is the commit message clear and traceable?
   - Were follow-on beads created for remaining work?

3. **Check for drift** — did the changes introduce any divergence from the
   authoritative planning artifacts? If so, classify whether the code should
   align to plan or the plan should update.

4. **Check for gaps** — did the other agent leave work incomplete? Are there
   open beads that should have been closed, or new work that wasn't captured
   as beads?

5. **Report** — summarize:
   - What was done
   - What's good
   - What needs correction
   - What follow-up work remains

Be specific. Reference file paths, bead IDs, and commit hashes.
