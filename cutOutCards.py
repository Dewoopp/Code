
# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open(r"fullDeck.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
cardWidth = 78
cardHeight = 109
x_margin = 10
y_margin = 19.5
x_between = cardWidth + x_margin
y_between = cardHeight + y_margin

suits = ["D", "C", "H", "S"]
cardNum = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cardTop = [1, 130, 258, 387]
cardBot = [109, 238, 366, 495]
# Setting the points for cropped image
for i in range(4):
    top = cardTop[i]
    bottom = cardBot[i] + 1
    for j in range(13):
        left = 1 + x_between*j
        right = left + cardWidth

 
        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        
        # Shows the image in image viewer
        im1.save("Cards/" + suits[i] + cardNum[j] + ".png")