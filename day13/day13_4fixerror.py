# # Fix the Errors
# age = input("How old are you?")         # greater than or smaller than sign is not supported with string/input statement
# if age > 18:
# print("You can drive at age {age}.")    # There should be an indentation before print statement 
                                          # f-string should also be mentioned in the print statement

age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
