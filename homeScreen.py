from turtle import window_height, window_width
from urllib.parse import ParseResultBytes
from Button import Button
from graphics import GraphWin, Rectangle, Point, _root, Image, Text

class HomeScreen:
    def __init__(self, gameWindow, gameDb):
        self.gameWindow = gameWindow
        self.window = self.gameWindow.window
        self.playButton = Button(self.window.width/2, self.window.height * 7/8, 150, 100, "Play")
        self.background = Rectangle(Point(0,0), Point(1000, 750))
        self.background.setFill("grey")

        self.delLbRows = []

        self.gameDb = gameDb

    def undraw(self):
        self.background.undraw()
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

        headingData = ["Place", "Name", "Moves", "Time(s)", "Score"]

        if len(data) > 0:
            # Displays the headings for the leaderboard
            lbRow = []
            for i in range(len(data[0])):
                headingText = Text(Point(self.window.width/3.35 + 100 * i, self.window.height/2 - 50), headingData[i])
                headingText.setFace('helvetica')
                headingText.setSize(15)
                headingText.setFill("white")
                headingText.draw(self.window)
                lbRow.append(headingText)
            self.delLbRows.append(lbRow)
            
            # Displays the data from the database
            for i, row in enumerate(data):
                if i >= 5:
                    break
                lbRow = []
                for j, field in enumerate(row):
                    fieldText = Text(Point(self.window.width/3.35 + 100 * j, self.window.height/2 + 50 * i), field if j != 0 else i+1)
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
        if self.playButton.isPressed(e.x, e.y):
            self.gameWindow.playGame()