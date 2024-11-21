class Parent:
    def show(self):
        print("I am the parent class.")

class Child(Parent):  # Inheriting Parent class
    def display(self):
        print("I am the child class.")

obj = Child()
obj.show()  # Access parent method
obj.display()  # Access child method
