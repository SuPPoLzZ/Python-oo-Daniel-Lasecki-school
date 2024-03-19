class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    
    def __eq__(self, another):
        return (self.year, self.month, self.day) == (another.year, another.month, another.day)

    def __lt__(self, another):
        return (self.year, self.month, self.day) < (another.year, another.month, another.day)

    def __gt__(self, another):
        return (self.year, self.month, self.day) > (another.year, another.month, another.day)

    def __ne__(self, another):
        return not self.__eq__(another)
    
    def __add__(self, days: int):
        from datetime import datetime, timedelta
        current_date = datetime(self.year, self.month, self.day)
        new_date = current_date + timedelta(days=days)
        return SimpleDate(new_date.day, new_date.month, new_date.year)



d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)
d3 = SimpleDate(28, 12, 1985)

print(d1)
print(d2)
print(d1 == d2)
print(d1 == d3)
print(d1 != d2)
print(d1 < d2)
print(d1 > d2)

d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)

d3 = d1 + 3
d4 = d2 + 400

print(d1)
print(d2)
print(d3)
print(d4)
