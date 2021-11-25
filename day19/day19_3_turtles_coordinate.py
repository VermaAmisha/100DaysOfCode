
from turtle import *

my_screen = Screen()
my_screen.setup(width=500,height=400)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

tammy = Turtle()
tammy.shape("turtle")
tammy.color("pink")
tammy.penup()
tammy.goto(x= -230, y= 100)
tammy.pendown()

temmy = Turtle()
temmy.shape("turtle")
tammy.color("blue")
temmy.penup()
temmy.goto(x= -230, y= 50)
temmy.pendown()

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.penup()
timmy.goto(x= -230, y= 0)
timmy.pendown()

tommy = Turtle()
tommy.shape("turtle")
tammy.color("yellow")
tommy.penup()
tommy.goto(x= -230, y= -50)
tommy.pendown()

tummy = Turtle()
tummy.shape("turtle")
tammy.color("purple")
tummy.penup()
tummy.goto(x= -230, y= -100)
tummy.pendown()

my_screen.exitonclick()

# this can also be done by the following way

# from turtle import *

# my_screen = Screen()
# my_screen.setup(width=500,height=400)

# user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)

# colors = ["pink", "blue", "green", "yellow", "purple"]
# y_position = [100, 50, 0, -50, -100]

# for i in range(0, 5):
#     timmy = Turtle(shape= "turtle")
#     timmy.color(colors[i])
#     timmy.penup()
#     timmy.goto(x = -230, y = y_position[i])

# my_screen.exitonclick()
