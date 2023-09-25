from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write("Score: "+ str(self.score), align="center", font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write("Score: "+ str(self.score), align="center", font=("Arial", 24, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
