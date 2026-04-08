# Slider Autonomy Test Harness

This document defines **concrete, measurable tests** for the slider autonomy feature before merge.

## Philosophy

- No "it works" assertions - only observable outputs
- Tests run against fixture projects with known inputs/outputs
- Measurable: pass/fail based on exact output comparison
- Can be run manually or automated via CI

---

## Test 1: Artifact ID Parsing

**Goal**: Verify `[[ID]]` extraction handles all real-world patterns.

### Setup
```bash
# Create test fixture file
cat > /tmp/test-crossrefs.md << 'EOF'
# Test Document

References: [[US-036-list-mcp-servers]], [[FEAT-011]], [[TD-001]]
Also: [[helix.workflow.artifact-hierarchy]], [[ADR-001]]
And slugs: [[US-999-completely-different-feature-name]]
EOF

# Run extraction command from TD-011 Decision 2
rg '\[\[([A-Z]+-\d+(?:-[a-z0-9-]+)?|helix(?:\.[a-z][a-z-]*)+)\]\]' /tmp/test-crossrefs.md | \
  sed 's/.*\[\[\([^]]*\)\]\].*/\1/' | sort -u
```

### Expected Output (exact match)
```
ADR-001
FEAT-011
TD-001
US-036-list-mcp-servers
US-999-completely-different-feature-name
helix.workflow.artifact-hierarchy
```

### Pass Criteria
```bash
# Save expected output
cat > /tmp/expected-ids.txt << 'EOF'
ADR-001
FEAT-011
TD-001
US-036-list-mcp-servers
US-999-completely-different-feature-name
helix.workflow.artifact-hierarchy
EOF

# Compare (exit 0 = pass)
diff -q /tmp/expected-ids.txt <(rg '\[\[([A-Z]+-\d+(?:-[a-z0-9-]+)?|helix(?:\.[a-z][a-z-]*)+)\]\]' /tmp/test-crossrefs.md | sed 's/.*\[\[\([^]]*\)\]\].*/\1/' | sort -u)
echo $?  # Should be 0
```

---

## Test 2: Reverse Index Construction

**Goal**: Verify downstream dependency mapping works correctly.

### Setup
Create minimal fixture project in `/tmp/test-project/`:

```bash
mkdir -p /tmp/test-project/docs/helix/{01-frame/features,01-frame/user-stories,02-design/technical-designs}

# FEAT-001 references US-001 and US-002
cat > /tmp/test-project/docs/helix/01-frame/features/FEAT-001-test.md << 'EOF'
# FEAT-001: Test Feature
**User Stories**: [[US-001-first]], [[US-002-second]]
EOF

# US-001 references TD-001
cat > /tmp/test-project/docs/helix/01-frame/user-stories/US-001-first.md << 'EOF'
# US-001: First Story
**Technical Design**: [[TD-001]]
EOF

# US-002 references TD-002
cat > /tmp/test-project/docs/helix/01-frame/user-stories/US-002-second.md << 'EOF'
# US-002: Second Story
**Technical Design**: [[TD-002]]
EOF

# TD-001 references TP-001
cat > /tmp/test-project/docs/helix/02-design/technical-designs/TD-001-first.md << 'EOF'
# TD-001: First Design
**Test Plan**: [[TP-001]]
EOF

# TD-002 references TP-002
cat > /tmp/test-project/docs/helix/02-design/technical-designs/TD-002-second.md << 'EOF'
# TD-002: Second Design
**Test Plan**: [[TP-002]]
EOF

# TP files (leaf nodes)
echo "# TP-001" > /tmp/test-project/docs/helix/03-test/test-plans/TP-001.md
echo "# TP-002" > /tmp/test-project/docs/helix/03-test/test-plans/TP-002.md
```

### Test: Downstream Traversal from FEAT-001

```bash
cd /tmp/test-project

# Expected downstream artifacts when FEAT-001 changes:
cat > /tmp/expected-downstream.txt << 'EOF'
TD-001
TD-002
TP-001
TP-002
US-001-first
US-002-second
EOF

# Run traversal (simplified version - actual implementation would use reverse index)
# For now, test the concept: find all artifacts that transitively reference FEAT-001

find_downstream() {
    local start_id="$1"
    local current_ids=("$start_id")
    local visited=()
    
    while [ ${#current_ids[@]} -gt 0 ]; do
        local id="${current_ids[0]}"
        current_ids=("${current_ids[@]:1}")
        
        # Skip if already visited
        [[ " ${visited[*]} " =~ " $id " ]] && continue
        visited+=("$id")
        
        # Find all artifacts that reference this ID
        local refs=$(rg "\[\[$id\]\]" docs/helix/ --glob "*.md" -l 2>/dev/null)
        for file in $refs; do
            # Extract the artifact ID from filename
            local ref_id=$(basename "$file" .md | cut -d'/' -f1)
            current_ids+=("$ref_id")
        done
    done
    
    # Output all visited except start node
    printf '%s\n' "${visited[@]}" | grep -v "^$start_id$" | sort
}

find_downstream "FEAT-001" > /tmp/actual-downstream.txt

# Compare (exit 0 = pass)
diff -q /tmp/expected-downstream.txt /tmp/actual-downstream.txt && echo "PASS: Downstream traversal correct" || echo "FAIL: Mismatch"
```

### Pass Criteria
- All downstream artifacts found: US-001, US-002, TD-001, TD-002, TP-001, TP-002
- No false positives (artifacts not in chain)

---

## Test 3: Authority Ordering

**Goal**: Verify artifacts are processed in correct canonical order.

### Setup
```bash
# Create test artifact list with mixed types
cat > /tmp/test-artifacts.txt << 'EOF'
TD-001-first-design
US-001-first-story
FEAT-001-test-feature
TP-001-tests
SD-001-solution
ADR-001-decision
prd.md
vision.md
```

### Test: Sort by Authority Tier

```bash
# Define authority tiers (from TD-011)
get_tier() {
    case "$1" in
        vision*) echo 0 ;;
        prd*) echo 1 ;;
        FEAT*) echo 2 ;;
        US*) echo 3 ;;
        ADR*|architecture*) echo 4 ;;
        SD*) echo 5 ;;
        TD*) echo 6 ;;
        TP*) echo 7 ;;
        tests*) echo 8 ;;
        implementation_plan*) echo 9 ;;
        code*) echo 10 ;;
    esac
}

# Sort artifacts by tier
while read artifact; do
    tier=$(get_tier "$artifact")
    echo "$tier $artifact"
done < /tmp/test-artifacts.txt | sort -n | cut -d' ' -f2 > /tmp/sorted-artifacts.txt

cat /tmp/sorted-artifacts.txt
```

### Expected Output (exact match)
```
vision.md
prd.md
FEAT-001-test-feature
US-001-first-story
ADR-001-decision
SD-001-solution
TD-001-first-design
TP-001-tests
```

### Pass Criteria
```bash
cat > /tmp/expected-order.txt << 'EOF'
vision.md
prd.md
FEAT-001-test-feature
US-001-first-story
ADR-001-decision
SD-001-solution
TD-001-first-design
TP-001-tests
EOF

diff -q /tmp/expected-order.txt /tmp/sorted-artifacts.txt && echo "PASS: Authority ordering correct" || echo "FAIL: Order mismatch"
```

---

## Test 4: Conflict Classification

**Goal**: Verify resolvable vs physics-level detection works correctly.

### Setup
Create test cases with known conflict types:

```bash
mkdir -p /tmp/conflict-tests/{resolvable,physics}

# Resolvable: Technology choice (Postgres vs SQLite)
cat > /tmp/conflict-tests/resolvable/tech-choice.md << 'EOF'
## Constraints
- Must use a relational database
- Prefer PostgreSQL for production workloads
EOF

cat > /tmp/conflict-tests/resolvable/tech-choice-alt.md << 'EOF'
## Constraints  
- Database layer should support SQLite for embedded deployments
EOF

# Physics-level: True contradiction
cat > /tmp/conflict-tests/physics/contradiction.md << 'EOF'
## Requirements
- System must process requests in real-time (< 100ms)
- All processing must be batch-only (no streaming allowed)
EOF
```

### Test: Classification Heuristic

```bash
# Simple heuristic test - check for contradiction patterns
classify_conflict() {
    local file="$1"
    
    # Check for physics-level patterns in structured sections only
    if grep -A5 "## Requirements\|## Constraints" "$file" | \
       rg -i "(real-time.*batch-only|must.*NOT.*must|only.*alternative)"; then
        echo "physics-level"
    else
        echo "resolvable"
    fi
}

# Test resolvable case
result=$(classify_conflict /tmp/conflict-tests/resolvable/tech-choice.md)
[ "$result" = "resolvable" ] && echo "PASS: Tech choice classified as resolvable" || echo "FAIL: Expected resolvable, got $result"

# Test physics-level case  
result=$(classify_conflict /tmp/conflict-tests/physics/contradiction.md)
[ "$result" = "physics-level" ] && echo "PASS: Contradiction classified as physics-level" || echo "FAIL: Expected physics-level, got $result"
```

### Pass Criteria
- Technology choices → resolvable (can escalate via bead)
- True contradictions → physics-level (block execution)

---

## Test 5: End-to-End Impact Detection

**Goal**: Verify complete flow from input to downstream beads.

### Setup
Use the fixture project from Test 2, add a "helix input" simulation:

```bash
cd /tmp/test-project

# Simulate user input that should impact FEAT-001
INPUT="change the authentication requirement in feature one"

# Expected impacted artifacts (based on graph traversal)
cat > /tmp/expected-impacted.txt << 'EOF'
FEAT-001-test-feature
TD-001-first-design
TD-002-second-design
TP-001-tests
TP-002-tests
US-001-first-story
US-002-second-story
```

### Test: Full Impact Detection Pipeline

```bash
# Phase 1: Search for "feature one" or "authentication" in artifacts
search_terms=("feature" "authentication")
impacted=()

for term in "${search_terms[@]}"; do
    # Find matching artifacts
    matches=$(rg "$term" docs/helix/ --glob "*.md" -l 2>/dev/null)
    for file in $matches; do
        id=$(basename "$file" .md | cut -d'/' -f1)
        impacted+=("$id")
        
        # Phase 2: Add downstream artifacts (using reverse index concept)
        # Simplified: find all that reference this ID
        downstream=$(rg "\[\[$id\]\]" docs/helix/ --glob "*.md" -l 2>/dev/null | \
                     xargs -I{} basename {} .md | cut -d'/' -f1)
        impacted+=("$downstream")
    done
done

# Deduplicate and sort
printf '%s\n' "${impacted[@]}" | sort -u > /tmp/actual-impacted.txt

cat /tmp/actual-impacted.txt
```

### Pass Criteria
```bash
# Check that all expected artifacts are in actual output (subset check)
all_found=true
while read expected; do
    if ! grep -q "^$expected$" /tmp/actual-impacted.txt; then
        echo "MISSING: $expected"
        all_found=false
    fi
done < /tmp/expected-impacted.txt

if [ "$all_found" = true ]; then
    echo "PASS: All expected artifacts detected"
else
    echo "FAIL: Some artifacts missing from impact detection"
fi
```

---

## Test 6: Verification Loop Traceback

**Goal**: Verify failing test traces back to correct spec.

### Setup
Create test file with spec reference metadata:

```bash
mkdir -p /tmp/verification-test/tests

cat > /tmp/verification-test/tests/auth.test.js << 'EOF'
/**
 * @spec-ref TD-001-auth-design
 * @requirement TC-001
 */
test('authentication returns 200 on valid token', async () => {
    const response = await auth('/api/login', { token: 'valid-token' });
    expect(response.status).toBe(200);  // This will fail - actual is 401
});
EOF

# Create corresponding spec
mkdir -p /tmp/verification-test/docs/helix/02-design/technical-designs
cat > /tmp/verification-test/docs/helix/02-design/technical-designs/TD-001-auth-design.md << 'EOF'
# TD-001: Auth Design
**User Story**: [[US-001-auth]]

## API Response Format
Authentication endpoint returns 200 on valid token.
EOF
```

### Test: Extract Spec Reference and Trace Back

```bash
cd /tmp/verification-test

# Step 1: Parse test metadata
spec_ref=$(grep '@spec-ref' tests/auth.test.js | sed 's/.*@spec-ref \([^ ]*\).*/\1/')
echo "Found spec reference: $spec_ref"

# Step 2: Verify spec exists and extract upstream refs
if [ -f "docs/helix/02-design/technical-designs/$spec_ref.md" ]; then
    echo "PASS: Spec file found"
    
    # Extract upstream references from spec
    upstream=$(grep '\[\[US-' "docs/helix/02-design/technical-designs/$spec_ref.md" | \
               sed 's/.*\[\[\([^]]*\)\]\].*/\1/')
    echo "Upstream reference: $upstream"
    
    # Verify upstream exists
    if [ -f "docs/helix/01-frame/user-stories/$upstream.md" ]; then
        echo "PASS: Upstream artifact found - traceback chain complete"
    else
        echo "FAIL: Upstream artifact missing"
    fi
else
    echo "FAIL: Spec file not found"
fi
```

### Pass Criteria
- Test metadata correctly parsed (`@spec-ref TD-001-auth-design`)
- Spec file exists and contains upstream reference
- Upstream artifact (US-001-auth) can be located

---

## Running All Tests

Create a test runner script:

```bash
cat > /tmp/run-slider-tests.sh << 'EOF'
#!/bin/bash
set -e

echo "=== Slider Autonomy Test Suite ==="
echo ""

# Track results
passed=0
failed=0

run_test() {
    local name="$1"
    local cmd="$2"
    
    echo "--- Test: $name ---"
    if eval "$cmd"; then
        ((passed++))
        return 0
    else
        ((failed++))
        return 1
    fi
}

# Run individual tests (implement each as described above)
run_test "ID Parsing" "bash /tmp/test-1-parsing.sh" || true
run_test "Reverse Index" "bash /tmp/test-2-reverse-index.sh" || true  
run_test "Authority Ordering" "bash /tmp/test-3-authority.sh" || true
run_test "Conflict Classification" "bash /tmp/test-4-conflicts.sh" || true
run_test "Impact Detection" "bash /tmp/test-5-impact.sh" || true
run_test "Verification Traceback" "bash /tmp/test-6-traceback.sh" || true

echo ""
echo "=== Results ==="
echo "Passed: $passed"
echo "Failed: $failed"
echo ""

if [ $failed -eq 0 ]; then
    echo "✓ All tests passed - ready for merge"
    exit 0
else
    echo "✗ Some tests failed - fix before merging"
    exit 1
fi
EOF

chmod +x /tmp/run-slider-tests.sh
```

---

## Merge Gate Checklist

Before merging slider autonomy changes:

- [ ] Test 1 (ID Parsing): PASS
- [ ] Test 2 (Reverse Index): PASS  
- [ ] Test 3 (Authority Ordering): PASS
- [ ] Test 4 (Conflict Classification): PASS
- [ ] Test 5 (Impact Detection): PASS
- [ ] Test 6 (Verification Traceback): PASS
- [ ] All existing HELIX tests still pass (`bash tests/helix-cli.sh`)
- [ ] No regressions in artifact hierarchy

**Run command**: `bash /tmp/run-slider-tests.sh`

---

## Notes for Implementation

When implementing the actual feature:

1. **Replace test fixtures with real code** - These bash scripts become unit tests
2. **Add to CI pipeline** - Run on every PR before merge
3. **Extend coverage** - Add more edge cases (circular refs, missing artifacts, etc.)
4. **Performance testing** - Measure traversal time on large artifact graphs

This harness proves the design works before any production code is written.
