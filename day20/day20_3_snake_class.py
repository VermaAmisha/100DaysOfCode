from turtle import *

X_POSITION = [0,-20,-40, ]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.timmy = []
        self.create_snake()   # method
        self.head = self.timmy[0]

# create snake
    def create_snake(self):
        for i in range(0, 3):
            self.add_snake(i)
            

    def add_snake(self,i):
        new_timmy = Turtle(shape= "square")   # timmy = Turtle("square")
        new_timmy.color("white")
        new_timmy.penup()
        new_timmy.goto(x = X_POSITION[i] , y = 0)
        self.timmy.append(new_timmy)

    def extend(self):
        self.add_snake(self.timmy[-1].i())


    def move(self):
        for s_num in range(len(self.timmy)-1, 0, -1):    # in reverse order 
            new_x = self.timmy[s_num - 1].xcor()
            new_y = self.timmy[s_num - 1].ycor()
            self.timmy[s_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)
