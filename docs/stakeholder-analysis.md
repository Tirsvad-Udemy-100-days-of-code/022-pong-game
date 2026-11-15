# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-002] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [0a05352] |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted with a Go (RC-002) | [0a05352] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-003 (QC-SA-001 criterion 9), the baseline concern CN-004, the baseline milestone in the communication table and a conflict about the stand-in reviewer; set the domain to education; reviewed in autonomous mode, not independent | [ed10d29] |

---

## Purpose

Identify who the Pong project serves and what each of them needs, using a Power/Interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finishes the assignment with a clean, reviewed result |
| S02 | Udemy coursists | Course participants | Udemy | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, plus README instructions to run it |
| S03 | GitHub viewers | Repository visitors | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

S01 decides scope and accepts every artifact, so power and interest are both
high. S02 and S03 have no say in the project but use its output.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Complete, tested game | Functionality, Reliability |
| CN-002 | S02 | Readable code, assignment names, run instructions | Usability, Supportability |
| CN-003 | S03 | Description, topics, README, no runtime dependencies | Usability, Implementation |
| CN-004 | S01 | The project follows the common baseline of the framework, with a wiki in English, Danish and Malay | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Reviewed artifacts and code | All |
| S02 | README | At release | Run instructions | MIL-001 |
| S03 | Repository page | At release | Description, topics, README | MIL-001 |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | [MIL-002] |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | [MIL-002] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Complete, tested game (CN-001) | Objectives 1 and 3 |
| S02 | Readable code with assignment names (CN-002) | Objective 2 |
| S03 | Discoverable, dependency-free repository (CN-003) | Objectives 1 and 3 |
| S01 | The project follows the common baseline of the framework (CN-004) | Objective 4 |

## Sign-Off

Accepted by S01's stand-in after RC-002 (Go). The changes of the baseline milestone were accepted by the same stand-in after RC-006 (Go).

---

[BC-001]: ./business-case.md
[0a05352]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/commit/0a0535278c3495c997b5cf36fb52f5573bfe0b35
[MIL-002]: ./milestones/mil-002-framework-baseline.md
[ed10d29]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/commit/ed10d294e5b938faf2ef44db16549180787d2187
