class Car:
    """A simple class to represenet a car"""

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the cars mileage"""
        print(f"This car has done {self.odometer_reading} miles")

    def update_odometer(self, mileage: int):
        """a method the set the odometer reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles: int):
        """a method to increment the odomenter value"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represents the aspects that make an electric car different"""

    def __init__(self, make: str, model: str, year: int):
        super().__init__(make, model, year)
        self.battery = Battery()



class Battery:
    """A class to decribe a battery"""

    def __init__(self , battery_size: int = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

    def get_range(self ):
        """print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")

if __name__ == "__main__":
    honda_jazz = ElectricCar('honda', 'jazz', 1999)
    honda_jazz.battery.get_range()
    honda_jazz.battery.upgrade_battery()
    honda_jazz.battery.get_range()
