import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import random

# Definition des parametres de la fenetre
fen = tk.Tk()
fen.geometry("1200x700")
fen.title("ImageDripper")
fen.resizable(False,False)

fond = "#ECF3FC"
fond2 = "#45536B"
boutton = "#9CB8E0"
bouttonsurvol = "#afcaf0"
fontperso=("Roboto", 20, "bold")

fen.configure(background=fond, padx=10, pady=10)

#Canvas pour le fond de l'image

imageback = Canvas(fen, width=1000, height=500, background=boutton, highlightthickness=0)
imageback.pack()
imageback.place(x=150, y=60)

#Canvas pour le fond des bouttons

buttonback = Canvas(fen, width=400, height=500, background=fond2, highlightthickness=0)
buttonback.pack()
buttonback.place(x=750, y=60)


chemin = 1
def selectionchemin(value):
    global chemin
    chemin = value
    return chemin

def preset1chemin(*args):
    selectionchemin(2)

def preset2chemin(*args):
    selectionchemin(1)

def preset3chemin(*args):
    selectionchemin(3)

def importerchemin(*args):
    selectionchemin(4)


imageimporter = None
preset1_image = None
preset2_image = None
preset3_image = None

def importerimage():
    if chemin == 4:
        # Spécification des types de fichiers autorisés dans la boîte de dialogue
        extensionsimage = [("JPG", "*.jpg"),("PNG","*.png"),("Tous","*")]
        # Ouverture de la boîte de dialogue pour sélectionner un fichier
        nomimage = filedialog.askopenfilename(filetypes=extensionsimage)
        if nomimage:
            global imageimporter
            imageimporter = Image.open(nomimage)
            # Redimensionnement de l'image
            imageimporter11 = imageimporter.resize((600,500))
            # Conversion de l'image en format utilisable par tkinter
            imageimporter11 = ImageTk.PhotoImage(imageimporter11)
            # Affichage de l'image dans un Label
            label_imageimporter = tk.Label(fen, image=imageimporter11, border=0)
            label_imageimporter.place(x=150, y=60)
            label_imageimporter.image = imageimporter11  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python (elle n'est pas réutilisée ailleurs)
    if chemin == 1:
        global preset1_image
        # Chargement du preset 1
        preset1_image = Image.open("preset1.png")
        preset11_image = preset1_image.resize((600,500))
        preset11_image = ImageTk.PhotoImage(preset11_image)
        # Création du label pour afficher le preset 1
        label_preset1 = Label(fen, image=preset11_image, border=0)
        label_preset1.place(x=150, y=60)  # Placement du label dans la fenêtre
        label_preset1.image = preset11_image  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python
    if chemin == 2:
        global preset2_image
        # Chargement du preset 2
        preset2_image = Image.open("preset2.png")
        preset21_image = preset2_image.resize((600,500))
        preset21_image = ImageTk.PhotoImage(preset21_image)
        # Création du label pour afficher le preset 2
        label_preset2 = Label(fen, image=preset21_image, border=0)
        label_preset2.place(x=150, y=60)  # Placement du label dans la fenêtre
        label_preset2.image = preset21_image  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python
    if chemin == 3:
        global preset3_image
        # Chargement du preset 3
        preset3_image = Image.open("preset3.png")
        preset31_image = preset3_image.resize((600,500))
        preset31_image = ImageTk.PhotoImage(preset31_image)
        # Création du label pour afficher le preset 3
        label_preset3 = Label(fen, image=preset31_image, border=0)
        label_preset3.place(x=150, y=60)  # Placement du label dans la fenêtre
        label_preset3.image = preset31_image  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python

variable = 1
def selectioneffet(value):
    global variable
    variable = value
    return variable

def bouton_horizontal_click(*args):
    selectioneffet(2)

def bouton_vertical_click(*args):
    selectioneffet(1)

def bouton_verthoriz_click(*args):
    selectioneffet(3)

horizontal2 = None
vertical2 = None
verthoriz3 = None

force = 0
def mise_a_jour_force(event):
    global force
    force = (scale.get() * 0.4) / 100
    print("Nouvelle valeur du curseur :", scale.get())
    print("Force calculée :", force)

# Slider Force
texte_force = tk.Label(fen, text="Force:",background=fond2, foreground=fond, font=fontperso, border=0)
texte_force.place(x=840, y=280)

style = ttk.Style()
style.configure('Custom.Horizontal.TScale', background=fond2, foreground=fond, troughcolor=fond)

scale = ttk.Scale(fen, from_=0, to=100, orient='horizontal', length=200, style='Custom.Horizontal.TScale', command=mise_a_jour_force)
scale.place(x=840, y=330)

def effetsimage():
    if variable == 2:
        if preset1_image is not None and chemin == 1 :
            horizontal1 = preset1_image
        if preset2_image is not None and chemin == 2 :
            horizontal1 = preset2_image
        if preset3_image is not None and chemin == 3 :
            horizontal1 = preset3_image
        if imageimporter is not None and chemin == 4 :
            horizontal1 = imageimporter
        L, H = horizontal1.size                      # Récupération de la longueur et de la hauteur de l'image d'origine dans les variables L et H
        global horizontal2
        horizontal2 = Image.new("RGB",(int(L * (1+2*force)),H))  # Création d'une nouvelle image vierge 1,2 fois plus large et de même hauteur que l'image d'origine
        for y in range(H):                                  # Itération pour chaque ligne
            N = random.randint(int(-force * L), int(force * L)) # Création d'un nombre aléatoire dans la variable N (correspond au décalage de la colonne)
            for x in range(L):                              # Itération pour chaque pixel de la ligne
                pixel = horizontal1.getpixel((x,y))    #Récupération du pixel de coordonées x,y
                r = pixel[0]        #Récupération de la composante rouge du pixel (RVB) dans la variable r
                v = pixel[1]        #Récupération de la composante verte du pixel (RVB) dans la variable v
                b = pixel[2]        #Récupération de la composante bleue du pixel (RVB) dans la variable b
                horizontal2.putpixel(((x + int(force * L) + N), y),(r,v,b))   #Placement du pixel sur la nouvelle image en tenant compte des marges latérales et du décalage (N)

        horizontal2 = horizontal2.crop((int(L * 0.2), 0, int(L * 1.2) - int(L * 0.2), H ))      #"Rognage" des marges latérales de l'image
        horizontal31 = horizontal2.resize((600,500))
        horizontal31 = ImageTk.PhotoImage(horizontal31)
        # Création du label pour afficher le preset 3
        label_horizontal = Label(fen, image=horizontal31, border=0)
        label_horizontal.place(x=150, y=60)  # Placement du label dans la fenêtre
        label_horizontal.image = horizontal31  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python

    if variable ==1:
        if preset1_image is not None and chemin == 1 :
            vertical1 = preset1_image
        if preset2_image is not None and chemin == 2 :
            vertical1 = preset2_image
        if preset3_image is not None and chemin == 3 :
            vertical1 = preset3_image
        if imageimporter is not None and chemin == 4 :
            vertical1 = imageimporter
        L, H = vertical1.size                      # Récupération de la longueur et de la hauteur de l'image d'origine dans les variables L et H
        global vertical2
        vertical2 = Image.new("RGB",(L,int(H * 1.2)))   # Création d'une nouvelle image vierge 1,2 fois plus haute et de même largeur que l'image d'origine

        for x in range(L):                                  # Itération pour chaque colonne
            N = random.randint(int(-0.1 * H), int(0.1 * H)) # Création d'un nombre aléatoire dans la variable N (correspond au décalage de la colonne)
            for y in range(H):                              # Itération pour chaque pixel de la colonne
                pixel = vertical1.getpixel((x,y))    #Récupération du pixel de coordonées x,y
                r = pixel[0]        #Récupération de la composante rouge du pixel (RVB) dans la variable r
                v = pixel[1]        #Récupération de la composante verte du pixel (RVB) dans la variable v
                b = pixel[2]        #Récupération de la composante bleue du pixel (RVB) dans la variable b
                vertical2.putpixel((x,(y + int(0.1 * H) + N)),(r,v,b))   #Placement du pixel sur la nouvelle image en tenant compte des marges hautes et basses et du décalage (N)

        vertical2 = vertical2.crop((0, int(H * 0.2), L, int(H * 1.2) - int(H * 0.2)))
        vertical31 = vertical2.resize((600,500))
        vertical31 = ImageTk.PhotoImage(vertical31)
        # Création du label pour afficher le preset 3
        label_horizontal = Label(fen, image=vertical31, border=0)
        label_horizontal.place(x=150, y=60)  # Placement du label dans la fenêtre
        label_horizontal.image = vertical31  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python

    if variable ==3:
        if preset1_image is not None and chemin == 1 :
            verthoriz1 = preset1_image
        if preset2_image is not None and chemin == 2 :
            verthoriz1 = preset2_image
        if preset3_image is not None and chemin == 3 :
            verthoriz1 = preset3_image
        if imageimporter is not None and chemin == 4 :
            verthoriz1 = imageimporter
        L, H = verthoriz1.size                      # Récupération de la longueur et de la hauteur de l'image d'origine dans les variables L et H
        verthoriz2 = Image.new("RGB",(L,int(H * 1.2)))   # Création d'une nouvelle image vierge 1,2 fois plus haute et de même largeur que l'image d'origine

        for x in range(L):                                  # Itération pour chaque colonne
            N = random.randint(int(-0.1 * H), int(0.1 * H)) # Création d'un nombre aléatoire dans la variable N (correspond au décalage de la colonne)
            for y in range(H):                              # Itération pour chaque pixel de la colonne
                pixel = verthoriz1.getpixel((x,y))    #Récupération du pixel de coordonées x,y
                r = pixel[0]        #Récupération de la composante rouge du pixel (RVB) dans la variable r
                v = pixel[1]        #Récupération de la composante verte du pixel (RVB) dans la variable v
                b = pixel[2]        #Récupération de la composante bleue du pixel (RVB) dans la variable b
                verthoriz2.putpixel((x,(y + int(0.1 * H) + N)),(r,v,b))   #Placement du pixel sur la nouvelle image en tenant compte des marges hautes et basses et du décalage (N)

        verthoriz2 = verthoriz2.crop((0, int(H * 0.2), L, int(H * 1.2) - int(H * 0.2)))      #"Rognage" des marges hautes et basses de l'image

        L, H = verthoriz2.size                      # Récupération de la longueur et de la hauteur de l'image2 qui vient d'être créée dans les variables L et H
        global verthoriz3
        verthoriz3 = Image.new("RGB",(int(L * 1.2),H))   # Création d'une nouvelle troisième image vierge 1,2 fois plus large et de même hauteur que l'image d'origine

        for y in range(H):                                  # Itération pour chaque ligne
            N = random.randint(int(-0.1 * L), int(0.1 * L)) # Création d'un nombre aléatoire dans la variable N (correspond au décalage de la ligne)
            for x in range(L):                              # Itération pour chaque pixel de la ligne
                pixel = verthoriz2.getpixel((x,y))    #Récupération du pixel de coordonées x,y
                r = pixel[0]        #Récupération de la composante rouge du pixel (RVB) dans la variable r
                v = pixel[1]        #Récupération de la composante verte du pixel (RVB) dans la variable v
                b = pixel[2]        #Récupération de la composante bleue du pixel (RVB) dans la variable b
                verthoriz3.putpixel(((x + int(0.1 * L) + N), y),(r,v,b))   #Placement du pixel sur la nouvelle image en tenant compte des marges droites et gauches et du décalage (N)

        verthoriz3 = verthoriz3.crop((int(L * 0.2), 0, int(L * 1.2) - int(L * 0.2), H ))      #"Rognage" des marges droites et gauches de l'image
        verthoriz41 = verthoriz3.resize((600,500))
        verthoriz41 = ImageTk.PhotoImage(verthoriz41)
        # Création du label pour afficher le preset 3
        label_verthoriz = Label(fen, image=verthoriz41, border=0)
        label_verthoriz.place(x=150, y=60)  # Placement du label dans la fenêtre
        label_verthoriz.image = verthoriz41  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python

# Fonction pour la logique d'upload
def sauvegarderimage():
    # Vérification si une image est présente
    if horizontal2 is not None and chemin == 1 :
        # Sauvegarde de l'image
        horizontal2.save("ImageHorizontal.png")
    if horizontal2 is not None and chemin == 2 :
        horizontal2.save("ImageHorizontal.png")
    if horizontal2 is not None and chemin == 3 :
        horizontal2.save("ImageHorizontal.png")
    if horizontal2 is not None and chemin == 4 :
        horizontal2.save("ImageHorizontal.png")

    if vertical2 is not None and chemin == 1 :
        # Sauvegarde de l'image
        vertical2.save("ImageVertical.png")
    if vertical2 is not None and chemin == 2 :
        vertical2.save("ImageVertical.png")
    if vertical2 is not None and chemin == 3 :
        vertical2.save("ImageVertical.png")
    if vertical2 is not None and chemin == 4 :
        vertical2.save("ImageVertical.png")

    if verthoriz3 is not None and chemin == 1 :
        # Sauvegarde de l'image
        verthoriz3.save("ImageVertHoriz.png")
    if verthoriz3 is not None and chemin == 2 :
        verthoriz3.save("ImageVertHoriz.png")
    if verthoriz3 is not None and chemin == 3 :
        verthoriz3.save("ImageVertHoriz.png")
    if verthoriz3 is not None and chemin == 4 :
        verthoriz3.save("ImageVertHoriz.png")


# Effets au survol pour Boutton

def on_enter(event):
    event.widget.config(background=bouttonsurvol)  # Changement de couleur au survol

def on_leave(event):
    event.widget.config(background=boutton)  # Retour à la couleur d'origine

# Boutton (Importer)

btnimport = tk.Button(fen, text="Importer", background=boutton, foreground=fond,font=fontperso, border=0, command= lambda:[importerchemin(),importerimage()])
btnimport.place(x=150, y=600)

btnimport.bind("<Enter>", on_enter)
btnimport.bind("<Leave>", on_leave)

# Boutton (Sauvegarder)

btnsave = tk.Button(fen, text="Sauvegarder", background=boutton, foreground=fond,font=fontperso, border=0, command=sauvegarderimage)
btnsave.place(x=960, y=600)

btnsave.bind("<Enter>", on_enter)
btnsave.bind("<Leave>", on_leave)

# Boutton (Appliquer)

btneffet = tk.Button(fen, text="Appliquer", background=boutton, foreground=fond,font=fontperso, border=0, command=effetsimage)
btneffet.place(x=870, y=450)

btneffet.bind("<Enter>", on_enter)
btneffet.bind("<Leave>", on_leave)

# Boutton effet

btnhorizontal = tk.Button(fen, text="\u2191", background=boutton, foreground=fond,font=fontperso, border=0, command=bouton_vertical_click)
btnhorizontal.place(x=850, y=150)
btnhorizontal.bind("<Enter>", on_enter)
btnhorizontal.bind("<Leave>", on_leave)

btnvertical = tk.Button(fen, text="\u2191 \u2192", background=boutton, foreground=fond,font=fontperso, border=0, command=bouton_verthoriz_click)
btnvertical.place(x=900, y=150)
btnvertical.bind("<Enter>", on_enter)
btnvertical.bind("<Leave>", on_leave)

btnverthoriz = tk.Button(fen, text="\u2192", background=boutton, foreground=fond,font=fontperso, border=0, command=bouton_horizontal_click)
btnverthoriz.place(x=985, y=150)
btnverthoriz.bind("<Enter>", on_enter)
btnverthoriz.bind("<Leave>", on_leave)

# Boutton Preset

btnpreset1 = tk.Button(fen, text="1", background=boutton, foreground=fond,font=fontperso, border=0, command= lambda:[preset1chemin(),importerimage()])
btnpreset1.place(x=50, y=200)
btnpreset1.bind("<Enter>", on_enter)
btnpreset1.bind("<Leave>", on_leave)

btnpreset2 = tk.Button(fen, text="2", background=boutton, foreground=fond,font=fontperso, border=0, command= lambda:[preset2chemin(),importerimage()])
btnpreset2.place(x=50, y=300)
btnpreset2.bind("<Enter>", on_enter)
btnpreset2.bind("<Leave>", on_leave)

btnpreset3 = tk.Button(fen, text="3", background=boutton, foreground=fond,font=fontperso, border=0, command= lambda:[preset3chemin(),importerimage()])
btnpreset3.place(x=50, y=400)
btnpreset3.bind("<Enter>", on_enter)
btnpreset3.bind("<Leave>", on_leave)

fen.mainloop()
