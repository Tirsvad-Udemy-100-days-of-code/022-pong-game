"""@file main.py
@brief Entry point of the Pong game.
"""

import time
from turtle import Screen

import rules
from ball import Ball
from constants import (
    LEFT_PADDLE_POSITION,
    RIGHT_PADDLE_POSITION,
    SCREEN_COLOR,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
)
from paddle import Paddle
from scoreboard import Scoreboard


def main() -> None:
    """@brief Set up the screen and run the game loop until the window is clicked."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_COLOR)
    screen.title(SCREEN_TITLE)
    screen.tracer(0)

    r_paddle = Paddle(RIGHT_PADDLE_POSITION)
    l_paddle = Paddle(LEFT_PADDLE_POSITION)
    ball = Ball()
    scoreboard = Scoreboard()

    is_game_on = True

    def stop_game(_x: float, _y: float) -> None:
        nonlocal is_game_on
        is_game_on = False

    screen.listen()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")
    screen.onclick(stop_game)

    while is_game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if rules.hits_wall(ball.ycor()):
            ball.bounce_y()

        towards_right = ball.x_move > 0
        paddle = r_paddle if towards_right else l_paddle
        if rules.hits_paddle(ball.distance(paddle), ball.xcor(), towards_right):
            ball.bounce_x()

        if rules.missed_by_right(ball.xcor()):
            ball.reset_position()
            scoreboard.l_point()
        elif rules.missed_by_left(ball.xcor()):
            ball.reset_position()
            scoreboard.r_point()

    screen.bye()


if __name__ == "__main__":
    main()
