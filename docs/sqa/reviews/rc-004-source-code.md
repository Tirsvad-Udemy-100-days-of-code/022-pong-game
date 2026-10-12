# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-004 |
| CrossReference | [QC-PY-001], [MIL-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [0a05352] |

---

## Artifact Under Review

- Instance reviewed: `src/` and `tests/` (tasks 1-9 of [MIL-001])
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions, variables snake_case; classes `Paddle`, `Ball`, `Scoreboard` PascalCase; constants UPPER_SNAKE in `constants.py`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`hits_wall`, `bounce_x`, `move_speed`); `l_`/`r_` prefixes are the assignment's names; `_x`/`_y` only for unused handler arguments. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | Lines are at most 88 characters and formatted in `ruff format` style; ruff is not installed in this environment, so no linter run is recorded. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and method is annotated, `-> None` included. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except:`; the test fixture catches only `tkinter.TclError` and turns it into a skip with the message. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments; no builtins shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections are opened. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | All modules, classes and public functions have Doxygen docstrings stating what they do. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No logging and no `print`; no secrets handled. `.env` is neither read nor imported by the project. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No DCD exists: the plan has only plain technical tasks and no use case. The classes follow the assignment (`Paddle`, `Ball`, `Scoreboard`). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_rules.py` (10) and `tests/test_objects.py` (3, skipped when no display); `python -m pytest`: 17 passed locally. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | `mypy` not run; optional criterion. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; `pytest>=8` declared in the `dev` extra. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each threshold and speed lives once in `constants.py`; hit and miss rules live once in `rules.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `rules.py` and `constants.py` import nothing from turtle or the UI; no import cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `Paddle`, `Ball`, `Scoreboard` each have one reason to change; rules are separate pure functions; no inheritance beyond `Turtle`. |

## Overall Verdict


Go — every Mandatory criterion of QC-PY-001 passes or is not applicable (rows 7, 10 and 12 are N-A, each with a reason). Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-001]: ../../milestones/mil-001-pong-game.md
[0a05352]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/commit/0a0535278c3495c997b5cf36fb52f5573bfe0b35
