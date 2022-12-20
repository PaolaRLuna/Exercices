class Cards:
    def __init__(self, cards):
        self.cards = cards

    def afficher(self):
        paquet_long = 13
        for carte in range(0, len(self.cards), paquet_long):
            ligne = self.cards[carte: carte + paquet_long]
            for num, card in enumerate(ligne):
                if (num + 1) % 13 == 0:
                    print(f"{card:>5s}\n")
                else:
                    print(f"{card:>5s}", end="")


class Deck:
    def __init__(self):
        self.cards = []
        self.creation_cartes()

    def creation_cartes(self):
        SUITS = ("♦", "♣", "♥", "♠")
        CARD_TYPE = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        for suit in SUITS:
            for card in CARD_TYPE:
                deck = card + suit
                self.cards.append(deck)
        

class Brassage:
    def __init__(self, deck):
        self.deck = deck

    def brassage_intercoupe(self):

        half = len(self.deck) // 2
        paquet1 = self.deck[:half]
        paquet2 = self.deck[half:]

        deck_brasse = []
        for i in range(len(paquet1)):
            deck_brasse.append(paquet1[i])
            deck_brasse.append(paquet2[i])

        return deck_brasse
    
    def brassage_paquets(self, deck):
        len_cartes = len(self.deck)
        deck_brasse = []
        for i in range(0, len_cartes, 4):
            deck_de_quatre = self.deck[i : i + 4]
            deck_brasse.append(deck_de_quatre)

        order = [7, 1, 3, 13, 2, 4, 11, 6, 8, 5, 12, 10, 9]
        deck_brasse_update = []
        for idx in order:
            paquet = deck_brasse[idx-1]
            deck_brasse_update.extend(paquet)

        return deck_brasse_update


if __name__ == "__main__":
    deck1 = Deck()
    deck1.afficher()