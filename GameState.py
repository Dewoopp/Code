from Cards import CardDeck
from CardStack import CardStack
from SuitStack import SuitStack

class GameState:

    def __init__(self):

        #Create deck
        self.cardDeck = CardDeck()

        #Creates 7 lists of increasing no. of cards - creates each card stack
        self.cardStacks = []
        for i in range(7):
            cardStack = CardStack(i)
            for j in range(i + 1):
                cardStack.append(self.cardDeck.topCard())
                self.cardDeck.removeTop()
            self.cardStacks.append(cardStack)

        #Create suit stacks
        self.suitStacks = []
        for i in range(4):
            suitStack = SuitStack()
            self.suitStacks.append(suitStack)

        #Creates the interactive discard of the deck
        self.deckDiscard = []
        
