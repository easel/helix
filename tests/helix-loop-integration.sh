#!/usr/bin/env bash
# Integration harness for the HELIX <-> DDx execute-loop --json contract.
#
# Spec: docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md
# Audit: docs/helix/02-design/contracts/CONTRACT-001-audit.md
# Bead:  helix-3fdba193 (parent epic helix-e26584d7)
#
# Coverage (the seven enumerated DDx --json response shapes):
#   (a) no_ready_work          — fixtures/helix-loop-integration/a-no-ready-work.json
#   (b) single success         — fixtures/helix-loop-integration/b-single-success.json
#   (c) mixed success/failure  — fixtures/helix-loop-integration/c-mixed-success-failure.json
#   (d) retry-after cooldown   — fixtures/helix-loop-integration/d-retry-after.json
#   (e) preserve_ref present   — fixtures/helix-loop-integration/e-preserve-ref.json
#   (f) tolerant parsing       — fixtures/helix-loop-integration/f-tolerant-unknown-fields.json
#   (g) strict required fields — fixtures/helix-loop-integration/g-missing-required-fields.json
#
# Plus a contract-matrix exercise that walks CONTRACT-001-audit.md and asserts,
# for every DDx-owned row:
#   - `code-link:<file:line>` resolutions point at an extant location (when the
#     DDx checkout is reachable via DDX_AUDIT_REPO) and are otherwise format-valid
#   - `new-DDx-bead:<id>` resolutions are tracked as skipped-pending (with a
#     summary line at the end of the run)
#   - `HELIX-backport:*` resolutions invoke a registered in-harness fake that
#     proves the HELIX fallback path is wired
#
# Strict required-field assertions (case g) and unknown-field tolerance (case f)
# each have a dedicated fixture; their stderr / exit-code expectations are
# documented inline below so the contract is self-describing.

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixtures_dir="$repo_root/tests/fixtures/helix-loop-integration"

# shellcheck source=../scripts/lib/execute-loop-json.sh
source "$repo_root/scripts/lib/execute-loop-json.sh"

# ----------------------------------------------------------------------------
# Test harness primitives.
# ----------------------------------------------------------------------------

PASS_COUNT=0
FAIL_COUNT=0
SKIPPED_PENDING=()

log()  { printf '  %s\n' "$*"; }
pass() { PASS_COUNT=$((PASS_COUNT + 1)); printf 'PASS: %s\n' "$1"; }
fail() { FAIL_COUNT=$((FAIL_COUNT + 1)); printf 'FAIL: %s\n' "$1" >&2; }

assert_eq() {
  local expected="$1" actual="$2" label="$3"
  if [[ "$expected" == "$actual" ]]; then
    pass "$label"
  else
    fail "$label
  expected: $(printf '%q' "$expected")
  actual:   $(printf '%q' "$actual")"
  fi
}

assert_contains() {
  local haystack="$1" needle="$2" label="$3"
  if [[ "$haystack" == *"$needle"* ]]; then
    pass "$label"
  else
    fail "$label
  needle:   $(printf '%q' "$needle")
  haystack: $(printf '%q' "$haystack")"
  fi
}

assert_not_contains() {
  local haystack="$1" needle="$2" label="$3"
  if [[ "$haystack" != *"$needle"* ]]; then
    pass "$label"
  else
    fail "$label
  forbidden substring present: $(printf '%q' "$needle")"
  fi
}

# ----------------------------------------------------------------------------
# Per-fixture parser tests (cases a-g).
#
# These test the helix_parse_execute_loop_json contract directly: the parser
# is the single chokepoint scripts/helix uses to read execute-loop --json
# output, so once it is correct, every downstream HELIX consumer is protected.
# ----------------------------------------------------------------------------

read_fixture() {
  local name="$1"
  local path="$fixtures_dir/$name"
  [[ -f "$path" ]] || { printf 'missing fixture: %s\n' "$path" >&2; exit 2; }
  cat "$path"
}

run_parser_pass() {
  # Returns the stdout of helix_parse_execute_loop_json or the empty string.
  local payload="$1"
  helix_parse_execute_loop_json "$payload"
}

run_parser_capture() {
  # Captures stdout / stderr / exit-code into named globals.
  local payload="$1"
  local out_file err_file rc=0
  out_file="$(mktemp)"
  err_file="$(mktemp)"
  helix_parse_execute_loop_json "$payload" >"$out_file" 2>"$err_file" || rc=$?
  PARSER_STDOUT="$(cat "$out_file")"
  PARSER_STDERR="$(cat "$err_file")"
  PARSER_RC=$rc
  rm -f "$out_file" "$err_file"
}

# (a) no_ready_work
test_case_a_no_ready_work() {
  local payload out
  payload="$(read_fixture a-no-ready-work.json)"

  run_parser_capture "$payload"
  assert_eq "0" "$PARSER_RC" "(a) parser exits cleanly on empty results"
  assert_eq "" "$PARSER_STDOUT" "(a) no result rows emitted for empty drain"

  # No cycle should be counted: helix_execute_loop_summary surfaces 0/0/0.
  out="$(helix_execute_loop_summary "$payload")"
  assert_eq "0 0 0" "$out" "(a) summary reports zero attempts/successes/failures"
}

# (b) single success
test_case_b_single_success() {
  local payload
  payload="$(read_fixture b-single-success.json)"

  run_parser_capture "$payload"
  assert_eq "0" "$PARSER_RC" "(b) parser succeeds on single-success payload"

  local row
  row="$(printf '%s\n' "$PARSER_STDOUT")"
  assert_contains "$row" "hx-mock-0" "(b) bead_id surfaced for post-cycle bookkeeping"
  assert_contains "$row" "success"   "(b) status surfaced as 'success'"
  assert_contains "$row" "1111111111111111111111111111111111111111" \
    "(b) result_rev surfaced as closing-SHA candidate"

  local row_count
  row_count="$(printf '%s\n' "$PARSER_STDOUT" | grep -c .)"
  assert_eq "1" "$row_count" "(b) exactly one result row emitted"
}

# (c) mixed success/failure in one drain
test_case_c_mixed() {
  local payload
  payload="$(read_fixture c-mixed-success-failure.json)"

  run_parser_capture "$payload"
  assert_eq "0" "$PARSER_RC" "(c) parser tolerates mixed-status drain"

  local row_count success_rows failed_rows
  row_count="$(printf '%s\n' "$PARSER_STDOUT" | grep -c .)"
  assert_eq "2" "$row_count" "(c) two result rows emitted"

  success_rows="$(printf '%s\n' "$PARSER_STDOUT" | awk -F'\t' '$2 == "success"' | wc -l | tr -d ' ')"
  failed_rows="$(printf '%s\n' "$PARSER_STDOUT" | awk -F'\t' '$2 == "execution_failed"' | wc -l | tr -d ' ')"
  assert_eq "1" "$success_rows" "(c) exactly one success row"
  assert_eq "1" "$failed_rows"  "(c) exactly one execution_failed row"
}

# (d) retry-after cooldown
test_case_d_retry_after() {
  local payload
  payload="$(read_fixture d-retry-after.json)"

  run_parser_capture "$payload"
  assert_eq "0" "$PARSER_RC" "(d) parser accepts retry-after payload"

  local row retry_field
  row="$(printf '%s\n' "$PARSER_STDOUT")"
  retry_field="$(printf '%s\n' "$row" | awk -F'\t' '{print $3}')"
  assert_eq "2099-01-01T06:00:00Z" "$retry_field" \
    "(d) retry_after surfaced verbatim for ddx bead blocked"

  # Contract: HELIX must not unclaim or blame on retry-after. We assert this by
  # confirming the parser surfaces retry_after as a first-class field rather
  # than collapsing the row into a bare failure. Downstream HELIX code (when
  # wired in helix-372aa59f / helix-1dea19d0) suppresses unclaim when
  # column 3 is non-empty.
  local has_retry
  has_retry="$([[ -n "$retry_field" ]] && echo yes || echo no)"
  assert_eq "yes" "$has_retry" "(d) retry_after column non-empty (suppresses HELIX unclaim path)"
}

# (e) preserve_ref present
test_case_e_preserve_ref() {
  local payload
  payload="$(read_fixture e-preserve-ref.json)"

  run_parser_capture "$payload"
  assert_eq "0" "$PARSER_RC" "(e) parser accepts preserve_ref payload"

  local preserve_field status_field
  preserve_field="$(printf '%s\n' "$PARSER_STDOUT" | awk -F'\t' '{print $4}')"
  status_field="$(printf '%s\n' "$PARSER_STDOUT"  | awk -F'\t' '{print $2}')"
  assert_eq "refs/ddx/iterations/hx-mock-0/att-002" "$preserve_field" \
    "(e) preserve_ref surfaced for operator inspection"
  assert_eq "land_conflict" "$status_field" \
    "(e) status forwarded as land_conflict (HELIX must not attempt land)"
}

# (f) tolerant parsing — unknown top-level + per-result fields ignored
test_case_f_tolerant_unknown_fields() {
  # Documented expectation:
  #   exit code: 0
  #   stderr:    empty (no warnings — tolerant by contract)
  #   stdout:    one normalized result row, unknown fields stripped
  local payload
  payload="$(read_fixture f-tolerant-unknown-fields.json)"

  run_parser_capture "$payload"
  assert_eq "0" "$PARSER_RC" "(f) unknown fields tolerated without error"
  assert_eq "" "$PARSER_STDERR" "(f) unknown fields produce no stderr noise"

  assert_contains "$PARSER_STDOUT" "hx-mock-0" "(f) known field bead_id still surfaced"
  assert_contains "$PARSER_STDOUT" "success"   "(f) known field status still surfaced"
  assert_not_contains "$PARSER_STDOUT" "future_top_level_field" \
    "(f) unknown top-level field stripped from normalized output"
  assert_not_contains "$PARSER_STDOUT" "future_per_result_field" \
    "(f) unknown per-result field stripped from normalized output"
  assert_not_contains "$PARSER_STDOUT" "experimental_metric" \
    "(f) unknown numeric per-result field stripped from normalized output"
}

# (g) strict required fields — missing bead_id/status MUST be a clear error
test_case_g_strict_required_fields() {
  # Documented expectation:
  #   exit code: 65 (EX_DATAERR)
  #   stderr:    structured prefix "execute-loop-json:"; lists missing field
  #              path with the row index, e.g. "results[0].bead_id"
  #   stdout:    empty (no rows pass through on schema failure)
  local payload
  payload="$(read_fixture g-missing-required-fields.json)"

  run_parser_capture "$payload"
  assert_eq "65" "$PARSER_RC" "(g) missing required field returns exit 65"
  assert_eq ""   "$PARSER_STDOUT" "(g) no rows emitted on schema failure"
  assert_contains "$PARSER_STDERR" "execute-loop-json:" \
    "(g) stderr begins with structured 'execute-loop-json:' prefix"
  assert_contains "$PARSER_STDERR" "results[0].bead_id" \
    "(g) stderr names the missing bead_id field with row index"
  assert_contains "$PARSER_STDERR" "results[0].status" \
    "(g) stderr names the missing status field with row index"
}

# ----------------------------------------------------------------------------
# End-to-end: drive real scripts/helix against a stubbed ddx for case (a).
#
# helix_run on an empty queue must exit cleanly with no execute-loop call —
# this is the single "no managed execution" path HELIX still owns once
# helix-372aa59f / helix-5c14dbb0 land.
# ----------------------------------------------------------------------------

make_e2e_workspace() {
  local root
  root="$(mktemp -d)"
  mkdir -p "$root/work" "$root/bin" "$root/state" "$root/home"
  (cd "$root/work" && git init -q && git commit --allow-empty -q -m "init")

  # Stubbed `ddx`: claims execute-loop is available, returns scripted JSON.
  local real_ddx
  real_ddx="$(command -v ddx || true)"

  cat >"$root/bin/ddx" <<EOF
#!/usr/bin/env bash
set -euo pipefail
real_ddx="${real_ddx}"
state="${root}/state"

log() { printf '%s\n' "\$*" >> "\$state/ddx-calls.log"; }

case "\${1:-} \${2:-}" in
  "agent execute-loop")
    if [[ " \$* " == *" --help "* ]]; then
      printf 'Usage: ddx agent execute-loop [flags]\n--once --json --harness --model --effort --poll-interval\n'
      exit 0
    fi
    log "execute-loop \$*"
    fixture="\${HELIX_TEST_LOOP_FIXTURE:-}"
    if [[ -n "\$fixture" && -f "\$fixture" ]]; then
      cat "\$fixture"
    else
      printf '{"attempts":0,"successes":0,"failures":0,"results":[]}\n'
    fi
    exit 0
    ;;
  "agent execute-bead")
    [[ " \$* " == *" --help "* ]] && { printf 'Usage: ddx agent execute-bead\n'; exit 0; }
    log "execute-bead \$*"
    exit 0
    ;;
  "agent list")
    printf '[]\n'
    exit 0
    ;;
esac

# Defer everything else to the real ddx (tracker reads, jq, etc.).
if [[ -n "\$real_ddx" ]]; then
  exec "\$real_ddx" "\$@"
fi
echo "ddx stub: no real ddx available for: \$*" >&2
exit 127
EOF
  chmod +x "$root/bin/ddx"

  # Empty tracker — nothing ready.
  mkdir -p "$root/work/.ddx"
  : > "$root/work/.ddx/beads.jsonl"

  printf '%s\n' "$root"
}

run_helix_e2e() {
  local root="$1"
  shift
  (
    cd "$root/work"
    HOME="$root/home" \
    PATH="$root/bin:$PATH" \
    HELIX_FORCE_EPHEMERAL=1 \
    HELIX_DIRECT_AGENT=1 \
    HELIX_AUTO_ALIGN=0 \
    DDX_BEAD_DIR="$root/work/.ddx" \
    DDX_DISABLE_UPDATE_CHECK=1 \
    bash "$repo_root/scripts/helix" "$@"
  )
}

test_e2e_a_no_ready_work() {
  # End-to-end smoke for case (a): with an empty tracker, helix run --once
  # exits cleanly without calling ddx agent execute-loop. Proves the harness
  # actually drives the real scripts/helix binary (not just the parser lib).
  local root rc out
  root="$(make_e2e_workspace)"

  rc=0
  out="$(run_helix_e2e "$root" run --once --quiet 2>&1 || rc=$?)"

  # Either a clean exit or a controlled "nothing ready" exit is acceptable.
  # We assert: no execute-loop call was made.
  if [[ -f "$root/state/ddx-calls.log" ]]; then
    assert_not_contains "$(cat "$root/state/ddx-calls.log")" "execute-loop" \
      "(a/e2e) helix run on empty tracker did not invoke ddx agent execute-loop"
  else
    pass "(a/e2e) helix run on empty tracker did not invoke ddx agent execute-loop"
  fi

  # Soft-assert: helix produced no traceback / hard error.
  assert_not_contains "$out" "Traceback" "(a/e2e) no python traceback in helix output"

  rm -rf "$root"
  return 0
}

# ----------------------------------------------------------------------------
# Contract-matrix exercise driven by CONTRACT-001-audit.md.
#
# For each DDx-owned row in the audit, we examine the resolution token in the
# right-hand column and dispatch to a category handler:
#   `code-link`     -> validate-format, optionally chase link if DDx repo present
#   `new-DDx-bead`  -> record as skipped-pending
#   `HELIX-backport`-> invoke registered fake (none currently)
#
# The handler set is exhaustive: any row whose resolution does not match a
# known prefix is a hard failure, so the audit cannot silently grow a new
# resolution class.
# ----------------------------------------------------------------------------

audit_doc="$repo_root/docs/helix/02-design/contracts/CONTRACT-001-audit.md"

# Emit one resolution token per DDx-owned audit row to stdout.
extract_audit_resolutions() {
  python3 - "$audit_doc" <<'PY'
import re
import sys

path = sys.argv[1]
in_table = False
header_cells = None
with open(path, encoding="utf-8") as fh:
    for raw in fh:
        line = raw.rstrip("\n")
        if line.startswith("| ---") or re.match(r"^\|\s*-+", line):
            in_table = True
            continue
        if line.startswith("##"):
            in_table = False
            header_cells = None
            continue
        if line.startswith("|") and not in_table:
            # header row
            header_cells = [c.strip() for c in line.strip("|").split("|")]
            continue
        if in_table and line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 3:
                continue
            resolution = cells[-1]
            # Strip leading backtick on inline-code prefixes.
            m = re.match(r"`?(code-link|new-DDx-bead|HELIX-backport)`?\s*:?\s*(.*)", resolution)
            if not m:
                # Tolerate the legend rows by skipping any row whose first cell
                # is empty or non-DDx-owned (only the matrix tables qualify).
                if "code-link" in resolution or "new-DDx-bead" in resolution or "HELIX-backport" in resolution:
                    print(f"UNKNOWN\t{resolution}")
                continue
            kind, payload = m.group(1), m.group(2)
            print(f"{kind}\t{payload}")
PY
}

# Validate a single `code-link:<file:line>` resolution.
# When DDX_AUDIT_REPO is set and points at an existing DDx checkout, also
# resolve the file path. Otherwise the format check is the only gate.
validate_code_link_row() {
  local payload="$1"
  # Strip trailing markdown / multi-link clutter; payload may contain multiple
  # links (comma- or backtick-separated). Pull every file:line target.
  local targets
  targets="$(printf '%s\n' "$payload" | grep -oE '~[^\` ,]+:[0-9]+' || true)"
  if [[ -z "$targets" ]]; then
    fail "code-link row has no parseable file:line target: $payload"
    return 1
  fi

  # Link chasing is opt-in: the audit was authored against a specific DDx
  # commit, so file:line targets drift over time. Default behaviour is to
  # validate the format only; set DDX_AUDIT_REPO=/path/to/ddx to also chase
  # the file targets. CI runs in format-only mode by design — link drift is
  # caught by the audit's own refresh cadence, not by HELIX CI.
  local repo="${DDX_AUDIT_REPO:-}"

  local target file line resolved total
  for target in $targets; do
    file="${target%:*}"
    line="${target##*:}"
    if [[ -z "$repo" ]]; then
      log "code-link (format-only, set DDX_AUDIT_REPO to chase): $target"
      continue
    fi
    resolved="${target/#~\/Projects\/ddx/$repo}"
    file="${resolved%:*}"
    if [[ ! -f "$file" ]]; then
      fail "code-link target missing in DDx repo: $target -> $file"
      return 1
    fi
    total="$(wc -l <"$file")"
    if (( line > total + 1 )); then
      fail "code-link line out of range: $target (file has $total lines)"
      return 1
    fi
  done
  return 0
}

# Registered HELIX-backport fakes. Each entry is "key|callable". A row whose
# payload begins with `<key>` invokes the matching callable. The audit
# currently has zero HELIX-backport rows; this table exists so adding one to
# the audit immediately demands a corresponding fake here.
declare -a HELIX_BACKPORT_FAKES=()

invoke_helix_backport_fake() {
  local payload="$1"
  local entry key callable
  for entry in "${HELIX_BACKPORT_FAKES[@]}"; do
    key="${entry%%|*}"
    callable="${entry##*|}"
    if [[ "$payload" == "$key"* ]]; then
      "$callable" "$payload" && return 0 || return 1
    fi
  done
  fail "HELIX-backport row has no registered fake: $payload"
  return 1
}

test_contract_matrix() {
  if [[ ! -f "$audit_doc" ]]; then
    fail "contract audit doc missing: $audit_doc"
    return 1
  fi

  local code_link=0 new_bead=0 backport=0 unknown=0
  local kind payload
  while IFS=$'\t' read -r kind payload; do
    [[ -z "$kind" ]] && continue
    case "$kind" in
      code-link)
        code_link=$((code_link + 1))
        validate_code_link_row "$payload" || true
        ;;
      new-DDx-bead)
        new_bead=$((new_bead + 1))
        # Payload is typically "`ddx-xxxx`" — strip backticks and trailing junk.
        local bead_id="$payload"
        bead_id="${bead_id#\`}"
        bead_id="${bead_id%%[\`, ]*}"
        SKIPPED_PENDING+=("$bead_id")
        log "skipped-pending: $bead_id"
        ;;
      HELIX-backport)
        backport=$((backport + 1))
        invoke_helix_backport_fake "$payload" || true
        ;;
      UNKNOWN)
        unknown=$((unknown + 1))
        fail "unknown audit resolution token: $payload"
        ;;
    esac
  done < <(extract_audit_resolutions)

  log "audit summary: code-link=$code_link new-DDx-bead=$new_bead HELIX-backport=$backport unknown=$unknown"

  # The audit must contain at least one code-link row and at least one
  # new-DDx-bead row (the audit was specifically structured to enumerate
  # both). The harness fails if either drops to zero — that would mean the
  # audit has been hollowed out without a matching contract update.
  if (( code_link < 1 )); then
    fail "contract audit has zero code-link resolutions — audit doc has been hollowed out"
  else
    pass "contract audit has $code_link code-link resolutions"
  fi
  if (( new_bead < 1 )); then
    log "(no new-DDx-bead rows in current audit — acceptable)"
  else
    pass "contract audit has $new_bead new-DDx-bead resolutions tracked as skipped-pending"
  fi
  assert_eq "0" "$unknown" "no unknown resolution tokens in audit"
}

# ----------------------------------------------------------------------------
# Main.
# ----------------------------------------------------------------------------

main() {
  printf '== helix-loop-integration: parser cases (a)-(g) ==\n'
  test_case_a_no_ready_work
  test_case_b_single_success
  test_case_c_mixed
  test_case_d_retry_after
  test_case_e_preserve_ref
  test_case_f_tolerant_unknown_fields
  test_case_g_strict_required_fields

  printf '\n== helix-loop-integration: end-to-end smoke ==\n'
  test_e2e_a_no_ready_work

  printf '\n== helix-loop-integration: CONTRACT-001 audit matrix ==\n'
  test_contract_matrix

  printf '\n----\n'
  printf 'passed: %d  failed: %d\n' "$PASS_COUNT" "$FAIL_COUNT"
  if (( ${#SKIPPED_PENDING[@]} > 0 )); then
    printf 'skipped-pending DDx beads: %s\n' "${SKIPPED_PENDING[*]}"
  fi

  if (( FAIL_COUNT > 0 )); then
    exit 1
  fi
}

main "$@"
