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
        self.cardNames = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        #Initialises the objects from the card class
        for i in range(4):
            for j in range(13):
                #Gives the card the file name as given by the cutOutCards.py file
                currfileName = "Cards/" + self.suits[i] + self.cardNames[j] + ".png"
                #Defines the current Card
                currCard = Card(self.suits[i], j + 1, self.colours[i], currfileName)
                #Appends all cards to the cards array
                self.cards.append(currCard)
        #Shuffles the deck
        self.shuffleDeck()
        self.createTestCase()


    def shuffleDeck(self):
        #Shuffle the cards
        random.shuffle(self.cards)

    def swapCards(self, cardToSwap, cardIdx):
        for i, card in enumerate(self.cards):
            if card == cardToSwap:
                self.cards[cardIdx], self.cards[i] = self.cards[i], self.cards[cardIdx]
                break

    def createTestCase(self):
        self.swapCards(self.getCard("S", 7), 0)
        self.swapCards(self.getCard("C", 7), 2)
        self.swapCards(self.getCard("D", 8), 5)

    def getCard(self, suit, number):
        for card in self.cards:
            if card.suit == suit and card.number == number:
                return card

    def printDeck(self):
        #Prints the card names
        print(len(self.cards))
        for m in range(len(self.cards)):
            print(self.cards[m].cardName())
    
    def removeTop(self):
        self.cards.remove(self.topCard())

    def topCard(self):
        return self.cards[0]

    def isEmpty(self):
        return len(self.cards) == 0