# Install HELIX

HELIX is a methodology, an artifact-type catalog, and a single routing skill.
It is not a CLI, a tracker, or a runtime. To use HELIX you make its content
discoverable from the runtime you already use. This index points at the
per-runtime install guides and states the minimal runtime contract HELIX
assumes.

The source content is the same across every runtime. Per-runtime guides
describe **discovery and invocation only**. They do not fork the skill or the
catalog. See [No-fork policy](#no-fork-policy) below.

## Minimal runtime contract

A HELIX-compliant runtime can:

1. **Read markdown files** from the project's filesystem.
2. **Write markdown files** to the project's filesystem.
3. **Search files** by path or pattern across the project.
4. **Optionally execute a shell command** for verification or build/run modes.

That is the full contract. HELIX assumes nothing else — no tracker, no queue,
no execution loop, no IDE integration, no language toolchain. This contract
is the binding form of PRD R-4 (runtime-neutral content) and the Constraints
section, which require the skill body to work given only "read file, write
file, search files" as runtime primitives. Items 1–3 are required; item 4 is
optional and only some routes (`build`, `run`, `commit`, `release`) make use
of it.

If your runtime satisfies items 1–3, HELIX's alignment, framing, design,
evolve, validate, and review routes all work. If it also satisfies item 4,
the execution-oriented routes become available.

## Source of truth

The runtime install guides are packaging notes. The normative HELIX content
lives in two places in this repo:

- [`skills/helix/SKILL.md`](../../skills/helix/SKILL.md) — the single routing
  skill. One public entry point (`helix`), one routing table, one set of
  per-mode workflow contracts. There are no separate public `helix-*` skills.
- [`workflows/`](../../workflows/) — the artifact-type catalog and
  methodology specification. `workflows/activities/00-discover` through
  `workflows/activities/06-iterate` carry the artifact templates, prompts,
  quality criteria, and examples. `workflows/principles.md`,
  `workflows/ratchets.md`, and `workflows/artifact-schema.md` carry the
  methodology invariants.

When a per-runtime guide and the skill or catalog disagree, the skill and
catalog win. The guides are about how a particular runtime finds and invokes
this content, not about what the content says.

## Per-runtime install guides

Each guide is self-contained: file layout, install steps, invocation, and
verification for one runtime. Pick the one that matches your environment;
install more than one if you use more than one.

### [Claude Code](claude-code.md)

Install HELIX as a Claude Code skill — user-global under
`~/.claude/skills/helix/` or per-repo under `.claude/skills/helix/`. The
artifact catalog is vendored alongside the skill. Invocation is through
`/helix` or natural language; Claude Code's skill loader picks up the
routing skill by its frontmatter description.

**Best fit for:** local development with full read/write/search and shell
access, on a per-repo or per-user basis. Supports every HELIX route,
including `build` and `run`.

### [Codex (CLI and Copilot/Codex extension)](codex.md)

Covers two distinct Codex surfaces in one guide:

- **OpenAI Codex CLI** — terminal agent that reads `AGENTS.md` at the repo
  root. HELIX is discovered by an `AGENTS.md` entry pointing at
  `skills/helix/SKILL.md` and `workflows/`. Full read/write/search plus
  shell.
- **GitHub Copilot Workspace / Codex extension** — chat-style editor
  surfaces that consume a repo-scoped instruction file (commonly
  `.github/copilot-instructions.md`) plus pinned or attached prompt
  context. Read/write/search within the editor sandbox; usually no shell.

**Best fit for:** teams already running on the Codex CLI for full HELIX
flow, or on Copilot surfaces for read-mostly HELIX work (align, frame,
evolve, review) where shell-bound modes are out of scope anyway.

### [Databricks Code Genie](databricks-genie.md)

Install HELIX as a Databricks Code Genie skill bundle. The skill and the
catalog are uploaded to workspace storage (recommended:
`/Workspace/Shared/skills/helix/`) and registered as a Genie skill so that
Genie routes natural-language HELIX requests to the routing skill body.

**Best fit for:** Databricks-resident teams who want HELIX governance to
live next to their data and notebook work, shared across the workspace
rather than installed per-user. Methodology-only — the build/run routes
that expect a CLI-style execution loop typically land in a Databricks job
or notebook instead.

## No-fork policy

The per-runtime guides exist so adopters can install HELIX. They do not
exist to localize, dialect, or rewrite the methodology.

- The normative skill body lives in `skills/helix/SKILL.md` and nowhere
  else. Per-runtime guides may quote it for orientation but must not paste
  a divergent copy.
- The artifact catalog lives in `workflows/` and nowhere else. Per-runtime
  guides may describe the directory layout (so users know what they are
  vendoring) but must not redefine artifact types, templates, or quality
  criteria.
- If a runtime genuinely requires content adaptation — for example, a
  manifest file, a wrapper instruction file, or a packaging metadata
  document — that adaptation lives **inside the per-runtime install
  guide**, clearly marked as a runtime-specific shim. It does not get
  pushed back into `skills/` or `workflows/`.
- A per-runtime guide that introduces normative HELIX behavior the other
  guides do not share is a bug against PRD R-4 and R-7. File it as a
  HELIX alignment finding.

This policy is what makes "the source content is the same across every
runtime" enforceable. Three install paths, one HELIX.

## Homepage linking

The HELIX website homepage links to `website/content/install/_index.md`, which
mirrors this index as an in-site Hugo page. The homepage carries a dedicated
"Install HELIX in your runtime" section with per-runtime CTA cards and a
"Read the full install index" link. The top-level nav also includes an
"Install" entry pointing at `/install`.

## See also

- [`skills/helix/SKILL.md`](../../skills/helix/SKILL.md) — routing skill
  and per-mode workflow contracts.
- [`workflows/README.md`](../../workflows/README.md) — methodology
  overview.
- [`workflows/principles.md`](../../workflows/principles.md) and
  [`workflows/ratchets.md`](../../workflows/ratchets.md) — methodology
  invariants.
- [`docs/helix/01-frame/prd.md`](../helix/01-frame/prd.md) — PRD,
  including R-4 (runtime-neutral content), R-7 (per-runtime packages),
  and the Constraints section that defines the minimal runtime contract.
