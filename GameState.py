from Cards import CardDeck
from CardStack import CardStack

class GameState:

    def __init__(self):

        self.cardDeck = CardDeck()
        self.cardStacks = []
        #Creates 7 lists of increasing no. of cards - creates each card stack
        for i in range(7):
            cardStack = CardStack(i)
            for j in range(i + 1):
                cardStack.append(self.cardDeck.topCard())
                self.cardDeck.removeTop()
            self.cardStacks.append(cardStack)

        self.cardDeck.printDeck()