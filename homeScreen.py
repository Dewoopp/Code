from turtle import window_height, window_width
from urllib.parse import ParseResultBytes
from Button import Button
from graphics import GraphWin, Rectangle, Point, _root, Image, Text

class HomeScreen:
    def __init__(self, gameWindow, gameDb):
        self.gameWindow = gameWindow
        self.window = self.gameWindow.window
        # Defines the play button
        self.playButton = Button(self.window.width/2, self.window.height * 7/8, 150, 100, "Play")
        # Sets the background rectangle
        self.background = Rectangle(Point(0,0), Point(1000, 750))
        self.background.setFill("grey")

        self.delLbRows = []

        self.gameDb = gameDb

    # Undraws the screen
    def undraw(self):
        # Undraws the background and play button
        self.background.undraw()
        self.playButton.undraw()
        # Undraws the title if it exists
        if self.titleText is not None:
            self.titleText.undraw()
        # Undraws the subtitle if it exists
        if self.subtitleText is not None:
            self.subtitleText.undraw()
        # Undraws everything in delLbRows, which contains all the leaderboard text on the screen
        for row in self.delLbRows:
            for field in row:
                field.undraw()

    # Draws the screen
    def draw(self):
        self.background.draw(self.window)
        self.playButton.draw(self.window)

        # Defines the title text
        self.titleText = Text(Point(self.window.width/2, self.window.height/8), "Solitaire")
        self.titleText.setFace('courier')
        self.titleText.setSize(70)
        self.titleText.setFill("white")
        self.titleText.draw(self.window)
        
        # Defines the subtitle text
        self.subtitleText = Text(Point(self.window.width/2, self.window.height/5), "by Joe Dobson")
        self.subtitleText.setFace('courier')
        self.subtitleText.setSize(30)
        self.subtitleText.setFill("white")
        self.subtitleText.draw(self.window)
        
        # Defines the leaderboard text
        self.scoreText = Text(Point(self.window.width/2, self.window.height/3), "Leaderboard")
        self.scoreText.setFace('helvetica')
        self.scoreText.setSize(20)
        self.scoreText.setFill("white")
        self.scoreText.draw(self.window)
        
        # Gets the data from the database
        data = self.gameDb.getData()

        # Sets the data for the headings
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
            # Adds the row of text to delLbRows, which is used to undraw the text
            self.delLbRows.append(lbRow)
            
            # Displays the data from the database
            for i, row in enumerate(data):
                # Ensures that only the top 5 players will be displayed
                if i >= 5:
                    break
                lbRow = []
                for j, field in enumerate(row):
                    # Creates the rank of the winners
                    fieldText = Text(Point(self.window.width/3.35 + 100 * j, self.window.height/2 + 50 * i), field if j != 0 else i+1)
                    fieldText.setFace('helvetica')
                    fieldText.setSize(15)
                    fieldText.setFill("white")
                    # Draws the text
                    fieldText.draw(self.window)
                    lbRow.append(fieldText)
                # Adds the row of text to delLbRows, which is used to undraw the text
                self.delLbRows.append(lbRow)

    def click(self, e):
        pass
    def drag(self, e):
        pass
    def drop(self, e):
        # If the user pressed the play button then start the game
        if self.playButton.isPressed(e.x, e.y):
            self.gameWindow.playGame()