from turtle import Turtle


class Ball(Turtle):
    """Initialize the ball object"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        """Set the ball in movement"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Make the ball bounce against a wall"""
        self.y_move *= -1

    def paddle_bounce(self):
        """Make the ball bounce against a paddle and increase its speed"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Bring the ball back to the center and reset its speed"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()