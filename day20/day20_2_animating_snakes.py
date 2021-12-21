

from turtle import *
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
# my_screen.tracer(0)
# t= Turtle()
# t.shape("square")
# t.color("white")
x_position = [0,-20,-40, ]    # instead tuples can also be created - [ (0,0),(-20,0), (-40,0)]

snake= []

for i in range(0, 3):
    new_timmy = Turtle(shape= "square")   # timmy = Turtle("square")
    new_timmy.color("white")
    new_timmy.penup()
    new_timmy.goto(x = x_position[i] , y = 0)
    
    snake.append(new_timmy)

game_on = True

while game_on:
    my_screen.update()
    time.sleep(0.1)
    # for s in snake:
    #     s.forward(20)
        
    for s_num in range(len(snake)-1, 0, -1):    # in reverse order 
        new_x = snake[s_num - 1].xcor()
        new_y = snake[s_num - 1].ycor()
        snake[s_num].goto(new_x,new_y)
    snake[0].forward(20) 
    snake[0].left(90) 
    
my_screen.exitonclick()
