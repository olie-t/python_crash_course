#save your 3 favorite types of pizza in a list then write a loop to print them all
pizza: list[str] = ["Pepperoni", "Meat Feast", "Double pepperoni double cheese"]
for piza in pizza:
    print(f"{piza} nom nom\n")
print("Pizza really is my most favorite food\n id do near anything for pizza\n I LOVE PIZZA")

#Add three animals with a common charactistic to a list, then use a loop to print them all
animals: list[str] = ["Dog", "Cat", "Bear"]
for ani in animals:
    print(ani)
#make a new loop making a statement about the animals
for ani in animals:
    print(f"{ani} sure are fluffy")

#copy the pizza list, then add a new pizza to the orginal list, add a new pizza to the new list, use loops to print both lists
friends_pizza: list[str] = pizza.copy()
pizza.append("Mushrooms")
friends_pizza.append("Hawiaan")
for i in pizza:
    print(i)
for i in friends_pizza:
    print(i)