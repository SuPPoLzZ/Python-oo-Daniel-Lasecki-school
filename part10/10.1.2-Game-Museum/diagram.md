
class ComputerGame {
    -name: str
    -developer: str
    -year: int
    +__init__(name: str, developer: str, year: int)
}

class GameWarehouse {
    -games: list
    +__init__()
    +add_game(game: ComputerGame)
    +list_games(): list
}

class GameMuseum {
    +__init__()
    +list_games(): list
}

ComputerGame <-- GameWarehouse
GameWarehouse <|-- GameMuseum


## Computer class
### Attributes:
- model: str
- speed: int
### Methods:
- __init__(model: str, speed: int): Initializes a new Computer object with the given model and speed.
- __str__(): Returns a string representation of the Computer object.
## Laptop class
### Attributes:
- Inherits attributes from Computer class
- weight: any
### Methods:
- __init__(model: str, speed: int, weight: any): Initializes a new Laptop object with the given model, speed, and weight.
- __str__(): Returns a string representation of the Laptop object.

