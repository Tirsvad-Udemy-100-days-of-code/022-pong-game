**English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

# Pong Game

The classic Pong arcade game for two players with Python turtle graphics: keep the ball in play and score when the other player misses.

![The Pong game window, mid-game, score 3 to 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/022-pong-game/raw/branch/main/docs/images/pong.png)

## What is it?

Day 22 of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*. A black 800 by 600 window titled "Pong" opens with a white paddle on each side and a white ball in the middle. The right player moves the right paddle with the <kbd>Up</kbd> and <kbd>Down</kbd> arrow keys, the left player moves the left paddle with <kbd>W</kbd> and <kbd>S</kbd>. The ball bounces off the top and bottom walls and off a paddle, and each paddle hit makes it faster. When a paddle misses, the other player scores a point, the ball returns to the centre, reverses direction and its speed is reset. The scores are shown at the top: the left player on the left, the right player on the right. A click on the window closes it. The game rules that need no display are in `rules.py`, so they are tested without a window.

## What the exercise teaches

- Setting up the turtle screen and drawing two paddles and a ball as `Turtle` objects
- Moving the ball frame by frame with `tracer`, `update` and `sleep`, and bouncing it off the walls and the paddles
- Writing the classes `Paddle`, `Ball` and `Scoreboard` as subclasses of `Turtle`
- Binding the keys of two players to two paddles
- Detecting a hit by distance and position, speeding the ball up and resetting it when a paddle misses
- Keeping the rules free of the display in `rules.py`, so that they can be tested without a window

## What it does

- Two paddles, one for each player: Up and Down for the right paddle, W and S for the left paddle
- A ball that bounces off the walls and the paddles and speeds up on each paddle hit
- A point for the other player when a paddle misses; the ball returns to the centre and its speed is reset
- A scoreboard with both scores at the top of the window
- No runtime dependencies beyond the Python standard library

## Next

- [Getting Started](Getting-Started)
- [Project Documents](Project-Documents)
