# program using class & objects where the class name is shape to find class
#attributes & instance methods the instance method , instance name


import math

class shape:

    shape_type = "geometric shape"

    def area(self):
        pass

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2 

obj = Circle(5)
print("shape type:", obj.shape_type)
print("Circle area:", obj.area())          