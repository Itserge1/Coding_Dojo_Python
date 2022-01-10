class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self.account_balance
    def display_user_balance(self):
        return (f"User:{self.name}, Balance:${self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        # self.account_balance -= amount
        # other_user.account_balance += amount ( IT IS LIKE STEALING. NOT GOOD)
        return (f"You send ${amount} to {other_user.name},Current Balance:${self.account_balance}")


# george = User("george", "george@gmail.com")
# george.make_deposit(100)
# george.make_deposit(100)
# george.make_deposit(100)
# george.make_withdrawal(200)
# print(george.display_user_balance())

# rene = User("rene", "rene@gmail.com")
# rene.make_deposit(150)
# rene.make_deposit(300)
# rene.make_withdrawal(50)
# rene.make_withdrawal(50)
# print(rene.display_user_balance())

# abdul = User("abdul", "abdul@gmail.com")
# abdul.make_deposit(10000)
# abdul.make_withdrawal(100)
# abdul.make_withdrawal(50)
# abdul.make_withdrawal(100)
# print(abdul.display_user_balance())

