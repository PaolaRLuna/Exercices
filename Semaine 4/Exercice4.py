# Écrire un programme avec une fonction prenant 2 floats et 
# retournant leur addition soustraction et division. 
# Les résultats des additions doivent avoir au plus 1 chiffre 
# après la virgule, la soustraction 2 chiffres après la virgule
# et la division 3 chiffres après la virgule.

def operation():

    n1 = float(input("Entrer un nombre: "))
    n2 = float(input("Entrer un nombre: "))

    addition = n1 + n2
    soustraction = n1 - n2
    division = n1/n2

    return addition, soustraction, division

print(operation())