



class Computer {
    -model: str
    -speed: int
    +__init__(model: str, speed: int)
    +__str__(): str
}

class LaptopComputer {
    -weight: any
    +__init__(model: str, speed: int, weight: any)
    +__str__(): str
}

Computer <|-- LaptopComputer



## Computer class 
### Attributes:
-model:str
-speed: int
### Methods:
+__init__(model: str, speed:int) 
+__str__(): str

## Laptop class
### Attributes:
-weight: any, and inherites attributes from Copmuter class
### Methods:
+__init__(model: str, speed: int, weight: any)
+__str__(): str







