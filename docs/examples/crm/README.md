---
ddx:
  id: crm.readme
---

# CRM Example — Greenfield Frame Artifacts

This directory holds frame-phase artifacts for a hypothetical CRM product,
authored from the sparse intake `"design a CRM"` via the HELIX methodology.

It exists for two reasons:

1. **Dogfood.** Exercise HELIX templates on a greenfield product distinct from
   HELIX itself.
2. **Demo material.** Provide a self-contained example of how HELIX turns a
   one-line intake into vision/PRD artifacts with explicit assumptions.

## Artifacts

| ID | Path | Purpose |
|---|---|---|
| `crm.vision` | `00-discover/product-vision.md` | North-star CRM product vision |
| `crm.prd` | `01-frame/prd.md` | CRM product requirements (MVP scope) |

## Scope and authority

These artifacts govern downstream CRM work referenced under the provisional
spec-id `CRM-001`. Beads filed against `CRM-001` should adopt `crm.prd` (or a
narrower canonical ID once feature specs land) as their governing reference.

The scope decision — whether the CRM artifact stack remains here as an example
or migrates to a dedicated product repo — is tracked separately by bead
`helix-5129f35d` ("Resolve CRM request scope against current HELIX repo
vision"). Until that resolves, treat this directory as a greenfield planning
exercise hosted inside the HELIX repo, not a HELIX product surface.

## Status

Frame artifacts only. Design (`02-design/`) and downstream phases are not
authored here yet; those are tracked by sibling beads `helix-8944c622` (design)
and `helix-7e8a9c4b` (decomposition).
