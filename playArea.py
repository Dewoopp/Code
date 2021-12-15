from graphics import GraphWin, Rectangle, Point, _root, Image
import tkinter as tk
from GameState import GameState

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
    
    def displayStacks(self, gameState):
        for i in range(7):
            for j in range(i + 1):
                topCardPos = Point(self.pos["Stacks"][i].x, self.pos["Stacks"][i].y + j * 30)
                if gameState.cardStacks[i].backNum > j:
                    topCardDeck = Image(topCardPos, "Cards/card_back.png")
                else:
                    topCardDeck = Image(topCardPos, gameState.cardStacks[i].cards[j].getFileName())
                topCardDeck.draw(self.window)
        
    def displaySuitStacks(self, gameState):
        for i in range(4):
            suitStackPos = Point(self.pos["SuitStacks"][i].x, self.pos["SuitStacks"][i].y)
            if gameState.suitStacks[i].isEmpty():
                topSuitStack = Image(suitStackPos, "Cards/blank_card.png")
            topSuitStack.draw(self.window)

    def displayDeckDiscard(self, gameState):
        for i in range(min(3, len(gameState.deckDiscard))):
            deckDiscardPos = Point(self.pos["DeckDiscard"][i].x + i * 30, self.pos["DeckDiscard"][i].y)
            topDeckDiscard = Image(deckDiscardPos, gameState.deckDiscard[-i].getFileName())
            topDeckDiscard.draw(self.window)
    
    def displayDeck(self, gameState):
        if gameState.cardDeck.isEmpty():
            topDeck = Image(self.pos["Deck"], "Cards/blank_card.png")
        else:
            topDeck = Image(self.pos["Deck"], "Cards/card_back.png")
        self.deckImg = topDeck.draw(self.window)

    def drag(self, e):
        if self.inDrag:
            return
        self.inDrag = True     
        self.deckImg.undraw()
        self.deckImg.anchor.x = e.x
        self.deckImg.anchor.y = e.y
        self.deckImg.draw(self.window)
        self.inDrag = False