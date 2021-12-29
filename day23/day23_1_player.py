from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        self = Turtle()
        self.shape("arrow")
        self.color("black")
        self.penup()
        self. goto(0 , 280)

    def go_up(self):
        new_y = self.ycor() + 2
        self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - 2
        self.goto(new_x,self.ycor())

    def go_right(self):
        new_x = self.xcor() + 2
        self.goto(new_x,self.ycor())
    

