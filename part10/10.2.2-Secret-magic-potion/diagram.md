
class MagicPotion {
  - name: str
  - ingredients: dict
  + __init__(name: str)
  + add_ingredient(ingredient: str, amount: float)
  + print_recipe()
}

class SecretMagicPotion {
  - password: str
  + __init__(name: str, password: str)
  + add_ingredient(ingredient: str, amount: float, password: str)
  + print_recipe(password: str)
}

MagicPotion <|-- SecretMagicPotion

## MagicPotion class
- name: Name of the potion.
- ingredients: stores ingredients and amounts.
- __init__(name: str): Creates  potion with a given name and an empty ingredient list.
- add_ingredient(ingredient: str, amount: float): Adds an ingredient to the potion.
- print_recipe(): Prints out the recipe of the potion, listing all ingredients and also amount of ingredients.

## SecretMagicPotion class
- Inherits from MagicPotion.
- password: A password required for adding ingredients or printing the recipe.
- __init__(name: str, password: str): Initializes a secret potion with a name and password.
- print_recipe(): Prints the potion's recipe.
