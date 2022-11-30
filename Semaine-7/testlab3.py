def creation_cartes():

    SUITS = ("♦", "♣", "♥", "♠")

#    suits = ["D", "C", "H", "S"]
    CARD_TYPE = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    card_deck = []
    for suit in SUITS:
        for card in CARD_TYPE:
            deck = card + suit
            card_deck.append(deck)

    return card_deck

def menu_utilisateur():

    paquet = creation_cartes()
    #print(paquet)
    choix = { 1 : "Afficher l'état du jeu de carte",
            2 : "Effectuer un brassage inter-coupé",
            3 : "Effectuer un brassage par paquets",
            4 : "Sauvegarder l'état final dans un fichier"
    }

    condition = False
    while not condition:
        print("\nMENU")
        for key, value in choix.items():
                print(f"{key}. {value}")

        user_input = input("Choisir un numéro (Ex. 1): ")
        if user_input == "1":
            affichage_etat_jeu(paquet)
        elif user_input == "2":
            paquet = brassage_intercoupe(paquet)
        elif user_input == "3":
            paquet = brassage_paquets(paquet)
            print(paquet)
        else:
            condition = True

def brassage_intercoupe(deck:list[str]):

    half = len(deck) // 2
    paquet1 = deck[:half]
    paquet2 = deck[half:]

    #https://stackoverflow.com/questions/19435476/python-intercalate-lists
    #Auteur:Blender
    #Idee intercalation de listes
    deck_brasse = []
    for i in range(len(paquet1)):
        deck_brasse.append(paquet1[i])
        deck_brasse.append(paquet2[i])

    return deck_brasse

def brassage_paquets(cartes:list[str]):
 
    len_cartes = len(cartes)
    deck_brasse = []
    for i in range(0, len_cartes, 4):
        deck_de_quatre = cartes[i : i + 4]
        deck_brasse.append(deck_de_quatre)

    #https://stackoverflow.com/questions/65773707/how-to-change-the-index-of-an-element-in-a-list-array-to-another-position-index
    #Auteur: Grigol Peradze
    #Idée de comment changer l'index d'un element dans une liste à une autre position.
    order = [7, 1, 3, 13, 2, 4, 11, 6, 8, 5, 12, 10, 9]
    deck_brasse_update = []
    for idx in order:
        paquet = deck_brasse[idx-1]
        deck_brasse_update.extend(paquet)

    # deck_entier = []
    # for cartes in deck_brasse_update:
    #     for carte in cartes:
    #         deck_entier.append(carte)

    return deck_brasse_update

def affichage_etat_jeu(cartes:list[str]):
    
    #https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
    #Auteur: Mateen Ulhaq
    #Idée pour diviser les cartes en 4 lignes de 13
    paquet_long = 13
    for carte in range(0, len(cartes), paquet_long):
        ligne = cartes[carte: carte + paquet_long]
        print(" ".join(ligne))
    
    # carte_split = [cartes[carte: carte + paquet_long] for carte in range(0,len(cartes),paquet_long)]
    # print("\n".join(carte_split))
        #print(f"{ligne}\n", end=' ')
    #    print(' '.join(paquet)+'\n', end=' ')
            #print(f'{cartes[i : i + 13]}')


menu_utilisateur()