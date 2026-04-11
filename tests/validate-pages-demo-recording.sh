#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
record_script="$repo_root/scripts/record_pages_demos.sh"
pages_workflow="$repo_root/.github/workflows/pages.yml"

fail() {
  printf 'pages demo recording validation failed: %s\n' "$*" >&2
  exit 1
}

assert_contains() {
  local haystack="$1"
  local needle="$2"
  local message="$3"

  if [[ "$haystack" != *"$needle"* ]]; then
    fail "$message"$'\n'"expected to find: $needle"$'\n'"in output: $haystack"
  fi
}

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

fake_repo="$tmpdir/repo"
fake_bin="$tmpdir/bin"
mkdir -p "$fake_repo/docs/demos/helix-pass" \
  "$fake_repo/docs/demos/helix-fail" \
  "$fake_repo/website/static/demos" \
  "$fake_bin"

cat >"$fake_repo/docs/demos/helix-pass/demo.sh" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
printf 'pass demo\n'
EOF
chmod +x "$fake_repo/docs/demos/helix-pass/demo.sh"

cat >"$fake_repo/docs/demos/helix-fail/demo.sh" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
printf 'fail demo\n' >&2
exit 23
EOF
chmod +x "$fake_repo/docs/demos/helix-fail/demo.sh"

cat >"$fake_bin/asciinema" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

command=""
output=""

while (($#)); do
  case "$1" in
    rec)
      shift
      ;;
    --cols|--rows)
      shift 2
      ;;
    --command)
      command="$2"
      shift 2
      ;;
    *)
      output="$1"
      shift
      ;;
  esac
done

[[ -n "$command" ]] || exit 64
[[ -n "$output" ]] || exit 64

set +e
bash -lc "$command" >/dev/null 2>&1
child_status=$?
set -e

printf 'fake cast child=%s\n' "$child_status" > "$output"
exit 0
EOF
chmod +x "$fake_bin/asciinema"

set +e
fail_output="$(
  PATH="$fake_bin:$PATH" \
  GITHUB_WORKSPACE="$fake_repo" \
  HELIX_PAGES_DEMOS="fail" \
  bash "$record_script" 2>&1
)"
fail_status=$?
set -e

[[ $fail_status -ne 0 ]] || fail "expected recording script to fail when the wrapped demo exits non-zero"
[[ ! -e "$fake_repo/website/static/demos/helix-fail.cast" ]] \
  || fail "failing wrapped demo should not copy a cast into website/static/demos"

pass_output="$(
  PATH="$fake_bin:$PATH" \
  GITHUB_WORKSPACE="$fake_repo" \
  HELIX_PAGES_DEMOS="pass" \
  bash "$record_script" 2>&1
)" || fail "expected recording script to pass when the wrapped demo exits zero"

[[ -s "$fake_repo/website/static/demos/helix-pass.cast" ]] \
  || fail "passing wrapped demo should copy a cast into website/static/demos"
assert_contains "$pass_output" "✓ pass recorded" \
  "passing wrapped demo should report a copied cast"

workflow_text="$(cat "$pages_workflow")"
assert_contains "$workflow_text" "bash scripts/record_pages_demos.sh" \
  "pages workflow should execute the checked-in recording script"

printf 'validated Pages demo recording checks\n'
