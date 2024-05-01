class Restaurant:
    """A class to represent a restaurant"""
    def __init__(self, restaurant_name:str, cuisine_type:str):
        """Method to initialize the class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Method to print a description of the class"""
        print(f'This is a {self.cuisine_type} restaurant called {self.restaurant_name.title()}')

    def open_restaurant(self):
        """Method to declare the restaurant open"""
        print(f'{self.restaurant_name.title()} is now open')

    def serve_customer(self):
        """Add one to the total customer count and print a message"""
        self.number_served += 1
        print("Another happy customer")

    def set_number_served(self, number:int):
        """Set the total number of served customers"""
        self.number_served = number
        print(f"{self.restaurant_name.title()} has served {self.number_served} customers.")

    def increment_number_served(self, number:int):
        """Increment the number of customers by a given value"""
        old_value = self.number_served
        self.number_served += number
        print(f"The number of customers served by {self.restaurant_name.title()} has gone from {old_value} too "
              f"{self.number_served}")

class User:
    """A simple class to represent a user"""

    def __init__(self, first_name:str, last_name:str, password:str, age:int, height_meters:float):
        """Method to initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age
        self.height_meters = height_meters
        self.login_attempts = 0

    def describe_user(self):
        """Method to describe the user"""
        print(f"""User information:
            First name - {self.first_name}
            Last Name - {self.last_name}
            Age - {self.age}
            Height (meters) - {self.height_meters}""")

    def greet_user(self):
        """Method to greet the user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, welcome to the platform")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1"""
        self.login_attempts += 1
        print(f"The user {self.first_name.title()} {self.last_name.title()} has attempted to login {self.login_attempts}"
              f" times.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The login attempts for {self.first_name.title()} {self.last_name.title()} has been reset to 0 ")

if __name__ == "__main__":
    deli_beli = Restaurant('deli beli', 'indian')
    print(deli_beli.restaurant_name)
    print(deli_beli.cuisine_type)
    deli_beli.describe_restaurant()
    deli_beli.open_restaurant()
    print(deli_beli.number_served)
    deli_beli.number_served += 1
    print(deli_beli.number_served)
    deli_beli.serve_customer()
    deli_beli.set_number_served(14)
    deli_beli.increment_number_served(12)


    john = User('John', 'Smith', 'gho11234aase1', 32, 1.85)

    john.describe_user()
    john.greet_user()
    print(john.password)
    john.increment_login_attempts()
    john.increment_login_attempts()
    john.reset_login_attempts()



