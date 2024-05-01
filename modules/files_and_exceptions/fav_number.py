from pathlib import Path
import json

def ask_fav_number():
    num = input("What is your fav number?")
    path = Path('num_store.json')
    num_json = json.dumps(num)
    path.write_text(num_json)

def tell_fav_number():
    path = Path('num_store.json')
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f'Your fav number is {fav_num}')

def number_rememberer():
    path = Path('num_store.json')
    if path.exists():
        tell_fav_number()
    else:
        ask_fav_number()


if __name__ == "__main__":
    number_rememberer()
    number_rememberer()