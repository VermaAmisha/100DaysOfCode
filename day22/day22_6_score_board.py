
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0    # p1 = player 1 and p2 = player 2
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()             # since the increasing point overlaps on the previous ones, the previous scores are to be cleared
        self.goto(-100 , 200)
        self.write(self.p1_score, align = "center" , font = ("Courier", 80, "normal") )
        self.goto(100 , 200)
        self.write(self.p2_score, align = "center" , font= ("Courier", 80, "normal"))

    def p2_point(self):
        self.p2_score += 1
        self.update_scoreboard()

    def p1_point(self):
        self.p1_score += 1
        self.update_scoreboard()
