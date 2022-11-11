# Écrire une fonction prenant deux nombres et vérifiant si le premier nombre est plus petit que le deuxième, 
# si ce n'est pas le cas, les retourner dans l'ordre inverse. Ex.: fonction(4, 3) retournerait 3 et, ensuite, 4.

def type_nombre(n1, n2):
    
    if n1 <= n2:
        return n1, n2
    else:
        return n2, n1
    
#resultat = type_nombre()

print(type_nombre(17, 9))
