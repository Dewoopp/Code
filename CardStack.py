class CardStack:
    def __init__(self, backNum):
        self.cards = []
        # Sets the number of cards that are back up (cannot be clicked on)
        self.backNum = backNum

    # Uses an exception to try to find the card
    def find(self, card):
        try:
            return self.cards.index(card)
        except Exception as excp:
            return None
    
    # Removes all cards below the specified index
    def removeBelow(self, idx):
        self.cards = self.cards[:idx]
    
    # Gets all cards below the specified index
    def getBelow(self, idx):
        return self.cards[idx:]

    # adds the card to cards array
    def append(self, card):
        self.cards.append(card)