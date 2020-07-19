pizzas = ['marhertia','dominoz','pizzahut','blablabla']
toppings = ('cheese','onoion','paneer','capsicum')

# Get the length of the list
available_pizza_count = len(pizzas)
toppings_pizza_count = len(toppings)

# Infinite loop in python
while True:
    user_ip = input("Enter Pizzas to menu (y/n)")
    if user_ip == "y" or user_ip == "n" :
        # dosomething
        if user_ip == "y":
            # add to list
            new_pizza = input("Enter the name of the pizza")
            pizzas.append(new_pizza)
            print("Pizza Added to menu")
            print(pizzas)
        else:
            # Break the loop
            break
    else:
        print("Invalid User Input")
# Come here
print("done")

pizza_del = int(input("Which pizza to delete ?"))
try:
    pizzas.pop(pizza_del)
except Exception as exc:
    print("Pizza does not exist")
    pass
print(pizzas)
