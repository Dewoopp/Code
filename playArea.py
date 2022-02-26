from graphics import GraphWin, Rectangle, Point, _root, Image, Text, Entry
from time import sleep
from Button import Button

class PlayingArea:

    # Defines the positions of everything on the window
    def __init__(self, gameWindow, gameState, gameDb):
        self.pos =  {
                    "Stacks": [],
                    "SuitStacks": [],
                    "Deck": None,
                    "DeckDiscard": None,
                    }
        
        # Defines the window
        self.gameWindow = gameWindow
        self.gameDb = gameDb
        self.window = self.gameWindow.window

        # Sets the background colour
        self.background = Rectangle(Point(0,0), Point(1000, 750))
        self.background.setFill("green")

        self.winRect = Rectangle(Point(self.window.width/6, self.window.height/4), Point(self.window.width * 5/6, self.window.height * 3/4))
        self.winRect.setFill("yellow")

        self.winRectText = Text(Point(self.window.width/2, self.window.height/3 + 75), "YOU WIN!!!")
        self.winRectText.setFace("courier")
        self.winRectText.setFill("black")
        self.winRectText.setSize(70)

        self.userNameText = Text(Point(self.window.width/2, self.window.height * 3/5 - 50), "Enter your name:")
        self.userNameText.setFace("courier")
        self.userNameText.setFill("black")
        self.userNameText.setSize(30)

        self.enterUserName = Entry(Point(self.window.width/2, self.window.height * 3/5), 10)
        self.enterUserName.setSize(20)

        self.enterButton = Button(self.window.width/2, self.window.height * 3/5 + 50, 75, 50, "Enter")

        self.gameState = gameState
        
        self.backDrawn = False
        
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

        self.scoreTimerRunning = True

        self.scoreText = Text(Point(self.window.width - 100, self.window.height - 50), "")
        self.scoreText.setFace("courier")
        self.scoreText.setFill("black")
        self.scoreText.setSize(20)


    # Adds a callback to call the validator function and the function to turn over the cards
    def setValidator(self, validatorFunc, turnCardsFunc):
        self.validatorFunc = validatorFunc
        self.turnCardsFunc = turnCardsFunc

    # Undraws then redraws the entire board - used after dropping anything in order to update the GUI
    def draw(self):
        self.undraw(False)
        if not self.backDrawn:
            self.background.draw(self.window)
            self.backDrawn = True
            print("start")
            self.scoreTimerRunning = True
            self.window.getRoot().after(500, self.showScore)
        self.displayStacks()
        self.displaySuitStacks()
        self.displayDeckDiscard()
        self.displayDeck()
        self.scoreText.draw(self.window)

    # Undraws everything
    def undraw(self, screenChange):
        if screenChange:
            self.background.undraw()
            self.backDrawn = False
            self.enterUserName.undraw()
            self.userNameText.undraw()
            self.winRect.undraw()
            self.winRectText.undraw()
            self.enterButton.undraw()
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
        self.scoreText.undraw()

    # Displays the stacks
    def displayStacks(self):
        # Loop through the card stacks
        for i in range(len(self.gameState.cardStacks)):
            self.stackTopImg[i] = []
            # Loop through the cards in the stacks
            for j in range(len(self.gameState.cardStacks[i].cards)):
                # Defines the location of the current card
                topCardPos = Point(self.pos["Stacks"][i].x, self.pos["Stacks"][i].y + j * self.stackCardDist)
                # If the current position is less than the number of backwards facing cards
                if self.gameState.cardStacks[i].backNum > j:
                    # Instead of displaying the image, it displays the card back instead
                    topCardDeck = Image(topCardPos, "Cards/card_back.png")
                    # Adds to the removeImgs list and draws it on the screen
                    self.removeImgs.append(topCardDeck.draw(self.window))
                    self.stackTopImg[i].append(None)

                else:
                    # Gets the image
                    topCardDeck = Image(topCardPos, self.gameState.cardStacks[i].cards[j].getFileName())
                    # Display the image with the filename
                    self.stackTopImg[i].append(topCardDeck.draw(self.window))

    # Displays the suit stacks
    def displaySuitStacks(self):
        for i in range(4):
            suitStackPos = Point(self.pos["SuitStacks"][i].x, self.pos["SuitStacks"][i].y)
            # If the suit stack is empty then display a blank card
            if self.gameState.suitStacks[i].isEmpty():
                topSuitStack = Image(suitStackPos, "Cards/blank_card.png")
                self.removeImgs.append(topSuitStack.draw(self.window))
                self.suitStackTopImg[i] = None
            else:
                # Gets the image of the card at the top of the suit stack
                topSuitStack = Image(suitStackPos, self.gameState.suitStacks[i].cards[-1].getFileName())
                self.suitStackTopImg[i] = topSuitStack.draw(self.window)

    # Displays the deck discard
    def displayDeckDiscard(self):
        self.deckDiscardImg = []
        # Finds the minimum of 3 and the length of the deck discard - makes the max cards displayed 3
        numToDisplay = min(3, len(self.gameState.deckDiscard))
        for i in range(numToDisplay):
            deckDiscardPos = Point(self.pos["DeckDiscard"].x + i * 30, self.pos["DeckDiscard"].y)
            topDeckDiscard = Image(deckDiscardPos, self.gameState.deckDiscard[-(numToDisplay-i)].getFileName())
            self.deckDiscardImg.append(topDeckDiscard.draw(self.window))
    
    # Displays the deck
    def displayDeck(self):
        # Checks if the deck is empty
        if self.gameState.cardDeck.isEmpty():
            topDeck = Image(self.pos["Deck"], "Cards/blank_card.png")
        else:
            topDeck = Image(self.pos["Deck"], "Cards/card_back.png")
        self.deckImg = topDeck.draw(self.window)

    # Called when the player initiates a drag
    def drag(self, e):
        # If we are already in a drag or we are trying to drag nothing
        if self.inDrag or len(self.clickImgs) == 0 or self.gameState.isGameOver():
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
        if not self.gameState.isGameOver():
            # If we are in a drag, sets a drop to do later
            if self.inDrag:
                self.dropToBe = (e.x, e.y)
            # If we aren't in a drag, do the drop now
            else:
                self.doDrop(e.x, e.y)
                self.dropToBe = None
        else:
            if self.enterButton.isPressed(e.x, e.y):
                self.gameDb.addWinner(self.enterUserName.getText(), self.gameState.moves, self.elapsed)
                self.gameWindow.returnHome()

    def doDrop(self, x, y):
        # Sets the neccessary variables required for a drop
        _, dropName, dropIdx, dropCard, dropStackLocation = self.findEventLocation(x, y)
        # Calls the validation 
        self.validatorFunc(self.clickName, self.clickIdx, self.clickCards, dropName, dropIdx, dropCard, dropStackLocation)
        if self.gameState.isGameOver():
            print("You won")
            self.winRect.draw(self.window)
            self.winRectText.draw(self.window)
            self.showScore()
            self.scoreTimerRunning = False
            self.enterUserName.draw(self.window)
            self.userNameText.draw(self.window)
            self.enterButton.draw(self.window)

    def click(self, e):
        if not self.gameState.isGameOver():
            # Sets the neccessary variables and uses them later when dropping
            self.clickImgs, self.clickName, self.clickIdx, self.clickCards, _ = self.findEventLocation(e.x, e.y)
            if self.clickName == "Deck":
                self.turnCardsFunc()

    # This is used to set variables for both a drop and a click
    def findEventLocation(self, x, y):
        # If we clicked on the deck
        if self.isClicked(x, y, self.pos["Deck"]):
            # The deck cannot be dropped on - so it will return almost no information
            return [], "Deck", 0, [], 0
        if self.isClicked(x, y, self.pos["DeckDiscard"].findOffset((min(3, len(self.gameState.deckDiscard))-1)*30, 0)):
            return [self.deckDiscardImg[-1]], "DeckDiscard", 0, [self.gameState.deckDiscard[-1]] if len(self.gameState.deckDiscard) > 0 else [], 0
        for i in range(len(self.pos["SuitStacks"])):
            if self.isClicked(x, y, self.pos["SuitStacks"][i]):
                return [self.suitStackTopImg[i]], "SuitStacks", i, [self.gameState.suitStacks[i].cards[-1]] if len(self.gameState.suitStacks[i].cards) > 0 else [], 0
        for i in range(len(self.pos["Stacks"])):
            numCards = len(self.gameState.cardStacks[i].cards)
            # Searching from bottom to top, so that we take the lower card if the card is covering a higher card
            if numCards == 0:
                newXPos = self.pos["Stacks"][i].x
                newYPos = self.pos["Stacks"][i].y
                if self.isClicked(x, y, Point(newXPos, newYPos)):
                    return [], "Stacks", i, [], 0
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
        return (midPoint.x - self.cardWidth/2 <= x <= midPoint.x + self.cardWidth/2) and (midPoint.y - self.cardHeight/2 <= y <= midPoint.y + self.cardHeight/2)

    def showScore(self):
        self.elapsed = int(self.gameState.elapsedTime())
        scoreStr = str(self.gameState.moves) + " " + str(self.elapsed)
        self.scoreText.setText(scoreStr)
        if not self.scoreTimerRunning:
            return
        self.window.getRoot().after(500, self.showScore)