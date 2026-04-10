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
if "Inspect tracker issues labeled helix, phase:deploy, story:US-{id}" not in body:
    errors.append("story iterate query must inspect deploy issues by story label")
if "all matching deploy issues are complete and no open deploy issue remains" not in body:
    errors.append("story iterate query must require all deploy issues complete with no open deploy issue remaining")
if "not queried by story ID" not in body:
    errors.append("story iterate rule must keep shared iterate docs out of story matching")

if errors:
    raise SystemExit("\n".join(errors))
PYEOF

grep -Fq "If all deploy issues for story US-036 are complete and no open deploy issues remain: Story is in ITERATE" "$state_machine" \
  || fail "state machine example must require all deploy issues closed before iterate"

printf 'validated story iterate state rules\n'
