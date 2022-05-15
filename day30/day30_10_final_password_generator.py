from tkinter import *
from tkinter import messagebox
from random import randint , choice , shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """ A function to generate password"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    # To automatically copy the generated password
    pyperclip.copy(password)

    print(f"Your password is: {password}")



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """ A function to save the details mentioned"""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
           "email" : email,
           "password" : password,
        }
        
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message="Please check if all the details are filled!")

    else:
    # Message box module to check if the user wants to proceed
        # is_ok = messagebox.askokcancel(title= website , message = f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it OK to save ?")
        # if is_ok:
        try:
            with open("day29_password_file.json" , "r") as password_file:
                # json.dump(new_data, password_file, indent=4)

                # Reading old data
                data = json.load(password_file)
                # print(data)
        except FileNotFoundError:
            with open("day29_password_file.json", "w") as password_file:
                json.dump(new_data, password_file , indent = 4)

        else:
            # Updating old data to new data 
            data.update(new_data)

            with open("day29_password_file.json" , "w") as password_file:
                # Saving updated data
                json.dump(data, password_file, indent=4)
        finally:
            # password_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0 , END)
            password_entry.delete(0 , END)

def find_password():
    """ A function to find the password for the saved website details"""

    website = website_entry.get()
    try:
        with open("day29_password_file.json") as password_file:
            data = json.load(password_file)
            # print(data)

    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No data file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title = "Error" , message = f"No details for {website} exists.")
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
website_entry = Entry(width= 27)
website_entry.grid(row = 1 , column = 1)
website_entry.focus()

email_entry = Entry(width = 45)
email_entry.grid(row = 2, column = 1 , columnspan = 2)
email_entry.insert(0, "amishaverma@gmail.com")

password_entry = Entry(width = 27)
# # To show "*" instead of actual password use show= "*"
# password_entry = Entry(width = 27 , show= "*")

password_entry.grid(row = 3, column = 1)

# Buttons
search_button = Button(text = "Search" , width = 13, command = find_password )
search_button.grid(row = 1 , column = 2)

generate_password_button = Button(text = "Generate Password" , width = 14, command = generate_password)
generate_password_button.grid(row = 3 , column = 2)

add_button = Button(text= "Add" , width = 38 ,command=save)
add_button.grid(row = 4 , column = 1 , columnspan = 2)

# canvas.pack()
window.mainloop()
