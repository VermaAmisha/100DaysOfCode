

from turtle import * 

# instead of importing many 

from turtle import Screen
import random

timmy =Turtle()

timmy.shape("turtle")

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g , b)
    return random_color

def triangle():
    for _ in range(3):
        timmy.forward(100)
        timmy.left(120)

for _ in range(18):
    triangle()
    timmy.right(20)
    timmy.color(random_color())
    timmy.speed("fastest")

timmy.left(36)
timmy.penup()
timmy.forward(250)
timmy.pendown()

for _ in range(18):
    triangle()
    timmy.right(20)
    timmy.color(random_color())
    timmy.speed("fastest")

timmy.penup()
timmy.back(500)
timmy.pendown()

for _ in range(18):
    triangle()
    timmy.right(20)
    timmy.color(random_color())
    timmy.speed("fastest")

timmy.left(60)
timmy.penup()
timmy.forward(300)
timmy.pendown()

for _ in range(18):
    triangle()
    timmy.right(20)
    timmy.color(random_color())
    timmy.speed("fastest")

timmy.left(50)
timmy.penup()
timmy.back(550)
timmy.pendown()

for _ in range(18):
    triangle()
    timmy.right(20)
    timmy.color(random_color())
    timmy.speed("fastest")

my_screen = Screen()

my_screen.exitonclick()
