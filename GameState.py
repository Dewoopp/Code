from Cards import CardDeck
from CardStack import CardStack
from SuitStack import SuitStack
from time import time

class GameState:

    def __init__(self):

        #Create deck
        self.cardDeck = CardDeck()

        self.startTime = 0
        self.moves = 0

        self.startCards = []

        #Creates 7 lists of increasing no. of cards - creates each card stack
        self.cardStacks = []
        for i in range(7):
            cardStack = CardStack(i)
            for j in range(i + 1):
                topCard = self.cardDeck.topCard()
                cardStack.append(topCard)
                self.cardDeck.removeTop()
                if i == j:
                    self.startCards.append(topCard)
            self.cardStacks.append(cardStack)

        #Create suit stacks
        self.suitStacks = []
        for i in range(4):
            suitStack = SuitStack()
            self.suitStacks.append(suitStack)

        #Creates the interactive discard of the deck
        self.deckDiscard = []

    def makeMove(self, clickedCards, dropName, dropIdx):
        if self.startTime == 0:
            self.startTime = time()
        self.moves += 1
        #find source card
        if clickedCards[0] in self.deckDiscard:
            sourceCards = [self.deckDiscard[-1]]
            self.deckDiscard.remove(sourceCards[0])
        for i in range(4):
            if clickedCards[0] in self.suitStacks[i].cards:
                sourceCards = [self.suitStacks[i].cards[-1]]
                self.suitStacks[i].cards.remove(sourceCards[0])
        for i in range(7):
            cardStackIdx = self.cardStacks[i].find(clickedCards[0])
            if cardStackIdx is not None:
                sourceCards = self.cardStacks[i].getBelow(cardStackIdx)
                # Turns over the next card
                if cardStackIdx == self.cardStacks[i].backNum:
                   self.cardStacks[i].backNum -= 1
                self.cardStacks[i].removeBelow(cardStackIdx)
        #find drop location
        if dropName == "SuitStacks":
            self.suitStacks[dropIdx].append(sourceCards[0])
        elif dropName == "Stacks":
            for card in sourceCards:
                self.cardStacks[dropIdx].append(card)

    def isGameOver(self):
        for stack in self.cardStacks:
            if stack.backNum != 0:
                return False
        self.totalTime = self.elapsedTime()
        return True

    def elapsedTime(self):
        return 0 if self.startTime == 0 else time() - self.startTime
        