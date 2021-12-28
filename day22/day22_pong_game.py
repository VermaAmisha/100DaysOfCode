
from turtle import Turtle,Screen, xcor
from day22_4_animating_paddles import Paddle
from day22_5_ball_class import Ball
from day22_6_score_board import Scoreboard
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width= 800 , height= 600)
my_screen.title("The Pong Game")
my_screen.tracer(0)

paddle_1 = Paddle((370,0))
paddle_2 = Paddle((-370,0))
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(paddle_1.go_up,"Up")
my_screen.onkey(paddle_1.go_down,"Down")
my_screen.onkey(paddle_2.go_up,"w")
my_screen.onkey(paddle_2.go_down,"s")


game_on = True
while game_on:
    time.sleep(0.1)
# the ball is moving too fast , so to make it move slow sleep method is used
    my_screen.update()
# because of tracer() , no animation(no turtle) is seen and to avoid this- while loop is used to update the screen everytime
    ball.move()

# Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
# needs to bounce
        ball.bounce_y()

# Detect collision with paddle_1
    if ball.distance(paddle_1) < 50 and ball.xcor() > 340 or ball.distance(paddle_2) < 50 and ball.xcor() < -340:
        ball.bounce_x()

# Detect when the ball collides the right wall / paddle_1 misses the ball
    if ball.xcor() > 380:
        ball.reset_position() 
        scoreboard.p2_point()

# Detect when the ball collides the left wall / paddle_2 misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p1_point()
# they both are written separately so as to keep a record of their scores separately

my_screen.exitonclick()
