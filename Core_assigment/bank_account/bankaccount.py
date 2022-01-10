class BankAccount:
    all_account = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = 0.02
        self.balance = 0
        BankAccount.all_account.append(self)
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info (self):
        print(f"Blance:${self.balance}")
    def yield_intrest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.interest_rate
            return self
        else :
            return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_account:
            print(f"Balance:{account.interest_rate}\n Balance: {account.balance}")

account1 = BankAccount( 0.02, 0)
account1.deposit(500).deposit(500).deposit(500).withdraw(200).display_account_info()

account2 = BankAccount( 0.02, 0)
account2.deposit(200).deposit(400).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_intrest().display_account_info()


BankAccount.all_balances()