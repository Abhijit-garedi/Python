# proagram to create class attributes and instance attributes

class  demo:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

obj = demo("aditya", 24)
print(obj.name)
print(obj.age)

#output aditya, 24