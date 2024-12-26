# Base class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info - Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity):
        super().__init__(brand, model, year)
        self.seating_capacity = seating_capacity

    def display_info(self):
        super().display_info()
        print(f"Car Seating Capacity: {self.seating_capacity}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, has_gears):
        super().__init__(brand, model, year)
        self.has_gears = has_gears

    def display_info(self):
        super().display_info()
        print(f"Bike Has Gears: {'Yes' if self.has_gears else 'No'}")

# Creating objects
car = Car("Toyota", "Corolla", 2021, 5)
bike = Bike("Yamaha", "MT-07", 2022, True)

car.display_info()
print()
bike.display_info()
