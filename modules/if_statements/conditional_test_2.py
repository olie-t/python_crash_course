alien_colour = 'green'
if alien_colour == 'green':
    print('You got 5 pts')

if alien_colour == 'yellow':
    pass

if alien_colour == 'green':
    print('You got 5 pts')

if alien_colour != 'green':
    print('You got 10 pts')

if alien_colour == 'green':
    print('You got 5 pts')
elif alien_colour == 'yellow':
    print('You got 10 pts')
else:
    print('You got 15 pts')

alien_colour = 'yellow'
if alien_colour == 'green':
    print('You got 5 pts')
elif alien_colour == 'yellow':
    print('You got 10 pts')
else:
    print('You got 15 pts')
alien_colour = 'red'
if alien_colour == 'green':
    print('You got 5 pts')
elif alien_colour == 'yellow':
    print('You got 10 pts')
else:
    print('You got 15 pts')

age:int = int(input("What is your age?"))

if age < 2:
    print("You are a baby")
if 2 <= age < 4:
    print("You are a toddler")
if 4 <= age < 13:
    print("You are a child")
if 13 <= age < 20:
    print("You are a teenager")
if 20 <= age < 65:
    print("You are an adult")
if age > 65:
    print("You are an elder")

fav_fruits = ["Banana", "Apple", "Orange", "Melon", "Pineapple", "Grapes"]

if "Banana" in fav_fruits:
    print("Bananas are great")

users: list[str] = ['Admin', 'Adam', 'Steve', 'Laura', 'Kath']

if users:
    for user in users:
        if user == 'Admin':
            print(f'Welcome to the program, {user}')
        else:
            print(f'Ur a nub lol, {user}')
else:
    print('we need some users')

current_users = ['Admin', 'Adam', 'Steve', 'Laura', 'Kath']
new_users = ['Steve', 'Dave', 'Ben', 'Syd', 'Laura']
current_users_map: dict = {}
for user in current_users:
    current_users_map[user.lower()] = True
for user in new_users:
    if user.lower() in current_users_map:
        print(f'{user} is in use, pick a new user name')
    else:
        print(f'Welcome to the platform {user}')

numbers = [i for i in range(1, 10)]
for i in numbers:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print(f'{i}th')


