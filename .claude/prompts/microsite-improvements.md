# Microsite improvements — resume prompt

Use this prompt to resume work on the HELIX microsite (`website/`). Paste it
verbatim into a fresh Claude Code session in the `helix` repo.

---

I want to keep improving the HELIX microsite (`website/`, Hugo + hextra theme,
deployed at https://documentdrivendx.github.io/helix/). We previously scoped two
starting improvements but did not implement them yet. Pick up from that scope.

## Scope to deliver

### 1. Hero visual — DNA double helix as the human/AI dance

The home page (`website/content/_index.md`) is currently text-only — it uses
`hextra/hero-headline`, `hero-subtitle`, and `hero-button` shortcodes with no
visual. Add a hero illustration that depicts the HELIX metaphor: a DNA double
helix where the two strands represent the human and the AI working in concert,
with the base-pair rungs as their collaboration moments (intent, review,
correction, approval).

Direction we agreed on:

- **Hand-authored inline SVG** (not a raster export). Keeps it small, crisp on
  retina/dark, and editable. Place it in `website/layouts/partials/` (e.g.
  `hero-visual.html`) or a shortcode under `website/layouts/shortcodes/`, then
  reference it from `_index.md` above the headline.
- **Two strands with distinct hues** — one "human" (warm tone), one "AI" (cool
  tone) — wound around each other. Use CSS variables so it adapts to the
  hextra light/dark theme. Match or complement the radial-gradient palette
  already used in the feature cards
  (`rgba(72,120,198,0.15)`, `rgba(142,53,163,0.15)`, `rgba(53,163,95,0.15)`).
- **Optional subtle motion** (slow rotate / shimmer / pulse on the rungs) via
  CSS — must respect `prefers-reduced-motion`.
- Should look intentional alongside the existing hextra hero typography, not
  fight it. Keep it composed, not busy.

Verify by running the Hugo dev server and viewing the home page in a browser.
Check both light and dark themes, mobile width, and reduced-motion.

### 2. Glossary artifact examples

`website/content/docs/glossary/artifacts.md` lists ~30 artifact types with
solid 1-paragraph descriptions but **no concrete examples**. Expand it so
each artifact has a realistic, filled-in example a reader can copy and adapt.

Direction we agreed on:

- **Option (a): split into per-artifact subpages.** Convert `artifacts.md`
  into `glossary/artifacts/_index.md` plus one subpage per artifact type.
  Each subpage: short description + full example + link to the upstream
  template/prompt. Match the existing card-grid pattern used elsewhere in
  the glossary index. Stable URLs per artifact, scales as artifacts get
  added.
- The repo already has `example.md` for **6 of 42** artifact directories
  under `workflows/phases/*/artifacts/*/`: `prd`, `parking-lot`,
  `feasibility-study`, `research-plan`, `proof-of-concept`, `tech-spike`.
  **Pull from these directly** for those 6.
- For the remaining ~25, generate realistic examples grounded in this
  project's own HELIX docs (`docs/helix/`) so the examples are coherent
  with each other and not invented from thin air. Where the project's own
  artifacts exist, use them as the example (with light editing for
  pedagogy).
- Each subpage should also link to the artifact's `template.md` and
  `prompt.md` upstream so readers know where the canonical structure lives.

If a single PR feels too large, split: ship the structure + the 6 artifacts
that already have examples first; follow with one PR per phase
(Discover/Frame/Design/Test/Build/Deploy/Iterate) for the rest.

## Repo orientation

- Hugo config: `website/hugo.yaml` (hextra theme, wide pages, edit-on-GitHub
  enabled).
- Hero source: `website/content/_index.md`.
- Glossary index: `website/content/docs/glossary/_index.md`.
- Artifacts page (target of expansion): `website/content/docs/glossary/artifacts.md`.
- Existing shortcodes: `website/layouts/shortcodes/asciinema.html` (only one).
  No existing `partials/` directory — create as needed.
- Upstream artifact source-of-truth: `workflows/phases/{00-discover,
  01-frame, 02-design, 03-test, 04-build, 05-deploy, 06-iterate}/artifacts/*/`.
  Each contains `prompt.md`, `template.md`, sometimes `example.md`,
  `meta.yml`, `dependencies.yaml`.
- Project's own HELIX artifacts (use as example source material):
  `docs/helix/`.

## Repo conventions to respect

- `CLAUDE.md` enforces YAGNI/KISS/DOWITYTD: implement only what's specified,
  no speculative additions.
- Default to no comments unless the WHY is non-obvious.
- For UI changes, run the Hugo dev server and verify in-browser before
  declaring done.
- Commit format follows `helix-commit` skill conventions; tracker beads via
  `helix-triage` if non-trivial work needs to be filed.

## Open questions to resolve before implementing

1. **Order**: hero first, then glossary — or both in parallel? (We didn't
   decide.)
2. **Glossary shape**: confirm option (a) per-artifact subpages, or fall
   back to (b) inline `<details>` blocks on the single page.
3. **Hero motion**: include the subtle animation, or keep it static?
4. **Splitting the glossary work** into multiple PRs vs. one big PR.

Ask these before writing code.
