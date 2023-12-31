#!/bin/bash/python3

class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        transaction = ('deposit', ammount)
        self.transactions.append(transaction)

    def withdraw(self, amount):
        transaction = ('withdraw', amount)
        self.transactions.append(transaction)

    def balance(self):
        total = 0
        for kind, amount in self.transactions:
            if kind == 'deposit':
                total += amount
            elif kind == 'withdraw':
                total -= amount

    def __repr__(self):
        return '<Account: {}>'.format(len(self.transactions)))
