"""Tests of the pure game rules (no display needed)."""

import pytest

import constants
import rules


@pytest.mark.parametrize(
    ("y_position", "expected"),
    [(0, False), (280, False), (281, True), (-281, True), (-280, False)],
)
def test_hits_wall_at_limit(y_position: float, expected: bool) -> None:
    assert rules.hits_wall(y_position) is expected


def test_hits_paddle_right_when_close_and_past_line() -> None:
    assert rules.hits_paddle(40, 330, towards_right=True)


def test_hits_paddle_right_not_when_far() -> None:
    assert not rules.hits_paddle(60, 330, towards_right=True)


def test_hits_paddle_right_not_before_line() -> None:
    assert not rules.hits_paddle(40, 300, towards_right=True)


def test_hits_paddle_left_when_close_and_past_line() -> None:
    assert rules.hits_paddle(40, -330, towards_right=False)


def test_hits_paddle_left_not_on_right_side() -> None:
    assert not rules.hits_paddle(40, 330, towards_right=False)


def test_missed_by_right_beyond_edge() -> None:
    assert rules.missed_by_right(381)
    assert not rules.missed_by_right(380)


def test_missed_by_left_beyond_edge() -> None:
    assert rules.missed_by_left(-381)
    assert not rules.missed_by_left(-380)


def test_faster_shortens_pause() -> None:
    assert rules.faster(0.1) == pytest.approx(0.1 * constants.BALL_SPEEDUP_FACTOR)


def test_screen_constants_match_assignment() -> None:
    assert (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT) == (800, 600)
    assert constants.SCREEN_TITLE == "Pong"
