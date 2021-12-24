
from turtle import Turtle,Screen

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width= 800 , height= 600)
my_screen.title("The Pong Game")

# creting 1st paddle

y_position_1 = [-40,-20,0,20,40]
for i in range(0,5):
    paddle_1 = Turtle()
    paddle_1.shape("square")
    paddle_1.color("white")
    paddle_1.penup()
    paddle_1.goto(x = 370, y= y_position_1[i])

# creting 2nd paddle

y_position_1 = [-40,-20,0,20,40]
for j in range(0,5):
    paddle_2 = Turtle()
    paddle_2.shape("square")
    paddle_2.color("white")
    paddle_2.penup()
    paddle_2.goto(x = -370, y= y_position_1[j])


my_screen.exitonclick()
