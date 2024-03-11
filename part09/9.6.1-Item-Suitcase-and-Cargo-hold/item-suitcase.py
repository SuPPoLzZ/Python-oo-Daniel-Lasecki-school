class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def __str__(self):
        item_count = len(self.__items)
        combined_weight = self.weight()
        return f"{item_count} {'items' if item_count != 1 else 'item'} ({combined_weight} kg)"

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        return max(self.__items, key=lambda x: x.weight(), default=None)

class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def __str__(self):
        suitcase_count = len(self.__suitcases)
        available_space = self.__max_weight - self.weight()
        return f"{suitcase_count} {'suitcases' if suitcase_count != 1 else 'suitcase'}, space for {available_space} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.__suitcases)



book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print(cargo_hold)
print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()

heaviest_item = adas_suitcase.heaviest_item()
print(f"The heaviest item in Adas's suitcase: {heaviest_item}")
