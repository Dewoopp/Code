import time, math, random
from graphics import GraphWin, Rectangle, Point, _root, Image
import tkinter as tk
import os


#Declare card class that will be used to build all the cards
class card:
    #Initialises all the parameters
    def __init__(self, suit, number, colour, fileName):
        self.suit = suit
        self.number = number
        self.colour = colour
        self.fileName = fileName

    #Getter fucntion to return the card name
    def cardName(self):
        cardName = self.suit + self.number
        return cardName

    def getFileName(self):
        return self.fileName



def main():

    #Defines the cards list which will store all the cards
    cards = []
    suits = ["D", "C", "H", "S"]
    colours = ["R", "B", "R", "B"]
    cardNum = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    #Initialises the objects from the card class
    for i in range(4):
        for j in range(13):
            #Gives the card the file name as given by the cutOutCards.py file
            currfileName = "Cards/" + suits[i] + cardNum[j] + ".png"
            #Defines the current Card
            currCard = card(suits[i], cardNum[j], colours[i], currfileName)
            #Appends all cards to the cards array
            cards.append(currCard)
    

    
    #Shuffle the cards
    random.shuffle(cards)



    #Swaps the cards - to randomise the cards in the cards array
    #storeCard = ""
    
    # for n in range(50):
    #     currPos = random.randint(0, len(cards) - 1)
    #     swapPos = random.randint(0, len(cards) - 1)
    #     storeCard = cards[currPos]
    #     cards[currPos] = cards[swapPos]
    #     cards[swapPos] = storeCard



    cardStack = []
    #Creates 7 lists of increasing no. of cards - creates each card stack
    for i in range(7):
        cardTemp = []
        for j in range(i + 1):
            cardTemp.append(cards[0])
            cards.remove(cards[0])
        cardStack.append(cardTemp)


    #Prints the card names
    print(len(cards))
    for m in range(len(cards)):
        print(cards[m].cardName())






    #Defines the window
    window = GraphWin("Solitaire", 800, 500)


    background = Rectangle(Point(0,0), Point(800, 500))
    background.setFill("green")
    background.draw(window)

    #Load top 10 score
    #print(os.getcwd())
    for i in range(7):
        for j in range(i + 1):
            topCardDeck = Image(Point(100 + 100*i,100 + 20*j), cardStack[i][j].getFileName())
            topCardDeck.draw(window)
            #tk.PhotoImage(file=cardStack[i][j].getFileName(), master=_root)
            #pass

    playgame = True
    while playgame == True:
        clickPos = window.getMouse()
        mouseX = int(clickPos.x)
        mouseY = int(clickPos.y)
    #Check clicked on deck
    #Check if clicked on one of 7 packs
    #Check if card valid
    #Check for game over
    #Check for restart button press

    window.close()
    #Add to top 10 if score is a new top 10
    #Display top 10
    #Ask to play again




main()