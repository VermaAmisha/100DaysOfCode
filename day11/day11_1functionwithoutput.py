# Functions with output

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")
# Instead of printing it we can also use return function
    return (f"{formated_f_name} {formated_l_name}")
    

formated_string= format_name("amisha","verma")
print(formated_string)

                # or
# we can also print the result by directly printing the format name
print(format_name("amisha", "verma"))
