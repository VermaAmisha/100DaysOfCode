
import tkinter

window = tkinter.Tk()

window.title("My First GUI program")
window.minsize(width=500, height=300)

# label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24,"bold"))
my_label.pack()  # the label is at top center until and unless this packer label line of code is not written the albel will not be seen on the window

# my_label.pack(side="left") - the label is moved to left similarly the label can be moved to top,bottom and right
# my_label.pack(expand=True) - in the middle of the window

# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.write()

# my_screen = Screen()
# my_screen.exitonclick()

window.mainloop()
