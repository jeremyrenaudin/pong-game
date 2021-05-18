from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# initialize the screen settings
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# initialize the game
winning_score = int(screen.textinput(title="Winning score", prompt="How many points to win the game?"))
left_name = screen.textinput(title="Player 1", prompt="Enter the name of Player 1:")
right_name = screen.textinput(title="Player 2", prompt="Enter the name of Player 2:")

left_paddle = Paddle((-350, 0), left_name)
right_paddle = Paddle((350, 0), right_name)
ball = Ball()
scoreboard = Scoreboard()

# define keys that the screen will detect and their related actions to execute
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# launch the game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # wait 0.1 second between each screen update (each while loop)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    # check if left player wins the game
    if scoreboard.l_score >= winning_score:
        scoreboard.winner(left_paddle.player_name)
        game_is_on=False

    # check if right player wins the game
    if scoreboard.r_score >= winning_score:
        scoreboard.winner(right_paddle.player_name)
        game_is_on=False


# exit the game on click
screen.exitonclick()
