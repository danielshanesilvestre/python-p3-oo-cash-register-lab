#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prices = []
        self.quantities = []
        pass

    def add_item(self, title, price, quantity = 1):
        for i in range(quantity):
            self.items.append(title)
        self.prices.append(price)
        self.quantities.append(quantity)
        self.total += price * quantity
    pass

    def apply_discount(self):
        if self.discount != 0:
            self.total *= 1 - (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        quantity = self.quantities.pop()
        for i in range(quantity):
            self.items.pop()
        self.total -= self.prices.pop() * quantity
