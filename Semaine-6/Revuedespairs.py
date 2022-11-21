# Partie 1:
# Créer un dictionnaire possédant les cours que vous suivez cette session 
# et leur enseignant respectif. Par exemple:

# Keven Presseau-St-Laurent - Concepts de programmation 1

# Ensuite, afficher un menu à la console présentant les 3 cours et offrant
#  à l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa 
# sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

def menu_dict():
    print("Cours:")
    menu = { 1 : "Keven Presseau-St-Laurent - Concepts de programmation 1",
            2 : "Nicolas Thavonekham Robidoux - Logique mathématique pour l'informatique",
            3 : "Keven Presseau-St-Laurent - Systèmes d'exploitation",
            4 : "Anna Claudia Onofri - Anglais de niveau collégial"
            }

    condition = False
    while not condition:

        user_input = int(input("Choisir un nombre entre 1 et 4, si vous chercher un enseignant la lettre 'C': "))
        if user_input in menu:
            condition = True
            option = (menu[user_input])
        elif user_input == "C":
            condition = True
            search(menu)
        
    return option, menu

# Partie 2:
# En se basant sur l'exercice 3, créer un fichier bdd.txt fonctionnant comme une base de données et remplir le dictionnaire à 
# partir de ce fichier. Pour vous faciliter la tâche, vous pouvez écrire les informations de la manière suivante:
# Nom de cours 1
# Nom de prof 1
# Nom de cours 2

def fichier(donnees: dict[int, str]):

    with open("bdd", "w") as file:

        delimiter = ""
        for value in donnees.values():
            cle = delimiter.join(i for i in value) + "\n"
            file.write(cle)


def search(donnees: dict[int, str]):

    search_user = input("Entrer nombre d'enseignant: ")
    for value in donnees.values():
        if search_user in donnees:
            print(f"L'enseignant {value} est dans la liste")

# Partie 3:

#En se basant sur la partie 2, modifier le menu utilisateur en y ajoutant une option lui permettant de faire une recherche d'enseignant. 
# Vérifier si l'enseignant entré par l'utilisateur est présent dans votre liste de cours et indiquer le résultat à la console.        

def output():

    option, menu = menu_dict()
    print(f"Cours: {option}")
    fichier(menu)

if __name__ == '__main__':
    output()