################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# ḷocal scope

def drink_potion():
    potion_strength = 2    # local variables which are inside any function are local variables which can't be used anywhere in the program except that very function
    print(potion_strength)

# global scope

player_health = 10    # global variables which are not inside any function are global variables which can be used anywhere in the program

def drink_potion():
    potion_strength = 2    # this is a local variable it is mentioned inside another function so it can't be accessed here
    print(player_health)   # this is local variable
drink_potion()
print(player_health)   # it is a global variable it can be accessed anywhere
