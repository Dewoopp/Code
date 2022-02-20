from GameState import GameState
from GameController import GameController
from playArea import PlayingArea
from homeScreen import HomeScreen
from gameWindow import GameWindow
from Database import GameDb
import argparse

def main():

    # Create the parser and add arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type = str, help="name a test case")

    # Parse and print the results
    args = parser.parse_args()
    print(args.t)

    gameDb = GameDb()
    #gameDb.deleteTable()
    #gameDb.createTestData()
    #gameDb.getData()

    gameState = GameState(args.t)

    # Creates the windows
    gameWindow = GameWindow(gameState)
    homeScreen = HomeScreen(gameWindow, gameDb)
    playingArea = PlayingArea(gameWindow, gameState)
    gameWindow.addScreens(homeScreen, playingArea)
    gameWindow.setActiveScreen(homeScreen if args.t is None else playingArea)

    
    gameController = GameController(playingArea, gameState, gameDb)
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