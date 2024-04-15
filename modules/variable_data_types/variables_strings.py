
# Assign a variable and print it to the console
test_var: str = "Hello and welcome to the python crash course"
print(test_var)

#Use a variable to represent a persons name, and print a message to that person
name: str = "Olie"
message: str = f"Welcome to the course {name}"
print(message)

#Print the message in lowercase, uppercase, and titlecase
print(message.lower())
print(message.upper())
print(message.title())

#Define a variable with whitespace, then use the 3 whitespace stripping tools and display the name
whitespace_name: str = "  Olie   \n\t Thomas   "
print(whitespace_name)
print(whitespace_name.lstrip())
print(whitespace_name.rstrip())
print(whitespace_name.strip())

#Define a filename variable, and then use remove suffix to clean it
filename: str = "python_course.txt"
print(filename.removesuffix(".txt"))