class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hellow, my name is {self.name} and i am {self.age} years old")
        
student1 = Student("avijit", 20)
student1.greet()    