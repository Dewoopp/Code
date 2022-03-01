from Cards import CardDeck
from CardStack import CardStack
from SuitStack import SuitStack
from time import time

class GameState:

    def __init__(self, testCase):

        # Create deck
        self.cardDeck = CardDeck()
        self.createDeckTestCase(testCase)

        # Sets the time and the moves at the start
        self.startTime = 0
        self.moves = 0

        self.numCardStacks = 7
        self.numSuitStacks = 4

        # Creates 7 lists of increasing no. of cards - creates each card stack
        self.cardStacks = []
        for i in range(self.numCardStacks):
            # Instantiates a new card stack object
            cardStack = CardStack(i)
            for j in range(i + 1):
                # Gets the top card of the deck
                topCard = self.cardDeck.topCard()
                # Adds it to the card stack
                cardStack.append(topCard)
                # Removes it from the deck
                self.cardDeck.removeTop()
            # Adds the newly created card stack to the list of card stacks
            self.cardStacks.append(cardStack)

        # Creates the suit stacks
        self.suitStacks = []
        for i in range(self.numSuitStacks):
            suitStack = SuitStack()
            self.suitStacks.append(suitStack)

        # Creates the interactive discard of the deck
        self.deckDiscard = []

        # Creates the test case
        self.createStateTestCase(testCase) 

    # Makes the move
    def makeMove(self, clickedCards, dropName, dropIdx):
        # Starts the time if it is the first move
        if self.startTime == 0:
            self.startTime = time()
        # Adds one to the moves
        self.moves += 1
        # Find source card
        # Checks the deck discard for the selected card
        if clickedCards[0] in self.deckDiscard:
            sourceCards = [self.deckDiscard[-1]]
            self.deckDiscard.remove(sourceCards[0])
        # Checks the suit stacks
        for i in range(self.numSuitStacks):
            if clickedCards[0] in self.suitStacks[i].cards:
                sourceCards = [self.suitStacks[i].cards[-1]]
                self.suitStacks[i].cards.remove(sourceCards[0])
        # Checks the card stacks
        for i in range(self.numCardStacks):
            cardStackIdx = self.cardStacks[i].find(clickedCards[0])
            if cardStackIdx is not None:
                sourceCards = self.cardStacks[i].getBelow(cardStackIdx)
                # Turns over the next card
                if cardStackIdx == self.cardStacks[i].backNum:
                   self.cardStacks[i].backNum -= 1
                self.cardStacks[i].removeBelow(cardStackIdx)
        # Find drop location
        if dropName == "SuitStacks":
            self.suitStacks[dropIdx].append(sourceCards[0])
        elif dropName == "Stacks":
            # Loops through as you can drop multiple cards on the stacks
            for card in sourceCards:
                self.cardStacks[dropIdx].append(card)

    # Checks if the game is over
    def isGameOver(self):
        # Sets the condition to be where all cards in the card stacks are turned over
        for stack in self.cardStacks:
            if stack.backNum != 0:
                return False
        self.totalTime = self.elapsedTime()
        return True

    # Returns the time elapsed since the game started
    def elapsedTime(self):
        return 0 if self.startTime == 0 else time() - self.startTime
    
    # Creates the test cases that simply modify the deck
    def createDeckTestCase(self, testCase):
        # Checks for the "mid_drop" test case
        if testCase == "mid_drop":
            # Swaps the card to ensure that we can access the cards we need
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 7), 0)
            self.cardDeck.swapCards(self.cardDeck.getCard("C", 7), 2)
            self.cardDeck.swapCards(self.cardDeck.getCard("D", 8), 5)
        # Checks for the "king_blank" test case
        elif testCase == "king_blank":
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 1), 0)
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 13), 2)
        # For the "win" test case, makes sure that the cards we need are in the deck
        # before overwriting the card stacks 
        elif testCase == "win":
            self.cardDeck.swapCards(self.cardDeck.getCard("D", 12), 36)
            self.cardDeck.swapCards(self.cardDeck.getCard("S", 13), 35)
        elif testCase == "queen_king":
            self.cardDeck.swapCards(self.cardDeck.getCard("D", 12), 0)
            self.cardDeck.swapCards(self.cardDeck.getCard("H", 13), 2)

    # Creates the test cases that need to modify the entire game state
    def createStateTestCase(self, testCase):
        # Checks for the "win" test case
        if testCase == "win":
            self.cardStacks = [CardStack(0) for i in range(self.numCardStacks)]
            self.cardStacks[6].backNum = 1
            self.cardStacks[6].append(self.cardDeck.getCard("D", 12))
            self.cardStacks[6].append(self.cardDeck.getCard("S", 13))