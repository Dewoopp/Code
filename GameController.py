class GameController:
    def __init__(self, playingArea, gameState):
        self.playingArea = playingArea
        self.gameState = gameState


    def validDrop(self, clickedName, clickedIdx, clickedCards, name, idx, onCard):
        dropValid = self.isValid(clickedName, clickedIdx, clickedCards, name, idx, onCard)
        if dropValid:
            self.gameState.makeMove(clickedCards, name, idx)
        
        self.playingArea.draw(self.gameState)

    def isValid(self, clickedName, clickedIdx, clickedCards, name, idx, onCard):
        # If we are dropping on a suitstack and the length of the cards we picked up is exactly 1
        if name == "SuitStacks" and len(clickedCards) == 1:
            # If dropping on an empty suitstack while the picked up card is an ace then return True else return False
            if len(onCard) == 0:
                return clickedCards[0].number == 1
            # If we have one card picked up, the suit is the same and the number is one more then return True else return False
            return clickedCards[0].suit == onCard[0].suit and clickedCards[0].number == onCard[0].number + 1
        return False