#Pr 73:-
 # Wapp using class and object where the class-name is shape ,define class, instance attributes, instance methods is area of rectangle.

class Shape:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def display(self):  
        
        return f"Area: {self.l * self.b}"  

obj = Shape(12, 4)
print(obj.l)
print(obj.display()) 