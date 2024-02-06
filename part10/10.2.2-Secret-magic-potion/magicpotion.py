class MagicPotion:
    def __init__(self, name: str):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self.ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(f"{self.name}:")
        for ingredient, amount in self.ingredients:
            print(f"{ingredient} {amount} grams")
