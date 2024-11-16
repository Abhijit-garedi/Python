# over riding

class A:
    def display(self):
        return "welcome"

class B(A):
    def display(self):
        return "to aitam" 

obj = B()
print(obj.display())  

