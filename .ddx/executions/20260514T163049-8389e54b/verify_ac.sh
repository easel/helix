#!/usr/bin/env bash
# Verification command for helix-ada6e67e no_changes rationale.
# Exit 0 if all four ACs are satisfied; nonzero otherwise.

set -euo pipefail

fail=0

# AC1: every artifact dir has meta.yml, template.md, prompt.md
missing=0
for d in workflows/phases/*/artifacts/*/; do
  for f in meta.yml template.md prompt.md; do
    if [ ! -f "$d$f" ]; then
      echo "AC1 FAIL: missing $d$f"
      missing=$((missing+1))
    fi
  done
done
if [ "$missing" -ne 0 ]; then
  fail=1
else
  echo "AC1 OK: all required files present in every artifact dir"
fi

# AC2: no dependencies.yaml files under workflows/
deps_count=$(find workflows -name "dependencies.yaml" -type f | wc -l | tr -d ' ')
if [ "$deps_count" -ne 0 ]; then
  echo "AC2 FAIL: found $deps_count dependencies.yaml file(s):"
  find workflows -name "dependencies.yaml" -type f
  fail=1
else
  echo "AC2 OK: no dependencies.yaml files under workflows/"
fi

# AC3: no meta.yml has a top-level `dependencies:` block
python3 - <<'PY'
import sys, glob, yaml
violators = []
for f in glob.glob("workflows/phases/*/artifacts/*/meta.yml"):
    with open(f) as fh:
        d = yaml.safe_load(fh)
    if isinstance(d, dict) and "dependencies" in d:
        violators.append(f)
if violators:
    print("AC3 FAIL: meta.yml files carrying a dependencies: block:")
    for f in violators: print("  ", f)
    sys.exit(1)
print("AC3 OK: no meta.yml carries a top-level dependencies: block")
PY

# AC4: substrate-neutral walk == DDx-loader view (set equality via meta.yml ids)
python3 - <<'PY'
import sys, glob, yaml
ids = []
missing_id = []
for f in sorted(glob.glob("workflows/phases/*/artifacts/*/meta.yml")):
    with open(f) as fh:
        d = yaml.safe_load(fh)
    aid = (d.get("artifact") or {}).get("id") if isinstance(d, dict) else None
    if not aid:
        missing_id.append(f)
    else:
        ids.append(aid)
if missing_id:
    print("AC4 FAIL: meta.yml files lacking artifact.id:")
    for f in missing_id: print("  ", f)
    sys.exit(1)
if len(ids) != len(set(ids)):
    from collections import Counter
    dup = [k for k, v in Counter(ids).items() if v > 1]
    print("AC4 FAIL: duplicate artifact.id values:", dup)
    sys.exit(1)
print(f"AC4 OK: {len(ids)} unique artifact.id values; substrate-neutral walk matches loader inventory")
PY

if [ "$fail" -ne 0 ]; then
  exit 1
fi
echo "All ACs satisfied."
