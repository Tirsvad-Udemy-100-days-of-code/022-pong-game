# Traceability Matrix: Pong Game

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the review records of the baseline (autonomous, not independent) | [ed10d29] |

---

## Purpose

Tracks backward and forward links between the artifact instances of Pong Game so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002] | [RC-005] (Go, re-review of the whole document), [RC-001] (Go, the first review) |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-006] (Go, re-review of the whole document), [RC-002] (Go, the first review) |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002] | [RC-007] (Go, review of the whole document; the plan had no review record before) |
| [MIL-001] | Milestone / Gateway | en | education | [BC-001], [PP-001] | [MIL-002] | [RC-008] (Go, re-review after the metadata change), [RC-003] (Go, the first review) |
| [MIL-002] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-001] | - | [RC-009] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001] | - | [RC-010] (Go-with-conditions) |
| Python code of MIL-001 (`src/`, `tests/`) | Python Source Code (PY) | - | - | [MIL-001] | - | [RC-004] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-001] (criteria 1 and 2) | - | - | Covered |
| CN-002 | [MIL-001] (criteria 2 and 4), [MIL-002] (criterion 4) | - | - | Covered |
| CN-003 | [MIL-001] (criteria 3 and 5) | - | - | Covered |
| CN-004 | [MIL-002] (criteria 1, 3, 4 and 5) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- No view, design or test-plan artifact exists (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of the milestones. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it yet.
- The source code is reviewed in [RC-004] and not again in [MIL-002], which changes no source file. These records and this matrix have no QC checklist for themselves and are not reviewed.
- The domain of every artifact is `education` since [MIL-002]; the earlier review records state the former domain `it` as it was at the time.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-pong-game.md
[MIL-002]: ../milestones/mil-002-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001-pong-game.md
[RC-004]: ./reviews/rc-004-source-code.md
[RC-005]: ./reviews/rc-005-business-case-baseline.md
[RC-006]: ./reviews/rc-006-stakeholder-analysis-baseline.md
[RC-007]: ./reviews/rc-007-project-plan-baseline.md
[RC-008]: ./reviews/rc-008-milestone-001-baseline.md
[RC-009]: ./reviews/rc-009-milestone-002.md
[RC-010]: ./reviews/rc-010-wiki.md
[ed10d29]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/commit/ed10d294e5b938faf2ef44db16549180787d2187
