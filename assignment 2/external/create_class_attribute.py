#Here's a Python program demonstrating class attributes and instance attributes:


# Define a class
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, brand, model, year):
        # Instance attributes
        self.brand = brand
        self.model = model
        self.year = year

    def print_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Wheels: {Car.wheels}")

# Create instances
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Access class attribute
print("Class Attribute:")
print(Car.wheels)

# Access instance attributes
print("\nInstance Attributes:")
car1.print_details()
print()
car2.print_details()

# Modify class attribute
Car.wheels = 6

# Verify changes
print("\nAfter modifying class attribute:")
car1.print_details()
print()
car2.print_details()

# Modify instance attribute
car1.brand = "Ford"

# Verify changes
print("\nAfter modifying instance attribute:")
car1.print_details()
print()
car2.print_details()
