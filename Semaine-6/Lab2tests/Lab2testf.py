def read_data1():
    with open("data1.txt","r", encoding='utf8') as file:
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
    with open("data2.txt","r", encoding='utf8') as file:
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
    with open("data3.txt","r", encoding='utf8') as file:
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

def menu_utilisateur():

    menu = {1 : "Afficher les statistiques", 
            2 : "Afficher l'équipe la plus homogène",
            3 : "Ajouter une faute à une équipe", 
            4 : "Sauvegarder les statistiques",
            5 : "Sortir" }

    print('\n MENU')
    for key, value in menu.items():
        print(f"{key}.{value}")

    condition = False
    while not condition:
        choix_user = input("Choisir une option: ")
        if choix_user == "1":
            condition = True
            affichage_stats()
        elif choix_user == "2":
            affichage_homogene()
            condition = True
        elif choix_user == "3":
            submenu()
            condition = True
        elif choix_user == "4":
            sauvegarde_stats()
            condition = True
        elif choix_user == "5":
            condition = True
            exit()
        else:
            print("Option invalide")
        

def plus_rapide(data1, data2, data3):

    data = data1, data2, data3
    equipes = data1[0], data2[0], data3[0]

    maxlist = []
    for value in data:
        max_val = max(value[1:])
        maxlist.append(max_val)

    max_equipe = zip(equipes,maxlist)
    equipe_rapide = max(max_equipe)

    return equipe_rapide


def moyenne_trie():
    data1, data2, data3 = read_data1(),read_data2(), read_data3()
    avgs = get_moyenne(read_data1(),read_data2(), read_data3())
    equipes = data1[0], data2[0], data3[0]

    moy_equipe = zip(avgs, equipes)
    moy_equipe = sorted(moy_equipe)

    return moy_equipe
    

def coureur_rapide():

    equipe = plus_rapide(read_data1(),read_data2(), read_data3())
    gagnant = equipe[0],equipe[1]
    return gagnant

def get_moyenne(data1, data2, data3):
    data = data1, data2, data3

    avgs= []
    for i in data:
        equipe = i[1:]
        sum = 0
        for j in equipe:
            sum = sum + j
        moyenne = sum / len(equipe)
        avgs.append(moyenne)
    return avgs

def moyenne_trie():
    data1, data2, data3 = read_data1(),read_data2(), read_data3()
    avgs = get_moyenne(read_data1(),read_data2(), read_data3())
    equipes = data1[0], data2[0], data3[0]

    moy_equipe = zip(avgs, equipes)
    moy_equipe = sorted(moy_equipe)

    return moy_equipe

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

def affichage_stats():

    moy_equipe = moyenne_trie()
    
    for moy, equipe in moy_equipe:
        print(f"{equipe}: {moy:.2f}s")

    eq, sec = coureur_rapide()
    print(f"Coureur gagnant: {eq} ({sec} secondes)")

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

def submenu():

    condition = False
    while not condition:
        
        opt_equipe = ["A", "B", "C"]
        print("\nSUB MENU")
        faute_input = input("Écrire la lettre de l'équipe (A, B ou C) ou autre chose pour retourner: ").upper()
        if faute_input in opt_equipe:
            while not condition:
                nb_fautes = input("Écrire le # de joueur suivi de sa faute, separer avec virgule (,) si plusieurs joueurs (Ex. 23 - faute offensive, 2-offensive): ").split(",")
                if nb_fautes == ['']:
                    condition = False
                else:
                    with open('fautes_équipe_'+ faute_input +'.txt', "w") as file:
                        delimiter = ""
                        for item in nb_fautes:
                            faute = delimiter.join(i for i in item) + "\n"
                            file.write(faute)
                            condition = True
                            print('Fichier .txt crée')
        else:
            condition = True
            menu_utilisateur()


def sauvegarde_stats():

    moy_equipe = moyenne_trie()
    fastest = coureur_rapide()

    statsfile = open("stats.txt", "w", encoding='utf8')

    print(f"Coureur rapide: {fastest}",file=statsfile)
    for m in moy_equipe:
        print(f"Moyenne: {m}", file=statsfile)
    
    print("Fichier stats.txt crée")
    statsfile.close()

menu_utilisateur()