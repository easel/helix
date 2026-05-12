---
name: helix-evolve
description: Thread additions, removals, amendments, and incident learnings through the HELIX artifact stack.
argument-hint: '"requirement description" [--scope S] [--artifact ID] [--from source]'
---

# Evolve: Propagate Changes Through the Artifact Stack

When a governing artifact needs to change, this skill threads the change
through the full artifact stack from vision down to executable follow-up work.
It applies equally to additions, removals, amendments, and incident-driven
requirements.

Rule of thumb: if the change touches or should touch a requirements, design,
decision, or test-plan artifact, use evolve. The doc-first rule is symmetric:
removing a system from a design requires the same artifact propagation as
adding one.

## When to Use

- a new feature is requested or a capability needs to be added
- a system, dependency, or capability is being dropped or excluded
- an incident or bug reveals a missing constraint or policy
- an existing specification needs amendment
- customer feedback identifies a gap in the current design
- a dependency or constraint changes
- a decision changes scope, such as moving work into or out of the current release

## Methodology

1. Analyze the requirement and identify affected product areas.
2. Discover which governing artifacts need updating.
3. Detect conflicts with existing artifacts and open work.
4. Update artifacts in authority order: vision, requirements, feature specs,
   designs, decisions, test plans, and implementation plans.
5. Create properly shaped follow-up work for implementation and verification.
6. Wire dependencies to existing open work where ordering matters.
7. Produce an evolution report with conflicts flagged for human resolution.

## Examples

```bash
# New feature requirement
helix evolve "Add WAL compression support with configurable algorithms"

# Scoped amendment
helix evolve --scope area:wal "WAL segments should support LZ4 and zstd compression"

# Target a specific artifact
helix evolve --artifact SD-017 "Verification engine needs loom support for concurrency testing"

# Incident-driven requirement
helix evolve --from incident "INC-042: ingest pipeline needs circuit breakers to prevent cascade failure"

# Removal / exclusion
helix evolve --artifact SD-022 "Drop StarRocks from the competitive benchmark suite - unreliable results"

# Scope change
helix evolve "Defer SD-026 bridge adapters to post-V1"
```

## Running with DDx

When DDx supplies the HELIX runtime, use these references:

- Action prompt: `.ddx/plugins/helix/workflows/actions/evolve.md`
- Authority order: `.ddx/plugins/helix/workflows/actions/implementation.md` (Authority Order section)
- Triage validation: `scripts/tracker.sh` (tracker_validate_create)
- Tracker conventions: see `ddx bead --help` (DDx FEAT-004)

DDx-specific output should include tracker issues with governing artifact links,
acceptance criteria, dependencies, and labels appropriate for queue execution.
