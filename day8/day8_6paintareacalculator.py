#Write your code below this line 👇

import math

# Code below is not required

# wall_height= int(input(f"Enter wall height: "))
# wall_width= int(input(f"Enter wall width: "))
# coverage = 5
# number_of_cans =math.ceil((wall_height * wall_width) / coverage)  
# print(f"Number of cans requires for your wall is approximately {number_of_cans}.")

# Code above is not required

# Round up can also be done by using round() function but here it won't be appropriate 
# Here it will remove small decimal places like 16.2 will become 16 and 16 cans will be less for the wall to be painted
# So it shoul convert 16.2 into 17  




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

def paint_calc(height, width, cover):
    number_of_cans = math.ceil(( height * width ) / cover)
    print(f"Number of cans requires for your wall is approximately {number_of_cans}.")
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
