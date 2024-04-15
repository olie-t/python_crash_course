#define a list of names, then print them using index, one by one
names: list[str] = ["Olie", "Ben", "Lorna", "Sara", "Tony"]
print(names[0], names[1], names[2], names[3], names[4])

#using the same list of names, define a personalised message and print it for each person
print(f"Hello and welcome to the python course {names[0]}")
print(f"Hello and welcome to the python course {names[1]}")
print(f"Hello and welcome to the python course {names[2]}")
print(f"Hello and welcome to the python course {names[3]}")
print(f"Hello and welcome to the python course {names[4]}")

#do a similiar thing with modes of transport
transport: list[str] = ["Car", "Bike", "Boat"]
print(f"I like my {transport[0]}")
print(f"I like my {transport[1]}")
print(f"I like my {transport[2]}")

