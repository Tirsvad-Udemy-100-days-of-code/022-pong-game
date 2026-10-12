"""@file ball.py
@brief The Ball class.
"""

from turtle import Turtle

import rules
from constants import BALL_START_SPEED, BALL_STEP, OBJECT_COLOR


class Ball(Turtle):
    """@brief The ball: moves, bounces and speeds up."""

    def __init__(self) -> None:
        """@brief Create the ball at the centre of the screen."""
        super().__init__()
        self.shape("circle")
        self.color(OBJECT_COLOR)
        self.penup()
        self.x_move: int = BALL_STEP
        self.y_move: int = BALL_STEP
        self.move_speed: float = BALL_START_SPEED

    def move(self) -> None:
        """@brief Advance the ball one step on both axes."""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self) -> None:
        """@brief Reverse the vertical direction (wall bounce)."""
        self.y_move *= -1

    def bounce_x(self) -> None:
        """@brief Reverse the horizontal direction and speed up (paddle bounce)."""
        self.x_move *= -1
        self.move_speed = rules.faster(self.move_speed)

    def reset_position(self) -> None:
        """@brief Return to the centre, reverse direction and reset the speed."""
        self.goto(0, 0)
        self.move_speed = BALL_START_SPEED
        self.x_move *= -1
