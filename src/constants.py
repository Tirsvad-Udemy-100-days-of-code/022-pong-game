"""@file constants.py
@brief Constants of the Pong game: screen, paddles, ball, scoreboard.
"""

## Window width in pixels.
SCREEN_WIDTH: int = 800
## Window height in pixels.
SCREEN_HEIGHT: int = 600
## Window background colour.
SCREEN_COLOR: str = "black"
## Window title.
SCREEN_TITLE: str = "Pong"

## Colour of paddles, ball and scoreboard.
OBJECT_COLOR: str = "white"

## Starting position of the right paddle.
RIGHT_PADDLE_POSITION: tuple[int, int] = (350, 0)
## Starting position of the left paddle.
LEFT_PADDLE_POSITION: tuple[int, int] = (-350, 0)
## Paddle height stretch factor (20 px base shape -> 100 px).
PADDLE_STRETCH_LENGTH: int = 5
## Paddle width stretch factor (20 px).
PADDLE_STRETCH_WIDTH: int = 1
## Pixels a paddle moves per key press.
PADDLE_STEP: int = 20

## Pixels the ball moves per frame on each axis.
BALL_STEP: int = 10
## Initial pause between frames in seconds.
BALL_START_SPEED: float = 0.1
## Factor applied to the pause after each paddle hit (smaller is faster).
BALL_SPEEDUP_FACTOR: float = 0.9

## Y distance from the centre at which the ball bounces off a wall.
WALL_LIMIT_Y: int = 280
## Ball-to-paddle distance below which a hit is considered.
PADDLE_HIT_DISTANCE: int = 50
## Absolute X position beyond which the ball can touch a paddle.
PADDLE_HIT_X: int = 320
## Absolute X position beyond which the ball is out of bounds.
OUT_OF_BOUNDS_X: int = 380

## Scoreboard font (family, size, style).
SCORE_FONT: tuple[str, int, str] = ("Courier", 80, "normal")
## Scoreboard X offset of each score from the centre.
SCORE_X: int = 100
## Scoreboard Y position.
SCORE_Y: int = 200
