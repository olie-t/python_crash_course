def display_message():
    print("This is me learning about functions")

def fav_book(fav_book: str = None):

    print(f"Oh wow! {fav_book} is one of my favs aswell")

def make_shirt(size: str, message: str):
    print(f"The shirt should be size {size}.\nThe shirt should have the message '{message}' printed on it")

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
    dream_vacation()