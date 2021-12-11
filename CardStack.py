class CardStack:
    def __init__(self, backNum):
        self.cards = []
        self.backNum = backNum

    def append(self, card):
        self.cards.append(card)