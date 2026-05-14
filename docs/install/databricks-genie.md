# HELIX on Databricks Code Genie

This guide installs HELIX as a Databricks Code Genie skill bundle so that
Genie can route requests to the HELIX methodology — alignment, framing,
evolution, design, review — over a project's governing artifacts.

HELIX is content-plus-one-skill: the artifact catalog under `workflows/` and
the routing skill at `skills/helix/SKILL.md`. The runtime does the file I/O.
This document maps that source content onto Databricks Code Genie's skill
surface.

> Status: Databricks Code Genie is a real product, but its public skill-bundle
> conventions are still moving. Sections that depend on Genie-specific format
> details are based on documentation current as of 2026-05; validate against
> the current Databricks documentation before relying on those details.

<!-- Skill format reference: https://docs.databricks.com/aws/en/genie-code/skills
     and the open Agent Skills standard at https://agentskills.io/specification -->

## 1. Genie skill format overview

Databricks Code Genie is Databricks' agentic coding assistant. It supports
extension via skills — reusable capability packages a workspace administrator
can register and that Genie can route to based on natural-language intent.

A HELIX Genie skill is a non-executing methodology skill: it loads artifact
templates, authoring prompts, and the routing rules in `skills/helix/SKILL.md`,
then guides Genie's responses against the user's existing markdown artifacts.
HELIX itself does not require Genie to run arbitrary code; it requires Genie
to read and write markdown files and search the workspace filesystem.

See the [Databricks Genie Code skill authoring documentation](https://docs.databricks.com/aws/en/genie-code/skills)
and the [Agent Skills open standard](https://agentskills.io/specification) for the authoritative skill format.

## 2. Bundle layout

The HELIX source content packaged for Genie is identical to the content the
Claude Code and Codex installs use. A Genie skill bundle for HELIX maps that
content onto Genie's expected directory structure.

Source content (unchanged across runtimes):

- `skills/helix/SKILL.md` — the routing skill. This is the single normative
  entry point for HELIX's planning, alignment, design, review, evolution,
  and execution routes.
- `workflows/phases/00-discover` through `workflows/phases/06-iterate` —
  the artifact catalog. Each phase directory holds artifact types with
  `template.md`, `prompt.md`, `meta.yml`, and examples.

Recommended bundle layout for a Genie skill named `helix`:

```text
helix-genie-bundle/
  manifest.yaml                 # Genie skill descriptor
  skill/
    SKILL.md                    # copy of skills/helix/SKILL.md
  catalog/
    phases/
      00-discover/              # copy of workflows/phases/00-discover
      01-frame/
      02-design/
      03-test/
      04-build/
      05-deploy/
      06-iterate/
  README.md                     # workspace-facing notes for operators
```

`manifest.yaml` declares the skill to Genie. The exact field names depend on
the current Genie skill schema.

Genie Code skills use a `SKILL.md` file with YAML frontmatter rather than a
separate manifest file. Per the [Genie Code skills documentation](https://docs.databricks.com/aws/en/genie-code/skills),
the required frontmatter fields are `name` and `description`. Supporting files
(scripts, catalogs) are referenced via relative paths from within `SKILL.md`.

Example `SKILL.md` frontmatter for the HELIX bundle:

```yaml
---
name: helix
description: >
  Route HELIX methodology work to the right planning, alignment, design,
  review, execution, or release workflow. Provides an artifact catalog
  and a single routing skill for AI-assisted artifact-driven development.
---
```

The body of `SKILL.md` (below the frontmatter) holds the routing instructions
and references to catalog resources. Use the content of `skills/helix/SKILL.md`
as the body, adjusting any resource paths to match the bundle layout above.
Additional supporting files are referenced by relative path from within the
`SKILL.md` body. Verify the current field set against the
[Agent Skills specification](https://agentskills.io/specification) before deploying.

The `description` should match the description in `skills/helix/SKILL.md`'s
frontmatter so Genie's skill router has the same intent surface that Claude
Code and Codex see.

## 3. Install path

These steps assume a Databricks workspace with Code Genie enabled and
permission to register workspace skills.

1. **Assemble the bundle.** Copy `skills/helix/SKILL.md` into
   `helix-genie-bundle/skill/SKILL.md`. Copy the `workflows/phases/` tree
   into `helix-genie-bundle/catalog/phases/`. Author `manifest.yaml`.
2. **Upload the bundle to the workspace filesystem.** Per the
   [Genie Code skills documentation](https://docs.databricks.com/aws/en/genie-code/skills),
   workspace-scoped skills are installed under
   `/Workspace/.assistant/skills/{skill-name}/`. Place the HELIX bundle
   at `/Workspace/.assistant/skills/helix/` so all workspace users with
   Genie access can resolve the catalog. User-scoped skills live under
   `/Users/{username}/.assistant/skills/{skill-name}/` instead.
3. **Register the skill with Genie.** Registration is automatic: placing a
   valid `SKILL.md` (with required frontmatter) into the `.assistant/skills/`
   directory is sufficient — Genie Code discovers skills by directory scan
   with no explicit CLI command or REST call required. Alternatively, the
   open-source [Skills CLI](https://docs.databricks.com/aws/en/agent-skills/)
   (`npx skills add`) can install skills from a GitHub repository directly.
   The [Databricks CLI `genie` command group](https://docs.databricks.com/aws/en/dev-tools/cli/reference/genie-commands)
   covers the conversational Genie API surface but is not used for skill
   registration. Verify this against the current
   [Genie Code skills documentation](https://docs.databricks.com/aws/en/genie-code/skills).
4. **Grant permissions.** Genie needs read access to the entire catalog
   (`catalog/phases/**`) and to whatever project artifact root the user
   wants HELIX to operate over (typically `docs/helix/` inside the user's
   repo or workspace folder). Genie needs write access only to the project
   artifact root, not to the catalog itself. The catalog is read-only
   reference content.
5. **Verify registration.** The skill should appear in the workspace's
   Genie skill list and be invokable by description-matching from the
   Genie chat surface.

The catalog lives in workspace storage so multiple users can share one copy.
HELIX does not require per-user installation; the bundle is methodology
content, not user state.

## 4. Invocation

Genie routes by natural language. HELIX is designed for that interface:
users describe what they want done; the routing skill picks the matching
workflow.

Examples a user can paste into a Genie chat once HELIX is installed:

- "Use HELIX to align the artifacts under `docs/helix/` for this repo."
- "Run a HELIX framing pass and produce a PRD for the new ingestion feature."
- "Evolve the HELIX artifacts to thread the new compliance requirement
  through vision, PRD, feature specs, and any affected designs."
- "Do a HELIX fresh-eyes review of the changes on this branch."
- "Decide the next safe HELIX action."

Genie's skill router uses the skill description and the routing rules in
`SKILL.md` to pick a HELIX mode (input, frame, align, evolve, design,
backfill, review, polish, check, build, run, commit, release, experiment,
worker). Users do not invoke modes by name; the routing skill resolves them.

If Genie does not select the HELIX skill automatically, name it explicitly:
"Using the HELIX skill, ..." This is a fallback; healthy routing should not
need it.

## 5. Verification

A small interaction confirms HELIX is loaded and the artifact catalog
resolves.

**Step 1.** Open Genie in the workspace. Ask:

```text
List the HELIX workflow modes you can route to, and cite the SKILL.md
section that defines each one.
```

Expected: Genie names input, frame, align, evolve, design, backfill, review,
polish, check, build, run, commit, release, experiment, and worker, and
references the routing table and workflow contracts inside `SKILL.md`. If
Genie cannot enumerate these, the skill bundle is not registered correctly
or the entrypoint path is wrong.

**Step 2.** Confirm the artifact catalog is reachable:

```text
Using HELIX, list the artifact types defined under phase 01-frame, and
show the path of each artifact-type directory in the catalog.
```

Expected: Genie returns the artifact-type directories under
`workflows/phases/01-frame/artifacts/` (as packaged into
`catalog/phases/01-frame/artifacts/`), with paths anchored at the catalog
root. If Genie returns generic descriptions without paths, the catalog
resources are not visible to the skill.

**Step 3.** Smoke-test a routing decision against a real project:

```text
I have docs/helix/00-discover/product-vision.md and
docs/helix/01-frame/prd.md in this repo. Use HELIX to check whether they
are aligned. Do not write any files yet.
```

Expected: Genie selects align mode, reads both artifacts, and returns an
alignment-shaped report (gaps classified as `ALIGNED`, `INCOMPLETE`,
`DIVERGENT`, `UNDERSPECIFIED`, `STALE_PLAN`, or `BLOCKED`) without modifying
files. If Genie writes files or proposes implementation work, routing is
mis-tuned.

## 6. Caveats and known gaps vs Claude Code / Codex installs

The HELIX source content is the same across runtimes; the differences are
in the runtime surface around it.

- **Skill format maturity.** The Claude Code skill format is documented and
  stable enough that the Claude Code install can be precise about manifest
  fields. The Genie skill-bundle format is less public at time of writing.
  Sections in this document that carry caveats are the places to
  reconcile when the Genie spec is final.
- **File-write surface.** Claude Code and Codex run with the user's local
  filesystem permissions and can edit any file the user can edit. Genie
  writes through the Databricks workspace; depending on workspace
  configuration, write access to a Git-backed repo folder may go through a
  Databricks Repos integration rather than direct filesystem writes. HELIX
  alignment and evolve passes that propose artifact edits may need to be
  applied via Repos commit flow rather than direct file write.
  The exact write path and commit-attribution behavior depend on your
  workspace's Repos configuration and have not been independently verified
  against public Databricks documentation at time of writing. Confirm with
  your workspace administrator before relying on attribution in audit trails.
- **Execution surface.** Claude Code and Codex can run shell commands as
  part of build/run modes if the user permits. Genie's shell-execution
  surface inside the workspace is more constrained. HELIX build and run
  modes that depend on running a project gate may need to be paired with a
  Databricks job, notebook, or CI pipeline rather than executed inline.
  Whether a Genie Code skill can directly invoke a workspace job or notebook
  is not documented in the current public skill authoring reference. Until
  confirmed, treat build and run modes as requiring a separately configured
  Databricks job or CI pipeline triggered outside the HELIX skill.
- **Multi-user state.** Claude Code and Codex are typically single-user.
  Genie is a shared workspace agent: multiple users may invoke HELIX
  against the same artifact tree. HELIX itself is stateless between
  invocations, so this is safe, but operators should be aware that
  concurrent edits flow through whatever the workspace's git or Repos
  surface enforces, not through HELIX.
- **DDx is not present.** The DDx reference runtime — beads queue,
  execution loop, evidence capture — is not installed by this bundle.
  HELIX-on-Genie is HELIX-as-methodology only. Projects that want the full
  HELIX-plus-runtime experience can use DDx in a connected dev environment
  and have Genie operate over the same artifact tree.
- **No CLI verbs.** This install does not introduce a `helix` CLI in the
  workspace. All invocation is natural language through Genie, exactly as
  with the Claude Code and Codex installs.

## See also

- `skills/helix/SKILL.md` — the routing skill (single source of truth)
- `workflows/phases/` — the artifact catalog
- `docs/helix/01-frame/prd.md` — PRD, including R-7 (per-runtime packages)
  and the minimal runtime contract (read file, write file, search files)
- [Install README index](README.md)
- Companion install guides: [Claude Code](claude-code.md) and [Codex](codex.md)
