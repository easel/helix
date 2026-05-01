# HELIX Microsite — Design Language

> Source of truth for all visual and structural decisions on the HELIX microsite (`website/`).
> Hugo + hextra theme. Deployed at https://documentdrivendx.github.io/helix/

---

## Core Metaphor

**The DNA double helix as human–AI dance.**

Two strands wind around each other — neither leads, neither follows alone. The base-pair rungs between them are the collaboration moments: intent, review, correction, approval. This is the visual and conceptual spine of everything on the site.

- **Human strand** — terracotta coral (`#C44B2F`) — organic, intentional, steering
- **AI strand** — indigo (`#3B6BA8`) — precise, continuous, executing; echoes DDx's Cold Steel Blue
- **Rungs** — the handoff moments — rendered as connecting bridges between the two strands, using a neutral that glows in accent colors at interaction points

---

## Color Tokens

HELIX complements DDx's industrial palette (Cold Steel / Aged Brass / Iron Gray on parchment) with
a biological palette: terracotta coral (human) + indigo (AI) + violet (connection). The indigo
echoes DDx's steel-blue family — they read as related. Coral and violet are HELIX-only territory.

### Brand Colors

| Token | Light value | Dark value | Role |
|---|---|---|---|
| `--helix-human` | `#C44B2F` | `#E07A5F` | Human strand — terracotta coral, organic, warm |
| `--helix-ai` | `#3B6BA8` | `#6B9FD4` | AI strand — indigo, echoes DDx steel-blue family |
| `--helix-connect` | `#6842A8` | `#9B74D4` | Rung/handoff — violet, bridges coral ↔ indigo |

### Gradient System

All feature card gradients use `radial-gradient(ellipse at 50% 80%, …, transparent)`.

| Name | Stops | Used for |
|---|---|---|
| `gradient-ai` | `rgba(59,107,168,0.15)` → transparent | AI/docs feature cards |
| `gradient-connect` | `rgba(104,66,168,0.15)` → transparent | Authority/process cards |
| `gradient-human` | `rgba(196,75,47,0.12)` → transparent | Human/progress cards |

### Neutral Scale

Inherits hextra's Tailwind neutral scale. No overrides needed — the brand colors provide all differentiation.

---

## Typography

### Font Stack

| Role | Font | Fallback |
|---|---|---|
| Headlines (`h1`–`h3`) | **Space Grotesk** | system-ui, sans-serif |
| Body / prose | **Inter** | system-ui, sans-serif |
| Code / monospace | **JetBrains Mono** | monospace |

Hextra loads Inter by default. Space Grotesk for headlines gives HELIX a technical-but-distinct personality without diverging from the functional sans-serif family.

### Type Scale (key levels)

| Level | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `display-lg` | 3.5rem | 700 | 1.1 | -0.03em |
| `display-md` | 2.25rem | 700 | 1.15 | -0.02em |
| `headline` | 1.5rem | 600 | 1.3 | -0.01em |
| `body-lg` | 1.125rem | 400 | 1.7 | 0 |
| `body-md` | 1rem | 400 | 1.65 | 0 |
| `label` | 0.875rem | 500 | 1.4 | 0.01em |
| `mono` | 0.875rem | 400 | 1.6 | 0 |

---

## Shape & Spacing

- **Roundness**: 8px (`ROUND_EIGHT`) — functional, not precious. Cards, buttons, code blocks.
- **Feature cards**: 12px — slightly softer for the home page marketing context.
- **Spacing unit**: 4px base. Key intervals: 4, 8, 12, 16, 24, 32, 48, 64, 96.
- **Max content width**: 72rem (already set in hextra config)
- **Max page width**: 90rem (already set)

---

## Motion

Philosophy: **slow, deliberate, purposeful**. HELIX is an autopilot, not an entertainer. Motion should feel like watching a controlled system work, not a product trying to impress.

### Hero SVG animation

- Strand rotation: `360deg` over `12s`, `linear`, `infinite` — imperceptible moment-to-moment, satisfying over time
- Rung pulse: opacity `0.4 → 1.0 → 0.4` over `3s`, staggered by index — mimics base-pair "activation"
- Shimmer sweep: subtle `linearGradient` opacity shift, `6s` ease-in-out

### Global motion rules

```css
@media (prefers-reduced-motion: reduce) {
  /* All HELIX animations pause — no fallback degraded state, just stopped */
  [data-helix-animate] {
    animation: none !important;
    transition: none !important;
  }
}
```

### Hover / interaction

- Links: `color` transition `150ms ease`
- Cards: `transform: translateY(-2px)` + `box-shadow` lift `200ms ease`
- Buttons: `background` shift `120ms ease`
- No bouncy easing — use `ease` or `ease-out` only

---

## Component Patterns

### Hero section

Structure (top to bottom):
1. Badge (`hextra/hero-badge`) — "Open Source" chip
2. **Hero visual** — DNA SVG, centered, `max-width: 320px`, floats right on `md+` or centers on mobile
3. Headline (`hextra/hero-headline`)
4. Subtitle (`hextra/hero-subtitle`)
5. CTA buttons (`hextra/hero-button`)
6. Feature grid (`hextra/feature-grid`)

The SVG sits alongside the text on desktop (two-column), stacks above on mobile. It should not compete with the headline — it complements it.

### Feature cards

Existing pattern: `radial-gradient(ellipse at 50% 80%, rgba(…), transparent)`. Keep exactly. The gradient washes are intentionally subtle — they create warmth without screaming color.

### Glossary cards

Use hextra `{{< cards >}}` / `{{< card >}}` for the top-level index. Each artifact subpage gets:
- Short 1–2 sentence description (prose, not bullets)
- Full worked example in a fenced code block or blockquote
- "Template" and "Prompt" links in a small footer row

### Navigation labels (post-reorganization)

See Site Architecture section below.

---

## Site Architecture — Reorganization Plan

### Problem with current structure

The current top nav (Docs, Background, Workflow, CLI Reference, Skills, Glossary, Demos) buries the Glossary — which is the conceptual core of HELIX — at position 6. "Background" and "Workflow" are opaque labels. First-time visitors have no clear path.

### Proposed navigation (3 top-level sections)

```
Home  |  Learn  |  Reference  |  Demos  |  GitHub
```

#### Home (`/`)
Current home page + hero SVG. No change to content, big change to visual impact.

#### Learn (`/docs/learn/`)
Audience: someone evaluating HELIX or onboarding. Linear reading path.

```
Learn/
  Getting Started          (← current /docs/getting-started)
  How HELIX Works          (← current /docs/background — renamed)
  The Autopilot Loop       (← current /docs/workflow — renamed)
  Cross-Cutting Concerns   (← current /docs/workflow/concerns)
```

#### Reference (`/docs/reference/`)
Audience: practitioner looking something up. The **Glossary promoted to top-level reference hub**.

```
Reference/
  Glossary/
    Phases                 (← current /docs/glossary/phases)
    Artifacts/             (← EXPANDED — per-artifact subpages, new)
      _index.md            (card grid of all artifacts)
      prd/
      parking-lot/
      feasibility-study/
      … (all ~30 artifact types)
    Actions                (← current /docs/glossary/actions)
    Concepts               (← current /docs/glossary/concepts)
    Concerns               (← current /docs/glossary/concerns)
    Tracker                (← current /docs/glossary/tracker)
  CLI Reference            (← current /docs/cli)
  Skills                   (← current /docs/skills)
```

#### Demos (`/docs/demos/`)
Current `/docs/demos/` — unchanged.

### URL migration

All old URLs redirect to new ones via Hugo aliases in front matter. Existing links from GitHub README don't break.

### Nav weight assignments (hugo.yaml)

```yaml
menu:
  main:
    - name: Learn
      pageRef: /docs/learn
      weight: 1
    - name: Reference
      pageRef: /docs/reference
      weight: 2
    - name: Demos
      pageRef: /docs/demos
      weight: 3
    - name: GitHub
      url: https://github.com/DocumentDrivenDX/helix
      weight: 10
      params:
        icon: github
```

---

## Implementation Sequence

1. **Hero SVG** — inline SVG partial in `website/layouts/partials/hero-visual.html`, referenced from `_index.md`. Delivers immediate visual impact with zero content changes.
2. **Glossary expansion** — PR 1: convert `artifacts.md` to `artifacts/_index.md` + 6 subpages that already have upstream `example.md`. PR 2+: remaining artifact types by phase.
3. **Site reorganization** — PR after glossary is stable. Move files, add Hugo aliases, update `hugo.yaml` nav, update internal links.

---

## Accessibility

- All SVG elements: `role="img"` + `<title>` + `aria-labelledby`
- Reduced motion: `@media (prefers-reduced-motion: reduce)` stops all animation
- Color contrast: brand colors used for decoration only — never as the sole carrier of information
- Focus rings: inherit hextra's defaults (do not suppress)
