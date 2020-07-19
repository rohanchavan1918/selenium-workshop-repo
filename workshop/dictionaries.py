user_db = []

while True:
    user_ip = input("Enter New User  (y/n)")
    user_profile = {}
    if user_ip == "y" or user_ip == "n" :
        # dosomething
        if user_ip == "y":
            # Create New USEr
            user_profile["name"] = input("User NAme")
            user_profile["age"] = int(input("User age"))
            user_profile["bio"] = input("User bio")
            print(user_profile)
            print(user_db)
            user_db.append(user_profile)
            print(user_db)
            print("User added successfully !!!")
        else:
            # Break the loop
            break
    else:
        print("Invalid User Input")
# Come here
print(user_db)
print("done")
user_id = int(input("Enter the user id to get data."))
user_data = user_db[user_id]
print(f" Username :- {user_data['name']}, Age :- {user_data['age']}, bio :- {user_data['bio']}")

