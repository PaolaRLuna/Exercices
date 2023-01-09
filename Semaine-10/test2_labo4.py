class guichet():
    def __init__(self, account_number, password, compte, balance):
        self.account = account_number
        self.motdepasse = password
        self.compte = compte
        self.balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Current account balance: {self.balance} \n")
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds")
            print(f"Your balance is: {self.balance}")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"{amount} withdrawn")
            print(f"Current balance: {self.balance}")
    