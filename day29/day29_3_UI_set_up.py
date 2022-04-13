from tkinter import *

# ---------------------------- UI SETUP ------------------------------- #

# Create window

window = Tk()
window.title("Password Generator")
window.config(padx = 20 , pady = 20 , bg = "white")

# Create canvas
canvas = Canvas(width = 200, height= 200 , bg = "white" , highlightthickness= 0)

canvas.grid(row = 0 , column = 1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row = 1 , column = 0 )

email_label = Label(text="Email/Username: ")
email_label.grid(row = 2 , column = 0)

password_label = Label(text="Password: ")
password_label.grid(row = 3, column = 0)

# Entries
website_entry = Entry(width= 45)
website_entry.grid(row = 1 , column = 1 , columnspan = 2)

email_entry = Entry(width = 45)
email_entry.grid(row = 2, column = 1 , columnspan = 2)

password_entry = Entry(width = 27)
password_entry.grid(row = 3, column = 1)

# Buttons
password_button = Button(text = "Generate Password")
password_button.grid(row = 3 , column = 2)

add_button = Button(text= "Add" , width = 38)
add_button.grid(row = 4 , column = 1 , columnspan = 2)

# canvas.pack()
window.mainloop()
