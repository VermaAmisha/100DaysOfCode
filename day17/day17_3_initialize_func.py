class user:    # to create a class
    def __init__(self):
       print("New user created!")
# initialize function is being used here 

user_1 = user()

user_1.id = "001"   # to create attribue, we can create as many attributes as we want
user_1.username = "Amisha"

print(user_1.username )

user_2 = user()
user_2.id = "002"
