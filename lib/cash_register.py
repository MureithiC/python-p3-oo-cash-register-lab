#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.transactions = []
        self.items = []

    def add_item(self, item_title, item_price, quantity=1):
        if isinstance(item_price, (int, float)) and isinstance(quantity, int) and quantity > 0:
            transaction_amount = item_price * quantity
            self.total += transaction_amount
            self.transactions.append(transaction_amount)
            for _ in range(quantity):
                self.items.append(item_title)
        else:
            raise ValueError("Item price must be a number and quantity must be a positive integer.")

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction

