import tkinter as tk
from tkinter import filedialog, Label, LabelFrame, PhotoImage
from PIL import Image, ImageTk

# Fonction pour la logique d'upload
def upload_file():
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]
    filename = tk.filedialog.askopenfilenames(multiple=False,filetypes=f_types)
    for f in filename:
        img=Image.open(f)
        img=img.resize((100,100))
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(fen)
        e1.grid(row=3, column=10)
        e1.image = img
        e1['image']=img

# Definition des parametres de la fenetre
fen = tk.Tk()
fen.geometry("1200x700")
fen.title('ImageDripper')

fond = '#000814'
boutton = '#003566'
bouttonactif = '#01447a'
texte = 'WHITE'


fen.configure(bg=fond, padx=10, pady=10)

fontperso=('Roboto', 10, 'bold')

# Button (Upload)

def on_enter(e):
    bimport.config(image=rimport_hover)

def on_leave(e):
    bimport.config(image=rimport)

rimport = tk.PhotoImage(file='button_importer.png')
rimport_hover = tk.PhotoImage(file='importer2.png')

bimport = tk.Button(fen,image=rimport,border=0,relief=tk.SUNKEN,command=upload_file)
bimport.bind("<Enter>", on_enter)
bimport.bind("<Leave>", on_leave)
bimport.place(x=60, y=60)

fen.mainloop()