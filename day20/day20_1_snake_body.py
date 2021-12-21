
from turtle import *

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")

# t= Turtle()
# t.shape("square")
# t.color("white")
x_position = [-20, 0, 20]    # instead tuples can also be created - [(-20,0), (0,0), (-40,0)]

for i in range(0, 3):
    timmy = Turtle(shape= "square")   # timmy = Turtle("square")
    timmy.color("white")
    timmy.penup()
    timmy.goto(x = x_position[i] , y = 0)



my_screen.exitonclick()
