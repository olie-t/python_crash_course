from pathlib import Path

file = Path('learning_python.txt')
file_contents = file.read_text()
print(file_contents)
new_contents = file_contents.replace('python', 'rust')

for line in new_contents.splitlines():
    print(line)

guest = input("What is your name?")

guest_file = Path('guest_log.txt')
guest_file.write_text(guest)

guest_book = Path('guest_book.txt')
guests_string = ""
while True:
    guest = input("What is your name?")
    if guest == 'q':
        break
    guests_string += f"{guest}\n"

guest_book.write_text(guests_string)

