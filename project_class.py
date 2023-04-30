from os import path
import csv

class Transaction:

    def __init__(self,transaction_number, name, phone_number, cost):
        self.transaction_number = transaction_number
        self.name = name
        self.phone_number = phone_number
        self.cost = cost

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, new):
        if new.isalpha() and len(new) >=1:
            self._name = new
        else:
            self._name = 'Invalid'

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def log_transactions(self, logger):
        if not path.isfile('transactions.csv'):
            with open('transactions.csv', 'w') as fp:
                data = csv.writer(fp)
                data.writerow(['Transaction Number', 'Name', 'Phone Number', 'Time', 'Services', 'Total'])
        with open('transactions.csv', 'a', newline='') as fp:
            data = csv.writer(fp)
            data.writerow(logger)

    def __str__(self):
        return f'Transaction {self.transaction_number}-Name: {self.name}, Phone number: {self.phone_number}, Total: ${self.cost}'
