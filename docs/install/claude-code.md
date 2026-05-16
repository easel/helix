# HELIX in Claude Code

This guide installs HELIX into Claude Code and shows how to invoke it. HELIX
ships as a single routing skill plus an artifact catalog (templates, prompts,
and metadata under `workflows/activities/`). Claude Code is one of HELIX's target
runtimes, alongside DDx and Databricks Genie. The content is the same; only
the packaging differs.

If you are publishing an install index later, link to this file as
`docs/install/claude-code.md`.

## What you are installing

Two pieces of content move into a location Claude Code can see:

1. **The skill** — `skills/helix/SKILL.md`. A single router that maps user
   intent (align, frame, design, evolve, review, build, release, etc.) to a
   workflow contract. There are no separate public `helix-*` skills; the
   router is the only entry point.
2. **The artifact catalog** — `workflows/activities/00-discover` through
   `06-iterate`. Each phase contains artifact-type directories (`prd`,
   `feature-specification`, `adr`, `test-plan`, and so on). Each artifact-type
   directory has `template.md`, `prompt.md`, `meta.yml`, and an example. The
   skill resolves these paths relative to the project root when it needs to
   open a template or quality rubric.

HELIX does not need a CLI, a tracker, or an execution loop to be useful in
Claude Code. The minimal runtime contract is the only thing the skill assumes:
read markdown, write markdown, search files, and optionally run a shell
command. Claude Code satisfies all of those by default.

## Requirements

- Claude Code 0.5 or later (skill discovery via `~/.claude/skills/` and
  per-project `.claude/skills/`).
- Frontmatter parser that tolerates `name:`, `description:`, and
  `argument-hint:` keys. The HELIX skill ships only those three.
- File-read, file-write, and file-search tools enabled in the Claude Code
  session.
- Optional: `Bash` tool, if you want the skill to run project-side
  verification commands during alignment or review work.

No other runtime dependency is required. HELIX content is plain Markdown plus
YAML frontmatter under the `ddx:` namespace; Claude Code does not need to
understand that namespace to render or edit the files.

## Install path A: user-global

Use this when you want HELIX available in every Claude Code session on your
machine, regardless of which repo you open.

Place the skill where Claude Code's user-scope skill loader looks:

```text
~/.claude/skills/helix/SKILL.md
```

Either copy the directory from a HELIX checkout or symlink it. A symlink is
preferable while HELIX is iterating, because skill updates land without a
re-copy.

Place the artifact catalog somewhere stable and discoverable. The conventional
location for user-global HELIX content is:

```text
~/.helix/workflows/activities/...
~/.helix/docs/helix/...
```

You can use a different root; the skill resolves template and prompt paths
relative to the project it is invoked in, so for the global install, ensure
each project that wants HELIX governance either vendors the catalog (see Path
B) or points the skill at the global root when asked.

User-global is right for solo projects and exploratory sessions. It is the
wrong default for a team repo, because the team cannot version the catalog
against the code.

## Install path B: per-repo

Use this when a repo should govern its own HELIX content — most production
projects.

Vendor the skill into the repo's per-project skill location:

```text
.claude/skills/helix/SKILL.md
```

Per-project skills override user-global skills with the same name in Claude
Code, so a vendored copy lets a repo pin a specific HELIX version. Commit the
directory so collaborators get the same skill.

Vendor the artifact catalog into the repo at the conventional layout:

```text
workflows/activities/00-discover/...
workflows/activities/01-frame/...
workflows/activities/02-design/...
workflows/activities/03-test/...
workflows/activities/04-build/...
workflows/activities/05-deploy/...
workflows/activities/06-iterate/...
workflows/artifact-schema.md
workflows/principles.md
```

HELIX's own repo at `/Users/erik/Projects/helix` is the canonical layout. A
new repo can adopt HELIX by copying the `skills/helix/` and `workflows/`
trees, or by using one of the per-runtime packages (the DDx plugin published
via `ddx install helix` is one such optional integration).

Once the catalog is in the repo, governing artifacts live under `docs/helix/`
by convention:

```text
docs/helix/00-discover/product-vision.md
docs/helix/01-frame/prd.md
docs/helix/02-design/...
```

The skill expects to find templates under `workflows/activities/` and project
artifacts under `docs/helix/` when those defaults apply. If your repo uses a
different artifact root, tell the skill in the prompt — it will resolve from
there.

## How invocation works

Users do not memorize workflow names. They state intent; the skill routes.

The supported shapes are:

- `/helix` — invoke the router with no arguments and let it ask.
- `/helix align this PRD with the design docs` — invoke with an inline intent.
- A natural-language ask in the chat: "use HELIX to evolve the auth
  requirement through the spec stack" or "ask HELIX which workflow fits
  this." Claude Code recognizes the skill by its `description:` frontmatter
  and loads it.

Claude Code resolves the skill name `helix` by looking in:

1. `.claude/skills/helix/` (per-repo, if present).
2. `~/.claude/skills/helix/` (user-global).
3. Any plugin-provided skill location enabled for this session.

First match wins. The router then consults its internal routing table
(`SKILL.md`) and selects one of: input, frame, align, evolve, design,
backfill, review, polish, check, build, run, commit, release, experiment,
worker. Each mode has a workflow contract in the same file that the skill
follows for the rest of the session.

When the routed workflow needs a template, prompt, or quality rubric, it opens
the matching file under `workflows/activities/<phase>/artifacts/<type>/`. For
example, framing a PRD reads
`workflows/activities/01-frame/artifacts/prd/template.md` and `prompt.md`. The
skill never invents these paths; they come from the catalog directory layout.

## Verify the install

In a Claude Code session with the project open, type:

```
/helix check
```

A working install produces, without further input:

1. A short statement that the HELIX router loaded.
2. A list of governing artifacts the skill can see under `docs/helix/` (or a
   note that none exist yet — that is fine; the skill will offer to start
   with `input` or `frame`).
3. A proposed next action drawn from the routing table.

If that does not happen, ask in plain English: "Is the HELIX skill available?
List the workflow modes you would route to." A loaded skill will return the
routing table from `SKILL.md`. A missing skill will produce a generic answer
or an apology that no `helix` skill is installed.

A second verification confirms the catalog is reachable. Ask:

> Open `workflows/activities/01-frame/artifacts/prd/template.md` and summarize
> the section headings.

A correct install returns the PRD template's actual section list. A broken
install (skill present but catalog missing or pointed at the wrong root)
fails the open step.

## Per-runtime contract

HELIX content assumes the minimum runtime contract from the PRD: read
markdown, write markdown, search files, and optionally execute a shell
command. Claude Code provides all of these. The skill body avoids
runtime-specific commands (no CLI verbs in the routing prose). If you see a
HELIX skill or workflow that hard-codes a runtime command in its normative
body, that is a bug against PRD R-4 and should be filed.

## Optional integration: DDx

If your team also uses DDx as a software factory, you can install the same
HELIX content as a DDx plugin so DDx-side automation and beads pick it up.
That is a single optional integration, not a requirement; Claude Code does
not need DDx to use HELIX.

## Further reading

- `skills/helix/SKILL.md` — the routing table and workflow contracts.
- `workflows/artifact-schema.md` — what `meta.yml` and instance frontmatter
  carry.
- `workflows/principles.md` — methodology invariants the skill enforces.
- `docs/helix/00-discover/product-vision.md` and `docs/helix/01-frame/prd.md`
  — the governing intent for HELIX itself.
