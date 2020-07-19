print("Welcome User - ")
user_age = input("Enter your age")
user_name = input("Enter your name")

if(int(user_age) > 18):
    print("userage is greater")
    some_movie = input("some movie")
    if len(some_movie) % 2 == 0:
        print("Movie available")
    else:
        print("Movie Not available")

elif(int(user_age) > 16):
    print("About age")
else:
    print("user is underage")
