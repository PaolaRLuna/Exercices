# Écrire un programme demandant à l'utilisateur de rentrer un 
# nombre entre 2 et 20, vérifier si ce dernier est bel et bien 
# entre 2 et 20, et indiquez-lui si son nombre est un nombre 
# premier (ayant aucun autre facteur entier que 1 et lui-même)

#Prime number is a number greater than 1, cannot be divided by any other number except 1 and itself.

# def premier():

#     nombre = int(input("Entrer un nombre entre 2 et 20: "))
    
#     prime = 2, 3, 5, 7, 11, 13, 17, 19

#     if 2 <= nombre <= 20:
#         if nombre in prime:
#             print("Votre nombre est premier")
#         else:
#             print("Votre nombre n'est pas premier")
#     else:
#         print("Votre nombre n'est pas entre 2 et 20")

# premier()

def premier():
    nombre = int(input("Entrer un nombre entre 2 et 20: "))

    if 2 <= nombre <= 20:
        if nombre % 2 == 0:
            print("Votre nombre n'est pas primer")
        elif nombre % 3 == 0:
            print("Votre nombre n'est pas primer")
        elif nombre % 5 == 0:
            print("Votre nombre n'est pas primer")
        elif nombre % 7 == 0:
            print("Votre nombre n'est pas primer")
        elif nombre % 11 == 0:
            print("Votre nombre n'est pas primer")
        elif nombre % 13 == 0:
            print("Votre nombre n'est pas primer")
        elif nombre % 17 == 0:
            print("Votre nombre n'est pas primer")
        elif nombre % 19 == 0:
            print("Votre nombre n'est pas primer")
        else:
            print("Votre nombre est prime")
    else:
        "Votre nombre n'est pas entre 2 et 20"

premier()
    
    
        