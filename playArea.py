from graphics import GraphWin, Rectangle, Point, _root, Image
from time import sleep

class PlayingArea:

    def __init__(self):
        self.pos =  {
                    "Stacks": [],
                    "SuitStacks": [],
                    "Deck": None,
                    "DeckDiscard": None,
                    }
        
        #Defines the window
        self.window = GraphWin("Solitaire", 1000, 750)
        self.window.bind('<B1-Motion>', self.drag)
        self.window.bind('<ButtonRelease-1>', self.drop)
        self.window.bind('<ButtonPress-1>', self.click)

        background = Rectangle(Point(0,0), Point(1000, 750))
        background.setFill("green")
        background.draw(self.window)
        
        for i in range(7):
            self.pos["Stacks"].append(Point(75 + 100*i, 75))

        for i in range(4):
            self.pos["SuitStacks"].append(Point(825 + 100*(i % 2), 75 + 130*(i // 2)))

        self.pos["Deck"] = Point(825, 345)
        self.pos["DeckDiscard"] = Point(825, 475)

        self.inDrag = False

        self.cardHeight = 109
        self.cardWidth = 78

        self.stackCardDist = 30

        self.deckImg = None
        self.deckDiscardImg = []
        self.suitStackTopImg = [None for _ in range(4)]
        self.stackTopImg =  [[] for _ in range(7)]

        self.removeImgs = []

        self.dropToBe = None

    def setValidator(self, validatorFunc):
        self.validatorFunc = validatorFunc

    def draw(self, gameState):
        self.undraw()
        self.displayStacks(gameState)
        self.displaySuitStacks(gameState)
        self.displayDeckDiscard(gameState)
        self.displayDeck(gameState)
        self.gameState = gameState

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


    def displayStacks(self, gameState):
        for i in range(len(gameState.cardStacks)):
            self.stackTopImg[i] = []
            for j in range(len(gameState.cardStacks[i].cards)):
                topCardPos = Point(self.pos["Stacks"][i].x, self.pos["Stacks"][i].y + j * self.stackCardDist)
                if gameState.cardStacks[i].backNum > j:
                    topCardDeck = Image(topCardPos, "Cards/card_back.png")
                    self.removeImgs.append(topCardDeck.draw(self.window))
                    self.stackTopImg[i].append(None)
                    
                else:
                    topCardDeck = Image(topCardPos, gameState.cardStacks[i].cards[j].getFileName())
                    self.stackTopImg[i].append(topCardDeck.draw(self.window))
        
    def displaySuitStacks(self, gameState):
        for i in range(4):
            suitStackPos = Point(self.pos["SuitStacks"][i].x, self.pos["SuitStacks"][i].y)
            if gameState.suitStacks[i].isEmpty():
                topSuitStack = Image(suitStackPos, "Cards/blank_card.png")
                self.removeImgs.append(topSuitStack.draw(self.window))
                self.suitStackTopImg[i] = None
            else:
                topSuitStack = Image(suitStackPos, gameState.suitStacks[i].cards[-1].getFileName())
                self.suitStackTopImg[i] = topSuitStack.draw(self.window)

    def displayDeckDiscard(self, gameState):
        self.deckDiscardImg = []
        for i in range(min(3, len(gameState.deckDiscard))):
            deckDiscardPos = Point(self.pos["DeckDiscard"][i].x + i * 30, self.pos["DeckDiscard"][i].y)
            topDeckDiscard = Image(deckDiscardPos, gameState.deckDiscard[-i].getFileName())
            self.deckDiscardImg.append(topDeckDiscard.draw(self.window))
    
    def displayDeck(self, gameState):
        if gameState.cardDeck.isEmpty():
            topDeck = Image(self.pos["Deck"], "Cards/blank_card.png")
        else:
            topDeck = Image(self.pos["Deck"], "Cards/card_back.png")
        self.deckImg = topDeck.draw(self.window)

    def drag(self, e):
        if self.inDrag or len(self.clickImgs) == 0:
            return

        self.inDrag = True
        for i, img in enumerate(self.clickImgs):
            img.undraw()
            img.anchor.x = e.x
            img.anchor.y = e.y + i * self.stackCardDist
            img.draw(self.window)
            sleep(0.001)
        self.inDrag = False
        if self.dropToBe is not None:
            self.doDrop(self.dropToBe[0], self.dropToBe[1])
        self.dropToBe = None

    def drop(self, e):
        if self.inDrag:
            self.dropToBe = (e.x, e.y)
        else:
            self.doDrop(e.x, e.y)
            self.dropToBe = None

    def doDrop(self, x, y):
        _, dropName, dropIdx, dropCard, dropStackLocation = self.findEventLocation(x, y)
        self.validatorFunc(self.clickName, self.clickIdx, self.clickCards, dropName, dropIdx, dropCard, dropStackLocation)


    def click(self, e):
        self.clickImgs, self.clickName, self.clickIdx, self.clickCards, _ = self.findEventLocation(e.x, e.y)

    def findEventLocation(self, x, y):
        if self.isClicked(x, y, self.pos["Deck"]):
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