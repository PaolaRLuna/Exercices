class Client:
    def __init__(self, account, password):
        self.account = account
        self.mdp = password

    def menu(self):
        pass

    def menu_placement(self):

        sortie = False
        while not sortie:
            choix = input("Voir mon retour de placement (o/n): ").lower()
            if not (choix == "o" or choix == "oui"):
                sortie = True


    def choisir_compte(self):
        sortie = False
        while not sortie:

            print("""
                CHOISIR COMPTE
            *********************
            1. Cheque
            2. Épargne
            3. Placements
            4. Sortir

            """)
            choix = input("Choisir compte: ")
            if choix == "1":
                pass
            elif choix =="2":
                pass
            elif choix =="3":
                pass
            elif choix == "4":
                sortie = True
            else:
                print("Choix invalide")


    def transaction(self, amount):
        sortie = False
        while not sortie:

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
                self.amount = float(input("Rentrer une quantité: "))
                Guichet.deposit(amount)
            elif option == "2":
                self.amount = float(input("Rentre montant a retirer: "))
                Guichet.withdraw(amount)
            elif option == "3":
                pass
            elif option == "4":
                sortie = True
            else:
                print("Choix invalide")

    def lire_bd():
        bd = {}
        with open ("Semaine-10/bd.txt","r", encoding='utf8') as f:
            for line in f.read().splitlines()[1:]: 
                (key,value) = line.split("\t", maxsplit=1)
                bd[int(key)] = [val for val in value.split("\t") if val]
        return bd


class Guichet():
    def __init__(self, bd, current_account_number, password, balance):
        self.infos_users = bd
        self.account = current_account_number
        self.motdepasse = password
        self.balance = balance

    def connection_user():
        pass
    
    def connection_mdp():
        pass

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Current account balance: {self.balance} \n")
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance")
            print(f"Your balance is: {self.balance}")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"{amount} withdrawn")
            print(f"Current balance: {self.balance}")

    def creation_basedonnees(self):
        with open ("bd.txt", "w", encoding='utf8') as fichier:
            fichier.write(f"{self.account}\n{self.motdepasse}\n")

    def proj_retour_cinq_ans(self, solde, interet):
        print(f"Solde: {solde}")
        for i in range(1,6):
            taux_compose = self.solde * (1 + interet) ** i
            print(f"{i} an(s): {taux_compose}", end=" ")

    
    

#source: https://www.bhutanpythoncoders.com/how-to-build-an-atm-program-in-python-with-classes-and-objects/


            
    
