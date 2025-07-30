from turtle import Turtle


class SnakeScoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, "center", ("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("The game is over ", False, "center", ("Arial", 24, "normal"))

    def inrease_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()