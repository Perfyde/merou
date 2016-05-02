from tkFileDialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *


def callback(event):
    if askyesno("", "Confirmer ?"):
        X = event.x
        Y = event.y
        print(X, Y)
fenetre = Tk()
label = Label(fenetre, text="Cliquez sur un pixel pour selectionner la couleur")
label.pack()  # explication
showinfo("Info", "N'oubliez pas de mettre l'image en .GIF...")  # affiche une info
filepath = askopenfilename(title="Ouvrir une image", filetypes=[('GIF files', '.GIF')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="white")
canvas.create_image(0, 0, anchor=NW, image=photo)  # ouvre une image
canvas.bind('<Button-1>', callback)  # active la pipette
canvas.pack()
fenetre.mainloop()
