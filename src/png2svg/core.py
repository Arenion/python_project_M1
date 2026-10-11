from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def conversion_pix_to_hexa(x,y):
    return ((int)(2*x/3),(int)((-np.sqrt(3)/3)*y+x/3))



def png2svg(source_image,output_file,size):
    image = Image.open(source_image)
    width,height =image.size
    print(width)
    print(height)
    height_hexagon=np.sqrt(3)*size/2
    width_hexagon=size
    nbr_col = (int) (width/(2*width_hexagon))
    nbr_lines = (int) (height/(2*height_hexagon))
    #taille de l'image en coordonnées hexagonales
    print(nbr_col)
    print(nbr_lines)
    Dict_color={}#we will put all the average colors in a single dictionary
    List_centers=np.zeros((nbr_lines,nbr_col,2))#array of the centers of the hexagons: the i,j correspond to the coordinates in hexagons and the value associated in the traditional coordinates
    for i in range(nbr_lines):
        for j in range(nbr_col):
            if i%2==1:
                List_centers[i,j,0]=(2*i+1)*height_hexagon
                List_centers[i,j,1]=(2*(j+1))*width_hexagon
            else:
                List_centers[i,j,0]=(2*i+1)*height_hexagon
                List_centers[i,j,1]=(2*j+1)*width_hexagon
    X=List_centers[:,:,0].reshape(-1)
    Y=List_centers[:,:,1].reshape(-1)
    print(X)
    plt.scatter(Y,X)
    plt.show()

print([1,2]+[3,4])
png2svg("img/screenshot.jpg","",10)
