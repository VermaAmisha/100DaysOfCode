from tkinter import *
from PIL import ImageTk , Image
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

def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# import time

# count = 5
# while True:
#     time.sleep(1)
#     count -= 1 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)    
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
# window = tkinter.Tk()
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg="#e2979c")


# fg = GREEN
# create a canvas
# from day28 import Tomatojpg
canvas = Canvas(width=200, height=224, bg= "#e2979c", highlightthickness=0)
# img = Image.open('C:\Users\AMISHA VERMA\OneDrive\Pictures\\tomato.png')

# tomato_img = ImageTk.PhotoImage(img)
# canvas.create_image(100, 112,image=tomato_img)
timer_text = canvas.create_text(100, 112,text= "00:00",fill="blue",font= (FONT_NAME,35,"bold"))
# check = Checkbutton(width=5, height=2,fg=GREEN)
# check.
# canvas.pack() instead of using pack use grid
canvas.create_text(100, 30, text= "Timer",fill="green", font= (FONT_NAME,40,"bold"))
# start_button = Button(35, 194, text= "Start",fill="white", font= (FONT_NAME,10,"bold"))
# restart_button = Button(175, 194, text= "Restart",fill="white", font= (FONT_NAME,10,"bold"))
canvas.create_text(100, 200, text= " 🗸", fill="green", font= (FONT_NAME,10,"bold"))

canvas.grid()
count_down(5)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
restart_button = Button(text="Restart", highlightthickness=0)
restart_button.grid(column=1, row=2)


window.mainloop()
