
from turtle import Turtle , Screen

timmy = Turtle()

print(timmy)

# call methods

timmy.shape("turtle")   # earlier the canvas was having an arrow instead of a turtle so its shape is changed now
timmy.color("DarkMagenta" , "DarkGreen")   # to change the color of the turtle

# Dashed line by turtle 

for i in range(15):

    timmy.forward(10)   
    timmy.penup()      # To stop drawing for 10 paces
    timmy.forward(10)
    timmy.pendown()      # To again start drawing 

my_screen = Screen()

my_screen.exitonclick()    # instead of our screen just popping ang then disappearing we can stop the screen untill we click on the screen
