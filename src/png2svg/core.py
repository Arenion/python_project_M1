from PIL import Image

source_image="img/screenshot.jpg"

image = Image.open(source_image)

width,height =image.size

def getsizehexa(): #The goal of this first function is to get the "size" of the hexagon according to: https://www.redblobgames.com/grids/hexagons/#basics
    #to find the size of an hexagon, we take a look at all the pixel, then we go right and left until we found another color, we then add the distances on the right and the left, and we then take the minimum of these distances as our width which we will divide by two to get our size
    for x in range(width):
        for y in range(height):
            color = image.getpixel((x,y))
            print(color)
getsizehexa()
