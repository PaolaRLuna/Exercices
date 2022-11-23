# data1 = ['Équipe A', 9.25, 9.0, 9.13, 8.5, 10.0]
# data2 = ['Équipe B', 8.25, 9.0, 9.28, 7.9, 11.0]
# date3 = ['Équipe C', 7.11, 6.5, 11.12, 8.0, 13.0]

def read_data1():
    with open("Semaine-6/Lab2tests/data1.txt","r", encoding='utf8') as file:
        lines = file.read().splitlines()
    
        data1 = []
        for data in lines:
            if "." in data:
                data = float(data)
            else:
                if data.isnumeric():
                    data = float(data)

            data1.append(data)
    return data1


def read_data2():
    with open("Semaine-6/Lab2tests/data2.txt","r", encoding='utf8') as file:
        lines = file.read().splitlines()
    
        data2 = []
        for data in lines:
            if "." in data:
                data = float(data)
            else:
                if data.isnumeric():
                    data = float(data)

            data2.append(data)
    return data2


def read_data3():
    with open("Semaine-6/Lab2tests/data3.txt","r", encoding='utf8') as file:
        lines = file.read().splitlines()
    
        data3 = []
        for data in lines:
            if "." in data:
                data = float(data)
            else:
                if data.isnumeric():
                    data = float(data)

            data3.append(data)
    return data3

# def moyenne(data1, data2, data3):

#     data = data1, data2, data3
#     equipes = data1[0], data2[0], data3[0]

#     avgs = []
#     for value in data:
#         avg = sum(value[1:]) / len(value[1:])
#         avgs.append(avg)

#     moy_equipe = zip(avgs, equipes)
#     moy_equipe = sorted(moy_equipe)

#     return moy_equipe

#moyenne(read_data1(),read_data2(), read_data3())
def get_moyenne(data1, data2, data3):
    data = data1, data2, data3
    # equipes = data1[0], data2[0], data3[0]

    avgs= []
    for i in data:
        equipe = i[1:]
        sum = 0
        for j in equipe:
            sum = sum + j
        moyenne = sum / len(equipe)
        avgs.append(moyenne)
    return avgs


def ecart_type(data1, data2, data3):

    data = data1, data2, data3
    equipes = data1[0], data2[0], data3[0]
    mean = get_moyenne(read_data1(),read_data2(), read_data3())
    
    eq = []
    for i in data:
        equipe = i[1:]
        eq.append(equipe)

    ecarts = []
    tup = zip(eq, mean)
    for equipe, m in tup:
        sum = 0
        nb_donnees = len(equipe) - 1
        for item in equipe:
            oper = item - m
            sum += oper ** 2
        ec_t = (sum / nb_donnees) ** 0.5
        ecarts.append(ec_t)

    ecart = list(zip(ecarts, equipes))

    return ecart


def minimum():

    ecarts = ecart_type(read_data1(),read_data2(), read_data3())
    
    min_number = ecarts[0]

    for ecart in ecarts:
        if ecart[0] < min_number[0]:
            min_number = ecart
    return min_number

def affichage_homogene():
    
    ecart, equipe = minimum()
    print(f"{equipe}, écart type: {ecart:.3f}")

def menu_utilisateur():

    menu = {1 : "Afficher les statistiques", 
            2 : "afficher l'équipe la plus homogène",
            3 : "Ajouter une faute à une équipe", 
            4 : "Sauvegarder les statistiques",
            5 : "Sortir" }

    for key, value in menu.items():
        print(f"{key}.{value}")

    choix_user = int(input("Choisir une option: "))
    condition = False
    while not condition:
        if choix_user == 1:
            condition = True
            affichage_homogene()
        elif choix_user == 3:
            submenu()

def submenu():

    condition = False
    while not condition:
        
        opt_equipe = ["a", "b", "c"]
        print("\n SUB MENU")
        faute_input = input("Écrire lettre de l'équipe (A, B ou C): ").lower()
        if faute_input in opt_equipe:
            condition = True
            nb_fautes = input("Ecrire le nb de jouer (): ")
            print(nb_fautes)
        else:
            print("Invalid option")

        # with open('fautes_équipe_'+faute_input+'.txt', "w") as file:
        #     nb_fautes

menu_utilisateur()
