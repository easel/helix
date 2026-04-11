#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
workspace_root="${GITHUB_WORKSPACE:-$repo_root}"
demos="${HELIX_PAGES_DEMOS:-quickstart concerns evolve experiment}"

record_demo() {
  local demo="$1"
  local tmpdir cast recorded_cast status_file demo_script

  tmpdir="$(mktemp -d)"
  trap 'rm -rf "$tmpdir"' RETURN

  cast="$workspace_root/website/static/demos/helix-${demo}.cast"
  recorded_cast="${tmpdir}/helix-${demo}.cast"
  status_file="${tmpdir}/helix-${demo}.status"
  demo_script="$workspace_root/docs/demos/helix-${demo}/demo.sh"

  test -f "$demo_script"

  echo "::group::Recording $demo"
  (
    cd "$tmpdir" &&
      asciinema rec \
        --cols 100 --rows 30 \
        --command "bash -lc 'set +e; HELIX_DEMO_RECORDING=1 bash \"${demo_script}\"; rc=\$?; printf \"%s\n\" \"\$rc\" > \"${status_file}\"; exit \"\$rc\"'" \
        "$recorded_cast" 2>&1
  )
  test -s "$status_file"
  test "$(tr -d '\r\n' < "$status_file")" = "0"
  test -s "$recorded_cast"
  mkdir -p "$(dirname "$cast")"
  cp -f "$recorded_cast" "$cast"
  echo "✓ $demo recorded ($(wc -c < "$cast") bytes)"
  echo "::endgroup::"
}

for demo in $demos; do
  record_demo "$demo"
done
