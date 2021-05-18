# Pong Game
According to [ponggame.org](https://www.ponggame.org), Pong is one of the first computer games that was ever created. Let's develop it using Python and object-oriented programming!

## Rules
This simple "tennis like" game features two paddles and a ball. The goal is to defeat your opponent by being the first one to gain 10 points. A player gets a point once the opponent misses the ball.

In the version that I developed, the players are able to choose the max number of points to win the game, as well as their names.

## How did I break this project down?
I divided the problem of building the Pong game into 11 steps:

1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with walls and bounce
6. Detect collision with paddle and bounce back
7. Detect when a paddle misses the ball
8. Create a scoreboard
9. Increase ball speed after each shot
10. Ask inputs from users like max number of points or players' names
11. Propose to users to play again

## Files
- `main.py`: application that runs the game
- `paddle.py`: package to model the paddles
- `ball.py`: package to model the ball
- `scoreboard.py`: package to initialize a scoreboard

## Keys to play
- Left player (player 1):
    - W: go up
    - S: go down

- Right player (player 2):
    - Up arrow: go up
    - Down arrow: go down
