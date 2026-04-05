# Practices: hugo-hextra

## Requirements (Frame phase)
- Define the site's target audience and what content they need
- List the documentation sections required (at minimum: getting started, concepts, CLI reference)
- Determine whether demo recordings are needed (see `demo-asciinema` concern)
- Decide on deployment target (default: GitHub Pages at `<org>.github.io/<project>`)

## Design
- Site lives in `website/` subdirectory — not the repo root
- Use Hugo Module system for Hextra theme (`go.mod` + `go.sum`)
- Navigation structure defined in `hugo.yaml` `menu.main` section
- Content hierarchy mirrors sidebar navigation — `_index.md` files create sections
- Prefer Hextra shortcodes over custom HTML for maintainability
- Static assets (images, recordings, downloads) go in `website/static/`
- Custom shortcodes only when Hextra has no equivalent

## Implementation
- Initialize with `hugo new site website` then add `go.mod` with Hextra import
- Pin Hextra version in `go.mod` — update deliberately, not automatically
- Pin Hugo version in CI — use the same version locally and in GitHub Actions
- Every content page needs YAML frontmatter with at minimum `title` and `weight`
- Section index pages (`_index.md`) use `cards` shortcode to link child pages
- Home page uses `layout: hextra-home` with hero and feature-grid shortcodes
- Menu items use `pageRef` for internal links, `url` for external (GitHub icon)
- Set `params.editURL.base` to enable "Edit this page" links
- Keep content readable as plain markdown — someone reading on GitHub should
  understand the docs even without Hextra rendering

## Content Authoring
- Write for the getting-started reader first — assume no prior knowledge of the project
- Getting Started page must get a user from zero to working in under 5 minutes
- CLI Reference must document every command with examples
- Use `tabs` shortcode for platform-specific instructions (macOS/Linux/Docker)
- Use `cards` shortcode for index pages that link to child content
- Embed terminal recordings with `asciinema` shortcode (see `demo-asciinema` concern)
- Include version badge on homepage hero using `hextra/hero-badge`
- Feature cards should each describe one capability with a concrete benefit

## Testing
- Playwright e2e tests in `website/e2e/` verify page loads and navigation
- Screenshot snapshot tests catch visual regressions after theme updates
- Test every section landing page and the homepage
- Run `hugo --gc --minify` locally before pushing to catch build errors
- After Hextra version bumps, run screenshot update and review diffs

## Quality Gates
- `hugo --gc --minify` builds without errors or warnings
- `playwright test` passes (if e2e tests exist)
- No broken internal links (Hugo reports these as build warnings)
- Content files have valid YAML frontmatter

## Deployment
- GitHub Actions deploys on successful test + push to main
- Hugo build uses `--gc --minify` with `HUGO_ENVIRONMENT=production`
- Checkout must use `fetch-depth: 0` for git-based last-modified dates
- Cache Hugo modules in CI for faster builds
- Enable concurrent deployment protection to prevent race conditions
