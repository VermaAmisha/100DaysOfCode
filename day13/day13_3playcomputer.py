# # Play Computer

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:      # the year 1994 is not included in this line so if 1994 is entered no output is shown
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")    
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
