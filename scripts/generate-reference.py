#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""
Generate website reference pages for HELIX artifacts and cross-cutting
concerns from the upstream source-of-truth in `workflows/`.

Reads:
  workflows/phases/<phase>/artifacts/<slug>/   -> meta.yml, dependencies.yaml,
                                                  prompt.md, template.md,
                                                  example.md (sometimes)
  workflows/concerns/<slug>/                   -> concern.md, practices.md

Writes:
  website/content/reference/glossary/artifacts/_index.md
  website/content/reference/glossary/artifacts/<slug>.md   (one per artifact)
  website/content/reference/glossary/concerns/_index.md
  website/content/reference/glossary/concerns/<slug>.md    (one per concern)

Idempotent — destination directories are wiped and rebuilt on every run.

Run with:
  uv run scripts/generate-reference.py
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS_SRC = ROOT / "workflows" / "phases"
CONCERNS_SRC = ROOT / "workflows" / "concerns"
CONTENT_ROOT = ROOT / "website" / "content"
ARTIFACTS_DEST = CONTENT_ROOT / "artifacts"
CONCERNS_DEST = CONTENT_ROOT / "concerns"
LEGACY_GLOSSARY = CONTENT_ROOT / "reference" / "glossary"

PHASES = {
    "00-discover": {
        "num": 0,
        "label": "Discover",
        "summary": "Validate that an opportunity is worth pursuing before committing to a development cycle.",
    },
    "01-frame": {
        "num": 1,
        "label": "Frame",
        "summary": "Define what the system should do, for whom, and how success will be measured.",
    },
    "02-design": {
        "num": 2,
        "label": "Design",
        "summary": "Decide how to build it. Capture trade-offs, contracts, and architecture decisions.",
    },
    "03-test": {
        "num": 3,
        "label": "Test",
        "summary": "Define how we know it works. Plans, suites, and procedures that bind specs to implementation.",
    },
    "04-build": {
        "num": 4,
        "label": "Build",
        "summary": "Implement against the specs and tests. Capture the implementation plan that scopes the work.",
    },
    "05-deploy": {
        "num": 5,
        "label": "Deploy",
        "summary": "Ship to users with appropriate operational support, monitoring, and rollback plans.",
    },
    "06-iterate": {
        "num": 6,
        "label": "Iterate",
        "summary": "Measure, align, and improve. Close the feedback loop back into the planning strand.",
    },
}


# ---------------------------------------------------------------------------
# HELIX real-example mapping (PR 1: defined but DISABLED)
#
# Each entry maps an artifact slug to the path of HELIX's actual instance of
# that artifact in `docs/helix/`. When the mapping is enabled (PR 2), the
# generator embeds the real document as the artifact's worked example,
# normalized via the helpers below.
#
# This dict is the source-of-truth audit list for the alignment review
# ahead of the PR 2 flip. validate_helix_real_examples() hard-fails the
# generator if any path is missing — drift in docs/helix/ surfaces loudly.

HELIX_REAL_EXAMPLES = {
    # Phase 0 — Discover
    "product-vision":        "docs/helix/00-discover/product-vision.md",
    # Phase 1 — Frame
    "prd":                   "docs/helix/01-frame/prd.md",
    "concerns":              "docs/helix/01-frame/concerns.md",
    "feature-specification": "docs/helix/01-frame/features/FEAT-002-helix-cli.md",
    # Phase 2 — Design
    "architecture":          "docs/helix/02-design/architecture.md",
    "data-design":           "docs/helix/02-design/data-design.md",
    "security-architecture": "docs/helix/02-design/security-architecture.md",
    # ADR-001 is foundational (supervisory control model); most ADRs cite it.
    "adr":                   "docs/helix/02-design/adr/ADR-001-supervisory-control-model.md",
    # CONTRACT-001 defines the DDx/HELIX boundary — most-cited downstream.
    "contract":              "docs/helix/02-design/contracts/CONTRACT-001-ddx-helix-boundary.md",
    "solution-design":       "docs/helix/02-design/solution-designs/SD-001-helix-supervisory-control.md",
    "technical-design":      "docs/helix/02-design/technical-designs/TD-002-helix-cli.md",
    # Phase 3 — Test
    "test-plan":             "docs/helix/03-test/test-plans/TP-002-helix-cli.md",
    # Phase 4 — Build
    "implementation-plan":   "docs/helix/04-build/implementation-plan.md",
    # Phase 5 — Deploy
    "runbook":               "docs/helix/05-deploy/runbook.md",
    "deployment-checklist":  "docs/helix/05-deploy/deployment-checklist.md",
    "release-notes":         "docs/helix/05-deploy/release-notes.md",
    "monitoring-setup":      "docs/helix/05-deploy/monitoring-setup.md",
    # Phase 6 — Iterate
    "improvement-backlog":   "docs/helix/06-iterate/improvement-backlog.md",
    "metrics-dashboard":     "docs/helix/06-iterate/metrics-dashboard.md",
    "security-metrics":      "docs/helix/06-iterate/security-metrics.md",
}

# Toggle the rendering path. Enabled in PR 2 after the alignment audit.
HELIX_REAL_EXAMPLES_ENABLED = True

# Of the slugs in HELIX_REAL_EXAMPLES, only these are publishable per the
# 2026-05-01 alignment review (AR-2026-05-01-public-examples.md).
# Others fall through to the example.md fallback or "no example yet".
HELIX_REAL_EXAMPLES_PUBLISHABLE = {
    "product-vision",
    "prd",
    "concerns",
    "feature-specification",
    "architecture",
    "adr",
    "contract",
    "technical-design",
    "solution-design",
    "test-plan",
    "data-design",
    "security-architecture",
    "implementation-plan",
    "runbook",
    "deployment-checklist",
    "release-notes",
    "monitoring-setup",
    "improvement-backlog",
}

# Branch to pin embedded relative-link rewrites against.
HELIX_REPO_BLOB_BASE = "https://github.com/DocumentDrivenDX/helix/blob/main"


def validate_helix_real_examples() -> None:
    """Hard-fail if any HELIX_REAL_EXAMPLES path is missing.

    Stale mappings are not a recoverable condition: if the generator says X
    is sourced from Y and Y is missing, the site would be semantically
    wrong. Surfacing this loudly is the drift detection we want.
    """
    errors = []
    for slug, rel_path in HELIX_REAL_EXAMPLES.items():
        full = ROOT / rel_path
        if not full.exists():
            errors.append(f"  - '{slug}' → '{rel_path}' (file not found)")
    if errors:
        msg = (
            "ERROR: stale HELIX example mappings:\n"
            + "\n".join(errors)
            + "\n\nFix by either: (a) restoring the missing file, "
            "(b) updating the mapping in scripts/generate-reference.py, "
            "or (c) removing the mapping if the artifact no longer has a real example."
        )
        print(msg, file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Embed normalization (used by the rendering path that flips on in PR 2)


def strip_frontmatter(content: str) -> str:
    """Strip leading YAML frontmatter (between two --- lines) from content."""
    if not content.startswith("---\n"):
        return content
    end = content.find("\n---\n", 4)
    if end == -1:
        return content
    return content[end + 5:].lstrip("\n")


def shift_headings(content: str, by: int = 1) -> str:
    """Shift every ATX heading down by `by` levels (max H6).

    Skips headings inside fenced code blocks. Setext-style headings
    (===/---) are left alone — rare in HELIX docs and risky to rewrite.
    """
    out = []
    in_fence = False
    fence_marker = None
    for line in content.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif stripped.startswith(fence_marker):
                in_fence = False
                fence_marker = None
            out.append(line)
            continue
        if not in_fence and line.startswith("#"):
            # Count existing # marks
            level = len(line) - len(line.lstrip("#"))
            if 1 <= level <= 6 and (len(line) > level and line[level] == " "):
                new_level = min(level + by, 6)
                out.append("#" * new_level + line[level:])
                continue
        out.append(line)
    return "".join(out)


def rewrite_relative_links(content: str, source_path: str, base_url: str = HELIX_REPO_BLOB_BASE) -> str:
    """Rewrite relative markdown links to absolute repo URLs.

    A link `[text](relative/path.md)` in `source_path` becomes
    `[text](<base_url>/<resolved-path>)` so that embedded docs link
    correctly even though they're rendered under a different URL on the site.

    Absolute URLs (http, https), site-absolute paths (/foo), in-page anchors
    (#section), and mailto: links are left alone.
    """
    import os

    source_dir = os.path.dirname(source_path).replace("\\", "/")
    pattern = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")

    def rewrite(m: re.Match) -> str:
        text = m.group(1)
        url = m.group(2)
        title = m.group(3) or ""
        if url.startswith(("http://", "https://", "/", "#", "mailto:")):
            return m.group(0)
        # Split off any anchor
        if "#" in url:
            path_part, anchor = url.split("#", 1)
            anchor = "#" + anchor
        else:
            path_part, anchor = url, ""
        if not path_part:
            return m.group(0)
        resolved = os.path.normpath(os.path.join(source_dir, path_part)).replace("\\", "/")
        return f"[{text}]({base_url}/{resolved}{anchor}{title})"

    return pattern.sub(rewrite, content)


def normalize_embedded_doc(content: str, source_path: str) -> str:
    """Apply all embed normalizations: strip frontmatter, shift headings, rewrite links."""
    content = strip_frontmatter(content)
    content = shift_headings(content, by=1)
    content = rewrite_relative_links(content, source_path)
    return content


# ---------------------------------------------------------------------------
# Helpers


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = yaml.safe_load(path.read_text())
        return data if isinstance(data, dict) else {}
    except Exception as exc:  # noqa: BLE001
        print(f"WARN: failed to parse {path}: {exc}", file=sys.stderr)
        return {}


def load_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def humanize(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def yaml_quote(value: str) -> str:
    """Safe YAML double-quoted scalar."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def card_subtitle(text: str, limit: int = 160) -> str:
    text = " ".join(text.split())
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text.replace('"', "&quot;")


# ---------------------------------------------------------------------------
# Artifact collection


def collect_artifacts():
    artifacts = []
    for phase_key, phase in PHASES.items():
        phase_dir = ARTIFACTS_SRC / phase_key / "artifacts"
        if not phase_dir.exists():
            continue
        for art_dir in sorted(p for p in phase_dir.iterdir() if p.is_dir()):
            slug = art_dir.name
            artifacts.append({
                "slug": slug,
                "phase_key": phase_key,
                "phase": phase,
                "src_dir": art_dir,
                "meta": load_yaml(art_dir / "meta.yml"),
                "deps": load_yaml(art_dir / "dependencies.yaml"),
                "prompt": load_text(art_dir / "prompt.md"),
                "template": load_text(art_dir / "template.md"),
                "example": load_text(art_dir / "example.md") if (art_dir / "example.md").exists() else None,
            })
    return artifacts


def _safe_dict(value) -> dict:
    return value if isinstance(value, dict) else {}


def get_artifact_name(meta: dict, deps: dict, slug: str) -> str:
    return (
        _safe_dict(meta.get("artifact")).get("name")
        or _safe_dict(deps.get("artifact")).get("name")
        or humanize(slug)
    )


def get_artifact_description(meta: dict, deps: dict) -> str:
    desc = (
        meta.get("description")
        or deps.get("description")
        or _safe_dict(meta.get("artifact")).get("description")
        or ""
    )
    return desc.strip() if isinstance(desc, str) else ""


def get_relationships(meta: dict, deps: dict) -> dict:
    """Pull requires/enables/informs/referenced_by from deps + meta."""
    out = {"requires": [], "enables": [], "informs": [], "referenced_by": []}

    def _bucket_from(source: dict, key: str, name_field: str):
        items = []
        for d in _safe_dict(source.get("dependencies")).get(key, []) or []:
            if not isinstance(d, dict):
                continue
            slug = d.get("path")
            if not slug:
                continue
            items.append({
                "slug": slug,
                "name": d.get(name_field) or humanize(slug),
                "relationship": d.get("relationship", "") or "",
                "required": d.get("required", True),
                "phase": d.get("phase", ""),
            })
        return items

    # deps.yaml is more structured; try it first, fall back to meta.yml
    out["requires"] = _bucket_from(deps, "requires", "input") or _bucket_from(meta, "requires", "input")
    out["enables"] = _bucket_from(deps, "enables", "output") or _bucket_from(meta, "enables", "output")

    rel = _safe_dict(deps.get("relationships")) or _safe_dict(meta.get("relationships"))
    for slug in rel.get("informs", []) or []:
        if isinstance(slug, str):
            out["informs"].append({"slug": slug, "name": humanize(slug)})
    for slug in rel.get("referenced_by", []) or []:
        if isinstance(slug, str):
            out["referenced_by"].append({"slug": slug, "name": humanize(slug)})

    return out


def get_output_location(meta: dict, deps: dict) -> str:
    out = _safe_dict(meta.get("output")) or _safe_dict(deps.get("output"))
    return (out.get("location") or "").strip()


def render_relationship_list(items: list, all_slugs: set) -> str:
    if not items:
        return "_None._"
    lines = []
    for r in items:
        slug = r["slug"]
        name = r["name"]
        rel = r.get("relationship", "")
        required = r.get("required", True)
        link = f"[{name}](../{slug}/)" if slug in all_slugs else name
        line = f"- {link}"
        if rel:
            line += f" — {rel}"
        if required is False:
            line += " *(optional)*"
        lines.append(line)
    return "\n".join(lines)


def render_artifact_page(art: dict, all_slugs: set) -> str:
    slug = art["slug"]
    phase = art["phase"]
    name = get_artifact_name(art["meta"], art["deps"], slug)
    desc = get_artifact_description(art["meta"], art["deps"])
    rels = get_relationships(art["meta"], art["deps"])
    output = get_output_location(art["meta"], art["deps"])

    weight = phase["num"] * 100  # within-phase order is alphabetical by Hugo

    out: list[str] = []
    out.append("---")
    out.append(f"title: {yaml_quote(name)}")
    out.append(f"slug: {slug}")
    out.append(f"phase: {yaml_quote(phase['label'])}")
    out.append(f"weight: {weight}")
    out.append("generated: true")
    out.append("aliases:")
    out.append(f"  - /reference/glossary/artifacts/{slug}")
    out.append("---")
    out.append("")

    out.append("## What it is")
    out.append("")
    out.append(desc or f"_({slug} — description not yet captured in upstream `meta.yml`.)_")
    out.append("")

    out.append("## Phase")
    out.append("")
    out.append(
        f"**[Phase {phase['num']} — {phase['label']}](/reference/glossary/phases/)** "
        f"— {phase['summary']}"
    )
    out.append("")

    if output:
        out.append("## Output location")
        out.append("")
        out.append(f"`{output}`")
        out.append("")

    out.append("## Relationships")
    out.append("")
    out.append("### Requires (upstream)")
    out.append("")
    out.append(render_relationship_list(rels["requires"], all_slugs))
    out.append("")
    out.append("### Enables (downstream)")
    out.append("")
    out.append(render_relationship_list(rels["enables"], all_slugs))
    out.append("")
    if rels["informs"]:
        out.append("### Informs")
        out.append("")
        out.append(render_relationship_list(rels["informs"], all_slugs))
        out.append("")
    if rels["referenced_by"]:
        out.append("### Referenced by")
        out.append("")
        out.append(render_relationship_list(rels["referenced_by"], all_slugs))
        out.append("")

    if art["prompt"]:
        out.append("## Generation prompt")
        out.append("")
        out.append("The agent prompt that produces this artifact.")
        out.append("")
        out.append("<details>")
        out.append("<summary>Show the full generation prompt</summary>")
        out.append("")
        out.append("``````markdown")
        out.append(art["prompt"].strip())
        out.append("``````")
        out.append("")
        out.append("</details>")
        out.append("")

    if art["template"]:
        out.append("## Template")
        out.append("")
        out.append("<details>")
        out.append("<summary>Show the template structure</summary>")
        out.append("")
        out.append("``````markdown")
        out.append(art["template"].strip())
        out.append("``````")
        out.append("")
        out.append("</details>")
        out.append("")

    out.append("## Example")
    out.append("")

    # Resolution order:
    #   1. HELIX_REAL_EXAMPLES (if enabled and slug is in PUBLISHABLE)
    #   2. hand-authored example.md
    #   3. fallback "no example yet"
    real_example_rendered = False
    if (
        HELIX_REAL_EXAMPLES_ENABLED
        and slug in HELIX_REAL_EXAMPLES_PUBLISHABLE
        and slug in HELIX_REAL_EXAMPLES
    ):
        rel_path = HELIX_REAL_EXAMPLES[slug]
        full_path = ROOT / rel_path
        if full_path.exists():
            raw = full_path.read_text()
            embedded = normalize_embedded_doc(raw, rel_path)
            blob_url = f"{HELIX_REPO_BLOB_BASE}/{rel_path}"
            out.append(
                f"This example is HELIX's actual {name.lower()}, sourced from "
                f"[`{rel_path}`]({blob_url}). It shows how this artifact is "
                "used in a live methodology project; it may include "
                "project-specific context."
            )
            out.append("")
            out.append(embedded.strip())
            out.append("")
            real_example_rendered = True

    if not real_example_rendered:
        if art["example"]:
            out.append("<details>")
            out.append("<summary>Show a worked example of this artifact</summary>")
            out.append("")
            out.append("``````markdown")
            out.append(art["example"].strip())
            out.append("``````")
            out.append("")
            out.append("</details>")
        else:
            out.append(
                "_No worked example captured yet. The prompt and template "
                "above describe the canonical structure._"
            )
        out.append("")

    return "\n".join(out)


def render_artifacts_index(artifacts: list) -> str:
    out: list[str] = []
    out.append("---")
    out.append("title: Artifacts")
    out.append("weight: 2")
    out.append("generated: true")
    out.append("aliases:")
    out.append("  - /docs/glossary/artifacts")
    out.append("  - /reference/glossary/artifacts")
    out.append("---")
    out.append("")
    out.append(
        "Every HELIX project produces a graph of governing artifacts — "
        "documents that define what to build, why, how, and how to verify it. "
        "When artifacts disagree, the [authority order](/why/principles/#3-authority-order-governs-reconciliation) "
        "governs: vision over requirements, requirements over design, design "
        "over code."
    )
    out.append("")
    out.append(
        "Each artifact below has its own page with description, relationships "
        "to other artifacts, the generation prompt, the template structure, "
        "and (where available) a worked example."
    )
    out.append("")

    by_phase: dict[str, list[dict]] = {}
    for a in artifacts:
        by_phase.setdefault(a["phase_key"], []).append(a)

    for phase_key, phase in PHASES.items():
        if phase_key not in by_phase:
            continue
        out.append(f"## Phase {phase['num']} — {phase['label']}")
        out.append("")
        out.append(f"_{phase['summary']}_")
        out.append("")
        out.append("{{< cards >}}")
        for a in by_phase[phase_key]:
            name = get_artifact_name(a["meta"], a["deps"], a["slug"])
            desc = get_artifact_description(a["meta"], a["deps"]) or f"({a['slug']})"
            sub = card_subtitle(desc, 160)
            out.append(f'  {{{{< card link="{a["slug"]}" title="{name}" subtitle="{sub}" >}}}}')
        out.append("{{< /cards >}}")
        out.append("")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Concerns


CONCERN_HEADING_MAP = [
    ("category", r"^##\s+Category\s*$"),
    ("areas", r"^##\s+Areas?\s*$"),
]


def parse_concern_md(md: str) -> dict:
    """Extract title, category, areas from a concern.md file."""
    out = {"title": "", "category": "", "areas": ""}
    if not md:
        return out

    # Title — first H1
    for line in md.splitlines():
        if line.startswith("# "):
            t = line[2:].strip()
            if t.lower().startswith("concern:"):
                t = t.split(":", 1)[1].strip()
            out["title"] = t
            break

    for key, pattern in CONCERN_HEADING_MAP:
        m = re.search(pattern + r"\n+(.+)", md, re.MULTILINE)
        if m:
            out[key] = m.group(1).strip()

    return out


CATEGORY_LABELS = {
    "tech-stack": "Tech Stack",
    "quality-attribute": "Quality Attributes",
    "testing": "Quality Attributes",
    "accessibility": "Quality Attributes",
    "internationalization": "Quality Attributes",
    "observability": "Quality Attributes",
    "security": "Security & Compliance",
    "infrastructure": "Infrastructure",
    "demo": "Documentation & Demos",
    "microsite": "Documentation & Demos",
}

CATEGORY_ORDER = [
    "Tech Stack",
    "Quality Attributes",
    "Security & Compliance",
    "Infrastructure",
    "Documentation & Demos",
]


def collect_concerns():
    concerns = []
    for cdir in sorted(p for p in CONCERNS_SRC.iterdir() if p.is_dir()):
        slug = cdir.name
        concern_md = load_text(cdir / "concern.md")
        practices_md = load_text(cdir / "practices.md")
        parsed = parse_concern_md(concern_md)
        concerns.append({
            "slug": slug,
            "concern_md": concern_md,
            "practices_md": practices_md,
            "parsed": parsed,
            "src_dir": cdir,
        })
    return concerns


def strip_first_h1(md: str) -> str:
    return re.sub(r"^#\s+.+\n+", "", md, count=1)


def render_concern_page(c: dict) -> str:
    slug = c["slug"]
    title = c["parsed"]["title"] or humanize(slug)
    category_raw = c["parsed"]["category"]
    category_label = CATEGORY_LABELS.get(category_raw.lower(), category_raw.title()) if category_raw else ""
    areas = c["parsed"]["areas"]

    out: list[str] = []
    out.append("---")
    out.append(f"title: {yaml_quote(title)}")
    out.append(f"slug: {slug}")
    out.append("generated: true")
    out.append("aliases:")
    out.append(f"  - /reference/glossary/concerns/{slug}")
    out.append("---")
    out.append("")

    if category_label or areas:
        bits = []
        if category_label:
            bits.append(f"**Category:** {category_label}")
        if areas:
            bits.append(f"**Areas:** {areas}")
        out.append(" · ".join(bits))
        out.append("")

    if c["concern_md"]:
        out.append("## Description")
        out.append("")
        out.append(strip_first_h1(c["concern_md"]).strip())
        out.append("")

    if c["practices_md"]:
        out.append("## Practices by phase")
        out.append("")
        out.append(
            "Agents working in any of these phases inherit the practices below "
            "via the bead's context digest."
        )
        out.append("")
        out.append(strip_first_h1(c["practices_md"]).strip())
        out.append("")

    return "\n".join(out)


def render_concerns_index(concerns: list) -> str:
    # Group by display category (consolidated)
    by_display: dict[str, list[dict]] = {}
    for c in concerns:
        raw = c["parsed"]["category"].lower().strip()
        display = CATEGORY_LABELS.get(raw, humanize(raw) if raw else "Other")
        by_display.setdefault(display, []).append(c)

    # Within each category, sort alphabetically by slug
    for display, items in by_display.items():
        items.sort(key=lambda c: c["slug"])

    out: list[str] = []
    out.append("---")
    out.append("title: Concerns")
    out.append("weight: 4")
    out.append("generated: true")
    out.append("aliases:")
    out.append("  - /docs/glossary/concerns")
    out.append("  - /reference/glossary/concerns")
    out.append("---")
    out.append("")
    out.append(
        "**Cross-cutting concerns** are HELIX's mechanism for declaring "
        "shared standards once and propagating them everywhere agents work."
    )
    out.append("")
    out.append(
        "A concern bundles a description, components, constraints, and "
        "drift signals with per-phase practices. When an agent claims a "
        "bead, HELIX synthesizes a *context digest* that includes the "
        "active concerns — so the agent makes consistent technology "
        "choices, follows the project's conventions, and respects "
        "quality requirements without having to re-derive them from "
        "the codebase."
    )
    out.append("")
    out.append(
        "Concerns are how HELIX answers \"every project needs this kind "
        "of consistency\" without forcing any specific tech stack on "
        "the framework itself."
    )
    out.append("")

    seen = set()
    for cat in CATEGORY_ORDER + sorted(set(by_display) - set(CATEGORY_ORDER)):
        if cat in seen or cat not in by_display:
            continue
        seen.add(cat)
        out.append(f"## {cat}")
        out.append("")
        out.append("{{< cards >}}")
        for c in by_display[cat]:
            title = c["parsed"]["title"] or humanize(c["slug"])
            areas = c["parsed"]["areas"]
            sub = areas if areas else c["slug"]
            out.append(
                f'  {{{{< card link="{c["slug"]}" title="{title}" '
                f'subtitle="{card_subtitle(sub, 80)}" >}}}}'
            )
        out.append("{{< /cards >}}")
        out.append("")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main


def main() -> None:
    # Validate the HELIX_REAL_EXAMPLES mapping before doing anything else.
    # Hard-fails on stale paths so drift surfaces loudly.
    validate_helix_real_examples()

    artifacts = collect_artifacts()
    concerns = collect_concerns()

    all_slugs = {a["slug"] for a in artifacts}

    # Wipe and recreate destination directories
    if ARTIFACTS_DEST.exists():
        shutil.rmtree(ARTIFACTS_DEST)
    ARTIFACTS_DEST.mkdir(parents=True)

    if CONCERNS_DEST.exists():
        shutil.rmtree(CONCERNS_DEST)
    CONCERNS_DEST.mkdir(parents=True)

    # Per-artifact pages
    for a in artifacts:
        (ARTIFACTS_DEST / f"{a['slug']}.md").write_text(render_artifact_page(a, all_slugs))

    # Artifacts index
    (ARTIFACTS_DEST / "_index.md").write_text(render_artifacts_index(artifacts))

    # Per-concern pages
    for c in concerns:
        (CONCERNS_DEST / f"{c['slug']}.md").write_text(render_concern_page(c))

    # Concerns index
    (CONCERNS_DEST / "_index.md").write_text(render_concerns_index(concerns))

    # Remove legacy locations under /reference/glossary/ (now at top level)
    for legacy in (
        LEGACY_GLOSSARY / "artifacts.md",
        LEGACY_GLOSSARY / "concerns.md",
        LEGACY_GLOSSARY / "artifacts",
        LEGACY_GLOSSARY / "concerns",
    ):
        if legacy.exists():
            if legacy.is_dir():
                shutil.rmtree(legacy)
            else:
                legacy.unlink()

    print(f"Generated {len(artifacts)} artifact pages → {ARTIFACTS_DEST.relative_to(ROOT)}/")
    print(f"Generated {len(concerns)} concern pages   → {CONCERNS_DEST.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
