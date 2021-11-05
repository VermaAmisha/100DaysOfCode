def format_name(f_name, l_name):
    """It takes the first name and the last name and formats it to its title version"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"{formated_f_name} {formated_l_name}")

print(format_name("AmiSha", "VerMa"))

# three double/single opening and closing quotation marks are used in writing a docstring for any function we define
