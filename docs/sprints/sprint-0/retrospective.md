# Sprint 0 — Retrospective

**Date:** 2026-11-19 (Thursday, sprint close) · **Format:** written, honest, short.

## What worked

- **Offline-first (DEC-008) kept the sprint moving under lockout.** The blocked GitHub lane never blocked work: local repo + `docs/board.md` + daily cloud backup meant ceremonies, commits and evidence accumulated on schedule. The one-sprint-old decision paid for itself within 48 hours.
- **The blind-authoring discipline produced its designed evidence.** Trees 2–5 were written from the problem sources alone, before any converter run, with every judgment call recorded in the author report; the tree-format checker then passed all five trees mechanically. The protocol produced what it was designed to produce — structured trees where the notation spec speaks, recorded flags where it is silent.
- **Commit discipline.** Every artefact references its backlog ID; the git history reads as the process record the working agreement demands.

## What did not work

- **Estimation blind spot on externally-blocked cards.** PB-12 and PB-14 were committed as if they were fully in the sprint's control; both turned out to depend on third parties (GitHub support, supervisor availability). "Committed" should have excluded or partitioned them — the burndown's 3 remaining points are blocked, not unfinished, and the chart can't show that distinction.
- **The stand-up log fell behind.** Days 2–3 of the sprint were written at close rather than daily — the work was real and recorded, but the log's own rule (written the same evening) was broken. The retrospective says so plainly; the log was not backdated to hide it.
- **The notation spec's silence cost adjudication time.** Chain-eq, mat delimiters, group-interior wrapping each required a recorded judgment call that a clearer v0.1 spec would have made unnecessary. Six spec-gap findings (B1–B7) are now on record for v0.2.

## What I learned (feeds CW2 and the design principles)

- A three-valued vocabulary (verified/refuted/unknown) isn't just checker output — it disciplined the *authoring* phase too: the author flagged rather than guessed at the ambiguous constructs, exactly as the methodology demands. The uncertainty discipline scales from the checker down into the methodology itself.
- Pre-registering expectations (trees before any converter) is what makes a comparison evidence rather than noise: the trees record what was expected before any tool ran, so a later mismatch is a finding, not a surprise.
- A single disciplined blind-authoring pass is enough to expose spec silence systematically — the flag list *is* the v0.2 backlog. This generalises: authoring blind against the spec, then reading the flags, is a cheap, effective spec-audit tool.

## Actions carried into Sprint 1 (maximum three — each becomes a board card)

1. **Partition externally-blocked work on the board** — cards that depend on third parties (GitHub restore, supervisor answers) get a "blocked" note and are excluded from "committed" points; burndown then reflects controllable work only. (Process card, 0 pts — working-agreement amendment recorded in the decision log.)
2. **PB-07 parser spike runs against fixture D-01's JSON as its acceptance test** — the hand-encoded nodes/edges/paths JSON becomes the spike's oracle; spike success = parse D-01's tikz-cd and match the JSON's nodes/edges exactly (directions, hook styles, labels included). Ties Sprint 1's biggest technical risk to Sprint 0's artefact.
3. **Spec v0.2 backlog items (B1–B7) enter the product backlog** as a Should card (est. 3) — not authoring work, but the recorded gaps now have a home; prevents v0.2 work drifting untracked.

(Fewer than three is fine. Zero is a red flag worth writing about, not hiding.)
