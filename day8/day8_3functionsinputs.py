# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello")
    print("Amisha")
    print("Verma")

greet()

# def greet()- these functions has brackets which can be filled with some data ,i.e., a variable 

def greet(name):
    print(f"Hello {name} !")
    print(f"How are you {name}? ")
    print("Isn't it a beautiful day? ")

greet("Amisha")

# This can also be written as follows

def greet(name):
    print(f"Hello {name} !\nHow are you {name}?\nIsn't it a beautiful day? ")

greet("Amisha")

# Here the variable "name" is set to a piece of data "Amisha"
# In programming language this variable is called "Parameter" and data input to it as "Argument"

# Parameter is the name of the data which is passed in and Argument is the value given to the variable/Parameter
