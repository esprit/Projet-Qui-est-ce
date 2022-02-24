from tkinter import *
import tkinter as tk
import tkinter.ttk
from recup import *

win_game = Tk()
win_game.title("Qui est-ce ?")
win_game.geometry("1050x750")
win_game.minsize(1050, 700)
win_game.config(background='grey')


frameMain = Frame(win_game,relief=RAISED, bg="DarkTurquoise", bd=4,)
frameConnect = Frame(frameMain,bg="DarkTurquoise")
frameChoix1 = Frame(win_game)
frameChoixPlus = Frame(win_game)

label_title = Label(frameMain,
                    font=("Courrier", 12),
                    bg="DarkTurquoise",
                    text="  Choisissez votre ou vos question(s) !  ")
label_title.grid(columnspan=2,pady=10,padx=50)

def affichage():
  liste=tri_keys("fichier")
  i=0
  while i<=23:
    perso=PhotoImage(file="personnages/"+liste[i])
    lab=Label(win_game,image=perso)
    lab.grid(row=i//6,column=i%6)
    i=i+1
    

def action2(event):
  liste=tri_keys(cb.get())
  cb1["values"]=liste
  cb1.set(":)")
  


def action3(event):
  liste=tri_keys(cbPlusChoix.get())
  cbPlusValeurs["values"]=liste
  cbPlusValeurs.set(":):)")
 

def OuvreChoix():
  global cbPlusChoix,line
  cbPlusChoix=tkinter.ttk.Combobox(frameMain, state="readonly",values=l)
  global cbPlusValeurs
  cbPlusValeurs=tkinter.ttk.Combobox(frameMain, state="readonly")
  cbPlusChoix.set("choix")
  cbPlusChoix.grid(row=line,pady=5)
  cbPlusValeurs.grid(row=line,column=1,pady=5)
  line+=1
  cbPlusChoix.bind("<<ComboboxSelected>>",action3)
  
affichage()
line=4 
l=recup_keys()
del l[0:2]
cb = tkinter.ttk.Combobox(frameMain, state="readonly",values=l)
cb1 = tkinter.ttk.Combobox(frameMain,state="readonly")
cb.set("choix")
cb.bind("<<ComboboxSelected>>", action2)
cb.grid(row=1,column=0,pady=15,padx=5)
cb1.grid(row=1,column=1,pady=15,padx=5)


def ET():
  OuvreChoix()
  et = Button(frameConnect,text="ET",command=ET)
  ou['state']=DISABLED
  

def OU():
  OuvreChoix()
  ou = Button(frameconnect,text="OU",command=OU)
  et['state']=DISABLED

  
frameMain.grid(row=1,column=7,padx=10)
#frameChoix1.pack(padx=10)
frameConnect.grid(row=2,columnspan=2,padx=0)
frameChoixPlus.grid(row=3,column=7,padx=10,pady=0)


et = Button(frameConnect,text="ET",command=ET)
et.grid(row=2,column=1,pady=15,padx=20)

ou = Button(frameConnect,text="OU",command=OU)
ou.grid(row=2,column=2,pady=15,padx=20)

valider = Button(frameConnect,text="valider")
valider.grid(row=2,column=0,pady=15,padx=20)

quitter = Button(frameConnect,text="quitter",command=frameConnect.destroy)
quitter.grid(row=2,column=3,padx=20)



win_game.mainloop()
