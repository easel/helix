# Project Concerns

## Active Concerns
- hugo-hextra (microsite)
- demo-asciinema (demo)

## Area Labels

| Label | Applies to |
|-------|-----------|
| `all` | Every bead |
| `cli` | scripts/helix, CLI wrapper |
| `workflow` | workflows/actions, workflows/concerns, workflow engine |
| `site` | website/, microsite content and deployment |
| `demo` | docs/demos/, demo scripts and recordings |

## Project Overrides

### hugo-hextra
- **Theme version**: Hextra v0.12.1 — pinned in `website/go.mod`
- **Hugo version**: 0.159.2 extended — pinned in `.github/workflows/pages.yml`
- **Deployment**: GitHub Pages at `easel.github.io/helix/`
- **E2E tests**: not yet implemented (DDx has the pattern to follow)
- **Custom shortcode**: `asciinema.html` for terminal recording embeds

### demo-asciinema
- **Current demos**: `docs/demos/helix-quickstart/` — full lifecycle demo
- **Recording container**: Ubuntu 24.04, Node.js, Claude Code CLI, asciinema
- **Demo project**: builds a Node.js temperature converter to show the HELIX lifecycle
- **Cast files**: archived in `docs/demos/*/recordings/` and copied to `website/static/demos/`
