#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
claude_skills_dir="${CLAUDE_HOME:-$HOME/.claude}/skills"
local_bin_dir="$HOME/.local/bin"

mkdir -p "$codex_skills_dir" "$claude_skills_dir" "$local_bin_dir"

install_link() {
  local src="$1"
  local dest="$2"

  if [[ -L "$dest" ]]; then
    ln -sfn "$src" "$dest"
    return
  fi

  if [[ -e "$dest" ]]; then
    echo "skip existing non-symlink: $dest" >&2
    return
  fi

  ln -s "$src" "$dest"
}

install_pair() {
  local name="$1"
  local src="$2"
  install_link "$src" "$codex_skills_dir/$name"
  install_link "$src" "$claude_skills_dir/$name"
}

install_helix_cli() {
  local dest="$local_bin_dir/helix"

  cat >"$dest" <<EOF
#!/usr/bin/env bash
exec bash "$repo_root/scripts/helix" "\$@"
EOF

  chmod +x "$dest"
}

install_pair "helix-workflow" "$repo_root/skills/helix"
install_pair "helix-alignment-review" "$repo_root/skills/helix-alignment-review"
install_pair "plan-workflow" "$repo_root/skills/plan"
install_pair "polish-workflow" "$repo_root/skills/polish"
install_pair "experiment-workflow" "$repo_root/skills/experiment"

echo "Installed skills into:"
echo "  Codex:  $codex_skills_dir"
echo "  Claude: $claude_skills_dir"

chmod +x "$repo_root/scripts/helix"
install_helix_cli

echo "Installed HELIX CLI into:"
echo "  $local_bin_dir/helix"
