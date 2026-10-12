"""@file rules.py
@brief Pure game rules, free of turtle and display, so they can be tested.
"""

from constants import (
    BALL_SPEEDUP_FACTOR,
    OUT_OF_BOUNDS_X,
    PADDLE_HIT_DISTANCE,
    PADDLE_HIT_X,
    WALL_LIMIT_Y,
)


def hits_wall(y_position: float) -> bool:
    """@brief Tell whether the ball touches the top or bottom wall.

    @param y_position Ball Y coordinate.
    @return True when the ball is beyond the wall limit.
    """
    return abs(y_position) > WALL_LIMIT_Y


def hits_paddle(distance: float, x_position: float, towards_right: bool) -> bool:
    """@brief Tell whether the ball hits the paddle on the side it moves to.

    @param distance Distance between ball and paddle.
    @param x_position Ball X coordinate.
    @param towards_right True when the ball moves to the right.
    @return True when the ball is close enough and past the paddle line.
    """
    if distance >= PADDLE_HIT_DISTANCE:
        return False
    if towards_right:
        return x_position > PADDLE_HIT_X
    return x_position < -PADDLE_HIT_X


def missed_by_right(x_position: float) -> bool:
    """@brief Tell whether the right paddle missed the ball (left player scores).

    @param x_position Ball X coordinate.
    @return True when the ball passed the right edge.
    """
    return x_position > OUT_OF_BOUNDS_X


def missed_by_left(x_position: float) -> bool:
    """@brief Tell whether the left paddle missed the ball (right player scores).

    @param x_position Ball X coordinate.
    @return True when the ball passed the left edge.
    """
    return x_position < -OUT_OF_BOUNDS_X


def faster(move_speed: float) -> float:
    """@brief Return the frame pause after a paddle hit.

    @param move_speed Current pause between frames in seconds.
    @return The shorter pause.
    """
    return move_speed * BALL_SPEEDUP_FACTOR
