from graphics import Rectangle, Point, Text

class Button:
    def __init__(self, x, y, w, h, text):
        self.button = None

        # Defines the x, y, width, height and text of the button
        self.text = text
        self.x = x
        self.y = y
        self.buttonWidth = w
        self.buttonHeight = h
        
    # Draws the button
    def draw(self, window):
        self.button = Rectangle(Point(self.x - self.buttonWidth/2, self.y - self.buttonHeight/2), Point(self.x + self.buttonWidth/2, self.y + self.buttonHeight/2))
        self.button.setFill("black")
        self.button.draw(window)
        if self.text is not None:
            self.buttonText = Text(Point(self.x, self.y), self.text)
            self.buttonText.setFace('courier')
            self.buttonText.setSize(15)
            self.buttonText.setFill("white")
            self.buttonText.draw(window)

    # Undraws the button
    def undraw(self):
        if self.button is not None:
            self.button.undraw()
        if self.buttonText is not None:
            self.buttonText.undraw()

    # Checks if the button is pressed
    def isPressed(self, x, y):
        return self.x - self.buttonWidth/2 < x < self.x + self.buttonWidth/2 and self.y - self.buttonHeight/2 < y < self.y + self.buttonHeight/2