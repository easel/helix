---
dun:
  id: TD-011
  depends_on:
    - FEAT-011
    - helix.workflow.artifact-hierarchy
    - ADR-001
---

# TD-011: Slider Autonomy Implementation Design (Revised)

| Date | Status | Deciders | Related | Confidence |
|------|--------|----------|---------|------------|
| 2026-04-07 | Proposed | HELIX maintainers | FEAT-011, ADR-001 | Medium |

## Context

This technical design specifies implementation details for the slider autonomy model that reduces HELIX from 15+ skills to 2 core capabilities while maintaining artifact stack coherence through automated graph traversal.

**Key constraints**:
- Must integrate with existing `[[ID]]` cross-reference pattern (no new storage format)
- Must maintain backward compatibility during deprecation period
- Must work within ADR-001 supervisory control model (`helix run` as supervisor)

## Requirements Summary

From FEAT-011:
1. Artifact graph traversal using existing `[[ID]]` cross-references
2. Two-phase impact detection (declared links + search fallback)
3. Physics-level vs resolvable conflict classification
4. Autonomy slider (low/medium/high) controlling flow behavior
5. Verification loop with failure triage and traceback
6. CLI simplification: `helix input` + `helix run`

## Design Decisions

### Decision 1: Graph Traversal Algorithm (Revised)

**Approach**: Two-phase traversal - collect subgraph first, then topological sort by authority tier

```pseudocode
# Phase 1: Collect all impacted artifacts (bidirectional BFS)
function collectImpactedSubgraph(startArtifact):
    visited = set()
    queue = [startArtifact]
    
    while queue not empty:
        current = queue.pop()
        if current in visited:
            continue
        visited.add(current)
        
        # Add both upstream and downstream neighbors
        for neighbor in getUpstreamNeighbors(current):
            if neighbor not in visited:
                queue.push(neighbor)
        for neighbor in getDownstreamNeighbors(current):
            if neighbor not in visited:
                queue.push(neighbor)
    
    return visited

# Phase 2: Sort by authority tier (stable topological sort)
function orderByAuthority(artifacts):
    # Canonical order from workflows/artifact-hierarchy.md
    authorityTiers = {
        "vision": 0, "prd": 1,
        "feat": 2, "us": 3,
        "adr": 4, "architecture": 4,  # ADRs at same tier as architecture
        "sd": 5, "td": 6,
        "tp": 7, "tests": 8,
        "implementation_plan": 9,
        "code": 10
    }
    
    return sortBy(artifacts, key=lambda a: authorityTiers[getArtifactType(a)])
```

**Authority ordering** (aligned with `workflows/artifact-hierarchy.md`):
1. Product Vision
2. PRD
3. Feature Specifications and User Stories
4. Architecture and ADRs
5. Solution Designs and Technical Designs
6. Test Plans and Executable Tests
7. Implementation Plans
8. Source Code and Build Artifacts

### Decision 2: Impact Detection Three-Phase System (Revised)

**Phase 0: Build Reverse Index (One-time, cached)**
```bash
# Create reverse index mapping each ID to its downstream dependents
# This enables efficient upstream→downstream traversal
function buildReverseIndex():
    idToFiles = {}      # ID → file path
    downstreamMap = {}  # ID → [IDs that reference this one]
    
    for artifact in allArtifacts(docs/helix/):
        id = extractArtifactId(artifact)
        idToFiles[id] = artifact.path
        
        # For each [[ID]] reference in this artifact
        for ref in parseCrossReferences(artifact):
            if ref not in downstreamMap:
                downstreamMap[ref] = []
            downstreamMap[ref].append(id)
    
    return idToFiles, downstreamMap
```

**Phase 1: Declared Links (Primary)**
```bash
# Extract all [[ID]] references - supports slugs and dotted IDs
# Pattern matches: US-036-list-mcp-servers, FEAT-011, helix.workflow.artifact-hierarchy
rg '\[\[([A-Z]+-\d+(?:-[a-z0-9-]+)?|helix(?:\.[a-z][a-z-]*)+)\]\]' docs/helix/ | \
  sed 's/.*\[\[\([^]]*\)\]\].*/\1/' | sort -u

# For each ID, resolve to file path and extract ITS references (recursive)
for id in ids; do
  # Resolve ID to artifact file
  file=$(findArtifactById "$id")
  if [ -f "$file" ]; then
    # Extract upstream refs from this artifact's [[ID]] links
    rg '\[\[([A-Z]+-\d+(?:-[a-z0-9-]+)?|helix(?:\.[a-z][a-z-]*)+)\]\]' "$file"
  fi
done
```

**Phase 2: Search Fallback (Supplemental)**
```bash
# Extract key terms from input text or change diff
# Use NLP-aware extraction, not just capitalization
if [ -n "$INPUT_TEXT" ]; then
  # For helix input: extract nouns and domain terms from natural language
  echo "$INPUT_TEXT" | rg -oP '\b(?:postgres|sqlite|database|api|auth|login|[A-Z][a-z]+)\b'
elif [ -n "$GIT_DIFF" ]; then
  # For file changes: extract added terms (case-insensitive)
  git diff HEAD~1 -- docs/helix/ | grep "^+" | rg -oiP '\b[a-z]{4,}\b'
fi | sort -u | head -20

# Search for term matches in artifact titles and content
for term in terms; do
  rg "$term" docs/helix/ --glob "*.md" --heading-line-number
done
```

**Precedence**: Declared links always take precedence. Search results only added if not already in declared set.

### Decision 3: Conflict Classification Rules (Revised)

| Pattern | Type | Detection Method | Action |
|---------|------|------------------|--------|
| Technology choice (Postgres vs SQLite) | Resolvable | Authority-tier precedence | Escalate bead, use highest authority |
| Constraint contradiction ("real-time" + "batch only") | Physics-level | Structured field analysis | Block, require human |
| Missing upstream artifact | Gap | Reference to non-existent ID | Create gap bead, continue with placeholder |
| Duplicate specification | Resolvable | Authority-tier precedence | Escalate bead, use highest authority |

**Physics-level detection heuristic**:
1. **Authority-tier precedence first**: If same constraint appears at different tiers, higher authority wins
2. **Structured field analysis only**: Only analyze `## Constraints` or `## Requirements` sections, not free text
3. **Explicit contradiction patterns**: Look for direct negations in structured fields (e.g., "must use X" vs "must NOT use X")
4. **Default to resolvable**: If unclear, classify as resolvable and escalate via bead

### Decision 4: Slider Config Schema (Revised)

```yaml
# .helix/slider-config.yaml
autonomy_level: "medium"  # low | medium | high

bead_size_target: "small"  # small | medium | large
question_threshold: 3  # decisions before asking human (low autonomy only)
escalation_mode: "bead"  # bead | block | auto-resolve

speculative_allowed: true  # allow speculative work with marking
speculation_label: "kind:speculative"

conflict_handling:
  resolvable: "escalate"  # escalate | assume-first | ask
  physics_level: "block"  # block only option

graph_traversal:
  max_depth: 10  # prevent infinite traversal
  cycle_detection: true
  authority_ordering: true

verification:
  auto_traceback: true
  failure_triage: "automatic"  # automatic | manual
```

**Environment overrides**: `HELIX_AUTONOMY=high`, `HELIX_SPECULATIVE=false`

**Note on conflict_handling.resolvable**: Even when set to `auto-resolve`, an escalation bead MUST be created for traceability. The auto-resolve only determines whether execution blocks while waiting for human review.

### Decision 5: CLI Implementation

#### New Command: `helix input`

```bash
# Usage
helix input "<natural language request>" [--autonomy low|medium|high]

# Examples
helix input "design a CRM with lead capture"
helix input "use postgres instead of sqlite" --autonomy high
helix input "the login button is broken" --autonomy medium
```

**Implementation flow**:
1. Parse natural language, extract key terms and intent
2. Load slider config (file + env overrides)
3. Run impact detection (declared links + search)
4. Traverse graph to identify all affected artifacts
5. For each artifact layer:
   - If autonomy=low: ask user before proceeding
   - Detect conflicts, classify as resolvable/physics-level
   - Create beads for work needed
6. Output summary of created beads and assumptions

#### Existing Command: `helix run` (Unchanged)

Continues to execute beads from queue. New bead types (`kind:escalation`, `kind:speculative`) are handled by existing worker logic with appropriate labeling.

### Decision 6: Verification Loop Integration (Revised)

**Traceability metadata format**:
```markdown
# TP-036-list-mcp-servers.md
**User Story**: [[US-036-list-mcp-servers]]
**Technical Design**: [[TD-036-list-mcp-servers]]

## Test Cases

### TC-001: List MCP servers returns array
**Spec Reference**: TD-036 §3.2 API Response Format
```

**Test file metadata** (for code tests):
```javascript
// tests/mcp-servers.test.js
/**
 * @spec-ref TD-036
 * @requirement TC-001
 */
test('list MCP servers returns array', async () => {
  // ...
});
```

**Failure traceback algorithm (integrated with helix measure/report)**:
```pseudocode
# Runs as part of helix measure phase after build completes
function traceBackFromFailure(failingTest, testOutput):
    # Step 1: Extract spec reference from test metadata
    specRef = parseTestMetadata(failingTest).spec_ref
    
    if not specRef:
        return createBuildBead("Missing spec ref", failingTest.path)
    
    # Step 2: Load spec and check for upstream conflicts
    spec = loadArtifact(specRef)
    upstreamRefs = parseCrossReferences(spec).upstream_dependencies
    
    conflict = detectUpstreamConflict(spec, upstreamRefs)
    if conflict:
        return createEscalationBead(
            "Spec conflict detected",
            specRef,
            details=conflict
        )
    
    # Step 3: Default triage - assume implementation bug unless evidence suggests otherwise
    # This is conservative and safe; helix report can refine if pattern emerges
    return createBuildBead(
        "Implementation does not meet spec",
        specRef,
        testOutput=testOutput
    )
```

**Integration with existing HELIX workflow**:
- Runs during `helix measure` phase (after build, before report)
- Uses existing `ddx bead create` for failure triage output
- Results feed into `helix report` for follow-on bead creation

## Component Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  helix input "<request>"                                     │
└──────────────────────┬──────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Input Parser                                                │
│  • Extract intent and key terms                              │
│  • Load slider config                                        │
└──────────────────────┬──────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Impact Detector                                             │
│  Phase 0: Build reverse index (cached)                      │
│  Phase 1: Parse [[ID]] cross-references                     │
│  Phase 2: Search fallback for term matches                  │
└──────────────────────┬──────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Graph Traverser                                             │
│  • Bidirectional BFS to collect subgraph                    │
│  • Topological sort by authority tier                       │
│  • Conflict classification                                   │
└──────────────────────┬──────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  Bead Creator                                                │
│  • Request beads                                             │
│  • Escalation beads (resolvable conflicts)                  │
│  • Gap beads (missing artifacts)                            │
│  • Speculative beads (high autonomy assumptions)            │
└──────────────────────┬──────────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  helix run (existing, unchanged)                             │
│  Executes all bead types from queue                         │
└─────────────────────────────────────────────────────────────┘
```

## Integration with Existing HELIX Components

### ADR-001 Supervisory Control Model

`helix input` is a **new entrypoint** that feeds into the existing supervisory model:
- `helix input` creates beads → `helix run` executes them
- No change to `helix run` behavior or supervisory logic
- Companion commands (`design`, `polish`, `align`, `check`) remain as subroutines

### Artifact Hierarchy Compatibility

Uses existing patterns:
- `[[ID]]` cross-references for graph metadata
- Standard artifact naming (FEAT-XXX, TD-XXX, etc.)
- Directory structure under `docs/helix/`

### DDx Bead Tracker Integration

New bead labels:
- `kind:escalation` - resolvable conflicts needing human review
- `kind:speculative` - assumptions made in high autonomy mode
- `phase:frame`, `phase:design`, etc. - existing phase labels preserved

## Testing Strategy

### Unit Tests
- Graph traversal with fixture artifacts (known input → known output)
- Conflict classification test cases (resolvable vs physics-level examples)
- Impact detection accuracy (declared links + search coverage)
- Reverse index correctness (ID resolution, downstream mapping)

### Integration Tests
- End-to-end `helix input` flow with sample requests
- Bead creation verification (correct types, labels, dependencies)
- Verification loop traceback with failing tests

### Acceptance Test Fixtures

Create minimal HELIX project with:
```
docs/helix/01-frame/
  prd.md [[FEAT-001]]
  features/
    FEAT-001-test-feature.md [[US-001, US-002]]
    user-stories/
      US-001-first-story.md
      US-002-second-story.md
docs/helix/02-design/
  solution-designs/
    SD-001-test-solution.md [[FEAT-001, TD-001]]
  technical-designs/
    TD-001-first-design.md [[US-001, TP-001]]
docs/helix/03-test/
  test-plans/
    TP-001-first-tests.md [[TD-001]]
```

Test: `helix input "change US-001 acceptance criteria"` should produce beads for TD-001, TP-001, and tests.

## Migration Path

### Phase 1: Planning (Current)
- [ ] FEAT-011 feature spec approved
- [ ] TD-011 technical design approved
- [ ] Implementation beads created

### Phase 2: Core Implementation
- [ ] Graph traversal module
- [ ] Impact detection (declared links + search)
- [ ] Conflict classification logic
- [ ] Slider config loader

### Phase 3: CLI Integration
- [ ] `helix input` command implementation
- [ ] Bead creator integration with DDx tracker
- [ ] Verification loop traceback

### Phase 4: Testing and Validation
- [ ] Unit tests for all components
- [ ] Integration tests with fixture projects
- [ ] Acceptance criteria validation

### Phase 5: Deprecation Period (v0.4.x)
- [ ] Add deprecation warnings to legacy commands
- [ ] Document migration path
- [ ] Monitor usage patterns

### Phase 6: Full Release (v1.0)
- [ ] Remove deprecated commands (optional, can keep as aliases)
- [ ] Update all documentation
- [ ] Training materials for new model

## Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Graph traversal produces incorrect results | Medium | High | Extensive test fixtures, gradual rollout |
| Conflict classification too aggressive/conservative | Medium | Medium | Tunable thresholds, human review option |
| Backward compatibility breaks existing workflows | Low | High | Deprecation period, thorough testing |
| Users confused by autonomy levels | Medium | Low | Clear documentation, sensible defaults |

## Open Questions

1. Should `helix input` support batch mode (multiple requests at once)?
2. How do we handle multi-repo scenarios where artifacts span repositories?
3. Should speculation beads auto-expire if not reviewed within N days?
4. What's the exact format for test-to-spec traceability in code files?

## References

- [FEAT-011: Slider Autonomy Control](../01-frame/features/FEAT-011-slider-autonomy.md)
- [Artifact Hierarchy](../../../workflows/artifact-hierarchy.md)
- [ADR-001: Supervisory Control Model](adr/ADR-001-supervisory-control-model.md)

---

*This technical design is in PROPOSED status. Requires review and approval before implementation begins.*
