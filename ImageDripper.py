import tkinter as tk
from tkinter import filedialog, Label, LabelFrame
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
        e1.grid(row=10, column=10)
        e1.image = img
        e1['image']=img

# Definition des parametres de la fenetre
fen = tk.Tk()
fen.geometry("1200x700")
fen.title('ImageDripper')
fen.configure(bg="#333333", padx=10, pady=10)

my_font1=('times', 18, 'bold')

# Label (Titre Upload)
l1 = tk.Label(fen, text='Upload Files & display', width=30, font=my_font1)
l1.grid(row=10, column=1)

# Button (Upload)
b1 = tk.Button(fen, text='Upload Files', width=20, command=upload_file)
b1.grid(row=2, column=0)

fen.mainloop()
