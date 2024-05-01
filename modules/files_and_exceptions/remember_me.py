from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available"""

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username"""
    username = input('What would you like your username to be?')
    age = input('How old are you?')
    fav_number = input('What is your fav number?')
    height = input('How tall are you?')
    userdict = {'username': username,
                'age': age,
                'fav_number': fav_number,
                'height': height
                }
    contents = json.dumps(userdict)
    path.write_text(contents)
    print(f'We will remember you {username}')
    return username
def greet_user():
    """Greet User by name"""
    path = Path('username.json')
    userdict = get_stored_username(path)
    if userdict:
        valid = input(f'Is this the correct username? - {userdict['username']}')
        if valid.lower() == 'no':
            get_new_username(path)
        else:
            print(f'Welcome back to the platform, {userdict['username']}')
    else:
        get_new_username(path)


if __name__ == '__main__':
    greet_user()