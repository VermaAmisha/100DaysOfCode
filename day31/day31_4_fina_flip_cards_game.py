from tkinter import *
from tkinter import PhotoImage
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
cards = {}

# # In order to save the new csv file
try:
    data = pandas.read_csv("100DAYSOFCODE/remaining_cards.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("day31/french_words.csv")
    # If the file is not found
    cards = original_data.to_dict(orient = "records")

else:
    cards = data.to_dict(orient = "records")

# data = pandas.read_csv("day31/french_words.csv")
# cards = data.to_dict(orient = "records")

def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(cards)
    
    canvas.itemconfig(card_title , text = "French" , fill = "black")
    canvas.itemconfig(card_word , text = current_card["French"] , fill = "black")
    canvas.itemconfig(canvas_img , image = card_front_img)
    # time.sleep(3)
    # To flip the card after 3 sec or 3000 milli-sec
    flip_timer = window.after(3000, func = english_card)

def english_card():
    canvas.itemconfig(card_title , text = "English" , fill = "white")
    canvas.itemconfig(card_word , text = current_card["English"] , fill = "white")
    # To change the image:
    canvas.itemconfig(canvas_img , image = card_back_image)

def known_word():
    cards.remove(current_card)
    new_data = pandas.DataFrame(cards)
    new_data.to_csv("remaining_cards.csv" , index = False)
    next_card()
    

# Creating Window

window = Tk()
window.title("Flash Card")
window.config(padx = 50 , pady = 50 , bg = BACKGROUND_COLOR)

# To flip the card after 3 sec or 3000 milli-sec
flip_timer = window.after(3000, func = english_card)

canvas = Canvas(width = 800, height= 526 , bg = "white" , highlightthickness= 0)
card_front_img = PhotoImage(file = "day31/card_front.png")
card_back_image = PhotoImage(file = "day31/card_back.png")

canvas.grid(row = 0 , column = 0, columnspan = 2)
canvas.config(bg= BACKGROUND_COLOR)

canvas_img = canvas.create_image(400 , 263 , image = card_front_img)

card_title = canvas.create_text(400 , 150 , text = "" , font = ("Arial" , 30 , "bold"))
card_word = canvas.create_text(400 , 263, text = "", font = ("Arial" , 60 , "bold"))

# canvas.create_image(400 , 263 , image = card_back_image)


# english_title = canvas.create_text(400 , 150 , text = "English" , font = ("Arial" , 30 , "bold"))
# english_word = canvas.create_text(400 , 263 , text = " " , font = ("Arial" , 60 , "bold"))

wrong_image = PhotoImage(file = "day31/wrong.png")
wrong_button = Button(image = wrong_image , highlightthickness= 0 , command= next_card)
wrong_button.grid(row = 1 , column = 0)

right_image = PhotoImage(file = "day31/right.png")
right_button = Button(image = right_image , highlightthickness= 0 , command= known_word)
right_button.grid(row = 1 , column = 1)

next_card()


window.mainloop()
