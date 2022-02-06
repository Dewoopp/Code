from urllib.parse import ParseResultBytes
from graphics import GraphWin, Rectangle, Point, _root, Image

class HomeScreen:
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.window = self.gameWindow.window
        self.playButton = None
        self.background = Rectangle(Point(0,0), Point(1000, 750))
        self.background.setFill("blue")

    def undraw(self):
        self.background.undraw()
        if self.playButton is not None:
            self.playButton.undraw()

    def draw(self):
        self.background.draw(self.window)
        self.playButton = Rectangle(Point(200, 200), Point(300, 300))
        self.playButton.setFill("purple")
        self.playButton.draw(self.window)

    def click(self, e):
        pass
    def drag(self, e):
        pass
    def drop(self, e):
        self.gameWindow.playGame()