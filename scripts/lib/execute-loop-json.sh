#!/usr/bin/env bash
# Parser for `ddx agent execute-loop --once --json` output.
#
# This library is sourced by both scripts/helix (for post-cycle bookkeeping)
# and tests/helix-loop-integration.sh (for direct schema assertions).
#
# Schema reference:
#   docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md
#   ("Workflow Handoff Points" section, lines ~200-240)
#
# Contract surface:
#   helix_parse_execute_loop_json <json-string>
#     Validates the top-level schema. Required fields per non-empty result:
#       results[].bead_id  (non-empty string)
#       results[].status   (non-empty string)
#     Unknown top-level or per-result fields are tolerated silently.
#     On success: emits one TSV line per result on stdout:
#       <bead_id>\t<status>\t<retry_after>\t<preserve_ref>\t<result_rev>
#       (missing optional fields emit empty strings)
#     On failure: emits a structured error to stderr beginning with
#       "execute-loop-json:" and exits with status 65 (EX_DATAERR).
#
#   helix_execute_loop_summary <json-string>
#     Emits a single line "<attempts> <successes> <failures>" for downstream
#     cycle counting; treats absent fields as 0.

# Resolve a jq runner. Prefer the system jq when present; fall back to
# `ddx jq` (which the CI step installs alongside ddx itself).
_helix_loop_json_jq() {
  if command -v jq >/dev/null 2>&1; then
    jq "$@"
  else
    ddx jq "$@"
  fi
}

helix_parse_execute_loop_json() {
  local payload="$1"

  if [[ -z "$payload" ]]; then
    printf 'execute-loop-json: empty payload\n' >&2
    return 65
  fi

  # Top-level must parse as an object.
  if ! printf '%s' "$payload" | _helix_loop_json_jq -e 'type == "object"' >/dev/null 2>&1; then
    printf 'execute-loop-json: top-level value is not a JSON object\n' >&2
    return 65
  fi

  # If results is present it must be an array.
  if ! printf '%s' "$payload" | _helix_loop_json_jq -e '(.results // []) | type == "array"' >/dev/null 2>&1; then
    printf 'execute-loop-json: results field is not an array\n' >&2
    return 65
  fi

  # Strict required-field check. Build a list of (index, missing-field) pairs.
  local missing
  missing="$(printf '%s' "$payload" | _helix_loop_json_jq -r '
    (.results // [])
    | to_entries[]
    | . as $entry
    | [
        (if ($entry.value.bead_id // "") == "" or ($entry.value.bead_id | type) != "string"
         then "results[\($entry.key)].bead_id" else empty end),
        (if ($entry.value.status // "") == "" or ($entry.value.status | type) != "string"
         then "results[\($entry.key)].status"  else empty end)
      ][]
  ' 2>/dev/null)"

  if [[ -n "$missing" ]]; then
    printf 'execute-loop-json: missing required field(s):\n' >&2
    printf '  - %s\n' $missing >&2
    return 65
  fi

  # Emit normalized TSV rows. Unknown fields are silently ignored.
  printf '%s' "$payload" | _helix_loop_json_jq -r '
    (.results // [])[]
    | [
        .bead_id,
        .status,
        (.retry_after   // ""),
        (.preserve_ref  // ""),
        (.result_rev    // "")
      ]
    | @tsv
  '
}

helix_execute_loop_summary() {
  local payload="$1"
  printf '%s' "$payload" | _helix_loop_json_jq -r '
    [
      (.attempts  // 0),
      (.successes // 0),
      (.failures  // 0)
    ] | join(" ")
  '
}
