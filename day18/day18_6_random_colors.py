
import turtle as t
import random

timmy = t.Turtle()

timmy.shape("turtle")

t.colormode(255)

def random_colors():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    random_colors = (r, g, b)
    return random_colors

random_colors

directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random_colors())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

