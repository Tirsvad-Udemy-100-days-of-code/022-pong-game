"""@file scoreboard.py
@brief The Scoreboard class.
"""

from turtle import Turtle

from constants import OBJECT_COLOR, SCORE_FONT, SCORE_X, SCORE_Y


class Scoreboard(Turtle):
    """@brief Shows the score of the left and right player."""

    def __init__(self) -> None:
        """@brief Create the scoreboard with both scores at zero."""
        super().__init__()
        self.color(OBJECT_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score: int = 0
        self.r_score: int = 0
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """@brief Redraw both scores."""
        self.clear()
        self.goto(-SCORE_X, SCORE_Y)
        self.write(self.l_score, align="center", font=SCORE_FONT)
        self.goto(SCORE_X, SCORE_Y)
        self.write(self.r_score, align="center", font=SCORE_FONT)

    def l_point(self) -> None:
        """@brief Give the left player a point."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self) -> None:
        """@brief Give the right player a point."""
        self.r_score += 1
        self.update_scoreboard()
