from pathlib import Path

while True:
    first = input("Provide the first number?")
    if first == 'q':
        break
    second = input("Provide the second number?")
    if second == 'q':
        break
    try:
        print(int(first) + int(second))
    except ValueError:
        print("One of those was not a number, sorry.")

try:
    cats = Path('cats.txt')
    cats_contents = cats.read_text()
    for cat in cats_contents.splitlines():
        print(cat)
    dogs = Path('dogs.txt')
    dogs_contents = dogs.read_text()
    for dog in dogs_contents.splitlines():
        print(dog)
except FileNotFoundError:
    pass
