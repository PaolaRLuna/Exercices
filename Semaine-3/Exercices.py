# Exercice 4:

# Créez un programme demandant à un utilisateur d'entrer sa date de fête et retournez-lui 
# sa saison de naissance s'il est né dans l'hémisphère Nord. (Vous pouvez assumer que les 
# équinoxes et solstices ont lieu le 21 du mois.) 

# spring = 3, 4, 5, 6
# summer = 6, 7, 8, 9
# fall = 9, 10, 11, 12 
# winter = 1, 2

# seasons = spring, summer, fall, winter

# def saison_naissance():
#     jour_fete = int(input("Entrer votre jour de fête : "))
#     mois_fete = int(input("Entrer votre mois de fête en nombre (ex. oct = 10) : "))
    
#     if mois_fete in (1, 2):
#         return "Votre saison est l'hiver"
#     elif mois_fete in (4, 5):
#         return "Votre saison est le printemps"
#     elif mois_fete in (7, 8):
#         return "Votre saison est l'ete"
#     elif mois_fete in (10, 11):
#         return "Votre saison est l'automne"
#     else:
#         if jour_fete <= 21 and mois_fete == 3:
#             return "Votre saison est l'hiver"
#         elif jour_fete > 21 and mois_fete == 3:
#             return "Votre saison est le printemps"
#         elif jour_fete <= 21 and mois_fete == 6:
#             return "Votre saison est le printemps"
#         elif jour_fete > 21 and mois_fete == 6:
#             return "Votre saison est l'ete"
#         elif jour_fete <= 21 and mois_fete == 9:
#             return "Votre saison est l'ete"
#         elif jour_fete > 21 and mois_fete == 9:
#             return "Votre saison est l'automne"
#         elif jour_fete <= 21 and mois_fete == 12:
#             return "Votre saison est l'automne"
#         elif jour_fete > 21 and mois_fete == 12:
#             return "Votre saison est l'hiver"
#         else:
#             return "Ce n'est pas une date valide"


# print(saison_naissance())


    

# Exercice 5:

# Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction 
# permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs, et affichez la 
# phrase suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de 
# leur division est égal à z. Vous ne devez qu'afficher 3 chiffres après le point.

from re import X


def type_nombre():
    x = int(input("Entrer un nombre pair ou impair : "))
    y = int(input("Entrer un nombre pair ou impair : "))

    modulo = x % y
    z = y / x

    if modulo != 0:
        return f"Votre nombre impair es le {X}, votre nombre pair est le {y} \
        et le resultat de leur division est egal a {z:.3f})"
    else:
        return f"Vos nombres sont pairs"

print(type_nombre())

# Exercice 6:

# En partant de l'exercice du système de géolocation, modifiez votre code pour que les positions 
# en DMS incluent la direction cardinale(N, S, E, W ou O) et retourne une position en DD pouvant 
# être négative. Modifiez ensuite votre code pour permettre à un utilisateur de manuellement 
# rentrer sa position.

