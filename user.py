class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

guido = User("Guido van Rossum", "guido@python.com")
klevis = User("Klevis Python", "klevis@python.com")
john = User("John Albiston", "john@gmail.com")
messi = User("Lionel Messi","lieonelmessi@live.com")

guido.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()
klevis.make_deposit(300).make_deposit(30000).make_withdrawal(100).make_withdrawal(100).display_user_balance()
john.make_deposit(1000).make_withdrawal(3000).make_withdrawal(300).make_withdrawal(300).display_user_balance()
messi.make_deposit(10000000).make_deposit(200120120).make_withdrawal(1000).make_withdrawal(2010).transfer_money(john,45540)
print("Info balanc")
guido.transfer_money(john, 500).display_user_balance()
messi.transfer_money(john,45540)
klevis.display_user_balance()
john.display_user_balance()
messi.display_user_balance()