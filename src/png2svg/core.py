from PIL import Image

source_image="img/screenshot.jpg"

image = Image.open(source_image)

width,height =image.size

def getsizehexa(): #The goal of this first function is to get the "size" of the hexagon according to: https://www.redblobgames.com/grids/hexagons/#basics
    #to find the size of an hexagon, we take a look at all the pixel, then we go right and left until we found another color, we then add the distances on the right and the left, and we then take the minimum of these distances as our size ( it would correspond to the upper/lower part of an hexagon)
    List_sizes= []
    for x in range(width):
        for y in range(height):
            color = image.getpixel((x,y))
            x_right= 0
            x_left = 0
            while (x+x_right<width) and image.getpixel((x+x_right,y))==color:
                x_right+=1
            while (x-x_left>0) and image.getpixel((x-x_left,y))==color:
                x_left+=1
            if (x_left+x_right) not in List_sizes:
                List_sizes.append(x_left+x_right)
    List_sizes.sort()
    print(List_sizes)
    for i in range(len(List_sizes)):
        if List_sizes[i]!=List_sizes[0]:#we do not count the cropped hexagons
            return List_sizes[i]
print(getsizehexa())
print(width)
print(height)
