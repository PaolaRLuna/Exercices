def algosomme(a,b,c = 7):
    somme = a + b + c
    soustraction = c - b
    produit = a * b
    return somme, soustraction, produit

result = algosomme(1,8,10)
result1 = algosomme(1,1)
print(result, result1)