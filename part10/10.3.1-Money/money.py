class Money:
    def __init__(self, euro: int, cents: int):
        self.euro = euro
        self.cents = cents

    def __str__(self):
        return f"{self.euro}.{self.cents:02d} eur"

    def __eq__(self, another):
        return self.euro == another.euro and self.cents == another.cents

    def __lt__(self, another):
        return (self.euro, self.cents) < (another.euro, another.cents)

    def __gt__(self, another):
        return (self.euro, self.cents) > (another.euro, another.cents)

    def __ne__(self, another):
        return not self.__eq__(another)

    def __add__(self, another):
        total_cents = self.euro * 100 + self.cents + another.euro * 100 + another.cents
        return Money(total_cents // 100, total_cents % 100)

    def __sub__(self, another):
        total_cents = self.euro * 100 + self.cents - (another.euro * 100 + another.cents)
        if total_cents < 0:
            raise ValueError("negative result")
        return Money(total_cents // 100, total_cents % 100)


e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2 - e1
print(e5)
