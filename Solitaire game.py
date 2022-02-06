from GameState import GameState
from GameController import GameController
from playArea import PlayingArea
from homeScreen import HomeScreen
from gameWindow import GameWindow

def main():
    
    gameState = GameState()

    # Creates the windows
    gameWindow = GameWindow(gameState)
    homeScreen = HomeScreen(gameWindow)
    playingArea = PlayingArea(gameWindow, gameState)
    gameWindow.addScreens(homeScreen, playingArea)
    gameWindow.setActiveScreen(homeScreen)

    
    gameController = GameController(playingArea, gameState)
    playingArea.setValidator(gameController.makeValidDrop, gameController.turnCards)

    gameWindow.drawActiveScreen()
        
    #playingArea.root.mainloop()

    playgame = True
    while playgame == True:
        clickPos = gameWindow.getMouse()
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