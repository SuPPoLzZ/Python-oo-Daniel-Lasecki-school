
class ShoppingList {
  - items: dict
  - shoppinglist: (Unused)
  + __init__()
  + add(item, amount)
  + number_of_items(): int
  + item(index): str
  + amount(index): int
  + __iter__()
  + __next__()
}

## ShoppingList class
- items: Stores items and amounts.
- __init__(): Initializes an empty shopping list.
- add(item, amount): Adds an item with the specified amount.
- number_of_items() -> int: Returns the count of items in the list.
- item(index) -> str: Returns the item at the given index.
- amount(index) -> int: Returns the amount of the item at the given index.
- __iter__(), __next__(): Iterator methods to iterate over items in the list.

## Output:
- Creates a ShoppingList object.
- Adds items "bananas" (10 units), "apples" (5 units), and "pineapple" (1 unit).
