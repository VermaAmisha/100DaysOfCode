

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



first_number = int(input("Enter the first number: "))

for symbol in operators:
    print(symbol)

wants_to_continue = True
while wants_to_continue:

    chosen_symbol = input("Which operator/symbol would you like to choose? ")

    second_number = int(input("Enter the next number: "))

    calculation = operators[chosen_symbol]
    answer = calculation(first_number , second_number)

    print(f"{first_number} {chosen_symbol} {second_number} = {answer} ") 

    if input(f"To continue with {answer} press 'y' or press 'n' to exit calculation: ") == "y":
        first_number = answer
            
    else:
        print("The calculation exits!")
        wants_to_continue = False
        
