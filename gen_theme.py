from ast import Global
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
from json import JSONEncoder

class perso :
    def __init__(self,name:str,image:str,dict:dict):
        self.name=name
        self.image=image
        self.dict=dict

class input:
        Vector= list[perso]
        def __init__(self,x:str,y:str,persos: Vector):
            self.x=x
            self.y=y
            self.persos=persos
class inputEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__            


def export() :
    global col
    global lign
    newInput= input(col.get(),lign.get(),listPerso)
    myFile = open("newInput.json", "w+")
    myFile.write(inputEncoder().encode(newInput))
    myFile.close()

listPerso=[]
global i
global col
global lign
win = Tk()
win.title("Qui est-ce ?")
win.geometry("750x550")
win.minsize(700, 500)
listAttribut=["cheuveux", "couleur", "yeux"]
win.config(background='grey')

global input_variable

global liste_attribut



def addAttribut ():
    print(input_variable)
    listAttribut.append(input_variable.get())
def updtcblist():
    liste_attribut['values'] = listAttribut

def addPerso():
    print(input_variable[0].get())
    global i
    dict = {}
    for _ in range(len(listAttribut)):
        dict[listAttribut[_]]=input_variable[_+1].get()
    newPerso = perso(input_variable[0],i,dict)
    listPerso.append(newPerso)


label_title = Label(win, text="Generateur de Theme", font=("Courrier", 40), bg='grey')
label_title.pack()
col = StringVar()

nbcolonnes = Label(win, text="Nombres de colonnes", font=("Courrier", 20), bg='grey')
nbcolonnes.place(x=20, y=150)
entrycolonnes = Entry(win,textvariable=col)
entrycolonnes.place(x=300, y=150)
lign = StringVar()
nblignes = Label(win, text="Nombres de lignes", font=("Courrier", 20), bg='grey')
nblignes.place(x=20, y=200)
entrylignes = Entry(win,textvariable=lign)
entrylignes.place(x=300, y=200)

def creer_attribut():
    win2=Toplevel()
    win2.title("new attribut")
    win2.geometry("550x200")
    win2.config(background='grey')

    new_attribut = Label(win2, text="Nouvelle Attribut : ", font=("Courrier", 20), bg='grey')
    new_attribut.place(x=10, y=30)
    global input_variable
    input_variable = StringVar(win)
    entryattribut = Entry(win2,textvariable=input_variable)
    entryattribut.place(x=200, y=30)
    ajoute = Button(win2, text="+",command=addAttribut)
    ajoute.place(x= 430, y=30)
    exist_attribut = Label(win2, text="Attribut deja existants", font=("Courrier", 20), bg='grey')

    exist_attribut.place(x=10, y=80)
    global liste_attribut

    def val(event):
        select=liste_attribut.get()
        print("attribut selectionne est ", select)
    liste_attribut = ttk.Combobox(win2, postcommand = updtcblist)
    liste_attribut.place(x=275 ,y=80)
    liste_attribut.current(0)
    liste_attribut.bind("<<ComboboxSelected>>", val)


def info_perso():
    win3=Tk()
    win3.title("new attribut")
    win3.geometry("550x375")
    win3.config(background='grey')
    global input_variable
    input_variable = [] 
    input_variable.append(StringVar(win3))
    nom_perso = Label(win3, text="Nom : ", font=("Courrier", 20), bg='grey')
    nom_perso.place(x=10, y=50)
    entryattribut = Entry(win3,textvariable=input_variable[0])
    entryattribut.place(x=200, y=50)

    def openImg():
        global i
        i = filedialog.askopenfilename()
        print(i)
    image = Label(win3, text="Upload image", font=("Courrier", 20), bg='grey')
    image.place(x=10, y=150)
    img = Button(win3, text="upload", command=openImg)
    img.place(x=250, y=150)

    attribut = Label(win3, text="Attribut", font=("Courrier", 20), bg='grey')
    attribut.place(x=10, y=250)

    

    for _ in range(len(listAttribut)):
            input_variable.append(StringVar(win3))
            new_attribut = Label(win3, text= listAttribut[_], font=("Courrier", 20), bg='grey')
            new_attribut.place(x=10, y=250+_*50)
            entryattribut = Entry(win3,textvariable=input_variable[_+1])
            entryattribut.place(x=200, y=250+_*50)
    ajoutePerso = Button(win3, text="Confirmer",command=addPerso)
    ajoutePerso.place (x=140,y=250+(len(listAttribut)+1)*50)

    


valider = Button(win, text="Creer attribut", command=creer_attribut)
valider.place(x=75, y=250)

valider1 = Button(win, text="Ajouter Perso", command=info_perso)
valider1.place(x=75, y=300)

valider2 = Button(win, text="Modifier Perso")
valider2.place(x=300, y=300)

valider3 = Button(win, text="Generer le Theme",command=export)
valider3.place(x=300, y=350)

win.mainloop()
