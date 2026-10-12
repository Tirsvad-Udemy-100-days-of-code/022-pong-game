"""@file paddle.py
@brief The Paddle class.
"""

from turtle import Turtle

from constants import (
    OBJECT_COLOR,
    PADDLE_STEP,
    PADDLE_STRETCH_LENGTH,
    PADDLE_STRETCH_WIDTH,
)


class Paddle(Turtle):
    """@brief A vertical paddle moved by two key handlers."""

    def __init__(self, position: tuple[int, int]) -> None:
        """@brief Create a paddle.

        @param position Starting (x, y) position of the paddle.
        """
        super().__init__()
        self.shape("square")
        self.color(OBJECT_COLOR)
        self.shapesize(
            stretch_wid=PADDLE_STRETCH_LENGTH, stretch_len=PADDLE_STRETCH_WIDTH
        )
        self.penup()
        self.goto(position)

    def go_up(self) -> None:
        """@brief Move the paddle up one step."""
        self.goto(self.xcor(), self.ycor() + PADDLE_STEP)

    def go_down(self) -> None:
        """@brief Move the paddle down one step."""
        self.goto(self.xcor(), self.ycor() - PADDLE_STEP)
