# Exercice 4:

# Créez un programme demandant à un utilisateur d'entrer sa date de fête et retournez-lui 
# sa saison de naissance s'il est né dans l'hémisphère Nord. (Vous pouvez assumer que les 
# équinoxes et solstices ont lieu le 21 du mois.) 
import datetime as date

spring = 3, 4, 5, 6
summer = 6, 7, 8, 9
fall = 9, 10, 11, 12 
winter = 12, 1, 2, 3

seasons = spring, summer, fall, winter

def saison_naissance():
    jour_fete = date.datetime.day(int(input("Entrer votre jour de fête : ")))
    mois_fete = date.datetime.month(int(input("Entrer votre mois de fête en nombre (ex. oct = 10) : ")))

    if

    if jour_fete >= 21 and mois_fete in seasons:
        seasons = spring, summer, fall, winter

        return spring, summer, fall, winter

print(saison_naissance())
    

# Exercice 5:

# Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction 
# permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs, et affichez la 
# phrase suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de 
# leur division est égal à z. Vous ne devez qu'afficher 3 chiffres après le point.

# Exercice 6:

# En partant de l'exercice du système de géolocation, modifiez votre code pour que les positions 
# en DMS incluent la direction cardinale(N, S, E, W ou O) et retourne une position en DD pouvant 
# être négative. Modifiez ensuite votre code pour permettre à un utilisateur de manuellement 
# rentrer sa position.

