class SuperHero {
  - _name: str
  - _power: str
  + __init__(name: str, power: str)
  + get_name(): str
  + get_power(): str
}

class SuperGroup {
  - _location: str
  - _members: list[SuperHero]
  + __init__(name: str, location: str)
  + get_name(): str
  + get_location(): str
  + add_member(hero: SuperHero)
  + print_group()
}

SuperHero --|> SuperGroup




## SuperHero class
### Attributes:
- _name: str (private)
- _power: str (private)
### Methods:
- __init__(name: str, power: str): creates new SuperHero object with given name and power.
- get_name() -> str: Returns the name of the superhero.
- get_power() -> str: Returns the power of the superhero.

## SuperGroup class
### Inherits from:
- SuperHero class
### Attributes:
- _location: str (private)
- _members: list[SuperHero] (private)
### Methods:
- __init__(name: str, location: str): creates new SuperGroup object with the given name and location.
- get_name() -> str: Returns the name of the group.
- get_location() -> str: Returns the location of the group.
- add_member(hero: SuperHero): Adds a member (SuperHero object) to the group.
- print_group(): Prints information about group and members.
