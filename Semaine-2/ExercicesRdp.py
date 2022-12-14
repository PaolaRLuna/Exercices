# Exercice 1, Partie 1:
# Créer une calculatrice pour fractions incluant les opérations suivantes: 

# Addition (a/b + d/c)
# Soustraction (a/b - d/c)
# Multiplication (a/b * d/c)
# Divisions (a/b / d/c)

# Exercice 1, Partie 2:
# Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).

def calcul(fraction1, fraction2):
    fraction1 = num1/den1
    fraction2 = num2/den2

    #Partie 1:

    addition = (fraction1 + fraction2)
    soustraction = (fraction1 - fraction2)
    multiplication = (fraction1 * fraction2)
    division = (fraction1 / fraction2)
    
    return addition, soustraction, multiplication, division

fraction1 = 4, 3 # Forme n1/d1, example: 3/4
fraction2 = 8, 7 # Forme n2/d2, example: 2/3

num1, den1 = fraction1
num2, den2 = fraction2
resultat = calcul(fraction1, fraction2)

# Exercice 1, Partie 3:

# Affichez vos résultats sous forme de fraction et sous forme d'un float.

add, sous, mult, div = resultat
print(f"Addition: \n- Fraction: {(num1*den2 + den1*num2)}/{(den1 * den2)} \n- Float: ", add)
print(f"Soustraction: \n- Fraction: {(num1*den2 - den1*num2)}/{(den1 * den2)} \n- Float: ", sous)
print(f"Multiplication: \n- Fraction: {num1 * num2}/{den1 * den2} \n- Float: ", mult)
print(f"Division: \n- Fraction: {num1 * den2}/{den1 * num2} \n- Float: ",div)

# Testez vos fonctions avec plusieurs fractions pour vous assurer du bon fonctionnement.
