class CardStack:
    def __init__(self, backNum):
        self.cards = []
        self.backNum = backNum

    def find(self, card):
        try:
            return self.cards.index(card)
        except Exception as excp:
            return None
    
    def removeBelow(self, idx):
        self.cards = self.cards[idx:]
    
    def getBelow(self, idx):
        return self.cards[idx:]

    def append(self, card):
        self.cards.append(card)