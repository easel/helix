#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
state_rules="$repo_root/workflows/state-rules.yml"
state_machine="$repo_root/workflows/state-machine.yaml"
iterate_readme="$repo_root/workflows/activities/06-iterate/README.md"

fail() {
  printf 'state rule validation failed: %s\n' "$*" >&2
  exit 1
}

python3 - "$state_rules" <<'PYEOF' || fail "story iterate rule contract regressed"
from pathlib import Path
import re
import sys

text = Path(sys.argv[1]).read_text(encoding="utf-8")
deploy_match = re.search(r"^    deploy:\n(?P<body>(?: {6}.+\n)+)", text, re.MULTILINE)
if not deploy_match:
    raise SystemExit("missing story deploy block")

match = re.search(r"^    iterate:\n(?P<body>(?: {6}.+\n)+)", text, re.MULTILINE)
if not match:
    raise SystemExit("missing story iterate block")

deploy_body = deploy_match.group("body")
body = match.group("body")
errors = []
if "Treat the story as DEPLOY while any matching deploy issue is not closed, including `status: in_progress`." not in deploy_body:
    errors.append("story deploy rule must keep DEPLOY active for any non-closed deploy issue, including in_progress")
if "pattern:" in body:
    errors.append("story iterate rule must not include a static artifact pattern")
if "query_only: true" not in body:
    errors.append("story iterate rule must be query-only")
if "Inspect tracker issues labeled helix, phase:deploy, story:US-{id}" not in body:
    errors.append("story iterate query must inspect deploy issues by story label")
if "all matching deploy issues are complete and no matching deploy issue remains not closed" not in body:
    errors.append("story iterate query must require all deploy issues complete with no matching deploy issue remaining not closed")
if "If any matching deploy issue is not closed, including `status: in_progress`, the story remains in DEPLOY." not in body:
    errors.append("story iterate query must explicitly keep DEPLOY active for non-closed deploy issues")
if "not queried by story ID" not in body:
    errors.append("story iterate rule must keep shared iterate docs out of story matching")

if errors:
    raise SystemExit("\n".join(errors))
PYEOF

python3 - "$iterate_readme" <<'PYEOF' || fail "iterate README story-state contract regressed"
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text(encoding="utf-8")
normalized = " ".join(text.split())
errors = []
if "completion of all matching `phase:deploy` issue(s) with no matching deploy issue remaining not closed." not in normalized:
    errors.append("iterate README must require all matching deploy issues complete with no matching deploy issue remaining not closed")
if "If any matching deploy issue is not closed, including `status: in_progress`, the story remains in DEPLOY." not in normalized:
    errors.append("iterate README must explicitly keep DEPLOY active for non-closed deploy issues, including in_progress")

if errors:
    raise SystemExit("\n".join(errors))
PYEOF

grep -Fq "If any HELIX deploy issue for story US-036 is not closed, including status: in_progress: Story is in DEPLOY" "$state_machine" \
  || fail "state machine example must keep DEPLOY active for non-closed deploy issues"
grep -Fq "If all deploy issues for story US-036 are complete and no matching deploy issue remains not closed: Story is in ITERATE" "$state_machine" \
  || fail "state machine example must require all deploy issues closed before iterate"

printf 'validated story iterate state rules\n'
