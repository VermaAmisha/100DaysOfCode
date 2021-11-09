################### Scope ####################

enemies = 1

def increase_enemies():
  global enemies   # to modify global variable
  enemies += 1     # a global variable can't be used inside any function 
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# It can be confusing to use global to modidy global variable
# so it is better to use return statement as output

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
