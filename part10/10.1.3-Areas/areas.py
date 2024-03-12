class Rectangle:
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length



class Square(Rectangle):
    def __init__(self, side_length: int):
        super().__init__(side_length, side_length)


rectangle = Rectangle(2, 3)
print(rectangle)
print("area:", rectangle.area())

square = Square(4)
print(square)
print("area:", square.area())