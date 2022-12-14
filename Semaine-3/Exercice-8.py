# Exercice 8:

# Partie 1:

# Reprendre l'exercice de la calculatrice de fraction, et implémenter un menu permettant à l'utilisateur d'effectuer
# les opérations définies et retourner les résultats sous forme de fraction réduite et sous forme de float avec 3 chiffres
# après la virgule.


# def calcul(fraction1, fraction2):
#     fraction1 = num1/den1
#     fraction2 = num2/den2

#     addition = (fraction1 + fraction2)
#     soustraction = (fraction1 - fraction2)
#     multiplication = (fraction1 * fraction2)
#     division = (fraction1 / fraction2)

#     return addition, soustraction, multiplication, division


# def user_input():
#     def input_fraction():
#         num = int(input("Num: "))
#         den = int(input("Denom: "))
#         return num, den

#     print("Entrer nombres fraction 1: ")
#     fraction1 = input_fraction()
#     print("Entrer nombres fraction 2: ")
#     fraction2 = input_fraction()
#     return fraction1, fraction2


# fraction1, fraction2 = user_input()
# num1, den1 = fraction1
# num2, den2 = fraction2

# resultat = calcul(fraction1, fraction2)

# add, sous, mult, div = resultat
# print(
#     f"Addition: \n- Fraction: {(num1*den2 + den1*num2)}/{(den1 * den2)} \n- Float:  {add:.3f}")
# print(
#     f"Soustraction: \n- Fraction: {(num1*den2 - den1*num2)}/{(den1 * den2)} \n- Float: {sous:.3f}")
# print(
#     f"Multiplication: \n- Fraction: {num1 * num2}/{den1 * den2} \n- Float: {mult:.3f}")
# print(f"Division: \n- Fraction: {num1 * den2}/{den1 * num2} \n- Float: {div:.3f}")


# Partie 2:

# Modifiez votre fonction de sorte que l'opération entrée par l'utilisateur vous permette de sélectionner la
# bonne fonction en utilisant l'instruction match au lieu de plusieurs if.
#Dentro de match en la linea de la indentacion de case se puede imprimir directamente, print(f' etc),
# Definir cada operacion y desoupes llamar a cada operacion y es importante de habilitar la operacion para un float


def addition(num1, den1, num2, den2):
    num = num1*den2 + den1*num2
    denum = den1 * den2
    return num/denum

def soustraction(num1, den1, num2, den2):
    num = num1*den2 - den1*num2
    denum = den1 * den2
    return num/denum

def produit(num1, den1, num2, den2):
    num = num1 * num2
    denum = den1 * den2
    return num/denum

def division(num1, den1, num2, den2):
    num = num1 * den2
    denum = den1 * num2
    return num/denum

def calcul(fraction1, fraction2):
    num1, den1 = fraction1
    num2, den2 = fraction2

    o1 = addition(num1, den1, num2, den2)
    o2 = soustraction(num1, den1, num2, den2)
    o3 = produit(num1, den1, num2, den2)
    o4 = division(num1, den1, num2, den2)
    return o1, o2, o3, o4 
    

def input_operation():

    fraction1, fraction2, operation = user_input()
    o1, o2, o3, o4 = calcul(fraction1, fraction2)
    

    match operation:
        case "1":
            resultat = o1
        case "2":
            resultat = o2
        case "3":
            resultat = o3
        case "4":
            resultat = o4
    
    return f'The result is {resultat}'


def user_input():
    def input_fraction():
        num = int(input("Num: "))
        den = int(input("Denom: "))
        return num, den

    print("1.Addition \n2.Soustraction \n3.Produit \n4.Division")
    operation = input("Entrer type d'operation: ")
    print("Entrer nombres fraction 1: ")
    fraction1 = input_fraction()
    print("Entrer nombres fraction 2: ")
    fraction2 = input_fraction()
    return fraction1, fraction2, operation

#print(user_input())

print(input_operation())


