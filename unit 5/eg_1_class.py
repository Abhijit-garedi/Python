class B:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self, addr):
        return "{} is located in {}".format(self.name, addr)

    def display(self):
        return "my name is {} and {} years old".format(self.name, self.age)

obj = B("avijit", 24)

# Display the values
print(obj.display())               # Output: my name is avijit and 24 years old
print(obj.info("tekkali"))         # Output: aitam is located in tekkali
