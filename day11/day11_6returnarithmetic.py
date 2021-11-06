

# addition

def add(n1 , n2):
    return n1 + n2

# subtraction

def subtract(n1 , n2):
    return n1 - n2

# multiply

def multiply(n1 , n2):
    return n1 * n2

# divide

def divide(n1 , n2):
    return n1 / n2

operators = {
    "+":add, 
    "-":subtract, 
    "*":multiply, 
    "/":divide 
}

first_number = int(input("Enter the value of n1: "))

for symbol in operators:
    print(symbol)

chosen_symbol = input("Which operator/symbol would you like to choose? ")

second_number = int(input("Enter the value of n2: "))

calculation = operators[chosen_symbol]
answer = calculation(first_number , second_number)

print(calculation)
print(f"{first_number} {chosen_symbol} {second_number} = {answer} ") 
