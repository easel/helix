# Install HELIX for Codex

HELIX is a methodology, an artifact-type catalog, and a single routing
skill (`skills/helix/`). It is not Codex-specific. This guide covers how
to make HELIX discoverable from **two distinct Codex surfaces**:

- **A. OpenAI Codex CLI** — the agent-style terminal CLI that runs an
  interactive coding session against a repo and reads `AGENTS.md`.
- **B. GitHub Copilot Workspace / Codex extension** — the chat-style
  Copilot surfaces (Copilot Workspace, Copilot Chat with the Codex/agent
  extension) that consume repo-scoped instruction files and ad-hoc
  prompt context rather than running a full agent loop.

Both paths consume the **same source content** that lives in this repo:

```
skills/helix/SKILL.md      # the routing skill (single public entrypoint)
workflows/                 # the artifact-type catalog and methodology spec
```

There is no Codex-specific fork. Differences are purely about how each
surface discovers a skill and how the user invokes it.

---

## 1. Which Codex am I using?

Use this matrix to pick an install path. If both apply, install both —
they are non-conflicting.

| Question | Codex CLI (Path A) | Copilot / Codex extension (Path B) |
|---|---|---|
| How is it launched? | `codex` in a terminal, inside a repo checkout | Inside VS Code, JetBrains, GitHub.com, or Copilot Workspace |
| Where does it run? | On your machine with shell + file tools | In the editor/host process; sandboxed tool access |
| How does it discover repo conventions? | Reads `AGENTS.md` at the repo root and follows links | Reads a repo-scoped instruction file (e.g. `.github/copilot-instructions.md`) plus pinned/attached prompt context |
| Skill loading model | Skill body is referenced from `AGENTS.md`; agent loads it on demand during the session | User pastes / pins / attaches `skills/helix/SKILL.md` into the prompt context, or relies on the instruction file pointing at it |
| Shell execution | Yes | Typically no — chat-only or constrained tool surface |
| Best for | Full HELIX work: align, frame, design, evolve, build | Lighter-touch HELIX: review, alignment-style read-only audits, routing |

If you are unsure, run `codex --version` in a terminal. If that resolves,
you have the CLI (Path A). If you only interact with HELIX through a
Copilot chat panel or Copilot Workspace, you are on Path B.

The canonical repo-wide instruction file is `.github/copilot-instructions.md`.
Per-file or per-path instructions are supported as `NAME.instructions.md`
files stored under `.github/instructions/` (or subdirectories), each with
an `applyTo:` glob in their frontmatter. When a path matches both a
per-file instruction and the global file, Copilot uses both.
(Source: GitHub Docs — "Adding repository custom instructions for GitHub Copilot")

---

## 2. Install A — OpenAI Codex CLI

The Codex CLI follows the `AGENTS.md` convention: a Markdown file at the
repo root that the agent reads on session start. HELIX exploits this by
pointing Codex at `skills/helix/SKILL.md` and at the `workflows/` catalog.

### 2.1 File layout

After installing HELIX (via clone, submodule, `ddx install helix`, or
copy), the following paths must be present and reachable from the repo
root your Codex session runs in:

```
<repo>/
  AGENTS.md                     # repo entrypoint Codex reads first
  skills/
    helix/
      SKILL.md                  # the routing skill
  workflows/
    README.md
    principles.md
    phases/
      00-discover/
      01-frame/
      02-design/
      03-test/
      04-build/
      05-deploy/
      06-iterate/
```

If HELIX is vendored under a subdirectory (e.g. `vendor/helix/`), keep
the same internal layout and reference it with relative paths from
`AGENTS.md`.

### 2.2 AGENTS.md entry

Add (or merge into) an `AGENTS.md` at the root of the repo Codex will
open. The minimum useful entry:

```markdown
# Agent Instructions

This repo uses HELIX (methodology + artifact catalog + one routing skill).

- Routing skill: `skills/helix/SKILL.md`
- Artifact catalog: `workflows/phases/` (00-discover through 06-iterate)
- Methodology spec: `workflows/README.md`, `workflows/principles.md`

When the user asks to use HELIX, align documents, frame requirements,
design a change, evolve specs, review work, or otherwise touch
HELIX-governed material, load `skills/helix/SKILL.md` and follow the
routing table inside it. Do not invent new `helix-*` skills.

HELIX requires only "read markdown, write markdown, search files" plus
optional shell execution. No HELIX-specific CLI is required by the
methodology itself.
```

If your repo already has an `AGENTS.md` (this HELIX repo does), append
a HELIX section rather than overwriting. Codex will read the whole file.

### 2.3 Verify (Codex CLI)

Open a Codex session in the repo and ask:

```
What HELIX routing modes are available, and where is the routing skill?
```

A correctly installed setup will:

1. Mention that it read `AGENTS.md`.
2. Cite `skills/helix/SKILL.md` as the routing skill.
3. List the routes (input, frame, align, evolve, design, backfill,
   review, polish, check/next, build, run, commit, release,
   experiment, worker) or a faithful subset.

If Codex does not mention the skill file, check that `AGENTS.md` is at
the working directory root and that `skills/helix/SKILL.md` exists.

The Codex CLI does **not** honor a `.codex/instructions.md` file. The
instruction files it checks are `AGENTS.override.md` and `AGENTS.md`, checked
in that order at the global scope (`~/.codex/`), the Git root, and each
directory down to the current working directory. Custom fallback filenames
(e.g. `TEAM_GUIDE.md`) can be added via `project_doc_fallback_filenames`
in `~/.codex/config.toml`, but there is no built-in `.codex/instructions.md`
path. Use `AGENTS.md` (or `AGENTS.override.md` to take absolute priority).
(Source: OpenAI Developers — "Custom instructions with AGENTS.md")

---

## 3. Install B — Codex extension / Copilot

The Copilot / Codex-extension surfaces typically do not run a full
agent loop with shell access. Instead they read repo-scoped instruction
files and let the user attach or pin prompt context.

### 3.1 Repo-instruction file

Place a HELIX pointer in the repo-instruction location the surface
expects. The most widely-supported location today:

```
.github/copilot-instructions.md
```

Suggested contents (parallel to the `AGENTS.md` entry, but voiced for a
chat surface):

```markdown
# Copilot Instructions

This repository uses HELIX for methodology and artifact governance.

When a request touches HELIX work (alignment, framing, design, evolve,
review, routing), use `skills/helix/SKILL.md` as the routing reference
and `workflows/phases/*` as the artifact-type catalog. Do not propose
new helix-prefixed skills; route inside the existing skill.

The methodology requires only the ability to read, write, and search
markdown files. Shell execution is optional and not required for
alignment, framing, evolve, or review modes.
```

Copilot also supports per-file or per-path instruction files: create
`NAME.instructions.md` files under `.github/instructions/` (or
subdirectories) with `applyTo:` glob frontmatter to scope HELIX guidance
to a subtree. For example, to apply HELIX guidance only to files under
`src/`, set `applyTo: "src/**"`. When a file matches both a per-path
instruction and the global `.github/copilot-instructions.md`, Copilot
merges both sets of instructions.
(Source: GitHub Docs — "Adding repository custom instructions for GitHub Copilot")

### 3.2 Loading the skill into prompt context

In addition to (or instead of) the instruction file, the user can load
the routing skill into the chat context directly:

- **Copilot Chat (VS Code / JetBrains):** use the file-attach or
  `#file:` reference to attach `skills/helix/SKILL.md` to the
  conversation. Re-attach when starting a new chat.
- **Copilot Workspace:** add `skills/helix/SKILL.md` to the workspace's
  pinned context for the task. The routing table will then be visible
  to the model when planning the task.
- **GitHub.com Copilot Chat:** open `skills/helix/SKILL.md` in the
  browser tab Copilot has focus on, or paste the routing section into
  the chat.

The skill body is intentionally short (one routing table plus per-mode
contracts) so it fits comfortably in a chat context window.

### 3.3 Verify (extension / Copilot)

In the chat surface, with the skill or instruction file loaded, ask:

```
Based on the HELIX routing skill in this repo, which mode handles
"add a new requirement and thread it through the artifacts"?
```

A correctly loaded setup will answer **evolve** and cite either the
instruction file or the attached `SKILL.md`. If it answers without
referencing the skill, the context is not loaded — re-attach the file
or confirm the instruction file is at the supported path.

---

## 4. Shared content reference

Both install paths consume the same content. Nothing below is
Codex-specific.

### 4.1 The routing skill

`skills/helix/SKILL.md` is the **only** public HELIX skill. It contains:

- a routing table mapping user intent → mode
- per-mode workflow contracts (input, frame, align, evolve, design,
  backfill, review, polish, check/next, build, run, commit, release,
  experiment, worker)
- operating discipline (authority order, bead-first for DDx-backed
  projects, etc.)

Per the PRD (R-4 / R-7), the skill body is runtime-neutral. A package
for a given runtime — Codex CLI, Copilot, DDx, Claude Code — wraps the
same content; it is not a fork.

### 4.2 Workflows catalog discovery

`workflows/phases/` is the artifact-type catalog. Each phase directory
follows the same layout:

```
workflows/phases/<NN>-<phase>/
  artifacts/
    <artifact-type>/
      template.md   # markdown skeleton
      prompt.md     # authoring guidance
      meta.yml      # metadata, quality criteria
      example.md    # worked example (where present)
```

The phases:

| Phase | Purpose |
|---|---|
| `00-discover` | Intent, context, product vision |
| `01-frame` | PRD, feature specs, user stories |
| `02-design` | Architecture, ADRs, solution designs |
| `03-test` | Test plans, test strategy |
| `04-build` | Implementation plans, build-time artifacts |
| `05-deploy` | Release, runbook, deploy artifacts |
| `06-iterate` | Feedback, retrospectives, evolution |

When a HELIX mode (e.g. `frame`, `design`) needs a template, it loads
the matching `template.md` and `prompt.md` from this tree. No catalog
data is duplicated into the skill body — the skill points at the
catalog.

### 4.3 Methodology spec

`workflows/README.md` and `workflows/principles.md` carry the
methodology specification (authority order, principles, ratchets). Both
Codex surfaces should treat these as authoritative when the skill body
defers to them.

---

## 5. Caveats and feature-parity notes

The two Codex surfaces differ in what they can do, even with identical
HELIX content loaded.

| Concern | Codex CLI (A) | Copilot / extension (B) |
|---|---|---|
| Read/write markdown | Yes | Yes (within sandbox/editor scope) |
| Search files across repo | Yes | Partial — depends on attachments / workspace scope |
| Shell execution | Yes | Usually no |
| Run a runtime CLI (e.g. DDx `ddx bead ...`) | Yes, when DDx is installed | No — HELIX modes that require tracker mutation will need to be performed outside the chat |
| Multi-file edits in one turn | Yes | Limited; varies by surface |
| Long-running build/run loop (HELIX `run` mode) | Possible, but a runtime (DDx) is what actually executes it | Not supported — `run` mode is out of scope for chat surfaces |
| Bead tracker discipline | Honored when DDx is available | Surface only — read-only review and alignment work; durable tracker writes happen elsewhere |

Practical guidance:

- **Planning, alignment, framing, evolve, review** work well on both
  surfaces. They are read-mostly, markdown-mostly, and produce
  artifact diffs.
- **Build, run, commit, release, experiment, worker** modes assume a
  runtime (DDx is the reference). Use Path A when you want HELIX to
  drive into execution; use Path B when you want HELIX to reason about
  artifacts without touching execution surfaces.
- HELIX itself does not depend on either Codex surface. Anything either
  surface can do, another agent runtime with the same `read / write /
  search markdown + optional shell` contract can also do. The Codex
  packages here exist to make discovery easy, not to lock HELIX to
  Codex.

As of 2026, the public GitHub Copilot documentation does not describe
Copilot Workspace as exposing a general shell-execution tool to agents;
the product itself may have been renamed or merged into other surfaces
(e.g. the cloud agent or Copilot Spaces). GitHub Copilot CLI — a
separate, terminal-native surface — does support full shell execution.
Verify the current Copilot Workspace feature set before assuming shell
access is available from the web-based task-planning surface.

---

## Where to go next

- Read `skills/helix/SKILL.md` for the full routing table and per-mode
  contracts.
- Read `workflows/README.md` for the methodology overview.
- Browse `workflows/phases/` to see the artifact-type catalog you will
  be authoring against.
- If your project also adopts a runtime (DDx, Claude Code, Genie),
  install that runtime's HELIX package alongside — they share this same
  source content.
