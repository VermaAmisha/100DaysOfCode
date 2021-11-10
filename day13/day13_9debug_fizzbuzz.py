# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:  # not 'or' but 'and' should be used as number divisible by both 3 and 5 should be replaced by fizzbuzz
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:    # else will only work if line 6 becomes false as it is associated with line 6 only as other ifs does not have any else statement
#     print("Buzz")        # It will be best to use elif instead of bunch of ifs
#   else:
#     print([number])

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

