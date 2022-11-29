# s = "Rayon X"
# y = s[::2]
# print(y)

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

def repeat_func(fonc_brassage):
    
    times = 1
    for i in range(times): fonc_brassage()


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

repeat_func(brassage_intercoupe(creation_cartes()))
