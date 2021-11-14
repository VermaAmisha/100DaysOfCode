

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

should_continue = True
while should_continue:

    would_like = input("\nWhat would you like? (espresso/latte/cappucino): ").lower()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"\nresources:\nwater = {water}\nmilk = {milk}\ncoffee = {coffee}"+"\n")

    # espresso
    e_water = 50
    e_coffee = 18
    e_cost = 1.5

    # latte
    l_water = 200
    l_milk = 150
    l_coffee = 24
    l_cost = 2.5

    # cappuccino
    c_water = 250
    c_milk = 100
    c_coffee = 24
    c_cost = 3.0

    if would_like == "espresso":
        print(f"Ingrediants required:\nwater= {water} ml\ncoffee= {coffee} mg\n" +"\n"+ f"Cost: ${e_cost}\n ")
    
    elif would_like == "latte":
        print(f"Ingrediants required:\nwater= {l_water} ml\nmilk= {l_milk} ml\ncoffee= {l_coffee} mg\n" +"\n"+ f"Cost: ${l_cost}\n ")

    else:
        print(f"Ingrediants required:\nwater= {c_water} ml\nmilk= {c_milk} ml\ncoffee= {c_coffee} mg\n" +"\n"+ f"Cost: ${c_cost}\n ")

    print("Please insert coins!")

    total = float(input("How many quarters? ")) * 2.5
    total += float(input("How many dimes? ")) * 0.1
    total += float(input("How many nickles? ")) * 0.05
    total += float(input("How many pennies? ")) * 0.01

    print(f"${total}")

    if would_like == "espresso" and total >= e_cost:
        print("Here is your coffee! enjoy!!")
        e_change = total - e_cost
        print(f"Your change = ${e_change}")

    elif would_like == "latte" and total >= l_cost:
        print("Here is your coffee! enjoy!!")
        l_change = total - l_cost
        print(f"Your change = ${l_change}")

    elif would_like == "cappuccino" and total >= c_cost:
        print("Here is your coffee! enjoy!!")
        c_change = total - c_cost
        print(f"Your change = ${c_change}")

    else:
        print("Sorry! coins inserted are not sufficient!")

    

    order_more = input("\nType 'y' to order more or type 'n' to close the machine: ").lower()
    if order_more == "y":
        should_continue = True
    else:
        should_continue = False

    if order_more == "y" and would_like == "espresso":
        def e_resources_left(water,coffee):
            water = water - e_water
            coffee = coffee - e_coffee
            print(f"Resources left:\nWater left = {water} ml\nCoffee left= {coffee} mg\nMilk left = {milk} ")
        e_resources_left(water,coffee)
     
    elif order_more == "y" and would_like == "latte":
        def l_resources_left(water,coffee,milk):
            water = water - l_water
            coffee = coffee - l_coffee
            milk = milk - l_milk
            print(f"Resources left:\nWater left = {water} ml\nCoffee left= {coffee} mg\nMilk left = {milk} ")
        l_resources_left(water,coffee,milk)

    elif order_more == "y" and would_like == "cappuccino":
        def c_resources_left(water,coffee,milk):
            water = water - c_water
            coffee = coffee - c_coffee
            milk = milk - c_milk
            print(f"Resources left:\nWater left = {water} ml\nCoffee left= {coffee} mg\nMilk left = {milk} ")
        c_resources_left(water,coffee,milk)
