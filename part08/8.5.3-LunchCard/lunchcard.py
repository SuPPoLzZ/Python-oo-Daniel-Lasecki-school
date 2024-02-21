class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def eat_lunch(self):
        if self.balance > 0:
            self.balance -= 2.60
        
    def eat_special(self):
         if self.balance > 0:
            self.balance -= 6.60

    def __str__(self):
        if self.balance < 0 or self.balance ==  0:
                return f"inssuficient balance try again later"
        finalbalance = round(self.balance, 2)
        return f"The balance is {finalbalance} Euro"
    
    
    

card = LunchCard(2.62)
print(card)

card.eat_lunch()
print(card)

card.eat_special()
card.eat_lunch()
print(card)