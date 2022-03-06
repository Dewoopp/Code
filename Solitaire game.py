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
    parser.add_argument('-d', type = str, help="database action (delete or create test)")

    # Parse and print the results
    args = parser.parse_args()
    print(args.t)

    # Creates a copy of the database and passes in the database argument
    gameDb = GameDb(args.d)

    # Create a gameState and passes in the test case argument
    gameState = GameState(args.t)

    # Creates the windows
    gameWindow = GameWindow(gameState)
    homeScreen = HomeScreen(gameWindow, gameDb)
    playingArea = PlayingArea(gameWindow, gameState, gameDb)
    # Adds new screens
    gameWindow.addScreens(homeScreen, playingArea)
    # Sets the active screen to be the home screen if there is no argument
    # If there is, then it sets the active screen to the game screen
    gameWindow.setActiveScreen(homeScreen if args.t is None else playingArea)

    # Creates instances of the controller and the play area
    gameController = GameController(playingArea, gameState, gameDb)
    # Sets the validator function
    playingArea.setValidator(gameController.makeValidDrop, gameController.turnCards)

    # Draws the active screen
    gameWindow.drawActiveScreen()

    # Main loops that waits for user input
    playgame = True
    while playgame == True:
        clickPos = gameWindow.getMouse()
        if clickPos is None:
            break

    playingArea.window.close()

main()