from GameState import GameState


class GameController:
    def __init__(self, playingArea, gameState, gameDb):
        self.playingArea = playingArea
        self.gameState = gameState

        self.gameDb = gameDb

    def makeValidDrop(self, clickedName, clickedIdx, clickedCards, name, idx, onCard, stackLocation):
        dropValid = self.isValid(clickedName, clickedIdx, clickedCards, name, idx, onCard, stackLocation)
        if dropValid:
            self.gameState.makeMove(clickedCards, name, idx)
            if self.gameState.isGameOver():
                print("You won")
        
        self.playingArea.draw()

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
            if len(onCard) == 0:
                return clickedCards[0].number == 13
            return clickedCards[0].colour != onCard[0].colour and clickedCards[0].number == onCard[0].number - 1
        return False

    def turnCards(self):
        if self.gameState.cardDeck.isEmpty():
            self.gameState.cardDeck.cards = self.gameState.deckDiscard
            self.gameState.deckDiscard = []
        else:
            # Move and remove using slice
            numToMove = min(3, len(self.gameState.cardDeck.cards))
            self.gameState.deckDiscard.extend(self.gameState.cardDeck.cards[:numToMove])
            self.gameState.cardDeck.cards = self.gameState.cardDeck.cards[numToMove:]

            # # Move and remove using list comp
            # moveList = self.gameState.cardDeck.cards[-min(3, len(self.gameState.cardDeck.cards)):]
            # self.gameState.deckDiscard.extend(moveList)
            # self.gameState.cardDeck.cards = [card for card in self.gameState.cardDeck.cards if card not in moveList]

            # # Move and remove using remove
            # moveList = self.gameState.cardDeck.cards[-min(3, len(self.gameState.cardDeck.cards)):]
            # self.gameState.deckDiscard.extend(moveList)
            # for card in moveList:
            #     self.gameState.cardDeck.cards.remove(card)