class user:    # to create a class
    def __init__(self, user_id, username):
       self.id = user_id
       self.username = username
       self.followers = 0 
# we can given a default value to followers of all the users
# since new users are created so there won,t be any followers in the beginning
# so it is inconvenient to write 0 again and again for every user

user_1 = user("001","Amisha")

# user_1.id = "001"   # to create attribue, we can create as many attributes as we want
# user_1.username = "Amisha"

print(user_1.id)
print(user_1.username )
print(user_1.followers)
# user_2 = user()  -- if we do not write user_id and username inside the brackets then it will show an error
user_2 = user("002", "Ankita")

# user_2.id = "002"   -- this is because we have already used these parameters for the 1st user
print(user_2.id)
print(user_2.username )
print(user_2.followers)
