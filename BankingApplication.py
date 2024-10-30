class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added. New balance is ${self.balance}.")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, transaction_fee=1):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self.balance -= self.transaction_fee
        print(f"Deducted transaction fee of ${self.transaction_fee}. New balance is ${self.balance}.")


# Example usage
savings_acc = SavingsAccount("SAV123", 1000, 0.02)
checking_acc = CheckingAccount("CHK456", 500)

savings_acc.display_balance()
savings_acc.deposit(500)
savings_acc.add_interest()
savings_acc.withdraw(200)

print()

checking_acc.display_balance()
checking_acc.deposit(300)
checking_acc.deduct_transaction_fee()
checking_acc.withdraw(100)
