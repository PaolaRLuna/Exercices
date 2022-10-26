# xercice 1, Partie 1:

# Créer une calculatrice pour fractions incluant les opérations suivantes: 

# Addition (a/b + d/c)
# Soustraction (a/b - d/c)
# Multiplication (a/b * d/c)
# Divisions (a/b / d/c)

def calcul(a,b,c,d):
    add = (a/b + c/d)
    sustrac = (a/b - d/c)
    produit = (a/b * d/c)
    div = (a/b / d/c)
    return add,sustrac,produit,div
print(calcul(1,2,3,4))

# Exercice 1, Partie 2:

# Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).



# Exercice 1, Partie 3:

# Affichez vos résultats sous forme de fraction et sous forme d'un float.

# Testez vos fonctions avec plusieurs fractions pour vous assurer du bon fonctionnement.