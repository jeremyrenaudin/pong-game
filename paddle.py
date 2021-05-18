from turtle import Turtle


class Paddle(Turtle):
    """initialize a paddle object"""
    def __init__(self, starting_position, player_name):
        super().__init__()
        self.player_name = player_name
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)

    def go_up(self):
        """Move the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)