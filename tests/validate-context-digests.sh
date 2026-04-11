#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

cat >"$tmpdir/valid.jsonl" <<'EOF'
{"id":"hx-digest-ok","title":"digest present","status":"open","labels":["helix","phase:build"],"description":"<context-digest>\n<principles>Validate Your Work</principles>\n</context-digest>\n\nBody"}
{"id":"hx-review-finding-ok","title":"review finding has area label","status":"open","labels":["helix","phase:build","review-finding","area:workflow"],"description":"<context-digest>\n<principles>Validate Your Work</principles>\n</context-digest>\n\nBody"}
{"id":"hx-closed-legacy","title":"closed legacy bead","status":"closed","labels":["helix","phase:build"],"description":"Legacy body"}
EOF

python3 "$repo_root/scripts/validate_context_digests.py" --tracker "$tmpdir/valid.jsonl" >/dev/null

cat >"$tmpdir/invalid.jsonl" <<'EOF'
{"id":"hx-digest-missing","title":"missing digest","status":"open","labels":["helix","phase:build"],"description":"Legacy body"}
{"id":"hx-review-finding-missing-area","title":"review finding missing area","status":"open","labels":["helix","phase:build","review-finding"],"description":"<context-digest>\n<principles>Validate Your Work</principles>\n</context-digest>\n\nBody"}
EOF

if python3 "$repo_root/scripts/validate_context_digests.py" --tracker "$tmpdir/invalid.jsonl" >"$tmpdir/invalid.out" 2>"$tmpdir/invalid.err"; then
  echo "FAIL: validator should reject open HELIX beads without a context digest" >&2
  exit 1
fi

grep -Fq "hx-digest-missing" "$tmpdir/invalid.err" || {
  echo "FAIL: validator should identify the offending bead" >&2
  exit 1
}

grep -Fq "hx-review-finding-missing-area" "$tmpdir/invalid.err" || {
  echo "FAIL: validator should identify review findings missing area labels" >&2
  exit 1
}

python3 "$repo_root/scripts/validate_context_digests.py" --tracker "$repo_root/.ddx/beads.jsonl"
