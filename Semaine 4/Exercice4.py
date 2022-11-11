# Écrire un programme avec une fonction prenant 2 floats et 
# retournant leur addition soustraction et division. 
# Les résultats des additions doivent avoir au plus 1 chiffre 
# après la virgule, la soustraction 2 chiffres après la virgule
# et la division 3 chiffres après la virgule.

# demande pas de input, pas d'utilisateur, pas de input

def operation(n1, n2):

    addition = round((n1 + n2),1)
    soustraction = round((n1 - n2),2)
    division = round((n1/n2),3)

    return addition, soustraction, division

n1, n2 = 1.235, 456.2185
a, b, c = operation(n1, n2)

print(f"Addition {a}, soustraction {b}, division {c}")

# writing operation() at the end calls once agan the function,
# which is not necessary because a,b,c are already calling
# the function above