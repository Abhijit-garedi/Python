#Pr 74:-
#Wapp to create class ,atrrributes
class A:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def display(self):
        return "My name is {} and I am {} years old.".format(self.name, self.age)

# Creating an object of class A
obj = A("aitam", 24)
print(obj.name)
print(obj.age)
print(obj.display())
print(obj.__class__.__name__)

class B(A):
    def info(self, addr):
        return "{} is located in {}".format(self.name, addr)

# Creating an object of class B
obj = B("aitam", 24)
print(obj.name)
print(obj.display())
print(obj.info("tekkali"))

# Output:
# aitam
# 24
# My name is aitam and I am 24 years old.
# A
# aitam
# My name is aitam and I am 24 years old.
# aitam is located in tekkali
