from GameState import GameState
from graphics import GraphWin, Rectangle, Point, _root, Image
import tkinter as Tk
from playArea import PlayingArea

def main():
    
    gameState = GameState()
    playingArea = PlayingArea()

    playingArea.displayStacks(gameState)
    playingArea.displaySuitStacks(gameState)
    playingArea.displayDeckDiscard(gameState)
    playingArea.displayDeck(gameState)
    
    #playingArea.root.mainloop()

    playgame = True
    while playgame == True:
        clickPos = playingArea.window.getMouse()
        mouseX = int(clickPos.x)
        mouseY = int(clickPos.y)
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