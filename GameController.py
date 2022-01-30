class GameController:
    def __init__(self, playingArea, gameState):
        self.playingArea = playingArea
        self.gameState = gameState


    def makeValidDrop(self, clickedName, clickedIdx, clickedCards, name, idx, onCard, stackLocation):
        dropValid = self.isValid(clickedName, clickedIdx, clickedCards, name, idx, onCard, stackLocation)
        if dropValid:
            self.gameState.makeMove(clickedCards, name, idx)
        
        self.playingArea.draw(self.gameState)

    def isValid(self, clickedName, clickedIdx, clickedCards, name, idx, onCard, stackLocation):
        # If we are dropping on a suitstack and the length of the cards we picked up is exactly 1
        if name == "SuitStacks" and len(clickedCards) == 1:
            # If dropping on an empty suitstack while the picked up card is an ace then return True else return False
            if len(onCard) == 0:
                return clickedCards[0].number == 1
            # If we have one card picked up, the suit is the same and the number is one more then return True else return False
            return clickedCards[0].suit == onCard[0].suit and clickedCards[0].number == onCard[0].number + 1
        # If we are dropping on a stack and we are dropping at the end of a stack
        if name == "Stacks" and stackLocation == 0:
            return clickedCards[0].colour != onCard[0].colour and clickedCards[0].number == onCard[0].number - 1
        return False
        