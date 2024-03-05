class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"The name of the present: {self.name}\n The weight of the present: {self.weight}"
    
class Box:
    def __init__(self):
        self.presents = []  # initialize an empty list to store presents

    def add_present(self, present: Present):
        self.presents.append(present)  
    
    def total_weight(self):
        total = sum(present.weight for present in self.presents)  
        return total


book = Present("ABC Book", 2)
box = Box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box.add_present(cd)
print(box.total_weight())
