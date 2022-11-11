# Écrire un programme demandant un entier à un utilisateur 
# et lui retournant sa parité. Ex.: Le nombre «4» est paire.

def parite():

    nombre = int(input("Entrer un entier: "))

    if nombre % 2 == 0:
        return f"Le nombre {nombre} est pair"
    else:
        return f"Le nombre {nombre} est impair"

print(parite())