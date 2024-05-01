from classes import Restaurant, User

class IceCreamStand(Restaurant):
    """Restaurant subclass"""

    def __init__(self, restaurant_name:str, cuisine_type:str, flavours: list):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def list_flavours(self):
        """Method to list available icecream flavours"""
        print(self.flavours)

class Admin(User):
    """Admin is a special type of user"""

    def __init__(self, first_name: str, last_name: str, password: str, age: int, height_meters: float, privileges: list[str]):
        super().__init__(first_name, last_name, password, age, height_meters)
        self.privileges = Privileges(privileges)


class Privileges:
    """Class to store and retreive privileges"""

    def __init__(self, privileges: list[str]):
        self.privileges = privileges

    def show_privileges(self):
        """A method to show the privileges available to the admin user"""
        print(self.privileges)


if __name__ == "__main__":
    swirlies = IceCreamStand('swirlies', 'icecream', ['Choc', 'Vanilla', 'Strawberry'])

    swirlies.list_flavours()

    steve = Admin('Steve',
                  'Jobs',
                  'sadhjfiughr',
                  57,
                  1.8,
                  ['read emails', 'delete accounts', 'run world'])

    steve.privileges.show_privileges()