class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print ((f"User:{self.name}, Balance:${self.account_balance}"))
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        # self.account_balance -= amount
        # other_user.account_balance += amount ( IT IS LIKE STEALING. NOT GOOD)
        return (f"You send ${amount} to {other_user.name},Current Balance:${self.account_balance}")


george = User("george", "george@gmail.com")
george.make_deposit(100).make_deposit(300).make_withdrawal(200)
george.display_user_balance()


rene = User("rene", "rene@gmail.com")
rene.make_deposit(150).make_deposit(300).make_withdrawal(50).make_withdrawal(50)
rene.display_user_balance()

abdul = User("abdul", "abdul@gmail.com")
abdul.make_deposit(10000).make_withdrawal(100).make_withdrawal(50).make_withdrawal(100)
abdul.display_user_balance()

