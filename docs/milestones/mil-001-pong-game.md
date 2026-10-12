# Pong game delivery

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [0a05352] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted with a Go (RC-003) | [0a05352] |

---

## Purpose

Decide whether the Pong game is complete enough to share with S02 and S03.

## Deliverable

A playable two-player Pong game in `src/` with tests in `tests/`, source documentation, a README and a repository with description and topics.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes | All tests pass | Any test fails |
| 2 | `python src/main.py` opens an 800x600 window titled "Pong" with two controllable paddles, a bouncing ball and a scoreboard | Observed | Missing any element |
| 3 | `pyproject.toml` lists no runtime dependencies | None listed | Any listed |
| 4 | `doxygen Doxyfile` builds without warnings | No warnings | Warnings |
| 5 | Repository description and topics are set | Both set | Either missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001 | Scope and objectives |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1: playable game | [BC-001] |
| Objective 2: assignment structure | [BC-001] |
| Objective 3: tests, README, documentation | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-20 — one week from the start; no external deadline in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Project scaffolding | Add `pyproject.toml` (Python 3.13+, pytest dev extra, no runtime dependencies), Python `.gitignore` (including `.env` and `.venv`), `Doxyfile`, `src/`, `tests/` layout and `constants.py`. | No | |
| 2 | Game screen | Create `main.py` with an 800x600 black `Screen` titled "Pong" that stays open until clicked. | No | |
| 3 | Paddle class and second paddle | Add `Paddle` (subclass of `Turtle`) with `go_up`/`go_down`; right paddle on Up/Down, left paddle on W/S; tracer off. | No | |
| 4 | Ball class and movement | Add `Ball` (subclass of `Turtle`) with `move()`, a sleep per frame, starting at (0, 0). | No | |
| 5 | Wall bounce | Reverse the ball's Y direction at the top and bottom walls (`bounce_y`). | No | |
| 6 | Paddle collision | Detect ball/paddle contact by distance and X position and reverse the X direction (`bounce_x`). | No | |
| 7 | Out of bounds and reset | Reset the ball to the centre and reverse direction when a paddle misses (`reset_position`). | No | |
| 8 | Scoreboard and speed | Add `Scoreboard` (left/right score, `l_point`, `r_point`), speed up the ball on each paddle hit and reset the speed on a miss. | No | |
| 9 | README, tests and CI | Write `README.md` from the Project's template, pytest tests for logic that does not need a display, and a CI workflow that runs the tests. | No | |
| 10 | Repository description and topics | Set the description and topics on the git host repository, using the token from `.env` (never imported into the project). | No | |

---

[BC-001]: ../business-case.md
[0a05352]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/commit/0a0535278c3495c997b5cf36fb52f5573bfe0b35
