# Exercice 3:

# Créer une fonction prenant une liste de nombres, d'une taille indéterminée
#, et permettant de les trier en ordre croissant. (Vous ne pouvez pas 
# utiliser sort() ou sorted(), vous devez vous-même implémenter 
# l'algorithme)
def trier(donnees):
    for donnee in len(donnees):
        print(min(donnee))

donnees = [1, 8, 3, 11, 2, 5, 6, 4]
trier(donnees)
# Exercice 4:

# Créer un menu demandant à un utilisateur d'entrer un nombre pair, 
# divisible par 3 et entre 10 et 29. Si l'utilisateur entre un nombre 
# ne correspondant pas à ces conditions, offrez-lui l'opportunité de 
# faire un nouvel essai, tant et aussi longtemps qu'il n'entre pas un 
# bon nombre.