import random
# Declare card class that will be used to build all the cards
class Card:
    # Initialises all the parameters
    def __init__(self, suit, number, colour, fileName):
        self.suit = suit
        self.number = number
        self.colour = colour
        self.fileName = fileName

    # Getter function to return the card name
    def cardName(self):
        cardName = self.suit + str(self.number)
        return cardName

    # Returns the file name
    def getFileName(self):
        return self.fileName


class CardDeck:
    def __init__(self):
        # Defines the cards list which will store all the cards
        self.cards = []
        self.suits = ["D", "C", "H", "S"]
        self.colours = ["R", "B", "R", "B"]
        self.cardNames = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # Initialises the objects from the card class
        for i in range(4):
            for j in range(13):
                # Gives the card the file name as given by the cutOutCards.py file
                currfileName = "Cards/" + self.suits[i] + self.cardNames[j] + ".png"
                # Defines the current Card
                currCard = Card(self.suits[i], j + 1, self.colours[i], currfileName)
                # Appends all cards to the cards array
                self.cards.append(currCard)
        # Shuffles the deck
        self.shuffleDeck()

    def shuffleDeck(self):
        # Shuffle the cards
        random.shuffle(self.cards)

    # Swaps two cards, this is used when creating test cases
    def swapCards(self, cardToSwap, cardIdx):
        for i, card in enumerate(self.cards):
            if card == cardToSwap:
                self.cards[cardIdx], self.cards[i] = self.cards[i], self.cards[cardIdx]
                break

    # Returns the card
    def getCard(self, suit, number):
        for card in self.cards:
            if card.suit == suit and card.number == number:
                return card

    def printDeck(self):
        # Prints the card names
        print(len(self.cards))
        for m in range(len(self.cards)):
            print(self.cards[m].cardName())
    
    # Remove the top card
    def removeTop(self):
        self.cards.remove(self.topCard())

    # Gets the top card
    def topCard(self):
        return self.cards[0]

    # Checks if the cards list is empty
    def isEmpty(self):
        return len(self.cards) == 0