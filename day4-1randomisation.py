# To randomise any number a random number is imported.

import random

random_integer = random.randint(1,10)
# In integer any random number is imported from 1 to 10 including both 1 and 10
print(random_integer)

# To import a floating point number no number is filled inside the () unlike random.randint
# Only the numbers between 0.0 and 1.0 is printed except the last one which is 1.0 
random_float = random.random()
print(random_float)

# To import a floating point number from a range of integers frpm 1 to 5

random_Float = random.random() * 5
print(random_Float)
