# Exercice 5:

# Créer une fonction prenant 4 paramètres et retournant la somme des deux 
# premiers multipliés par le 3ième et divisé par le 4ème.



def fct (a, b, c, d):
    operation = ((a + b) * c) / d
    return operation
#print(fct(1, 2, 3, 1))

# Exercice 6:

# Créer une fonction qui calcule la moyenne de 4 paramètre et qui retourne 
# aussi la somme de ces 4 paramètres.

def fct_moyenne_somme(n1, n2, n3, n4):
    avg = (n1 + n2 + n3 + n4) / 4
    somme = n1 + n2 + n3+ n4
    return avg, somme

#print(fct_moyenne_somme(1,1,1,1))

# Exercice 7:

# Créer une fonction qui permet de calculer la fonction suivante: (x + y) / z.

# Essayer avec z = 0.

def function(x,y,z):
    oper = (x + y) / z
    return oper

#print(function(2,3,0))

# Exercice 8:

# Créer une fonction prenant un seul paramètre 
# retournant le modulo de deux nombres(a modulo b).
#packing unpacking

def modulo(a,b):
    mod = a % b
    return mod 
n = modulo(103,3)
#print(n)

# Exercice 9:

# Créer une fonction permettant de faire la puissance d'un nombre 
# pour ensuite en faire la division. Votre fonction doit prendre 
# de 1 à 3 paramètres, le premier paramètre étant la base, le deuxième 
# paramètre étant l'exposant et le troisième paramètre étant la division.
#  Si aucun exposant n'est donné, faites le carré. Si aucun diviseur 
#  n'est donné, n'effectuez pas de division.
# packing unpacking

def fonction(n1,n2,n3 = 1):
    def puissance(n1,n2 = 2):
        return n1 ** n2
    result  = puissance(n1,n2)
    return result / n3
print(fonction(1,2))

