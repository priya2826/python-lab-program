class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient balance")

acc = BankAccount()
acc.deposit(int(input()))
acc.withdraw(int(input()))
