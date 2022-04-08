from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# repetition
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    # stop Timer
    window.after_cancel(timer)

    # timer text 00:00
    canvas.itemconfig(timer_text, text = "00:00")

    # title label "Timer"
    title_label.config(text = "Timer")

    # reset check_marks
    check_marks.config(text = "")
    
    # to restart from the beginning not to continue after where it stopped
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # 1st. 25 min work
    # 2nd. 5 min break
    # 3rd. 25 min work
    # 4th. 5 min break
    # 5th. 25 min work
    # 6th. 5 min break
    # 7th. 25 min work
    # 8th. 20 min break
    
    global title_label

    # if it's the 2nd/4th/6th rep:
    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text = "Break", fg= PINK)

    # if it's the 8th rep:
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "Break", fg= RED)


    # if it's the 1st/3rd/5th/7th rep:
    else: 
        count_down(work_sec)
        title_label.config(text = "Work", fg= GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
#  to count time in 00:00 format
    count_min = math.floor(count/60)
    count_sec = count % 60

# using dynamic typing to change the data type of count_sec = 0 to 00

    # if count_sec == 0:
    #     count_sec = '00'

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text , text =f"{count_min} : {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down , count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text = marks)
# ---------------------------- UI SETUP ------------------------------- #
# window = tkinter.Tk()

window = Tk()
window.title("Tomato")
window.config(padx= 100 , pady = 50, bg = YELLOW)


title_label = Label(text = "Timer", fg= GREEN, bg = YELLOW, font = (FONT_NAME , 40 , "bold"))
title_label.grid(column = 0, row = 0)


# # create a canvas as the size of the tomato
canvas = Canvas(width = 200, height = 224 , bg = YELLOW , highlightthickness= 0)

# tomato_img = PhotoImage(file="red_tomato.jpg")

# # Add Image to the center (x , y axes)
# canvas.create_image(92, 100, image= tomato_img)

# Add text to canvas
timer_text = canvas.create_text(100 , 112 , text = "00:00" , font = (FONT_NAME, 35, "bold"))

canvas.grid()

start_button = Button(text = 'Start', command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = 'Reset', command = reset_timer)
reset_button.grid(column = 1, row = 2)

check_marks = Label(text = "", fg = GREEN , bg = YELLOW)
check_marks.grid(column = 0 , row = 3)


# canvas.pack()



window.mainloop()
