# Oracle — Product Backlog (seed, v0)

Seeded 2026-11-16 from the project records and the two-track plan. Priorities are MoSCoW;
sizes are fibonacci story points (1 focused day of familiar work ≈ 3 points). IDs are
stable: `PB-xx`. Items move between priorities only via the decision log.

## Track A — evidence and needs (research core)

| ID | Story / task | MoSCoW | Pts | Notes |
|---|---|---|---|---|
| PB-01 | As the developer, I want the Round-2 discovery results verified (DOIs re-checked, consequential claims logged) so that the evidence base stays trustworthy. | Must | 5 | On the research round's return; verification pass before any new citation |
| PB-02 | As the developer, I want the 8 verification-priority papers read in full so that load-bearing claims are content-verified, not tool-synthesised. | Must | 8 | Brown 2004; Butler 2016; Spivak 2012; Fleming 2003; Fitzpatrick 2017; Yang 2020; Austin & Sorge 2023; Zhao 2024 |
| PB-03 | As the developer, I want the problem statement promoted from working to final (kill-criteria check) so that B1 rests on a closed decision. | Must | 2 | Procedure already written (Problem Statement v1 §4) |
| PB-04 | As the developer, I want a rich picture and stakeholder onion model drawn once the client-role question is answered. | Should | 3 | Waits on supervisor answer |
| PB-05 | As the developer, I want the fixture set assembled (2–3 real worksheet documents + 2–3 advanced-math documents with commutative diagrams) so evaluation has real inputs. | Must | 5 | Advanced-math component DONE 2026-11-19 (D-01 + D-02, parser-verified); worksheet component split to PB-05b at Sprint 1 retro |
| PB-05b | As the developer, I want 2–3 module worksheets encoded as fixtures with their permission basis recorded so the corpus covers classroom material, not only textbook diagrams. | Must | 3 | Split from PB-05 (Sprint 1 retro action 1: material-logistics cards separate from engineering); Sprint 2 pull |

## Track B — prototype (diagram-as-data)

| ID | Story / task | MoSCoW | Pts | Notes |
|---|---|---|---|---|
| PB-06 | As the developer, I want a hand-encoded pullback square as structured data (nodes, edges, labels, paths) so the smallest end-to-end case exists on paper before any parser. | Must | 2 | The smallest experiment from the records |
| PB-07 | As the developer, I want the smallest tikz-cd parser spike (one real diagram from source to nodes/edges/paths JSON) so the intake lane's feasibility is tested. | Must | 5 | Technology spike; Python working recommendation, tested against a real fixture |
| PB-08 | As a blind reader, I want a spoken overview of a diagram ("5 objects, 7 arrows, 2 declared commuting conditions") so I know what I am about to explore. | Must | 3 | Navigation layer, rung 1 |
| PB-09 | As a blind reader, I want to navigate object-by-object and arrow-by-arrow with path readings ("from A, arrow f to B, arrow g to C") so I can traverse the diagram. | Must | 5 | MathCAT-style node navigation |
| PB-10 | As a blind reader, I want declared commutativity conditions checked mechanically and reported three ways (verified / refuted / unknown) so I can trust what I hear. | Should | 8 | Oracle layer; three-valued answers are settled design (DEC-007) |
| PB-11 | As the developer, I want a structural-fidelity check comparing my structured data against the diagram's mathematical content so rung-1 evaluation exists from the start. | Must | 5 | The non-negotiable evaluation floor |

## Module / process track (portfolio-coupled)

| ID | Story / task | MoSCoW | Pts | Notes |
|---|---|---|---|---|
| PB-12 | Set up task board + Git repository, add supervisor, seed this backlog and the working agreement. | Must | 2 | Sprint 0 item — this is the setup you are doing |
| PB-13 | Run Sprint 0 ceremonies and record all four artefacts (planning, daily log, review, retrospective). | Must | 3 | Sprint 0 item |
| PB-14 | Ask the supervisor the two framing questions (solo adaptations; client role) and log the answers. | Must | 1 | Gates PB-04 and elicitation records |
| PB-15 | Register the project domain and deploy the landing page over HTTPS. | Should | 3 | B8; starter page exists |
| PB-16 | Draft the requirements elicitation record from the published-evidence base (pending client-role answer). | Should | 5 | B3 |
| PB-17 | Draft UML suite + test strategy once requirements stabilise. | Should | 8 | B4; sequenced after elicitation |
| PB-18 | Hi-fi prototype of the reading interface, screen-reader-accessible by construction. | Could | 8 | B5; shape fixed in Sprint 1 |
| PB-19 | Portfolio assembly pass (B7 skeleton, declaration, referencing). | Should | 5 | Late sprint; checklist exists |
| PB-20 | Presentation outline + slides draft. | Could | 3 | B9; due at A4 meeting |
| PB-21 | Grow the expected-structure tree spec to v0.2 (B1 chain-eq type or nesting rule, B2 mat delimiter, B3 row/cell typing, B4 pre-order numbering, B5 ident list, B6 ident-application, B7 `...` marker collision) so the notation's known gaps are closed systematically. | Should | 3 | Spec gaps attested by the author report's judgment calls (fixtures/author-report.md); retro action 3 |

## Not yet scheduled (parking lot)

- Local-language math speech (Sinhala/Tamil) — parked alternative ALT-001.
- Revision-safe annotation workflow — parked alternative ALT-002.
- Ecosystem integration decision (PreTeXt/PreFigure/LaTeXML home) — waits on addendum A6 results.

Sprint 0 pulled: **PB-12, PB-13, PB-14, PB-06** (closed 19 Nov — PB-13, PB-06, PB-14 Done;
PB-12 blocked on R-11). Sprint 1 pulled: **PB-07, PB-05, PB-16** (closed 22 Nov — PB-07 GO,
PB-16 Done interim; PB-05 worksheet component split to PB-05b, carried). Sprint 2 pulls:
**PB-05b, PB-08, PB-09** (planning at sprint close, 2026-11-22).
