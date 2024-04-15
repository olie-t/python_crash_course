#use a for loop to print 1-20 inclusive
for i in range(1, 21):
    print(i)

#make a list of numbers 1-1million, then print it
one_in_a_million: list[int] = [i for i in range(1, 1000001)]
#for i in one_in_a_million:
 #   print(i)
# use min and max to make sure that your list actually contains a million, then sum it
print(max(one_in_a_million))
print(min(one_in_a_million))
print(sum(one_in_a_million))

#use a third argument in range to make a list of odd numbers
odd_nums: list[int] = [i for i in range(1, 20, 2)]
print(odd_nums)

#make a list of multiples of 3, then a for loop to print them
multiples_three: list[int] = [i for i in range(3, 30, 3)]
for i in multiples_three:
    print(i)

#make a list of the first 10 cubes, then a loop to print them
ten_cubes: list[int] = [i**3 for i in range(11)]
for i in ten_cubes:
    print(i)

#slice the first three items in a list above, and print it
print(f"The first three items in ten_cubes are {ten_cubes[:3]}")
print(f"Three items from the middle of the ten_sums list are {ten_cubes[2:5]}")
print(f"Three items from the end of the ten_cubes list are {ten_cubes[-3:]}")