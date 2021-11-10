############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20): -- the bug is that i will never reach 20 as in for loop range the last number is not counted
#     if i == 20:
#       print("You got it")
# my_function()



def my_function():          
  for i in range(1, 21):
    if i == 20:              
      print("You got it")    
my_function()
