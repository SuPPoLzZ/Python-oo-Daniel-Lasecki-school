class ShoppingList:
    def __init__(self):
        self.items = {}
        self.shoppinglist = {}

    def add(self, item, amount):
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount

    def number_of_items(self):
        return len(self.items)

    def item(self, index):
        if 1 <= index <= len(self.items):
            return list(self.items.keys())[index - 1]
        else:
            raise IndexError("Item index out of range")

    def amount(self, index):
        if 1 <= index <= len(self.items):
            return list(self.items.values())[index - 1]
        else:
            raise IndexError("Item index out of range")
        
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.items):
            keys = list(self.items.keys())
            values = list(self.items.values())
            result = (keys[self._index], values[self._index])
            self._index += 1
            return result
        else:
            raise StopIteration

        
        
        
    
    
shopping_list = ShoppingList()
shopping_list.add("bananas", 10)
shopping_list.add("apples", 5)
shopping_list.add("pineapple", 1)

for product in shopping_list:
    print(f"{product[0]}: {product[1]} units")
