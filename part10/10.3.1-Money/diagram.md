



class Money {
  - euro: int
  - cents: int
  + __init__(euro: int, cents: int)
  + __str__(): str
  + __eq__(another: Money): bool
  + __lt__(another: Money): bool
  + __gt__(another: Money): bool
  + __ne__(another: Money): bool
  + __add__(another: Money): Money
  + __sub__(another: Money): Money
}

## Money class
- euro: euro amount integer.
- cents: cents amount integer.
- __init__(euro: int, cents: int): Money object with the given amount of euros and cents.
- __str__() -> str: Returns a string representation of the Money object in the format "euro.cents".
- __eq__(another) -> bool: Checks if two Money objects are equal.
- __lt__(another) -> bool: Checks if the current Money object is less than another Money object.
- __gt__(another) -> bool: Checks if the current Money object is greater than another Money object.
- __ne__(another) -> bool: Checks if two Money objects are not equal.
- __add__(another) -> Money: Adds two Money objects together.
- __sub__(another) -> Money: Subtracts another Money object from the current Money object.

## Output:
- e1: Creates a Money object.
- e2: Creates a Money object.
- e3: Adds e1 and e2 together.
- e4: Subtracts e2 from e1.
- e5: Subtracts e1 from e2.


