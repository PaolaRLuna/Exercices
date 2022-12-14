def creation_cartes():

    SUITS = ("♦", "♣", "♥", "♠")

    CARD_TYPE = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    card_deck = []
    for suit in SUITS:
        for card in CARD_TYPE:
            deck = card + suit
            card_deck.append(deck)

    return card_deck

def menu_utilisateur():

    paquet = creation_cartes()

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
        else:
            condition = True
            sauvegarder_fichier(paquet)

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
        deck_brasse_update.extend(paquet) # adds at the end without the brackets

    # deck_entier = []
    # for cartes in deck_brasse_update:
    #     for carte in cartes:
    #         deck_entier.append(carte)

    return deck_brasse_update

def affichage_etat_jeu(cartes:list[str]):
    
    paquet_long = 13
    for carte in range(0, len(cartes), paquet_long):
        ligne = cartes[carte: carte + paquet_long]
        print(" ".join(ligne))
    
    # carte_split = [cartes[carte: carte + paquet_long] for carte in range(0,len(cartes),paquet_long)]
    # print("\n".join(carte_split))

def sauvegarder_fichier(cartes:list[str]):

    with open('cards.txt', "w", encoding='utf8') as fichier:
        
        for carte in range(0, len(cartes), 13):
            ligne = cartes[carte: carte + 13]
            #https://stackoverflow.com/questions/50608207/print-5-elements-of-a-list-per-line
            #Auteur:
            #Idee de comment utiliser modulo pour imprimer
            for i, card in enumerate(ligne):
                if (i + 1) % 13 == 0:
                    print(card + "\n", file=fichier)
                else:
                    print(card, end=" ", file=fichier)
    
        print('Fichier .txt cree')

menu_utilisateur()