from tkinter import *
from tkinter import PhotoImage


BACKGROUND_COLOR = "#B1DDC6"

# Creating Window

window = Tk()
window.title("Flash Card")
window.config(padx = 50 , pady = 50 , bg = BACKGROUND_COLOR)


canvas = Canvas(width = 800, height= 526 , bg = "white" , highlightthickness= 0)
card_front_img = PhotoImage(file = "day31/card_front.png")

canvas.grid(row = 0 , column = 0, columnspan = 2)
canvas.config(bg= BACKGROUND_COLOR)

canvas.create_image(400 , 263 , image = card_front_img)

french_title = canvas.create_text(400 , 150 , text = "French" , font = ("Arial" , 30 , "bold"))
french_word = canvas.create_text(400 , 263, text = "word", font = ("Arial" , 60 , "bold"))

wrong_image = PhotoImage(file = "day31/wrong.png")
wrong_button = Button(image = wrong_image , highlightthickness= 0)
wrong_button.grid(row = 1 , column = 0)

right_image = PhotoImage(file = "day31/right.png")
right_button = Button(image = right_image , highlightthickness= 0)
right_button.grid(row = 1 , column = 1)




window.mainloop()
