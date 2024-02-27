class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def eat_lunch(self):
        if self.balance > 0:
            self.balance -= 2.60
        
    def deposit_money(self, amount: float):
        self.balance += amount
    
    def eat_special(self):
         if self.balance > 0:
            self.balance -= 6.60

    def __str__(self):
        if self.balance < 0 or self.balance ==  0:
                return f"inssuficient balance try again later"
        finalbalance = round(self.balance, 2)
        return f"The balance is {finalbalance} Euro"
    
    
peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"........................................................................")
print(f"Balance after Grace eats normal lunch and Peter eats special lunch")
print(f"Peter balance {peters_card}")
print(f"Graces balance {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"........................................................................")
print(f"Balance after Grace eats special lunch and Peter deposits 20")
print(f"Peter balance {peters_card}")
print(f"Graces balance {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"........................................................................")
print(f"Balance after Peter eats 2x lunch and Grace deposits 50")
print(f"Peter balance {peters_card}")
print(f"Graces balance {graces_card}")
print(f"........................................................................")


