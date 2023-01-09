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

    def creation_basedonnees(self):
        with open ("bd.txt", "w", encoding='utf8') as fichier:
            fichier.write(f"{self.account}\n{self.motdepasse}\n{self.compte}")

    
    def transaction(self):
        print("""
            OPÉRATIONS
         *******************
         Menu:
         1. Faire un dépôt
         2. Faire un retrait
         3. Voir mon retour de placement
         4. Terminer
         """)

        option = input("Entrer votre choix")
        if option == "1":
            amount = int(input("Rentrer une quantité"))
            guichet.deposit()
        elif option == "2":
            guichet.withdraw

#source: https://www.bhutanpythoncoders.com/how-to-build-an-atm-program-in-python-with-classes-and-objects/