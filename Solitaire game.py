from GameState import GameState
from GameController import GameController
from playArea import PlayingArea

def main():
    
    gameState = GameState()
    playingArea = PlayingArea()
    gameController = GameController(playingArea, gameState)
    playingArea.setValidator(gameController.makeValidDrop, gameController.turnCards)

    playingArea.draw(gameState)
    
    #playingArea.root.mainloop()

    playgame = True
    while playgame == True:
        clickPos = playingArea.window.getMouse()
        if clickPos is None:
            break
        # mouseX = int(clickPos.x)
        # mouseY = int(clickPos.y)
    #Load top 10 score
    #Check clicked on deck
    #Check if clicked on one of 7 packs
    #Check if card valid
    #Check for game over
    #Check for restart button press

    playingArea.window.close()
    #Add to top 10 if score is a new top 10
    #Display top 10
    #Ask to play again

main()