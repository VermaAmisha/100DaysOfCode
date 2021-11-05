# Functions with output

def format_name(f_name, l_name):
    # we can use multiple return in a function
    # but the function will stop just after the first return if the condition/s for the same appears to be true
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")
# Instead of printing it we can also use return function
    return (f"{formated_f_name} {formated_l_name}")
    print("This got printed") # ṭhis will not get printed because "return" tells the computer that this is the end of the function   
# Anything after return - comes out of the function  
print(format_name(input("What is your first name? "),input("What is your last name? ")))
# instead of directly givingthe name as inputs in the function,
# we can ask questions through input function
