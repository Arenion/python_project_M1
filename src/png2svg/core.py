from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import svg

def conversion_pix_to_hexa(x,y):
    return ((int)(2*x/3),(int)((-np.sqrt(3)/3)*y+x/3))
def avg_col(L):

    if isinstance(L[0], list):
        sum_r,sum_g,sum_b = 0,0,0
        for ele in L:
            sum_r+=ele[0]/len(ele)
            sum_g+=ele[1]/len(ele)
            sum_b+=ele[2]/len(ele)
        return (int(sum_r),int(sum_g),int(sum_b))
    else:
        sum= 0
        for ele in L:
            sum+=ele
        return (int(sum),int(sum),int(sum))

def hexagon(height_hexagon,width_hexagon,flattop,center):
    Points=""
    Points+=str(center[0]+width_hexagon/2)+","+str(center[1]+height_hexagon)+" "
    Points+=str(center[0]+width_hexagon)+","+str(center[1])+" "
    Points+=str(center[0]+width_hexagon/2)+","+str(center[1]-height_hexagon)+" "
    Points+=str(center[0]-width_hexagon/2)+","+str(center[1]-height_hexagon)+" "
    Points+=str(center[0]-width_hexagon)+","+str(center[1])+" "
    Points+=str(center[0]-width_hexagon/2)+","+str(center[1]+height_hexagon)+" "

    return(Points)

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

    for i in range(width):
        for j in range(height):
            if conversion_pix_to_hexa(i,j) not in Dict_color:
                Dict_color[conversion_pix_to_hexa(i,j)] =[]
            Dict_color[conversion_pix_to_hexa(i,j)].append(image.getpixel(conversion_pix_to_hexa(i,j)))
    for ele in Dict_color:
        Dict_color[ele]=avg_col(Dict_color[ele])
    print("Dict_color:\n")
    print(Dict_color)
    print("List_Center:\n")
    print(List_centers)
    print("Dimensions:")
    print(len(Dict_color))
    print(len(List_centers))
    print(width)
    print(height)
    with open('output.svg','w') as f:
        f.write('<?xml version="1.0" standalone="no"?>\n')
        f.write('<svg width="4cm" height="4cm" viewBox="0 0 1200 400"\n')
        f.write('xmlns="http://www.w3.org/2000/svg" version="1.1">\n')
        f.write('<desc>Hexago output</desc>\n')
        for i in range(nbr_lines):
                for j in range(nbr_col):
                    if(i,j in List_centers):
                        center = List_centers[i,j,:]
                        if (i,j) in Dict_color:
                            color= Dict_color[(i,j)]
                        else:
                            color = (0,0,0)
                        f.write('<polygon fill="rgb('+str(color[0])+','+str(color[1])+','+str(color[2])+')" stroke="transparent" stroke_width="1" \n'+'points="'+hexagon(height_hexagon,width_hexagon,True,center)+'"'+"/>\n")
        # f.write('<polygon fill="red" stroke="rgb(1,1,1)" stroke-width="10" points="350,75  379,161 469,161 397,215 423,301 350,250 277,301 303,215 231,161 321,161" />')
        f.write('</svg>')
print([1,2]+[3,4])
png2svg("img/test.jpg","",5)
