
# _____Definition______
#nom : str
#age : int
class Personne:
    def __init__(self, nom : str = "", age : int = 0): # creer toujour les variables d'instance au niveau de constructeur
        self.nom = nom #Creation de variable d'instance: nom, c'est stocke dans nom et dans self, une fois cree on peut acceder au self.nom dans autre fonction
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur " + self.nom) # Construcsteur

    #Methodes d'instances
    def SePresenter(self):
        #Bonjour, je m'appelle Jean, j'ai 30 ans
        info_personne = "Bonjour, "+ self.nom
        if self.age == 0:
            print(info_personne)
        else:
            print(info_personne + "j'ai " + str(self.age) + "ans")
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
            #print("EstMaajeur: ", self.EstMajeur())
    
    def EstMajeur(self):
        return self.age >= 18
        # if self.age >= 18:
        #     return True
        # return False
    
    def DemanderNom(self):
        self.nom = input("Nom de la personne ?: ")

# ____UTILISATION_____
personne1 = Personne("Jean", 30) #Creation d'une personne
personne1.SePresenter() # methode d'instance
#personne1.AutreFonction()

personne2 = Personne("Paul", 15)
personne2.SePresenter()
#Personne.AutreFonction()    #methode de classe

personne3 = Personne()
#personne3.DemanderNom()
personne3.SePresenter()

personne4 = Personne(age=20)
personne4.SePresenter()
#print("estMajeur: ", personne1.EstMajeur())
#print("nom1 " + personne1.nom)