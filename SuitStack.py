class SuitStack:
    def __init__(self):
        self.cards = []

    def append(self, card):
        self.cards.append(card)    
            
    def isEmpty(self):
        return len(self.cards) == 0