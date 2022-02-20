from Cards import CardDeck
from CardStack import CardStack
from SuitStack import SuitStack
from time import time

class GameState:

    def __init__(self, testCase):

        #Create deck
        self.cardDeck = CardDeck()
        self.createDeckTestCase(testCase)

        self.startTime = 0
        self.moves = 0

        self.numCardStacks = 7
        self.numSuitStacks = 4

        self.startCards = []

        #Creates 7 lists of increasing no. of cards - creates each card stack
        self.cardStacks = []
        for i in range(self.numCardStacks):
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
        for i in range(self.numSuitStacks):
            suitStack = SuitStack()
            self.suitStacks.append(suitStack)

        #Creates the interactive discard of the deck
        self.deckDiscard = []

        self.createStateTestCase(testCase) 

    def makeMove(self, clickedCards, dropName, dropIdx):
        if self.startTime == 0:
            self.startTime = time()
        self.moves += 1
        #find source card
        if clickedCards[0] in self.deckDiscard:
            sourceCards = [self.deckDiscard[-1]]
            self.deckDiscard.remove(sourceCards[0])
        for i in range(self.numSuitStacks):
            if clickedCards[0] in self.suitStacks[i].cards:
                sourceCards = [self.suitStacks[i].cards[-1]]
                self.suitStacks[i].cards.remove(sourceCards[0])
        for i in range(self.numCardStacks):
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
    
    def createDeckTestCase(self, testCase):
        if testCase == "mid_drop":
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 7), 0)
            self.cardDeck.swapCards(self.cardDeck.getCard("C", 7), 2)
            self.cardDeck.swapCards(self.cardDeck.getCard("D", 8), 5)
        elif testCase == "king_blank":
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 1), 0)
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 13), 2)
        elif testCase == "win":
            self.cardDeck.swapCards(self.cardDeck.getCard("D", 12), 36)
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 13), 35)


    def createStateTestCase(self, testCase):
        if testCase == "win":
            self.cardStacks = [CardStack(0) for i in range(self.numCardStacks)]
            self.cardStacks[6].backNum = 1
            self.cardStacks[6].append(self.cardDeck.getCard("D", 12))
            self.cardStacks[6].append(self.cardDeck.getCard("S", 13))

