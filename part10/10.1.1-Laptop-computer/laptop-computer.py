class Computer:
    def __init__(self, model: str, speed: int):
        self.model = model
        self.speed = speed
    
    def __str__(self):
        return f"Model: {self.model}, Speed: {self.speed}"

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight):
        super().__init__(model, speed)
        self.weight = weight
    
    def __str__(self):
        return f"Model: {self.model}, Speed: {self.speed}, Weight: {self.weight} kg"


laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)
