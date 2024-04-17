#make a list of 5 places you would like to visit
places :list[str] = ["Paris", "Peru", "Cambodia", "Oman", "Sydney"]

#print the list
print(places)

#use sorted to print the list wihtout modfiying it
print(sorted(places))

#check the list hasnt changed
print(places)

#use reverse to change the list
places.reverse()
print(places)

#sort the list in place
places.sort()
print(places)

#sort the list in reverse order with sort
places.sort(reverse=True)
print(places)

#Think of something you can list, write a list of those things, and the use every function at least once
bbq_meats: list[str] = ["Steaks", "Chicken Thigh", "Sausage", "Burger", "Lamb Kebab"]
print(bbq_meats)
bbq_meats.insert(2, "Spicy Glaze Things")
print(bbq_meats)
bbq_meats.append("Hallumi Cheese")
print(bbq_meats)
bbq_meats.sort()
print(bbq_meats)
bbq_meats.sort(reverse=True)
print(bbq_meats)
bbq_meats.reverse()
print(bbq_meats)
del bbq_meats[3]
print(bbq_meats)
last_item = bbq_meats.pop()
print(last_item)
print(bbq_meats)
print(f"There are {len(bbq_meats)} items available")