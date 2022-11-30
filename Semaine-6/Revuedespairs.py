# Partie 1:
# Créer un dictionnaire possédant les cours que vous suivez cette session 
# et leur enseignant respectif. Par exemple:

# Keven Presseau-St-Laurent - Concepts de programmation 1

# Ensuite, afficher un menu à la console présentant les 3 cours et offrant
#  à l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa 
# sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

def data():
   
    cours = { 1 : "Concepts de programmation 1",
            2 : "Logique mathématique",
            3 : "Systèmes d'exploitation",
            4 : "Anglais de niveau collégial"
            }

    prof = { 1 : "Keven Presseau-St-Laurent",
             2: "Nicolas Thavonekham Robidoux" ,
             3: "Keven Presseau-St-Laurent",
             4 : "Anna Claudia Onofri" 
            }

    return cours, prof

def fichier():

    _, cours, prof = data()
    courses = cours.values()
    profs = prof.values()

    infos = {}
    for c, p in list(zip(courses, profs)):
        infos [c] = p

    with open("bdd.txt", "w", encoding='utf8') as fichier:

        #https://stackoverflow.com/questions/34069702/write-dict-to-file-with-each-key-value-pair-on-a-separate-line
        #Auteur: JCVanHamme
        #Idée de comment imprimer dans un fichier à partir du dictionnaire
        for matiere, prof in infos.items():
            print(f"{matiere} \n{prof}", file=fichier)

    return infos

def read_file():
    
    pass

def menu():

    choisir = { 1 : "Choisir un cours",
            2 : "Chercher un enseignant",
            3 : "Ajouter un cours et un prof"
            }

    condition = False
    while not condition:

        print("\nMENU")
        for key, value in choisir.items():
            print(f"{key}.{value}")

        user_input = input("Choisir un numéro (Ex. 1): ")
        if user_input == "1":
            submenu_choisir()
        elif user_input == "2":
            search(fichier())
        elif user_input == "3":
            input_user()
        else:
            condition = True

def submenu_choisir():

    _, cours, prof = data()
        
    print("\nSUB MENU")
    for key, value in cours.items():
        print(f"{key}.{value}")

    condition = False
    while not condition:
        user_input = input("Choisir un cours (Ex. 1): ")
        if user_input == "1":
            condition = True
            print(f"{cours.get(1)} - {prof.get(1)}")
        elif user_input == "2":
            condition = True
            print(f"{cours.get(2)} - {prof.get(2)}")
        elif user_input == "3":
            condition = True
            print(f"{cours.get(3)} - {prof.get(3)}")
        elif user_input == "4":
            condition = True
            print(f"{cours.get(4)} - {prof.get(4)}")
# Partie 2:
# En se basant sur la partie 1, créer un fichier bdd.txt fonctionnant comme une base de données et remplir le dictionnaire à 
# partir de ce fichier. Pour vous faciliter la tâche, vous pouvez écrire les informations de la manière suivante:
# Nom de cours 1
# Nom de prof 1
# Nom de cours 2
#ds1: dict[int, str]

# Partie 3:

#En se basant sur la partie 2, modifier le menu utilisateur en y ajoutant une option lui permettant de faire une recherche d'enseignant. 
# Vérifier si l'enseignant entré par l'utilisateur est présent dans votre liste de cours et indiquer le résultat à la console.     

def search(donnees:dict[str,str]):

    condition = False
    while not condition:
        search_user = input("Entrer nombre d'enseignant: ")

        if search_user == '':
            condition = True
        #https://stackoverflow.com/questions/18763905/print-out-message-only-once-from-the-for-loop
        #Auteur: HennyH
        #Idee de comment retourner une seule fois un print
        elif any(search_user in value for value in donnees.values()):
            print(f"L'enseignant {search_user} est dans la liste")
            condition = True
        else:
            print("Not found")


menu()

# Partie 4:

# Offrir à l'utilisateur une nouvelle option au menu lui permettant d'ajouter un cours et un nom d'enseignant à la base de données de la partie 2. 
# Une fois les données utilisateurs entrées, ajouter les informations à la fin du document bdd.txt

def input_user():

    cours, prof = data()

    with open("bdd.txt","a", encoding='utf8') as append_file:
        infos = fichier()
        condition = False
        while not condition:
            ajout_cours = input("Ajouter un nom de cours: ")
            ajout_enseignant = input("Ajouter un enseignant")
            infos[ajout_cours] = ajout_enseignant

        #with open("bdd.txt", "a", encoding='utf8') as fichier:

# if __name__ == '__main__':
#     output()
