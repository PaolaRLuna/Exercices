# Exercice 3:

# Créer une fonction prenant une liste de nombres, d'une taille indéterminée
#, et permettant de les trier en ordre croissant. (Vous ne pouvez pas 
# utiliser sort() ou sorted(), vous devez vous-même implémenter 
# l'algorithme)

def trier(donnees: list[int]):
    length = len(donnees)
    f_donnees = []
    i = 0
    while i < length:
        num = min(donnees)
        f_donnees.append(num)
        donnees.remove(num)
        i += 1
    print(f_donnees)

    

donnees = [1, 8, 3, 11, 2, 5, 6, 4]
trier(donnees)

# Exercice 4:

# Créer un menu demandant à un utilisateur d'entrer un nombre pair, 
# divisible par 3 et entre 10 et 29. Si l'utilisateur entre un nombre 
# ne correspondant pas à ces conditions, offrez-lui l'opportunité de 
# faire un nouvel essai, tant et aussi longtemps qu'il n'entre pas un 
# bon nombre.

def menu():

    condition = False
    while not condition:
        u_input = int(input("Entre un nombre entre 10 et 29, pair et divisible par 3: "))

        if 10 <= u_input <= 29 and u_input % 3 == 0 and u_input % 2 == 0:
            condition = True
            print(f"Votre nombre {u_input} es correct")
        else:
            print("Entrer autre nombre")

#menu()
