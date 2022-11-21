#Exercice 1:

# Créer une liste contenant tous les nombres premiers entre 2 et 20. 
#Ensuite, demander à l'utilisateur d'écrire un nombre entre 2 et 20 
#(bien vérifier si c'est le cas) et vérifier si ce nombre est premier 
#à l'aide de votre liste en affichant le résultat à la console


def verifier_premier():

    
    premiers = [2, 3, 5, 7, 11, 13, 17, 19]
    condition = False
    while not condition:
        user_input = int(input("Entrer nombre premier entre 2 et 20: "))
        if 2 <= user_input <= 20:
            if user_input in premiers:
                condition = True
                print("Votre nombre est premier")
            else:
                print("Votre nombres n'est pas premier")
    
verifier_premier()