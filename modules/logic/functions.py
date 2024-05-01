def display_message():
    print("This is me learning about functions")

def fav_book(fav_book: str = None):

    print(f"Oh wow! {fav_book} is one of my favs aswell")

def make_shirt(size: str = 'Large', message: str = 'I Love Python'):
    print(f"The shirt should be size {size}.\nThe shirt should have the message '{message}' printed on it")

def describe_city(name:str, country: str = 'england'):
    print(f"{name.title()} is in {country.title()}")

def city_country(city:str, country:str):
    city_with_country = f"{city.title()}, {country.title()}"
    return city_with_country

def make_album(artist_name: str, album_title: str, no_of_songs: int = None):
    album = {'artist name': artist_name, 'album_title': album_title}
    if no_of_songs:
        album['no_of_songs'] = no_of_songs
    return album


def make_albums_from_input():
    while True:
        print("Lets make an album!")
        print("Enter 'q' at any point to quit")
        artist_name = input("What is the artists name?")
        if artist_name == 'q':
            break
        album_name = input("What is the album name")
        if album_name == 'q':
            break
        songs = input("How many songs does the album have?")
        if songs == 'q':
            break
        if int(songs) != 0:
            print(make_album(artist_name, album_name, songs))
        else:
            print(make_album(artist_name, album_name))

messages: list[str] = ['Hello', 'World', 'How', 'Are', 'you']

def show_messages(messages_list: list[str]):
    for message in messages_list:
        print(message)

def send_messages(messages_list: list[str]):
    sent_messages = []
    while messages_list:
        current_message = messages_list.pop()
        sent_messages.append(current_message)
        print(current_message)
    print(messages_list)
    print(sent_messages)

def sandwhiches(*fillings: str):
    print(fillings)
def dream_vacation():
    locations = {}
    while True:
        current_location = input("Where is your dream location for a holiday?")
        if current_location == "quit":
            return print(locations)
        if current_location not in locations:
            locations[current_location] = 1
        else:
            locations[current_location] += 1

if __name__ == "__main__":
    display_message()
    fav_book("Moby Dick")
    make_shirt("M", "This is a shirt")
    make_shirt(message="This is also a shirt", size="Medium")
    make_shirt()
    describe_city('London')
    describe_city('Birmingham')
    describe_city('Paris', 'france')
    print(city_country('paris', 'france'))
    print(city_country('london', 'england'))
    print(city_country('auckland', 'new zealand'))
    print(make_album('Altin Gun', 'OK'))
    print(make_album('NOFX', 'So long and thanks for all the fish'))
    print(make_album('Test artist', 'test album', 12))
    make_albums_from_input()
    show_messages(messages)
    send_messages(messages[:])
    print(messages)
    send_messages(messages)
    send_messages(messages)
    sandwhiches('cheese', 'ham', 'bacon')

    #dream_vacation()