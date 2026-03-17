# WAPP using classes to find the area of a circle.

import math

class shape:
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # Calculates the area of the circle

# Creating an object of class circle
obj = circle(5)
print(obj.area())

# Output:
# 78.53981633974483
