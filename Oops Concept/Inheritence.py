# Inheritance


# Base class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived
class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak() 

#Ouptput Dog barks
