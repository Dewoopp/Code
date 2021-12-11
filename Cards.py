import random
#Declare card class that will be used to build all the cards
class Card:
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


class CardDeck:
    def __init__(self):
        #Defines the cards list which will store all the cards
        self.cards = []
        self.suits = ["D", "C", "H", "S"]
        self.colours = ["R", "B", "R", "B"]
        self.cardNum = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        #Initialises the objects from the card class
        for i in range(4):
            for j in range(13):
                #Gives the card the file name as given by the cutOutCards.py file
                currfileName = "Cards/" + self.suits[i] + self.cardNum[j] + ".png"
                #Defines the current Card
                currCard = Card(self.suits[i], self.cardNum[j], self.colours[i], currfileName)
                #Appends all cards to the cards array
                self.cards.append(currCard)
        #Shuffles the deck
        self.shuffleDeck()


    def shuffleDeck(self):
        #Shuffle the cards
        random.shuffle(self.cards)

    def printDeck(self):
        #Prints the card names
        print(len(self.cards))
        for m in range(len(self.cards)):
            print(self.cards[m].cardName())
    
    def removeTop(self):
        self.cards.remove(self.topCard())

    def topCard(self):
        return self.cards[0]