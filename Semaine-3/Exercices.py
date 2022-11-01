# Exercice 5:

# Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction 
# permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs, et affichez la 
# phrase suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de 
# leur division est égal à z. Vous ne devez qu'afficher 3 chiffres après le point.

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

