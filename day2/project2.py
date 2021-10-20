# If the bill was $150.00 , spli between 5 people, with 12% tip
# Each person should pay (150.00/5) *1.12 = 33.6
# Round off the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

bill = float(input("What is the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

total_bill = tip / 100 * bill + bill

print(total_bill)

bill_per_head = total_bill / people

final_amount = round(bill_per_head , 2)

print(f"Each person should pay: ${final_amount}")
