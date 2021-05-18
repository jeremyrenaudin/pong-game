from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 60, "normal")
GAMEOVER_FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    """Initialize a score board object"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the score"""
        self.goto(0, 200)
        self.write(f"{self.l_score} - {self.r_score}", align=ALIGNMENT, font=SCORE_FONT)

    def left_point(self):
        """Add 1 point to the left paddle"""
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def right_point(self):
        """Add 1 point to the right paddle"""
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def winner(self, player_name):
        """Declare the winner"""
        self.goto(0, 0)
        self.write(f"{player_name} wins!", align=ALIGNMENT, font=GAMEOVER_FONT)