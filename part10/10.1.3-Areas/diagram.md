
class Rectangle {
  - width: int
  - length: int
  + __init__(width: int, length: int)
  + area(): int
}

class Square {
  + __init__(side_length: int)
}

Rectangle <|-- Square


## Rectangle class
### Attributes:
- width: int
- length: int
### Methods:
- __init__(width: int, length: int): Creates a Rectangle object with given parameters(width and lengthd).
- area(): returns the area of the rectangle.

## Square class
### Inherits from:
- Rectangle class
### Methods:
- __init__(side_length: int): Creates a Square object with the given side length, setting width and length to the same value.
- Inherits area() method from Rectangle class.