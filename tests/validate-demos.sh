#!/usr/bin/env bash
# Validate every committed demo session record and render it to .cast.
#
# Each demo lives at docs/demos/<slug>/session.jsonl. The render is
# deterministic, so this test asserts that re-rendering produces a
# byte-identical cast file (unless the committed cast is intentionally
# stale because session.jsonl was just updated, in which case the test
# rebuilds it).
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
demos_root="$repo_root/docs/demos"
cast_root="$repo_root/website/static/demos"
render="$repo_root/scripts/demos/render_session.py"
validate="$repo_root/scripts/demos/validate_session.py"
check_assertions="$repo_root/scripts/demos/check_assertions.py"

fail() {
  printf 'demo validation failed: %s\n' "$*" >&2
  exit 1
}

shopt -s nullglob
sessions=("$demos_root"/*/session.jsonl)
if (( ${#sessions[@]} == 0 )); then
  printf 'no demo session records found under %s\n' "$demos_root"
  exit 0
fi

# Schema-level validation.
python3 "$validate" "${sessions[@]}" || fail "session schema validation failed"

# Assertion check for demos that ship an assertions.yml.
demo_dirs=()
for s in "${sessions[@]}"; do
  demo_dirs+=("$(dirname "$s")")
done
python3 "$check_assertions" "${demo_dirs[@]}" || fail "demo assertions failed"

# Render each, compare to committed cast.
for session in "${sessions[@]}"; do
  slug="$(basename "$(dirname "$session")")"
  expected="$cast_root/${slug}.cast"
  rendered="$(mktemp)"
  python3 "$render" "$session" --output "$rendered" >/dev/null \
    || fail "render failed for $slug"

  if [[ -f "$expected" ]]; then
    if ! diff -q "$rendered" "$expected" >/dev/null 2>&1; then
      fail "rendered $slug differs from committed $expected — re-render and commit"
    fi
    printf 'demo %s: cast matches committed (%d events)\n' "$slug" \
      "$(($(wc -l < "$rendered") - 1))"
  else
    printf 'demo %s: no committed cast yet (rendered ok)\n' "$slug"
  fi
  rm -f "$rendered"
done
