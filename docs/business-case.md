# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-001], [MIL-002] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [0a05352] |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted with a Go (RC-001) | [0a05352] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 4, success criterion 5, a scope item, a constraint exception, an assumption and a risk for the baseline milestone MIL-002; set the domain to education; reviewed in autonomous mode, not independent | [ed10d29] |

---

## Executive Summary

Build the classic Pong arcade game in Python as the Day 22 assignment of Udemy's
"100 Days of Code: The Complete Python Pro Bootcamp". The result is a small,
readable, runnable repository that course participants can compare with their
own solutions and GitHub visitors can browse for ideas. A second milestone, [MIL-002], later brought the finished project to the baseline of the framework.

## Methodological and Standards Foundation

ISO/IEC 25010:2023 quality characteristics and the SQA/QC framework in
`framework/`. Code follows the `coding-conventions` skill (Python).

## Problem Statement

The course assignment needs a finished, documented Pong implementation that
others can run and read. Without a structured repository the solution is a
loose set of scripts that is hard to share, run or verify.

## Business Opportunity

A reusable reference solution for the course community, and a portfolio piece
that shows planned, tested and documented work.

## Objectives

1. Deliver a playable two-player Pong game using only the Python standard library (`turtle`).
2. Keep the code structured as the assignment describes: `Paddle`, `Ball` and `Scoreboard` classes and a main game loop.
3. Provide tests, a README with run instructions and generated source documentation.
4. Bring the finished project to the common baseline of the framework: the adopted framework release, a wiki in English, Danish and Malay, the README in the framework template, complete licence metadata, a traceability matrix and review records ([MIL-002]).

## Scope

### In Scope

- Game screen (800x600, black, titled "Pong"), two paddles, ball movement, wall and paddle bounces, out-of-bounds reset, scoreboard, ball speed-up and speed reset.
- Constants in `constants.py`, Doxygen comments and a `Doxyfile`.
- `pyproject.toml`, `.gitignore`, README, pytest tests, a CI workflow.
- Repository description and topics on the git host.
- The baseline milestone [MIL-002]: framework release, wiki in English, Danish and Malay, README in the framework template, licence metadata, traceability matrix and review records. It changes no behaviour of the game.

### Out of Scope

- Sound, menus, AI opponent, network play, packaging for PyPI.
- Runtime dependencies beyond the standard library.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-002].

## Expected Benefits

### Tangible Benefits

- A runnable game and a test suite that others can reuse.

### Intangible Benefits

- Practice in object-oriented design and in working plan-first with reviews.

## Strategic Alignment

Supports the personal learning goal of completing the 100 Days of Code course
with a process-driven repository.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Game is playable by two players | Window opens; both paddles move; scores update | Manual run following the README |
| 2 | Tests pass | All pytest tests green | `python -m pytest` |
| 3 | No runtime dependencies | `dependencies = []` in `pyproject.toml` | Inspection |
| 4 | Repository is discoverable | Description and topics set | Inspection on the git host |
| 5 | The baseline milestone is done (objective 4) | Wiki pages in 3 languages, `framework/scripts/check-readme.sh` exits with code 0, 100 % of the continuous integration (CI) checks of the pull request of [MIL-002] pass | Files in `docs/wiki/`, the script exit code and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `turtle` needs Tk, absent on some Linux installs | Game does not start | README documents installing `python3-tk` |
| Game loop is hard to unit-test | Low test coverage | Keep logic in classes with no `Screen` dependency where possible |
| The documents of the baseline milestone [MIL-002] are reviewed by an AI stand-in for S01 | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |

## Assumptions

- Python 3.13 or newer with Tk is available on the player's machine.
- The baseline milestone [MIL-002] is finished within one week of its own start, 2026-11-15, by 2026-11-22. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.

## Constraints

- Python 3.13+, `venv`, `pytest`, folders `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed.
- The baseline milestone [MIL-002] is the exception to the plan-first rule of one reviewer: S01 has authorised the assistant to commit, push, open the pull request and merge it in autonomous mode.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| A few hours of the Product Owner's time | Shareable reference solution and portfolio piece |

The assessment is qualitative on purpose: no money is spent and the benefits (learning, sharing) have no market value to measure.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment; owns, builds and reviews it |
| S02 | Readable, runnable code to compare with their own |
| S03 | Clear description, topics and README for browsing |

## Recommendation

Proceed — small scope, no cost, and a clear learning and sharing benefit.

---

[0a05352]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/commit/0a0535278c3495c997b5cf36fb52f5573bfe0b35
[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[MIL-001]: ./milestones/mil-001-pong-game.md
[MIL-002]: ./milestones/mil-002-framework-baseline.md
[ed10d29]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/commit/ed10d294e5b938faf2ef44db16549180787d2187
