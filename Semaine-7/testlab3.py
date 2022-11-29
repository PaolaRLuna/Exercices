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
            paquet = brassage_intercoupe(paquet)
            print(paquet)
        elif user_input == "2":
            paquet = brassage_intercoupe(paquet)
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
    #packagefour = len(cartes) // 13

    deck_brasse = []
    for i in range(1, len(cartes), 4):
        deck_brasse = cartes[i : i + 4]
        deck_brasse.append()

    #https://stackoverflow.com/questions/65773707/how-to-change-the-index-of-an-element-in-a-list-array-to-another-position-index
    #Auteur: Grigol Peradze
    #Comment changer l'index d'un element dans une liste à une autre position.
    order = [7, 1, 3, 13, 2, 4, 11, 6, 8, 5, 12, 10, 9]
    deck_brasse_update = [deck_brasse[idx] for idx in order]

    return deck_brasse_update

menu_utilisateur()