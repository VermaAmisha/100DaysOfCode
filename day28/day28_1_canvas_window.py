from tkinter import *
# import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# window = tkinter.Tk()
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg="#e2979c")

# create a canvas
# from day28 import Tomatojpg
canvas = Canvas(width=200, height=224, bg= "#e2979c", highlightthickness=0)
# tomato_img = PhotoImage(file="Tomatojpg.jpg")
# canvas.create_image(100, 112,image=tomato_img)
canvas.create_text(100, 112,text= "00:00",fill="blue",font= (FONT_NAME,35,"bold"))

canvas.pack()






window.mainloop()
