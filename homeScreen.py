from turtle import window_height, window_width
from urllib.parse import ParseResultBytes
from graphics import GraphWin, Rectangle, Point, _root, Image, Text

class HomeScreen:
    def __init__(self, gameWindow, gameDb):
        self.gameWindow = gameWindow
        self.window = self.gameWindow.window
        self.playButton = None
        self.background = Rectangle(Point(0,0), Point(1000, 750))
        self.background.setFill("grey")

        self.delLbRows = []

        self.gameDb = gameDb

    def undraw(self):
        self.background.undraw()
        if self.playButton is not None:
            self.playButton.undraw()
        if self.titleText is not None:
            self.titleText.undraw()
        if self.subtitleText is not None:
            self.subtitleText.undraw()
        for row in self.delLbRows:
            for field in row:
                field.undraw()


    def draw(self):
        self.background.draw(self.window)
        self.playButton = Rectangle(Point(200, 400), Point(300, 300))
        self.playButton.setFill("purple")
        self.playButton.draw(self.window)

        self.titleText = Text(Point(self.window.width/2, self.window.height/8), "Solitaire")
        self.titleText.setFace('courier')
        self.titleText.setSize(70)
        self.titleText.setFill("white")
        self.titleText.draw(self.window)
        

        self.subtitleText = Text(Point(self.window.width/2, self.window.height/5), "by Joe Dobson")
        self.subtitleText.setFace('courier')
        self.subtitleText.setSize(30)
        self.subtitleText.setFill("white")
        self.subtitleText.draw(self.window)
        

        self.scoreText = Text(Point(self.window.width/2, self.window.height/3), "Leaderboard")
        self.scoreText.setFace('helvetica')
        self.scoreText.setSize(20)
        self.scoreText.setFill("white")
        self.scoreText.draw(self.window)
        

        data = self.gameDb.getData()

        for i, row in enumerate(data):
            lbRow = []
            for j, field in enumerate(row):
                fieldText = Text(Point(self.window.width/3 + 100 * j, self.window.height/2 + 50 * i), field)
                fieldText.setFace('helvetica')
                fieldText.setSize(15)
                fieldText.setFill("white")
                fieldText.draw(self.window)
                lbRow.append(fieldText)
            self.delLbRows.append(lbRow)

        print(data)



    def click(self, e):
        pass
    def drag(self, e):
        pass
    def drop(self, e):
        self.gameWindow.playGame()