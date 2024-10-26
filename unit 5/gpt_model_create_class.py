#program to create a simple class 

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

person1 = Person("Alice")