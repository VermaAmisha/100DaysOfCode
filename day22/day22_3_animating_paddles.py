
from turtle import Turtle,Screen

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width= 800 , height= 600)
my_screen.title("The Pong Game")
my_screen.tracer(0)
# used to avoid the animation being seen while the paddle moves to the position

# creating 1st paddle
# def paddle_1():
    # y_position_1 = [-40,-20,0,20,40]
    # for i in range(0,5):
paddle_1 = Turtle()                                 # paddle_1 = Turtle()
paddle_1.shape("square")                            # paddle_1.shape("square")
paddle_1.shapesize(stretch_wid= 5,stretch_len= 1)   # paddle_1.color("white")
paddle_1.color("white")                             # paddle_1.penup()
paddle_1.penup()                                    # paddle_1.speed("fastest")
paddle_1.goto(x = 370, y= 0)                        # paddle_1.goto(x = 370, y= y_position_1[i])

# creting 2nd paddle

# def paddle_2():
#     # y_position_1 = [-40,-20,0,20,40]
#     # for j in range(0,5):
paddle_2 = Turtle()
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid= 5,stretch_len= 1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.speed("fastest")
paddle_2.goto(x = -370, y= 0)

def go_up():
    new_y = paddle_1.ycor() + 20
    paddle_1.goto(paddle_1.xcor(), new_y)
    my_screen.listen()
    my_screen.onkey(go_up,"Up")


def go_down():
    new_y = paddle_1.ycor() - 20
    paddle_1.goto(paddle_1.xcor(), new_y)
    my_screen.listen()
    my_screen.onkey(go_down,"Down")


def go_up_2():
    new_y = paddle_2.ycor + 20
    paddle_2.goto(paddle_2.xcor, y = new_y)
    my_screen.listen()
    my_screen.onkey(key="u",fun=go_up_2)

def go_down_2():
    new_y =  paddle_2.ycor - 20
    paddle_2.goto(paddle_2.xcor(),new_y)
    my_screen.listen()
    my_screen.onkey(key="d",fun=go_down_2)

go_up()
go_down()
go_up_2()
go_down_2()

# paddle_1()
# paddle_2()
game_on = True
while game_on:
    my_screen.update()
# because of tracer() , no animation(no turtle) is seen and to avoid this- while loop is used to update the screen everytime
my_screen.exitonclick()

