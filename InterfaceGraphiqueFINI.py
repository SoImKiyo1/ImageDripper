import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

# Fonction pour la logique d'upload
def importerimage():
    # Spécification des types de fichiers autorisés dans la boîte de dialogue
    extensionsimage = [("JPG", "*.jpg"),("PNG","*.png"),("Tous","*")]
    # Ouverture de la boîte de dialogue pour sélectionner un fichier
    nomimage = filedialog.askopenfilename(filetypes=extensionsimage)
    if nomimage:
        imageimporter = Image.open(nomimage)
        # Redimensionnement de l'image
        imageimporter = imageimporter.resize((600,500))
        # Conversion de l'image en format utilisable par tkinter
        imageimporter = ImageTk.PhotoImage(imageimporter)
        # Affichage de l'image dans un Label
        label_imageimporter = tk.Label(fen, image=imageimporter, border=0)
        label_imageimporter.place(x=150, y=60)
        label_imageimporter.image = imageimporter  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python (elle n'est pas réutilisée ailleurs)

def preset1():
    # Chargement du preset 1
    preset1_image = Image.open("preset1.png")
    preset1_image = preset1_image.resize((600,500))
    preset1_image = ImageTk.PhotoImage(preset1_image)
    # Création du label pour afficher le preset 1
    label_preset1 = Label(fen, image=preset1_image, border=0)
    label_preset1.place(x=150, y=60)  # Placement du label dans la fenêtre
    label_preset1.image = preset1_image  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python

def preset2():
    # Chargement du preset 2
    preset2_image = Image.open("preset2.png")
    preset2_image = preset2_image.resize((600,500))
    preset2_image = ImageTk.PhotoImage(preset2_image)
    # Création du label pour afficher le preset 2
    label_preset2 = Label(fen, image=preset2_image, border=0)
    label_preset2.place(x=150, y=60)  # Placement du label dans la fenêtre
    label_preset2.image = preset2_image  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python

def preset3():
    # Chargement du preset 3
    preset3_image = Image.open("preset3.png")
    preset3_image = preset3_image.resize((600,500))
    preset3_image = ImageTk.PhotoImage(preset3_image)
    # Création du label pour afficher le preset 3
    label_preset3 = Label(fen, image=preset3_image, border=0)
    label_preset3.place(x=150, y=60)  # Placement du label dans la fenêtre
    label_preset3.image = preset3_image  # Garde une référence de l'image pour éviter qu'elle ne soit supprimée par python


# Fonction pour la logique d'upload
def sauvegarderimage():
    # Vérification si une image est présente
    if "imagemodifier" in globals():
        # Sauvegarde de l'image
        imagemodifier.save("maNouvelleImage.png")
    else:
        print("Aucune image à sauvegarder.")

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

fen.configure(bg=fond, padx=10, pady=10)

#Canvas pour le fond de l'image

imageback = Canvas(fen, width=1000, height=500, bg=boutton, highlightthickness=0)
imageback.pack()
imageback.place(x=150, y=60)

#Canvas pour le fond des bouttons

buttonback = Canvas(fen, width=400, height=500, bg=fond2, highlightthickness=0)
buttonback.pack()
buttonback.place(x=750, y=60)

# Effets au survol pour Boutton

def on_enter(event):
    event.widget.config(background=bouttonsurvol)  # Changement de couleur au survol

def on_leave(event):
    event.widget.config(background=boutton)  # Retour à la couleur d'origine

# Boutton (Importer)

btnimport = tk.Button(fen, text="Importer", background=boutton, foreground=fond,font=fontperso, border=0, command=importerimage)
btnimport.place(x=150, y=600)

btnimport.bind("<Enter>", on_enter)
btnimport.bind("<Leave>", on_leave)

# Boutton (Sauvegarder)

btnsave = tk.Button(fen, text="Sauvegarder", background=boutton, foreground=fond,font=fontperso, border=0, command=sauvegarderimage)
btnsave.place(x=960, y=600)

btnsave.bind("<Enter>", on_enter)
btnsave.bind("<Leave>", on_leave)

# Boutton (Appliquer)

btneffet = tk.Button(fen, text="Appliquer", background=boutton, foreground=fond,font=fontperso, border=0)#, command=modifierimage)
btneffet.place(x=870, y=450)

btneffet.bind("<Enter>", on_enter)
btneffet.bind("<Leave>", on_leave)

# Boutton effet

btnpreset1 = tk.Button(fen, text="\u2191", background=boutton, foreground=fond,font=fontperso, border=0)
btnpreset1.place(x=850, y=150)
btnpreset1.bind("<Enter>", on_enter)
btnpreset1.bind("<Leave>", on_leave)

btnpreset2 = tk.Button(fen, text="\u2191 \u2192", background=boutton, foreground=fond,font=fontperso, border=0)
btnpreset2.place(x=900, y=150)
btnpreset2.bind("<Enter>", on_enter)
btnpreset2.bind("<Leave>", on_leave)

btnpreset3 = tk.Button(fen, text="\u2192", background=boutton, foreground=fond,font=fontperso, border=0)
btnpreset3.place(x=985, y=150)
btnpreset3.bind("<Enter>", on_enter)
btnpreset3.bind("<Leave>", on_leave)

# Slider Force
texte_force = tk.Label(fen, text="Force:",background=fond2, foreground=fond, font=fontperso, border=0)
texte_force.place(x=840, y=280)

style = ttk.Style()
style.configure('Custom.Horizontal.TScale', background=fond2, foreground=fond, troughcolor=fond)

scale = ttk.Scale(fen, from_=0, to=100, orient='horizontal', length=200, style='Custom.Horizontal.TScale')
scale.place(x=840, y=330)

# Boutton Preset

btnpreset1 = tk.Button(fen, text="1", background=boutton, foreground=fond,font=fontperso, border=0, command=preset1)
btnpreset1.place(x=50, y=200)
btnpreset1.bind("<Enter>", on_enter)
btnpreset1.bind("<Leave>", on_leave)

btnpreset2 = tk.Button(fen, text="2", background=boutton, foreground=fond,font=fontperso, border=0, command=preset2)
btnpreset2.place(x=50, y=300)
btnpreset2.bind("<Enter>", on_enter)
btnpreset2.bind("<Leave>", on_leave)

btnpreset3 = tk.Button(fen, text="3", background=boutton, foreground=fond,font=fontperso, border=0, command=preset3)
btnpreset3.place(x=50, y=400)
btnpreset3.bind("<Enter>", on_enter)
btnpreset3.bind("<Leave>", on_leave)

fen.mainloop()
