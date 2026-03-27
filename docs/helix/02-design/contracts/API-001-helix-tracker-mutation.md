# API Contract: HELIX Tracker Mutation Surface [FEAT-002]

**Contract ID**: API-001
**Type**: CLI | Library

## CLI Interface

### Command: `helix tracker update`
**Purpose**: Mutate one existing tracker issue through supported field-level operations.  
**Usage**: `$ helix tracker update <id> [mutation flags]`

**Supported mutation classes**:
- workflow state: `--status`, `--claim`, `--assignee`, `--priority`
- descriptive fields: `--title`, `--description`, `--design`, `--acceptance`, `--notes`
- structural metadata: `--labels`
- required future metadata surface for HELIX refinement flows:
  - `--spec-id`
  - `--parent`
  - `--deps`
  - `--refs`

**Input**: command-line flags mapped to one issue mutation request  
**Output**: human-readable success or explicit failure  

**Exit Codes**:
- `0`: mutation applied successfully
- `1`: invalid command usage, missing issue, malformed tracker state, or failed safety check
- `2`: conflict detected and mutation not applied

**Examples**:
```bash
$ helix tracker update hx-abc123 --description "Clarify failure handling"
$ helix tracker update hx-abc123 --spec-id workflows/TRACKER.md
$ helix tracker update hx-abc123 --deps hx-def456,hx-fedcba
```

### Command: `helix tracker dep add`
**Purpose**: Add one dependency edge between tracker issues.

**Safety Requirement**:
- The mutation must not silently overwrite unrelated concurrent changes.
- If the tracker state is malformed or the write cannot be applied safely, the
  command must fail explicitly.

## Library API

### Function: `tracker_write_all`
```bash
tracker_write_all <json-array>
```
- **Purpose**: Replace the tracker file with a validated JSON array serialized
  back to JSONL.
- **Returns**: success only when the write completes safely
- **Fails**: when the current tracker state is malformed, the target state is
  invalid, or the write cannot be applied safely under the supported local
  execution model

### Function: `tracker_read_all`
```bash
tracker_read_all
```
- **Purpose**: Read all tracker issues as a JSON array
- **Returns**: valid JSON array of issues
- **Fails**: when `.helix/issues.jsonl` is malformed

## Data Contracts

### Issue Mutation Request
```json
{
  "id": "hx-abc123",
  "mutations": {
    "description": "Clarify failure handling",
    "spec-id": "workflows/TRACKER.md",
    "deps": ["hx-def456"]
  }
}
```

### Error Response Format
```json
{
  "error": {
    "code": "TRACKER_CONFLICT",
    "message": "Tracker mutation could not be applied safely",
    "details": {
      "issue_id": "hx-abc123",
      "reason": "stale base state or malformed tracker file"
    }
  }
}
```

## Validation

### Test Scenarios
1. **Happy Path**: supported field mutations update exactly one issue and
   preserve valid JSONL output.
2. **Malformed Input File**: tracker commands fail explicitly when
   `.helix/issues.jsonl` cannot be parsed as valid JSONL.
3. **Interrupted or Partial Write Detection**: commands surface failure rather
   than continuing on invalid tracker state.
4. **Conflicting Mutation Handling**: overlapping write attempts are detected
   or prevented under the supported local execution model.
5. **Metadata Mutation Coverage**: supported HELIX refinement fields are
   mutated through CLI/API surfaces instead of direct JSONL edits.
