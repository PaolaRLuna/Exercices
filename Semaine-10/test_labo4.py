def read_db():
    bd = {}
    with open ("Semaine-10/bd.txt","r", encoding='utf8') as f:
        for line in f.read().splitlines()[1:]: # en vez de readlines(), porque este ultimo te da un \n al final si se lee de esta manera
            (key,value) = line.split("\t", maxsplit=1)
            bd[int(key)] = [val for val in value.split("\t") if val]
    return bd

read_db()

#https://stackoverflow.com/questions/67649685/add-keys-and-values-from-a-text-file-to-a-dictionary
#https://stackoverflow.com/questions/17038426/splitting-a-string-based-on-tab-in-the-file

# def compte_utilisateur():

#     sortie = False
#     while not sortie:
#         user_input = input("Choisir un numéro à 4 chiffres (Ex. 1234): ")
#         if len(user_input) != 4 or not user_input.isdigit():
#             print("You must enter 4 digits or the input is not a digit")
#             sortie = False
#         else:
#             mot_de_passe = input("Entrer un mot de passe :")
#             sortie = True

#     if user_input == 0000 and mot_de_passe == "admin":
#         pass

# def choisir_compte():
#     compte_utilisateur()
#     choisir = { 1 : "Cheque",
#             2 : "Épargne",
#             3 : "Placement",
#             }
        
#     sortie = False
#     while not sortie:

#         print("\nMENU")
#         for key, value in choisir.items():
#             print(f"{key}.{value}")
#         compte_input = input("Choisir un numéro (Ex. 1)")

#         if compte_input in choisir.keys():
#             sortie = True
#         else:
#             print("Choix invalide")