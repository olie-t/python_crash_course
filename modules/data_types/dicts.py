ben: dict = {'age': 32, 'city': 'London', 'first_name': 'Ben', 'last_name': 'Thomas'}

for key, value in ben.items():
    print(key, value)

fav_numbers: dict = {'ben': [12, 42, 420, 42069], 'syd': 13, 'dave': 101, 'dani': 99, 'olie': 42, 'lloyd': 420, 'gav': 69}

for key, value in fav_numbers.items():
    print(f"{key}'s fav numbers are {value}")

glossary: dict = {'string': 'This is a string', 'int': 'An int is a whole number',
                  'float': 'A float is a floating point number',
                  'function': 'a function is a small unit of code which does something',
                  'if statement': 'an if statement determines if a condition is met'}
for key, value in glossary.items():
    print(f"Key = '{key}'\n Value = '{value}'")

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'rust',
                      'phil': 'python'
}

people = ['ben', 'steve', 'sarah', 'edward', 'jesus', 'tom', 'niyathi']

for name in people:
    if name not in favorite_languages:
        print(f'We invite you to complete our survey {name.title()}')
    else:
        print(f'You have already completed this survey {name.title()}!')

olie:dict = {'age': 35,
             'city': 'falmouth',
             'first_name': 'Olie',
             'last_name': 'Thomas'}
syd: dict = {'age': 35,
             'city': 'falmouth',
             'first_name': 'Sydney',
             'last_name': 'Fleming-Gale'}
hector: dict = {'age': 0.2,
                'city': 'falmouth',
                'first_name': 'Hector',
                'last_name': 'Fleming-Gale-Thomas'}
gav: dict = {'age': 35,
             'city': 'guildford',
             'first_name': 'Gavin',
             'last_name': 'Budd'}

more_people: list[dict] = [ben, olie, syd, hector, gav]

for person in more_people:
    for key, value in person.items():
        print(f'{key}:\n {value}')

