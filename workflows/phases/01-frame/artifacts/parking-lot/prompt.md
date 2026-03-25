# Prompt: Parking Lot (Deferred / Future Work)

You are creating the HELIX Parking Lot registry at `docs/helix/parking-lot.md`.

Goals:
- Capture deferred and future work without adding inline sections to core HELIX artifacts.
- Require traceability: Source + Rationale + Revisit Trigger.
- Keep this as a lightweight registry with links to parked artifacts.

Instructions:
1. Use the template structure as-is.
2. Each item must include **Type**, **Source**, and **Revisit Trigger**.
   - Source may be a HELIX ID (FEAT/US/ADR/etc.) or an external reference (ticket, note, roadmap item).
3. If a full artifact exists, keep it in its normal HELIX directory and set:
   - `dun.parking_lot: true` in its frontmatter
   - A clear **Parking Lot** status in the header
4. Do not embed full artifacts in this registry. Link to their file path instead.
5. Do not add inline Future/Deferred sections to PRD or other core artifacts.
6. When an item becomes active, follow the **Unparking** steps:
   - Remove `dun.parking_lot: true` from the artifact
   - Update the artifact status to active
   - Add it to the main PRD flow/registries
   - Remove the registry entry immediately

Checklist before finalizing:
- [ ] All items have Source + Rationale + Revisit Trigger
- [ ] Any parked artifacts are linked and carry `dun.parking_lot: true`
- [ ] Registry stays concise and editable
