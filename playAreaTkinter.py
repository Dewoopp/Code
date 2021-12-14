import tkinter as Tk
from Point import Point
from Image import Image
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
        self.root = Tk.Tk()
        self.root.title("Solitaire")
        self.root.geometry("1000x750")
        self.root.bind('<B1-Motion>', self.drag)

        self.canvas = Tk.Canvas(self.root, width=1000, height=750, bg="green")
        self.canvas.pack()

        #background = Rectangle(Point(0,0), Point(1000, 750))
        #background.setFill("green")
        #background.draw(self.window)
        
        for i in range(7):
            self.pos["Stacks"].append(Point(75 + 100*i, 75))

        for i in range(4):
            self.pos["SuitStacks"].append(Point(825 + 100*(i % 2), 75 + 130*(i // 2)))

        self.pos["Deck"] = Point(825, 345)
        self.pos["DeckDiscard"] = Point(825, 475)

    def displayStacks(self, gameState):
        self.stackImgs = []
        for i in range(7):
            for j in range(i + 1):
                topCardPos = Point(self.pos["Stacks"][i].x, self.pos["Stacks"][i].y + j * 30)
                if gameState.cardStacks[i].backNum > j:
                    filename = "Cards/card_backii.png"
                else:
                    filename = gameState.cardStacks[i].cards[j].getFileName()
                self.stackImgs.append(Image(filename, topCardPos.x, topCardPos.y, self.root, self.canvas))
        
    def displaySuitStacks(self, gameState):
        for i in range(4):
            suitStackPos = Point(self.pos["SuitStacks"][i].x, self.pos["SuitStacks"][i].y)
            if gameState.suitStacks[i].isEmpty():
                filename = "Cards/blank_card.png"
            Image(filename, suitStackPos.x, suitStackPos.y, self.root, self.canvas)

    def displayDeckDiscard(self, gameState):
        for i in range(min(3, len(gameState.deckDiscard))):
            deckDiscardPos = Point(self.pos["DeckDiscard"][i].x + i * 30, self.pos["DeckDiscard"][i].y)
            filename = gameState.deckDiscard[-i].getFileName()
            Image(filename, deckDiscardPos.x, deckDiscardPos.y, self.root, self.canvas)
    
    def displayDeck(self, gameState):
        if gameState.cardDeck.isEmpty():
            filename = "Cards/blank_card.png"
        else:
            filename = "Cards/card_back.png"
        Image(filename, self.pos["Deck"].x, self.pos["Deck"].y, self.root, self.canvas)

    def drag(self, e):
        print(e.widget)
        #self.window.redraw()
