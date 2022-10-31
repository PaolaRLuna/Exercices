# Exercice 1, Partie 1:

# Créer une calculatrice pour fractions incluant les opérations suivantes: 

# Addition (a/b + d/c)
# Soustraction (a/b - d/c)
# Multiplication (a/b * d/c)
# Divisions (a/b / d/c)

# Exercice 1, Partie 2:

# Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).

def calcul(fraction1, fraction2):
    fraction1 = n1/d1
    fraction2 = n2/d2
    # Exercice 1, Partie 1:

    addition = (fraction1 + fraction2)
    soustraction = (fraction1 - fraction2)
    multiplication = (fraction1 * fraction2)
    division = (fraction1 / fraction2)
    
    return addition, soustraction, multiplication, division

fraction1 = 3, 4 # 3/4
fraction2 = 2, 3 # 2/3

n1, d1 = fraction1
n2, d2 = fraction2
resultat = calcul(fraction1, fraction2)
#print(resultat)

# Exercice 1, Partie 3:

# Affichez vos résultats sous forme de fraction et sous forme d'un float.

add, sous, mult, div = resultat
print(f"Addition: \n- Fraction form: {(n1*d2 + d1*n2)}/{(d1 * d2)} ") ; print("- Forme de float: ", add)
print(f"Soustraction: \n- Fraction form: {(n1*d2 - d1*n2)}/{(d1 * d2)} ") ; print("- Forme de float: ", sous)
print(f"Multiplication: \n- Fraction form: {(n1 * n2)}/{(d1 * d2)} ") ; print("- Forme de float: ", mult)
print(f"Division: \n- Fraction  form: {(n1 * d2)}/{(d1 * n2)} ") ; print("- Forme de float: ",div)

# Testez vos fonctions avec plusieurs fractions pour vous assurer du bon fonctionnement.

#
# 