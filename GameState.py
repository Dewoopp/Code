from Cards import CardDeck

class GameState:

    def __init__(self):

        self.cardDeck = CardDeck()
        self.cardStacks = []
        #Creates 7 lists of increasing no. of cards - creates each card stack
        for i in range(7):
            cardStack = []
            for j in range(i + 1):
                cardStack.append(self.cardDeck.cards[0])
                self.cardDeck.cards.remove(self.cardDeck.cards[0])
            self.cardStacks.append(cardStack)

        self.cardDeck.printDeck()