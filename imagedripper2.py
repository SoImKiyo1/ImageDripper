from PIL import Image
import random

image1 = Image.open("Mon_image.jpg")	# L’image se situe dans le même répertoire
L, H = image1.size
image2 = Image.new("RGB",(L,int(H * 1.2)))

for x in range(L):
    N = random.randint(int(-0.1 * H), int(0.1 * H))
    for y in range(H):
        pixel = image1.getpixel((x,y))
        r = pixel[0]
        v = pixel[1]
        b = pixel[2]
        image2.putpixel((x,(y + int(0.1 * H) + N)),(r,v,b))

image2 = image2.crop((0, int(H * 0.2), L, int(H * 1.2) - int(H * 0.2)))

image2.save("maNouvelleImage7.png")
image2.show()