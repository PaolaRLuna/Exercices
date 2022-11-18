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
# https://stackoverflow.com/questions/66333471/read-and-save-list-of-numbers-as-numbers-in-txt-files-in-python

def create_input():

    filename = input("Entrer un nom de fichier: ")
    with open(filename, "w") as file:

        inputs = []
        #condition = False
        while True:
            u_input = input("Entre un nombre positif: ")

            if u_input == "":
                break #condition = True
            elif int(u_input) > 0:
                inputs.append(str(u_input))
            else:
                True

        delimiter = ","
        for item in inputs:
            value = delimiter.join(i for i in item) + "\n"
            file.write(value)

create_input()

def 