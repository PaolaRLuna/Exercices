# Exercice 8:

# Partie 1:

# Reprendre l'exercice de la calculatrice de fraction, et implémenter un menu permettant à l'utilisateur d'effectuer
# les opérations définies et retourner les résultats sous forme de fraction réduite et sous forme de float avec 3 chiffres
# après la virgule.


def calcul(fraction1, fraction2):
    fraction1 = num1/den1
    fraction2 = num2/den2

    addition = (fraction1 + fraction2)
    soustraction = (fraction1 - fraction2)
    multiplication = (fraction1 * fraction2)
    division = (fraction1 / fraction2)

    return addition, soustraction, multiplication, division


def user_input():
    def input_fraction():
        num = int(input("Num: "))
        den = int(input("Denom: "))
        return num, den

    print("Entrer nombres fraction 1: ")
    fraction1 = input_fraction()
    print("Entrer nombres fraction 2: ")
    fraction2 = input_fraction()
    return fraction1, fraction2


fraction1, fraction2 = user_input()
num1, den1 = fraction1
num2, den2 = fraction2

resultat = calcul(fraction1, fraction2)

add, sous, mult, div = resultat
print(
    f"Addition: \n- Fraction: {(num1*den2 + den1*num2)}/{(den1 * den2)} \n- Float: ", add)
print(
    f"Soustraction: \n- Fraction: {(num1*den2 - den1*num2)}/{(den1 * den2)} \n- Float: ", sous)
print(
    f"Multiplication: \n- Fraction: {num1 * num2}/{den1 * den2} \n- Float: ", mult)
print(f"Division: \n- Fraction: {num1 * den2}/{den1 * num2} \n- Float: ", div)


# Partie 2:

# Modifiez votre fonction de sorte que l'opération entrée par l'utilisateur vous permette de sélectionner la
# bonne fonction en utilisant l'instruction match au lieu de plusieurs if.
#Dentro de match en la linea de la indentacion de case se puede imprimir directamente, print(f' etc),
# Definir cada operacion y desoupes llamar a cada operacion y es importante de habilitar la operacion para un float

def calcul():
    fraction1 = num1/den1
    fraction2 = num2/den2


    def input_operation(operation, fraction1, fraction2):
        #""
        resultat = ""
        match(operation):
            case("+"):
                resultat = addition(fraction1, fraction2)
                return f'Resultat: {resultat}'
            case("-"):
                resultat = soustraction(fraction1,fraction2)
                return resultat
            case ("*"):
                resultat = produit(fraction1,fraction2)
                return resultat
            case("/"):
                resultat = division(fraction1,fraction2)
                return resultat

        if operation_type() == addition:
            return fraction1 + fraction2

        elif operation == soustraction:
            return fraction1 - fraction2

        elif operation == produit:
            return fraction1 * fraction2

        elif operation == division:
            return fraction1 / fraction2
    print(resultat)
    return 


def user_input():
    def operation_type():
        def input_fraction():
            num = int(input("Num: "))
            den = int(input("Denom: "))
            return num, den

        print("Entrer type d'operation: ")
        operation = input_fraction()
        
        return operation
    print("Entrer nombres fraction 1: ")
    fraction1 = input_fraction()
    print("Entrer nombres fraction 2: ")
    fraction2 = input_fraction()
    return fraction1, fraction2

fraction1, fraction2 = user_input()
num1, den1 = fraction1
num2, den2 = fraction2

resultat = calcul(fraction1, fraction2)

add, sous, mult, div = resultat
print(
    f"Addition: \n- Fraction: {(num1*den2 + den1*num2)}/{(den1 * den2)} \n- Float: ", add)
print(
    f"Soustraction: \n- Fraction: {(num1*den2 - den1*num2)}/{(den1 * den2)} \n- Float: ", sous)
print(
    f"Multiplication: \n- Fraction: {num1 * num2}/{den1 * den2} \n- Float: ", mult)
print(f"Division: \n- Fraction: {num1 * den2}/{den1 * num2} \n- Float: ", div)
