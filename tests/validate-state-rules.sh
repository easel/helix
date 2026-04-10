#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
state_rules="$repo_root/workflows/state-rules.yml"
state_machine="$repo_root/workflows/state-machine.yaml"

fail() {
  printf 'state rule validation failed: %s\n' "$*" >&2
  exit 1
}

python3 - "$state_rules" <<'PYEOF' || fail "story iterate rule contract regressed"
from pathlib import Path
import re
import sys

text = Path(sys.argv[1]).read_text(encoding="utf-8")
match = re.search(r"^    iterate:\n(?P<body>(?: {6}.+\n)+)", text, re.MULTILINE)
if not match:
    raise SystemExit("missing story iterate block")

body = match.group("body")
errors = []
if "pattern:" in body:
    errors.append("story iterate rule must not include a static artifact pattern")
if "query_only: true" not in body:
    errors.append("story iterate rule must be query-only")
if "completed tracker issues labeled helix, phase:deploy, story:US-{id}" not in body:
    errors.append("story iterate query must key off completed deploy issues")
if "not queried by story ID" not in body:
    errors.append("story iterate rule must keep shared iterate docs out of story matching")

if errors:
    raise SystemExit("\n".join(errors))
PYEOF

grep -Fq "If deploy issues for story US-036 are complete: Story is in ITERATE" "$state_machine" \
  || fail "state machine example must show deploy completion as the iterate threshold"

printf 'validated story iterate state rules\n'
