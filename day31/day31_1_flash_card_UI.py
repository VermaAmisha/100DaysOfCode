from tkinter import *
from tkinter import PhotoImage


BACKGROUND_COLOR = "#B1DDC6"

# Creating Window

window = Tk()
window.title("Flash Card")
window.config(padx = 50 , pady = 50)

right_img = PhotoImage(file = "path/to/right.png")
right_button = Button(image = right_img, highlightthickness = 0)

wrong_img = PhotoImage(file = "path/to/wrong.png")
button = Button(image= wrong_img, highlightthickness = 0)

canvas = Canvas(width = 200, height= 200 , bg = "white" , highlightthickness= 0)
canvas.grid(row = 0 , column = 1)


window.mainloop()
