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

        background = Rectangle(Point(0,0), Point(800, 500))
        background.setFill("green")
        background.draw(self.window)
        
        for i in range(7):
            self.pos["Stacks"].append(Point(50 + 100*i, 50))

        for i in range(4):
            self.pos["SuitStacks"].append(Point(800 + 100*(i % 2), 50 + 130*(i // 2)))

        self.pos["Deck"] = Point(800, 500)
        self.pos["DeckDiscard"] = Point(900, 500)
    
    def displayStacks(self, gameState):
        for i in range(7):
            for j in range(i + 1):
                topCardDeck = Image(self.pos["Stacks"][i], gameState.cardStacks[i][j].getFileName())
                topCardDeck.draw(self.window)

