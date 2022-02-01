from graphics import GraphWin, Rectangle, Point, _root, Image
from time import sleep

class PlayingArea:

    # Defines the positions of everything on the window
    def __init__(self):
        self.pos =  {
                    "Stacks": [],
                    "SuitStacks": [],
                    "Deck": None,
                    "DeckDiscard": None,
                    }
        
        # Defines the window
        self.window = GraphWin("Solitaire", 1000, 750)
        # Binds function calls to actions from the user
        self.window.bind('<B1-Motion>', self.drag)
        self.window.bind('<ButtonRelease-1>', self.drop)
        self.window.bind('<ButtonPress-1>', self.click)

        # Sets the background colour and draws it on the window
        background = Rectangle(Point(0,0), Point(1000, 750))
        background.setFill("green")
        background.draw(self.window)
        
        # These point positions are all the middle of the card
        # Adds the positions of the top of the stacks to the pos dictionary
        for i in range(7):
            self.pos["Stacks"].append(Point(75 + 100*i, 75))

        # Adds the position of the suit stacks to the pos dictionary
        for i in range(4):
            self.pos["SuitStacks"].append(Point(825 + 100*(i % 2), 75 + 130*(i // 2)))

        # The deck and deck discard are only defined as single points
        self.pos["Deck"] = Point(825, 345)
        self.pos["DeckDiscard"] = Point(825, 475)

        # Sets the inDrag variable to be used later
        self.inDrag = False

        # Sets the size of every card, from what was cut out in the cutOutCards file
        self.cardHeight = 109
        self.cardWidth = 78

        # The distance between cards in the stacks
        self.stackCardDist = 30

        # Sets lists and variables to be set and used later
        self.deckImg = None
        self.deckDiscardImg = []
        self.suitStackTopImg = [None for _ in range(4)]
        self.stackTopImg =  [[] for _ in range(7)]

        # 
        self.removeImgs = []

        self.dropToBe = None

    # Adds a callback to call the validator function
    def setValidator(self, validatorFunc):
        self.validatorFunc = validatorFunc

    # Undraws then redraws the entire board - used after dropping anything in order to update the GUI
    def draw(self, gameState):
        self.undraw()
        self.displayStacks(gameState)
        self.displaySuitStacks(gameState)
        self.displayDeckDiscard(gameState)
        self.displayDeck(gameState)
        # Defines the gameState
        self.gameState = gameState

    # Undraws everything
    def undraw(self):
        for card in self.removeImgs:
            card.undraw()
        for card in self.deckDiscardImg:
            card.undraw()
        for card in self.suitStackTopImg:
            if card is not None:
                card.undraw()
        for stack in self.stackTopImg:
            for card in stack:
                if card is not None:
                    card.undraw()
        if self.deckImg is not None:
            self.deckImg.undraw()

    # Displays the stacks
    def displayStacks(self, gameState):
        # Loop through the card stacks
        for i in range(len(gameState.cardStacks)):
            self.stackTopImg[i] = []
            # Loop through the cards in the stacks
            for j in range(len(gameState.cardStacks[i].cards)):
                # Defines the location of the current card
                topCardPos = Point(self.pos["Stacks"][i].x, self.pos["Stacks"][i].y + j * self.stackCardDist)
                # If the current position is less than the number of backwards facing cards
                if gameState.cardStacks[i].backNum > j:
                    # Instead of displaying the image, it displays the card back instead
                    topCardDeck = Image(topCardPos, "Cards/card_back.png")
                    # Adds to the removeImgs list and draws it on the screen
                    self.removeImgs.append(topCardDeck.draw(self.window))
                    self.stackTopImg[i].append(None)

                else:
                    # Gets the image
                    topCardDeck = Image(topCardPos, gameState.cardStacks[i].cards[j].getFileName())
                    # Display the image with the filename
                    self.stackTopImg[i].append(topCardDeck.draw(self.window))

    # Displays the suit stacks
    def displaySuitStacks(self, gameState):
        for i in range(4):
            suitStackPos = Point(self.pos["SuitStacks"][i].x, self.pos["SuitStacks"][i].y)
            # If the suit stack is empty then display a blank card
            if gameState.suitStacks[i].isEmpty():
                topSuitStack = Image(suitStackPos, "Cards/blank_card.png")
                self.removeImgs.append(topSuitStack.draw(self.window))
                self.suitStackTopImg[i] = None
            else:
                # Gets the image of the card at the top of the suit stack
                topSuitStack = Image(suitStackPos, gameState.suitStacks[i].cards[-1].getFileName())
                self.suitStackTopImg[i] = topSuitStack.draw(self.window)

    # Displays the deck discard
    def displayDeckDiscard(self, gameState):
        self.deckDiscardImg = []
        # Finds the minimum of 3 and the length of the deck discard - makes the max cards displayed 3
        for i in range(min(3, len(gameState.deckDiscard))):
            deckDiscardPos = Point(self.pos["DeckDiscard"][i].x + i * 30, self.pos["DeckDiscard"][i].y)
            topDeckDiscard = Image(deckDiscardPos, gameState.deckDiscard[-i].getFileName())
            self.deckDiscardImg.append(topDeckDiscard.draw(self.window))
    
    # Displays the deck
    def displayDeck(self, gameState):
        # Checks if the deck is empty
        if gameState.cardDeck.isEmpty():
            topDeck = Image(self.pos["Deck"], "Cards/blank_card.png")
        else:
            topDeck = Image(self.pos["Deck"], "Cards/card_back.png")
        self.deckImg = topDeck.draw(self.window)

    # Called when the player initiates a drag
    def drag(self, e):

        # If we are already in a drag or we are trying to drag nothing
        if self.inDrag or len(self.clickImgs) == 0:
            return

        # We are in a drag - sets flag to true
        self.inDrag = True
        # Gets the image and the index for each element that we are dragging - which can be multiple cards
        for i, img in enumerate(self.clickImgs):
            # Undraws the images
            img.undraw()
            # Redraws the image at the event location, using the index to drag multiple cards together
            img.anchor.x = e.x
            img.anchor.y = e.y + i * self.stackCardDist
            img.draw(self.window)
            sleep(0.001)
        # Sets the flag to False
        self.inDrag = False
        # Does the drop to be if it is set
        # This fixes a bug where a drop and drag are called at the same time - causing a visual bug
        if self.dropToBe is not None:
            self.doDrop(self.dropToBe[0], self.dropToBe[1])
        self.dropToBe = None

    def drop(self, e):
        # If we are in a drag, sets a drop to do later
        if self.inDrag:
            self.dropToBe = (e.x, e.y)
        # If we aren't in a drag, do the drop now
        else:
            self.doDrop(e.x, e.y)
            self.dropToBe = None

    def doDrop(self, x, y):
        # Sets the neccessary variables required for a drop
        _, dropName, dropIdx, dropCard, dropStackLocation = self.findEventLocation(x, y)
        # Calls the validation 
        self.validatorFunc(self.clickName, self.clickIdx, self.clickCards, dropName, dropIdx, dropCard, dropStackLocation)

    def click(self, e):
        # Sets the neccessary variables required for a click
        self.clickImgs, self.clickName, self.clickIdx, self.clickCards, _ = self.findEventLocation(e.x, e.y)

    # This is used to set variables for both a drop and a click
    def findEventLocation(self, x, y):
        # If we clicked on the deck
        if self.isClicked(x, y, self.pos["Deck"]):
            # The deck cannot be clicked or dropped on - so it will return almost no information
            return [], "Deck", 0, [], 0
        if self.isClicked(x, y, self.pos["DeckDiscard"]):
            return [self.deckDiscardImg[-1]], "DeckDiscard", 0, [self.gameState.deckDiscard[-1]] if len(self.gameState.deckDiscard) > 0 else [], 0
        for i in range(len(self.pos["SuitStacks"])):
            if self.isClicked(x, y, self.pos["SuitStacks"][i]):
                return [self.suitStackTopImg[i]], "SuitStacks", i, [self.gameState.suitStacks[i].cards[-1]] if len(self.gameState.suitStacks[i].cards) > 0 else [], 0
        for i in range(len(self.pos["Stacks"])):
            numCards = len(self.gameState.cardStacks[i].cards)
            # Searching from bottom to top, so that we take the lower card if the card is covering a higher card
            for j in range(numCards):
                newXPos = self.pos["Stacks"][i].x
                newYPos = self.pos["Stacks"][i].y + self.stackCardDist * (numCards - j - 1)
                if self.isClicked(x, y, Point(newXPos, newYPos)):
                    imgList = self.stackTopImg[i][numCards - j - 1:]
                    cardList = self.gameState.cardStacks[i].cards[numCards - j - 1:]
                    return imgList, "Stacks", i, cardList, j
        return [], "", 0, [], 0

    # def findEventLocation2(self, x, y):
    #     for area in self.pos:
    #         for card in self.pos[area]:
    #             if card.isClicked(x, y):
    #                 return card
    #     else:
    #         return None

    def isClicked(self, x, y, midPoint):
        #print(midPoint.x, midPoint.y, x, y, midPoint.x + self.cardWidth, midPoint.y + self.cardHeight)
        return (midPoint.x - self.cardWidth/2 <= x <= midPoint.x + self.cardWidth/2) and (midPoint.y - self.cardHeight/2 <= y <= midPoint.y + self.cardHeight/2)