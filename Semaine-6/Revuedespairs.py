# Partie 1:
# Créer un dictionnaire possédant les cours que vous suivez cette session 
# et leur enseignant respectif. Par exemple:

# Keven Presseau-St-Laurent - Concepts de programmation 1

# Ensuite, afficher un menu à la console présentant les 3 cours et offrant
#  à l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa 
# sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

def menu_dict():

    print("\nMENU")
    cours = { 1 : "Concepts de programmation 1",
            2 : "Logique mathématique",
            3 : "Systèmes d'exploitation",
            4 : "Anglais de niveau collégial"
            }

    for key, value in cours.items():
        print(f"{key}.{value}")

    prof = { 1 : "Keven Presseau-St-Laurent",
             2: "Nicolas Thavonekham Robidoux" ,
             3: "Keven Presseau-St-Laurent",
             4 : "Anna Claudia Onofri" 
            }

    condition = False
    while not condition:

        user_input = input("Choisir un numéro (Ex. 1) pour afficher l'enseignant: ")
        if user_input == "1":
            #condition = True
            print(f"{prof.get(1)}")
        elif user_input == "2":
            #condition = True
            print(f"{prof.get(2)}")
        elif user_input == "3":
            #condition = True
            print(f"{prof.get(3)}")
        elif user_input == "4":
            #condition = True
            print(f"{prof.get(4)}")
        else:
            condition = True

    return cours, prof

# Partie 2:
# En se basant sur la partie 1, créer un fichier bdd.txt fonctionnant comme une base de données et remplir le dictionnaire à 
# partir de ce fichier. Pour vous faciliter la tâche, vous pouvez écrire les informations de la manière suivante:
# Nom de cours 1
# Nom de prof 1
# Nom de cours 2
#ds1: dict[int, str]

def fichier():

    cours, prof = menu_dict()

    infos = {}
    for c, p in list(zip(cours.values(), prof.values())):
        infos [c] = p

    with open("bdd.txt", "w", encoding='utf8') as fichier:

        #https://stackoverflow.com/questions/34069702/write-dict-to-file-with-each-key-value-pair-on-a-separate-line
        #Auteur: JCVanHamme
        #Idée de comment imprimer dans un fichier à partir du dictionnaire
        for matiere, prof in infos.items():
            print(f"{matiere} \n{prof}", file=fichier)

    return infos

def search():

    donnees = fichier()

    search_user = input("Entrer nombre d'enseignant: ")
    for value in donnees:
        if search_user in donnees.values():
            print(f"L'enseignant {value} est dans la liste")

search()
# Partie 3:

#En se basant sur la partie 2, modifier le menu utilisateur en y ajoutant une option lui permettant de faire une recherche d'enseignant. 
# Vérifier si l'enseignant entré par l'utilisateur est présent dans votre liste de cours et indiquer le résultat à la console.        

# def output():

#     option, menu = menu_dict()
#     print(f"Cours: {option}")
#     fichier(menu)

# if __name__ == '__main__':
#     output()