class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = 0.02
        self.balance = 0
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

# account1 = BankAccount( 0.02, 0)
# account1.deposit(500).deposit(500).deposit(500).withdraw(200).display_account_info()

# account2 = BankAccount( 0.02, 0)
# account2.deposit(200).deposit(400).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_intrest().display_account_info()




class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.saving = BankAccount(interest_rate = 0.02 , balance = 4000)
    def make_deposit(self, amount):
        self.saving.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.saving.withdraw(amount)
        return self
    def display_user_balance(self):
        print ((f"User:{self.name},Ballance: ${self.saving.balance}"))
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        # self.account_balance -= amount
        # other_user.account_balance += amount ( IT IS LIKE STEALING. NOT GOOD)
        return (f"You send ${amount} to {other_user.name},Current Balance:${self.account_balance}")


george = User("george", "george@gmail.com")
george.make_deposit(100).make_deposit(300).make_withdrawal(200).display_user_balance()


rene = User("rene", "rene@gmail.com")
rene.make_deposit(150).make_deposit(300).make_withdrawal(50).make_withdrawal(50)
rene.display_user_balance()

abdul = User("abdul", "abdul@gmail.com")
abdul.make_deposit(10000).make_withdrawal(100).make_withdrawal(50).make_withdrawal(100).display_user_balance()

