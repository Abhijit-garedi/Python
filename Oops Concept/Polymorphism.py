#Polymorphism

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

for animal in [Dog(), Cat()]:
    animal.speak()


    #output Dog barks, Cat meows
