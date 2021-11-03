from os import name
import qrcode
from qrcode.constants import ERROR_CORRECT_L

from tkinter import *

from tkinter import ttk
from tkinter import filedialog, messagebox
#from tqdm import tqdm

window = Tk()

window.geometry('630x400')

window.resizable(0,0)

window.title('Djimbalinux App')

Label(window, text="Générateur de QRcode", font=("arial", 20, "bold")).pack()

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

folderPath = StringVar()

Label(window ,text="Chemin d'enregistrement de l'image générée").place(x=150, y=180)
folderPath_entered = Entry(window,textvariable=folderPath, width=70).place(x=15, y=210)
ttk.Button(window, text="choisir le dossier", command=getFolderPath).place(x=240, y=240)


link = StringVar()
nameCode = StringVar()

Label(window, text="mettez un lien ou un numéro ⬇️ ou tout autre text que vous voulez coder", font='arial 13 bold').place(x=5, y=60)

link_entered = Entry(window, width=70, textvariable=link).place(x=15, y=90)

Label(window, text="Donner un nom à votre image ⬇️ ", font='arial 13 bold').place(x=170, y=120)

nameCode_entered = Entry(window, width=70, textvariable=nameCode).place(x=15, y=150)


def ExitApp():
    window.destroy()



def getQrcode():

    try:
        qrGenerate = qrcode.QRCode(
        version=3,
        error_correction=ERROR_CORRECT_L,
        box_size=3,
        border=5
        )

        qrGenerate.add_data(str(link.get()))
        qrGenerate.make(fit=True)

        name = nameCode.get()
        chemin = folderPath.get()

        img = qrGenerate.make_image(fill_color="red", back_color="white")
        img.save(f"{chemin}/{name}.png")
        #img.save(folderPath.get())

        # Displaying the message
        messagebox.showinfo("Image générée avec succès !", "Sauvegardée dans\n" + folderPath.get())
   
    except Exception as e:
        messagebox.showinfo("échec !", "verifié votre les informations ou le chemin du dossier")

Button(window, text="Générer le code", font='arial 15 bold', bg='green', fg='white', padx=5, command=getQrcode).place(x=30, y=300)

Button(window, text="Quiter", font='arial 15 bold', bg='red', fg='white', padx=5, command=ExitApp).place(x=395, y=300)

window.mainloop()









