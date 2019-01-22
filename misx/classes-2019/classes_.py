class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

h = Holding('AA', '2007-06-11', 100, 32.2)

print(h)
print(h.name)
print(h.date)
print(h.shares)
print(h.price)
