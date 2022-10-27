# xercice 1, Partie 1:

# Créer une calculatrice pour fractions incluant les opérations suivantes: 

# Addition (a/b + d/c)
# Soustraction (a/b - d/c)
# Multiplication (a/b * d/c)
# Divisions (a/b / d/c)


def calcul(n1,n2,n3,n4):
    add = (n1/n2 + n3/n4)
    sustrac = (n1/n2 - n3/n4)
    produit = (n1/n2 * n3/n4)
    div = (n1/n2 / n3/n4)
    return add,sustrac,produit,div
#print(calcul(2,3,1,4))

# Exercice 1, Partie 2:

# Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).
def calcul(fraction1, fraction2):
    num1, denum1 = fraction1
    num2, denum2 = fraction2
    
    # ad+bc / bd
    def sum(num1, num2, denum1, denum2):
        num = (num1*denum2) + (num2*denum1)
        den = denum1*denum2
        addition = num / den
        return addition
    #print(f'float form: {sum()}')

    #ad - bc / bd
    def sous(num1, num2, denum1, denum2):
        num = (num1*denum2) - (num2*denum1)
        den = denum1*denum2
        soustraction = num / den
        print(num)#f'Fraction form: {str(num)} / {str(den)} float form: {soustraction}')
        return soustraction

    # ac/bd
    def produit(num1, num2, denum1, denum2):
        num = num1 * num2
        den = denum1 * denum2
        multiplication = num / den
       # print(f'Fraction form: {str(num)} / {str(den)} float form: {multiplication}')
        return multiplication

    # ad/bc
    def div(num1, num2, denum1, denum2):
        num = num1 * denum2
        den = denum1 * num2
        division = num / den
        #print(f'Fraction form: {str(num)} / {str(den)} float form: {division}')
        return division
        
    #print(f'Fraction form: {str()} / {str(den)}')
    return sum (num1,num2,denum1,denum2), sous(num1,num2,denum1,denum2), produit(num1,num2,denum1,denum2), div(num1,num2,denum1,denum2)
    

    

fraction1 = 2, 3
fraction2 = 1, 4
print(calcul(fraction1,fraction2))

        
# Exercice 1, Partie 3:

# Affichez vos résultats sous forme de fraction et sous forme d'un float.

# Testez vos fonctions avec plusieurs fractions pour vous assurer du bon fonctionnement.

#
# 