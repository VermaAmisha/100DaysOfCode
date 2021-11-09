
# Ṭhere is no Block Scope

game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]    #  any variable which is named inside the if/while/for loop are not local variables

print(new_enemy)

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_foe = enemies[0]    

    print(new_foe)    # here in this case print statement should be inside the function to be accessed
