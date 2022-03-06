
# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open(r"fullDeck.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Sets the width, height and the distance between the cards
cardWidth = 78
cardHeight = 109
x_margin = 10
y_margin = 19.5
x_between = cardWidth + x_margin
y_between = cardHeight + y_margin

# Sets the suits and the number, this is used when making the file name
suits = ["D", "C", "H", "S"]
cardNum = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Manually setting the locations of the cards
cardTop = [1, 130, 258, 387]
cardBot = [109, 238, 366, 495]
# Setting the points for cropped image
for i in range(4):
    # Sets the top and bottom of the current cards using the cardTop and cardBot arrays
    top = cardTop[i]
    bottom = cardBot[i] + 1
    for j in range(13):
        # Sets the left and right of the cards by using the distance between them
        left = 1 + x_between*j
        right = left + cardWidth

        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        
        # Saves the image to a new file
        im1.save("Cards/" + suits[i] + cardNum[j] + ".png")