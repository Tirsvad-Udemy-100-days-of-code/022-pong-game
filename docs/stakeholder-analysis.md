# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted with a Go (RC-002) | pending |

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

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Complete, tested game | Functionality, Reliability |
| S02 | Readable code, assignment names, run instructions | Usability, Supportability |
| S03 | Description, topics, README, no runtime dependencies | Usability, Implementation |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Reviewed artifacts and code | All |
| S02 | README | At release | Run instructions | MIL-001 |
| S03 | Repository page | At release | Description, topics, README | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| None identified | | |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Complete, tested game | Objectives 1 and 3 |
| S02 | Readable code with assignment names | Objective 2 |
| S03 | Discoverable, dependency-free repository | Objectives 1 and 3 |

## Sign-Off

Accepted by S01's stand-in after RC-002 (Go).

---

[BC-001]: ./business-case.md
