import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

fen = tk.Tk()
fen.geometry("410x300")  # Size of the window
fen.title('ImageDripper')
my_font1=('times', 18, 'bold')
l1 = tk.Label(fen,text='Upload Files & display',width=30,font=my_font1)
l1.grid(row=1,column=1,columnspan=4)
b1 = tk.Button(fen, text='Upload Files',
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1,columnspan=4)

def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    col=1 # start from column 1
    row=3 # start from row 3
    for f in filename:
        img=Image.open(f) # read the image file
        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(my_w)
        e1.grid(row=row,column=col)
        e1.image = img # keep a reference! by attaching it to a widget attribute
        e1['image']=img # Show Image
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row
            col=col+1 # increase to next column

fen.mainloop()  # Keep the window open