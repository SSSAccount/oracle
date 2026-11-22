# Oracle — Risk Register (v0)

Seeded 2026-11-16. Reviewed at each sprint planning; new risks append; closed risks are
marked with the date and how they closed. Likelihood × impact scored 1–5; exposure = L×I.
Owner acts on any risk with exposure ≥ 8 before lower ones.

| ID | Risk | L | I | Exp | Mitigation / response | Status |
|---|---|---|---|---|---|---|
| R-01 | Round-2 discovery results return late, shifting the research schedule right | 4 | 3 | 12 | Prototype track proceeds on Round-1 evidence; research items re-planned at each review, not silently dropped | Open |
| R-02 | Client-role question unanswered, blocking elicitation artefacts (B1 rich picture, B3 elicitation records) | 3 | 4 | 12 | Asked at Meeting 1; interim elicitation record built from the published-evidence base and labelled as such | Open |
| R-03 | tikz-cd parsing proves harder than estimated (TikZ is a full macro language) | 4 | 3 | 12 | PB-07 is an explicit spike with a time-box; fallback is restricting to the tikz-cd subset used by real fixtures | Open |
| R-04 | Fixture documents' permission basis is unclear for some sources | 3 | 4 | 12 | Permitted/attributed use only; anything unclear is replaced, not risked (zero-mark rule) | Open |
| R-05 | Solo bandwidth: illness or workload spikes break the weekly rhythm | 3 | 4 | 12 | Small sprint scopes; the stand-up log makes slumps visible early; the module team can be informed at the first available contact, not after | Open |
| R-06 | Scope creep: the checking layer grows beyond module scope (word problem is undecidable in general) | 3 | 3 | 9 | Scope statement fixes the boundary: declared commutativity conditions only; three-valued answers keep claims honest | Open |
| R-07 | Prototype not screen-reader-accessible, undermining the project's own claim | 2 | 5 | 10 | Accessibility is a Definition-of-Done item for every interface increment, not a final polish | Open |
| R-08 | Evidence claims rest on tool-synthesised summaries; full reads fail to confirm them | 2 | 4 | 8 | Verification-priority reads scheduled (PB-02); claims downgraded or rephrased immediately if not confirmed | Open |
| R-09 | Landing-page domain/hosting cost or setup delays B8 | 2 | 2 | 4 | Starter page is deploy-ready; domain registration is a single deliberate errand | Open |
| R-10 | Board/Git portfolio drift out of sync (board says one thing, Git another) | 2 | 3 | 6 | Commit messages reference PB IDs; board updated in the same session as commits | Open |
| R-11 | GitHub account locked out (2FA SMS not delivered to Sri Lanka; recovery codes misplaced) | 3 | 3 | 9 | Recovery ticket filed with GitHub support; until restored: local-first repo (DEC-008) with daily cloud-drive backup; board kept in docs/board.md and imported to GitHub Projects on restore | Open — 2026-11-17 |
