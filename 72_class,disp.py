
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return "my name is {} and i am {} years old".format(self.name, self.age)

person = A("Avijit", 20)
print(person.display())
