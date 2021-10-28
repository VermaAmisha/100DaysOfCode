
# This will use positional argument

def greet(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet("Jamshedpur", "Amisha")

# The computer will check the position of the values and will then set them to the variables position-wise.
# Here "Jamshedpur" will be set to variable "name" and "Amisha" will be set to variable "location"

print("*******************************")

# This will use Keyword Argument.
# By specifying the value of each variable the values allotted to them will get printed in their assigned places
# In this case wherever the value be lolcated it will be set to the variable where it should be.

def greet(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet(location="Jamshedpur", name= "Amisha")

