# Exercice 5:

# Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction 
# permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs, et affichez la 
# phrase suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de 
# leur division est égal à z. Vous ne devez qu'afficher 3 chiffres après le point.

def type_nombre():
    n1, n2 = int(input("Entrer un nombre pair et un nombre impair : ")), int(input())
    #y = int(input("Entrer un nombre pair ou impair : "))

    modulo_n1 = n1 % 2
    modulo_n2 = n2 % 2
    z = n2 / n1

    if modulo_n1 == 0 and modulo_n2 == 0:
        return "Vos 2 nombres sont pairs"
    elif modulo_n1 == 1 and modulo_n2 == 1:
        return "Vos 2 nombres sont impairs"
    else:
        if modulo_n1 != 1 and modulo_n2 == 1:     #  X being unpair and Y being pair
            n1, n2 = (y, x)
            
            return f"Votre nombre impair est le {x}, votre nombre pair est le  {y} \
        et le resultat de leur division est egal a {z}"
        elif modulo_n1 != 0 and modulo_n2 == 0: #unpair and pair
            n1, n2 = x, y 

            return f"Votre nombre impair est le {x}, votre nombre pair est le  {y} \
        et le resultat de leur division est egal a {z}"
    return

print(type_nombre())



