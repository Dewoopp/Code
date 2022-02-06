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

    def drawActiveScreen(self):
        self.activeScreen.draw()
    def setActiveScreen(self, window):
        self.activeScreen = window

    def addScreens(self, homeScreen, playArea):
        self.homeScreen = homeScreen
        self.playArea = playArea

    def getMouse(self):
        self.window.getMouse()

    def playGame(self):
        self.homeScreen.undraw()
        self.activeScreen = self.playArea
        self.playArea.draw()

    def drag(self, e):
        self.activeScreen.drag(e)
    def drop(self, e):
        self.activeScreen.drop(e)
    def click(self, e):
        self.activeScreen.click(e)
