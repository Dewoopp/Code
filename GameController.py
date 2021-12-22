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
        if name == "SuitStacks" and len(clickedCards) == 1:
            if onCard == None and clickedCards[0].number == 1:
                return True
            if clickedCards[0].suit == onCard.suit and clickedCards[0].number == onCard.number + 1:
                return True
        return False