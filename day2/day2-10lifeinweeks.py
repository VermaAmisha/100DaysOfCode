age = input("What is your current age? ")
# converting age into an int as input value is always string
a = int(age)
# Time remaining is mentioned below
years = 90 - a
days = years * 365
weeks = years * 52
months = years * 12
print(f"You have{days} days, {weeks} weeks, and {months} months left.")
