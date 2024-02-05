
from PIL import Image           #Importation du module PIL
import random           #Importation du module random

image1 = Image.open("Mon_image.jpg")	# L’image se situe dans le même répertoire
L, H = image1.size    #Récupération de la longueur et de la hauteur dans les variables L et H
image2 = Image.new("RGB",(L,int(H * 1.2)))  #Augmentation de la hauteur de l'image en multipliant par 1.2

for x in range(L):
    N = random.randint(int(-0.1 * H), int(0.1 * H))  #Création d'un nombre aléatoire dans la variable N
    for y in range(H):
        pixel = image1.getpixel((x,y))  #Récupération des pixels de coordonées x,y
        r = pixel[0]    #Placement des pixel rouges dans la variable r
        v = pixel[1]    #Placement des pixel verts dans la variable v
        b = pixel[2]    #Placement des pixel bleus dans la variable b
        image2.putpixel((x,(y + int(0.1 * H) + N)),(r,v,b))     #

image2 = image2.crop((0, 100, 0, -100))

image2.save("maNouvelleImage6.png")	# L’image se situera au même endroit
image2.show()