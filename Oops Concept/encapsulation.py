# Encapsulation 


class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute
    
    def get_name(self):
        return self.__name

person = Person("Avijit")
print(person.get_name())  

# Output: Avijit
