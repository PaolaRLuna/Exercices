# Offrir à l'utilisateur d'entrer un nom de fichier et un nombre illimité de nombres positifs, tant et aussi longtemps qu'il ne rentre pas un nombre négatif. 
# Ajouter les nombres entrés par l'utilisateur à une liste en excluant le nombre négatif. Ensuite, écrire les résultats suivants dans le fichier nommé par l'utilisateur:

# La liste en ordre croissant
# La liste en ordre décroissant
# Le maximum
# Le minimum
# La moyenne de la liste
# La médiane (la valeur à la position centrale si la longueur de la liste est impaire et la moyenne des deux valeurs centrales si paire)
# Ex: 1, 2, 3, 5, 4. Médiane = 3.
# Ex: 1, 2, 3, 4, 5, 6. Médiane = 3.5
# Le mode (l'occurrence la plus fréquente s'il y a lieu. Si chaque entrée est unique, inscrire que le mode = none)
# Ex: 1, 2, 2, 2, 3, 4, 3, 4. La mode = 2

#Inspiration: https://stackoverflow.com/questions/31593212/how-to-take-any-number-of-inputs-in-python-without-defining-any-limit
#https://stackoverflow.com/questions/3011680/take-user-input-and-put-it-into-a-file-in-python

def menu():

    filename = input("Entrer un nom de fichier: ")
    with open(filename, "") as file:
        file.write(filename)
  
    condition = False
    while not condition:
        u_input = input("Entre un nombre: ")
        inputs = []
        if u_input == "":
            condition = True
        inputs.append(int(u_input))

