#create a list of people you would like to invite to dinner, then print a message to each, inviting them
guests: list[str] = ["Bob Ross", "Ross Bob", "Rossy Bobby"]
print(f"Wont you come to dinner {guests[0]}")
print(f"Wont you come to dinner {guests[1]}")
print(f"Wont you come to dinner {guests[2]}")

#one guest cant make it, print their name
print(guests[1])

#replace the guest who cant make it
guests[1] = "Steve Erwin"

#print new invitations
print(f"You, {guests[0]} are invited to dinner")
print(f"You, {guests[1]} are invited to dinner")
print(f"You, {guests[2]} are invited to dinner")

#You found a bigger table, think of 3 more guests to add
print(guests, "We have a larger table, more guests will be invited")

#Use insert, and append to add new guests to the list
guests.insert(1, "Jim Bob")
guests.insert(0, "Adam Smith")
guests.append("Donald Trump")

#Print a new set of invitations
for guest in guests:
    print(f"Dear {guest},\n You are cordially invited to dinner")

#change of plan, you only have room for 2 guests
while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry {guest}, we will have to rescind your invite.")
    print(len(guests))
#re-invite the remaining guests
for guest in guests:
    print(f"We are still on, see you at 8? {guest}")

#use del to remove the last 2 guests from your list, and print it
del guests[1]
del guests[0]
print(guests)

