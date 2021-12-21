from graphics import GraphWin, Rectangle, Point, _root, Image
import tkinter as tk

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
        self.firstClick = True

        self.cardHeight = 109
        self.cardWidth = 78

        self.stackCardDist = 30

        self.deckDiscardImg = None
        self.deckImg = None
        self.suitStackTopImg = [None for _ in range(4)]
        self.stackTopImg =  [[] for _ in range(7)]

    def draw(self, gameState):
        self.displayStacks(gameState)
        self.displaySuitStacks(gameState)
        self.displayDeckDiscard(gameState)
        self.displayDeck(gameState)
        self.gameState = gameState

    def displayStacks(self, gameState):
        for i in range(len(gameState.cardStacks)):
            for j in range(len(gameState.cardStacks[i].cards)):
                topCardPos = Point(self.pos["Stacks"][i].x, self.pos["Stacks"][i].y + j * self.stackCardDist)
                if gameState.cardStacks[i].backNum > j:
                    topCardDeck = Image(topCardPos, "Cards/card_back.png")
                    topCardDeck.draw(self.window)
                    self.stackTopImg[i].append(None)
                else:
                    topCardDeck = Image(topCardPos, gameState.cardStacks[i].cards[j].getFileName())
                    self.stackTopImg[i].append(topCardDeck.draw(self.window))
        
    def displaySuitStacks(self, gameState):
        for i in range(4):
            suitStackPos = Point(self.pos["SuitStacks"][i].x, self.pos["SuitStacks"][i].y)
            if gameState.suitStacks[i].isEmpty():
                topSuitStack = Image(suitStackPos, "Cards/blank_card.png")
                topSuitStack.draw(self.window)
                self.suitStackTopImg[i] = None
            else:
                topSuitStack = Image(suitStackPos, gameState.suitStacks[i].cards[-1].getFileName())
                self.suitStackTopImg[i] = topSuitStack.draw(self.window)

    def displayDeckDiscard(self, gameState):
        for i in range(min(3, len(gameState.deckDiscard))):
            deckDiscardPos = Point(self.pos["DeckDiscard"][i].x + i * 30, self.pos["DeckDiscard"][i].y)
            topDeckDiscard = Image(deckDiscardPos, gameState.deckDiscard[-i].getFileName())
            self.deckDiscardImg = topDeckDiscard.draw(self.window)
    
    def displayDeck(self, gameState):
        if gameState.cardDeck.isEmpty():
            topDeck = Image(self.pos["Deck"], "Cards/blank_card.png")
        else:
            topDeck = Image(self.pos["Deck"], "Cards/card_back.png")
        self.deckImg = topDeck.draw(self.window)

    def drag(self, e):
        if self.inDrag or self.clickImg is None:
            return

        if self.firstClick:
            self.firstClick = False
        

        self.inDrag = True     
        self.clickImg.undraw()
        self.clickImg.anchor.x = e.x
        self.clickImg.anchor.y = e.y
        self.clickImg.draw(self.window)
        self.inDrag = False

    def drop(self, e):
        self.firstClick = True

    def click(self, e):
        self.clickImg = self.findClickedCard(e.x, e.y)

    def findClickedCard(self, x, y):
        if self.isClicked(x, y, self.pos["Deck"]):
            return self.deckImg
        if self.isClicked(x, y, self.pos["DeckDiscard"]):
            return self.deckDiscardImg
        for i in range(len(self.pos["SuitStacks"])):
            if self.isClicked(x, y, self.pos["SuitStacks"][i]) and self.suitStackTopImg[i] is not None:
                return self.suitStackTopImg[i]
        for i in range(len(self.pos["Stacks"])):
            numCards = len(self.gameState.cardStacks[i].cards)
            for j in range(numCards):
                newXPos = self.pos["Stacks"][i].x
                newYPos = self.pos["Stacks"][i].y + self.stackCardDist * (numCards - j - 1)
                if self.isClicked(x, y, Point(newXPos, newYPos)):
                    return self.stackTopImg[i][numCards - j - 1]
        return None

    # def findClickedCard2(self, x, y):
    #     for area in self.pos:
    #         for card in self.pos[area]:
    #             if card.isClicked(x, y):
    #                 return card
    #     else:
    #         return None


    def isClicked(self, x, y, midPoint):
        #print(midPoint.x, midPoint.y, x, y, midPoint.x + self.cardWidth, midPoint.y + self.cardHeight)
        return (midPoint.x - self.cardWidth/2 <= x <= midPoint.x + self.cardWidth/2) and (midPoint.y - self.cardHeight/2 <= y <= midPoint.y + self.cardHeight/2)
