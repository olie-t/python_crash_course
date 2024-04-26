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
