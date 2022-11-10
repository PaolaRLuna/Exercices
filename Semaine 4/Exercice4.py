# Écrire un programme avec une fonction prenant 2 floats et 
# retournant leur addition soustraction et division. 
# Les résultats des additions doivent avoir au plus 1 chiffre 
# après la virgule, la soustraction 2 chiffres après la virgule
# et la division 3 chiffres après la virgule.

def operation():

    n1 = float(input("Entrer un nombre: "))
    n2 = float(input("Entrer un nombre: "))

    addition = round((n1 + n2),1)
    soustraction = round((n1 - n2),1)
    division = round((n1/n2),1)

    return addition, soustraction, division

a, b, c = operation()

print(f"Addition {a}, soustraction {b}, division {c}")

operation()