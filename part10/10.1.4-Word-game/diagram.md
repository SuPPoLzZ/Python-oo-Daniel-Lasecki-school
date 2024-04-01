
class WordGame {
  - wins1: int
  - wins2: int
  - rounds: int
  + __init__(rounds: int)
  + round_winner(player1_word: str, player2_word: str): int
  + play(): void
}

class LongestWord {
  + __init__(rounds: int)
  + round_winner(player1_word: str, player2_word: str): int
}

WordGame <|-- LongestWord

## WordGame class
### Attributes:
- wins1: int
- wins2: int
- rounds: int
### Methods:
- __init__(rounds: int): Initializes WordGame object with specified number of rounds.
- round_winner(player1_word: str, player2_word: str): int: Winner of a round based on randomly generated result.
- play(): void: Starts the game, prompting players for input every round and displaying winner at the end.

## LongestWord class
### Inherits from:
- WordGame class
### Methods:
- __init__(rounds: int): Initializes LongestWord object with the specified number of rounds.
- round_winner(player1_word: str, player2_word: str): int: Overrides the round_winner method from WordGame to determine the winner based on the length of the words. If lengths are equal, winner is chosen randomly.
