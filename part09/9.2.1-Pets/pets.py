
class Person:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return f"{self.name}, whose pal is {self.pet.name}, a {self.pet.breed}"


class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


hulda = Pet("Hulda", "mixed-breed dog")
levi = Person("Levi", hulda)

print(levi)
