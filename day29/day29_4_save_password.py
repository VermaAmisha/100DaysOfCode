from tkinter import *

from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message="Please make sure you haven't left any field empty!")

    else:
    # Message box module to check if the user wants to proceed
        is_ok = messagebox.askokcancel(title= website , message = f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it OK to save ?")

        if is_ok:
            with open("day29_password_file.txt" , "a") as password_file:
                password_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0 , END)
                password_entry.delete(0 , END)

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
website_entry.focus()

email_entry = Entry(width = 45)
email_entry.grid(row = 2, column = 1 , columnspan = 2)
email_entry.insert(0, "amishaverma@gmail.com")

password_entry = Entry(width = 27)
# # To show "*" instead of actual password use show= "*"
# password_entry = Entry(width = 27 , show= "*")
password_entry.grid(row = 3, column = 1)


# Buttons
password_button = Button(text = "Generate Password")
password_button.grid(row = 3 , column = 2)

add_button = Button(text= "Add" , width = 38 ,command=save)
add_button.grid(row = 4 , column = 1 , columnspan = 2)

# canvas.pack()
window.mainloop()
