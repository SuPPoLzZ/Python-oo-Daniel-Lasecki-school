
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


##
