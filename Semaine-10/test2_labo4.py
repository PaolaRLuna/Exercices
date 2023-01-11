class Guichet():
    def __init__(self, bd, current_account_number, password, balance):
        self.infos_users = bd
        self.account = current_account_number
        self.motdepasse = password
        self.balance = balance

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
            fichier.write(f"{self.account}\n{self.motdepasse}\n")

    
    

#source: https://www.bhutanpythoncoders.com/how-to-build-an-atm-program-in-python-with-classes-and-objects/

class Client:
    def __init__(self, account, password):
        self.account = account
        self.mdp = password

    def transaction(self, amount):
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
            self.amount = int(input("Rentrer une quantité"))
            Guichet.deposit()
        elif option == "2":
            Guichet.withdraw()

