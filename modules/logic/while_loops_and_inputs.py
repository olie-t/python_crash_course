car_type: str = input("What kind of car would you like to rent?")
print(f"Let me see if we have any {car_type}s available!")

num_guests: int = int(input("How many guests will be joining you tonight?"))
if num_guests > 8:
    print("You will have to wait for a table")
else:
    print(" Please come this way")

is_ten:int = int(input("Please enter a number: "))
if is_ten % 10 == 0:
    print("Your number is divisable by 10")
else:
    print("Your number is not divisiable by 10")

quit_next = False
while quit_next == False:
    var = input("What topping would you like to add?")
    if var == "quit":
        print("Ok no more toppings")
        quit_next = True
    else:
        print(f"Add some {var} to the pizza!!")

while True:
    var: int = input("What is your age? ")
    if var == "quit":
        break
    var = int(var)
    if var < 3:
        print("Your ticket is free")
    elif 3 <= var <= 12:
        print("Your ticket is $12")
    elif var > 12:
        print("Your ticket is $15")

deli_sandwhiches = ["Cheese",
                    "Ham",
                    "Cheese + Ham",
                    "Tuna Melt",
                    "Phily Cheese Steak",
                    "Chicken and choirzo",
                    "Tomato and mozerella",
                    "Pastrami",
                    "Pastrami"]
finished_sandwhiches = []

while deli_sandwhiches:
    current_sandwhich = deli_sandwhiches.pop()
    if current_sandwhich == "Pastrami":
        print("Sorry no pastrami")
        continue
    print(f"Currently making: {current_sandwhich}")
    finished_sandwhiches.append(current_sandwhich)

print(finished_sandwhiches)