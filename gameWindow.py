from graphics import GraphWin, Rectangle, Point, _root, Image
from playArea import PlayingArea

class GameWindow:
    def __init__(self, gameState):

        self.gameState = gameState
        self.window = GraphWin("Screen", 1000, 750)

        self.activeScreen = None

        # Binds function calls to actions from the user
        self.window.bind('<B1-Motion>', self.drag)
        self.window.bind('<ButtonRelease-1>', self.drop)
        self.window.bind('<ButtonPress-1>', self.click)

    # Calls the draw function of whichever screen is currently active
    def drawActiveScreen(self):
        self.activeScreen.draw()
    
    # Sets the active screen
    def setActiveScreen(self, window):
        self.activeScreen = window

    # Adds a new screen
    def addScreens(self, homeScreen, playArea):
        self.homeScreen = homeScreen
        self.playArea = playArea

    def getMouse(self):
        self.window.getMouse()

    # Deactivates the home screen and draws the play area screen
    def playGame(self):
        self.homeScreen.undraw()
        self.activeScreen = self.playArea
        self.playArea.draw()

    # Deactivates the play area screen and draws the home screen
    def returnHome(self):
        self.playArea.undraw(True)
        self.activeScreen = self.homeScreen
        self.homeScreen.draw()

    # Calls the drag, drop or click function of the current active screen
    def drag(self, e):
        self.activeScreen.drag(e)
    def drop(self, e):
        self.activeScreen.drop(e)
    def click(self, e):
        self.activeScreen.click(e)
