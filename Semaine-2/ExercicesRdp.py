# xercice 1, Partie 1:

# Créer une calculatrice pour fractions incluant les opérations suivantes: 

# Addition (a/b + d/c)
# Soustraction (a/b - d/c)
# Multiplication (a/b * d/c)
# Divisions (a/b / d/c)

# Exercice 1, Partie 2:

# Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).

def calcul(fraction1, fraction2):
    n1, n2 = fraction1
    n3, n4 = fraction2

    fraction1 = n1/n2
    fraction2 = n3/n4

    addition = (fraction1 + fraction2)
    soustraction = (fraction1 - fraction2)
    multiplication = (fraction1 * fraction2)
    division = (fraction1 / fraction2)
    
    return addition, soustraction, multiplication, division

fraction1 = 3, 4
fraction2 = 2, 3 
print(calcul(fraction1, fraction2))

#print(str(fraction1[0]) + "/" + str(fraction1[1]), fraction1[0]/fraction1[1])


# Exercice 1, Partie 3:

# Affichez vos résultats sous forme de fraction et sous forme d'un float.

# Testez vos fonctions avec plusieurs fractions pour vous assurer du bon fonctionnement.

#
# 