
# # Earlier to add a number to each element of the list "For Loop"

numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# # using list comprehension instead of all these 4 lines of code only 1 line of code will be used
# # using keyword method
# new_list = [new_item for item in list]

new_list = [n + 1 for n in numbers]
