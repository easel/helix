# Feature: Slider Autonomy Control

**Status**: Planning  
**Priority**: P1  
**Created**: 2026-04-07

## Problem Statement

Current HELIX has 15+ skills that mirror CLI commands. This creates cognitive load and doesn't match the actual user workflow, which is:

1. **Two primary modes**: "take design input" vs "work the queue"
2. **Human input is sparse**: "design a CRM", "use postgres", "make logout blue", "here's a bug"
3. **Agent must maintain artifact stack coherence**: Vision → PRD → Specs → ADRs → Designs → Tests → Code

The current command-centric model doesn't support:
- Natural language input interpretation
- Cross-cutting concern enforcement (e.g., "use postgres" should check existing SQLite ADR)
- Human-agentic continuum (sometimes human does work, sometimes agent runs away)
- Non-blocking conflict escalation
- **Automated artifact graph traversal**

## Requirements

### FR-01: Artifact Graph Metadata
Each artifact shall declare its connections to other artifacts:
- **Upstream dependencies**: What higher-authority artifacts govern this one?
- **Downstream dependents**: What lower-authority artifacts derive from this one?
- **Peer relationships**: What artifacts at the same level are related?

This metadata enables automated graph traversal when changes occur.

### FR-02: Impact Detection via Search
The system shall identify impacted artifacts through content search:
- Use `rg` or similar to find references to changed concepts/terms
- Match against artifact declarations (e.g., "Postgres" matches ADRs about database choice)
- Build initial impact set from search results + declared relationships

### FR-03: Graph Traversal and Change Flow
Once impacted artifacts are identified, the system shall:
1. **Trace the graph**: Follow upstream/downstream connections from impact point
2. **Order by authority**: Process changes in authority order (Vision → Code)
3. **Flow changes**: Propagate modifications through each layer
4. **Create downstream work**: Generate beads for artifacts that need updating

### FR-04: Physics-Level Conflict Detection
The system shall distinguish between:
- **Resolvable conflicts**: Different approaches to same goal (e.g., Postgres vs SQLite) → escalate via bead, continue with assumption
- **Physics-level conflicts**: True contradictions that cannot coexist (e.g., "must be real-time" + "batch processing only") → block and require human resolution

High autonomy mode proceeds through resolvable conflicts; blocks only on physics-level.

### FR-05: Autonomy Slider Controls Flow Behavior
The system shall support configurable autonomy level:
- **Low**: Ask before each graph traversal step; human approves change flow
- **Medium**: Traverse graph autonomously, ask on conflicts/ambiguity  
- **High**: Full autonomous traversal; escalate resolvable conflicts via beads; block only physics-level

### FR-06: Minimal CLI Surface
CLI commands reduce to two core capabilities:
1. **Input command**: `helix input "<natural language>"` - accepts sparse input, triggers graph traversal
2. **Execute command**: `helix run` - executes beads from queue (existing behavior preserved)

All other current commands become either deprecated or internal implementation details.

### FR-07: Bead-Centric Coordination
All work flows through beads:
- User input → [Bead: Request]
- Agent refines → [Children: Questions/Decisions]
- Conflicts → [Bead: Escalation - non-blocking]
- Gaps → [Bead: Gap - speculative]

Workers execute from the bead queue without blocking on conflicts.

### FR-08: Verification Loop and Functional Artifacts
The system shall verify that artifact flow produces **functional, measurable results**:
1. **Each artifact layer has acceptance criteria**: Vision (strategic goals), PRD (requirements), Specs (testable behaviors), ADRs (architectural constraints), Designs (implementation specs), Tests (executable verification), Code (working implementation)
2. **Test code proves requirements are met**: Once specs exist, test code demonstrates they're satisfied
3. **Metrics and acceptance criteria evolve with specs**: As artifacts refine, new constraints emerge that must be solved for
4. **Verification is automated where possible**: Tests run automatically; metrics collected continuously
5. **Failure triggers reflow**: If verification fails, the system traces back through the graph to identify which artifact layer needs adjustment

## Acceptance Criteria

### AC-01: Artifact Graph Metadata
- [ ] Each artifact type declares upstream/downstream relationships in metadata
- [ ] Graph traversal can follow declared connections automatically
- [ ] Search-based impact detection supplements declared relationships

### AC-02: Impact Detection and Traversal
- [ ] `rg` or similar identifies initial impacted artifacts from user input
- [ ] Graph traversal follows authority order (Vision → PRD → Specs → ADRs → Designs → Tests → Code)
- [ ] Changes flow through each layer, creating downstream work beads

### AC-03: Conflict Classification
- [ ] System distinguishes resolvable vs physics-level conflicts
- [ ] Resolvable conflicts create escalation beads and continue with documented assumptions
- [ ] Physics-level conflicts block execution and require human resolution

### AC-04: Autonomy Slider Behavior
- [ ] Low autonomy: asks before each graph step, human approves flow
- [ ] Medium autonomy: autonomous traversal, asks on conflicts  
- [ ] High autonomy: full autonomous flow, escalates resolvable via beads, blocks only physics-level

### AC-05: CLI Simplification
- [ ] `helix input "<text>"` command accepts natural language and triggers graph traversal
- [ ] `helix run` continues to execute beads from queue (backward compatible)
- [ ] Legacy commands (`design`, `build`, etc.) either deprecated or routed through new model

### AC-06: Verification Loop
- [ ] Each artifact layer has measurable acceptance criteria
- [ ] Test code exists for spec-defined behaviors and can be executed automatically
- [ ] Metrics are defined, collected, and trigger reflow when thresholds violated
- [ ] Failed verification traces back through graph to identify adjustment point
- [ ] New constraints discovered during verification create follow-on beads for resolution

### AC-07: Backward Compatibility
- [ ] Existing CLI commands continue to work during transition
- [ ] Existing skills remain functional (may be deprecated but not broken)
- [ ] `helix run` loop continues to function with new bead types

## Non-Requirements

- This feature does NOT replace the existing CLI/skill contract immediately
- This feature does NOT eliminate phase enforcers (they become parameterized by slider)
- This feature is NOT production-ready until fully tested in sandbox

## Dependencies

- DDx tracker must support custom labels for escalation/gap/speculative beads
- Artifact stack must be properly indexed for conflict detection
- Slider config schema needs to be defined and validated
- Each artifact type needs graph metadata declarations

## Risks

1. **Breaking existing workflows**: If we replace skills too aggressively, automation breaks
2. **Silent divergence**: Speculative work might drift from intent without proper reconciliation
3. **Cognitive load shift**: Users need to understand slider settings and their implications
4. **Graph traversal complexity**: Following artifact relationships correctly is non-trivial

## Success Metrics

- Reduced skill count (from 15+ to 2 core + optional specialized)
- Faster time from input to first artifact creation
- Higher quality conflict detection (fewer silent drifts)
- User satisfaction with autonomy level control
- **Automated change flow through artifact graph works reliably**
- **Verification loop closes successfully**: tests pass, metrics met, failures trigger correct reflow
- **Functional artifacts produced**: each layer produces measurable, verifiable output

---

*This feature is in PLANNING mode. Do not implement until design document is approved and beads are created through proper HELIX workflow.*
