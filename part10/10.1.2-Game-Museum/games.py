class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.games = []

    def add_game(self, game: ComputerGame):
        self.games.append(game)

    def list_games(self):
        return self.games
