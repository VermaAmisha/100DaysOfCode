def greet(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet("Amisha", "Jamshedpur")

print("******************")

# This can also be written as follows:

def greet(name, location):
    print(f"Hello {name}\nWhat is it like in {location}?")

greet("Amisha", "Jamshedpur")

# Just by putting a comma "," all the inputs can be separated

print("******************")

# 1st input is set in the 1st variable, 2nd input is set in the 2nd variable, 3rd input is set to the 3rd variable and so on all are set to their own respected places.
# This is called a positional argument as no specific position is not alloted to the input so the computer checks the position to the input and is assinged to respective places
# example:

def greet(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet("Jamshedpur", "Amisha")
