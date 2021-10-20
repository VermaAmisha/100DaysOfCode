two_digit_number = input("Type a two digit number: ")
# first digit is written as 'a' and second digit is written as 'b' below
# [0] extracts the first digit and [1] extracts the second digit from the two digit number chosen 
a = two_digit_number[0] 
b = two_digit_number[1]
# a and b are string as 'input("Type a two digit number:") is string code and cannot be added
x = int(a) +int(b)
print(x)

# or it can also be written as follows:
# a = int(a)[0]
# b = int(b)[1]
# x = a + b
# print(x)
