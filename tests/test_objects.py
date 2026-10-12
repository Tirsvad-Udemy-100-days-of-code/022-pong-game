"""Tests of the turtle objects; skipped when no display is available."""

import pytest

import constants


@pytest.fixture(scope="module")
def screen():
    turtle = pytest.importorskip("turtle")
    tkinter = pytest.importorskip("tkinter")
    try:
        screen = turtle.Screen()
    except tkinter.TclError as error:
        pytest.skip(f"no usable display: {error}")
    screen.tracer(0)
    yield screen
    screen.bye()


def test_paddle_moves_by_step(screen) -> None:
    from paddle import Paddle

    paddle = Paddle(constants.RIGHT_PADDLE_POSITION)
    paddle.go_up()
    assert paddle.ycor() == constants.PADDLE_STEP
    paddle.go_down()
    paddle.go_down()
    assert paddle.ycor() == -constants.PADDLE_STEP


def test_ball_bounces_and_resets(screen) -> None:
    from ball import Ball

    ball = Ball()
    ball.move()
    assert (ball.xcor(), ball.ycor()) == (constants.BALL_STEP, constants.BALL_STEP)
    ball.bounce_y()
    assert ball.y_move == -constants.BALL_STEP
    ball.bounce_x()
    assert ball.x_move == -constants.BALL_STEP
    assert ball.move_speed < constants.BALL_START_SPEED
    ball.reset_position()
    assert (ball.xcor(), ball.ycor()) == (0, 0)
    assert ball.move_speed == constants.BALL_START_SPEED
    assert ball.x_move == constants.BALL_STEP


def test_scoreboard_counts_points(screen) -> None:
    from scoreboard import Scoreboard

    scoreboard = Scoreboard()
    scoreboard.l_point()
    scoreboard.r_point()
    scoreboard.r_point()
    assert (scoreboard.l_score, scoreboard.r_score) == (1, 2)
