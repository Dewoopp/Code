from Cards import CardDeck
from CardStack import CardStack
from SuitStack import SuitStack
from time import time

class GameState:

    # Passes in the test case so we can check if the user has initiated a test
    def __init__(self, testCase):

        # Create deck
        self.cardDeck = CardDeck()
        self.createDeckTestCase(testCase)

        # Sets the time and the moves at the start
        self.startTime = 0
        self.moves = 0

        # Sets the number of stacks and suit stacks to be used later
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

    # Makes the move - this is done after the validation so we are sure that the move is legal
    def makeMove(self, clickedCards, dropName, dropIdx):
        # Starts the time if it is the first move
        if self.startTime == 0:
            self.startTime = time()
        # Adds one to the moves
        self.moves += 1
        # Find source card
        # Checks the deck discard for the selected card
        if clickedCards[0] in self.deckDiscard:
            # Gives us the top card of the deck discard
            sourceCards = [self.deckDiscard[-1]]
            # Removes the card selected from the deck discard
            self.deckDiscard.remove(sourceCards[0])
        # Loops through the suit stacks
        for i in range(self.numSuitStacks):
            # if the clicked card is in the suit stack
            if clickedCards[0] in self.suitStacks[i].cards:
                # Gives the top card of the selected suit stack
                sourceCards = [self.suitStacks[i].cards[-1]]
                # Removes the card from the suit stack
                self.suitStacks[i].cards.remove(sourceCards[0])
        # Loops through the card stacks
        for i in range(self.numCardStacks):
            # For the stacks we need the actual location of the selected card in the stack
            # Because you can select a card that is midway up the stack
            # Sets the index for the selected card
            cardStackIdx = self.cardStacks[i].find(clickedCards[0])
            # If the card actually was in the stack
            if cardStackIdx is not None:
                # Gets all the cards below the index of the clicked card
                # This is so it can move multiple cards at the same time
                sourceCards = self.cardStacks[i].getBelow(cardStackIdx)
                # Turns over the next card if the index is the same as the number of back up cards
                # i.e. if the clicked on card is the first after the set of back up cards
                if cardStackIdx == self.cardStacks[i].backNum:
                    # Decreases the backnum by one, which will draw the next card when the screen redraws
                    self.cardStacks[i].backNum -= 1
                # Removes the cards from the stack
                self.cardStacks[i].removeBelow(cardStackIdx)
        # Find drop location
        if dropName == "SuitStacks":
            # Adds the card to the top of the suit stack
            self.suitStacks[dropIdx].append(sourceCards[0])
        elif dropName == "Stacks":
            # Loops through as you can drop multiple cards on the stacks
            for card in sourceCards:
                # Adds those cards to the stack
                self.cardStacks[dropIdx].append(card)

    # Checks if the game is over
    def isGameOver(self):
        # Sets the condition to be where all cards in the card stacks are turned over
        for stack in self.cardStacks:
            # If the backnum of any stack is not 0
            if stack.backNum != 0:
                # The player hasnt won
                return False
        # Sets the total time, which will be inserted into the database
        self.totalTime = self.elapsedTime()
        # If the function doesnt return before this point, the player has won
        return True

    # Returns the time elapsed since the game started
    def elapsedTime(self):
        # Uses the time() function, which is used to find the exact time between events
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
            # The backnums for all stacks are usually automatically generated from the size of the stack
            # Manually sets the backnum for all card stacks to 0
            # This will cause the program to not draw any cards where the stacks should be
            self.cardStacks = [CardStack(0) for i in range(self.numCardStacks)]
            # Sets the backnum of the last stack to 1 so we can turn over the last card and win
            self.cardStacks[6].backNum = 1
            # Put a movable king and a second random card to the top of the stack
            self.cardStacks[6].append(self.cardDeck.getCard("D", 12))
            self.cardStacks[6].append(self.cardDeck.getCard("S", 13))