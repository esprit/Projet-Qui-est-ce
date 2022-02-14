from tkinter import *
import tkinter as tk
import tkinter.ttk
from recup import *

win_game = Tk()
win_game.title("Qui est-ce ?")
win_game.geometry("300x550")
win_game.minsize(700, 500)

win_game.config(background='grey')

frame = Frame(win_game,relief=RAISED, bg="pink", bd=4,)
frame.place(x=400, y=300)


label_title = Label(frame,
                    font=("Courrier", 12),
                    bg="pink",
                    text="  Choisissez votre question !  ")
label_title.pack(pady=20)


def action2(event):
  liste=tri_keys(cb.get())
  cb1["values"]=liste
  cb1.set(":)")


def action3(event):

  
  liste=tri_keys(cbPlusChoix.get())
  
  cbPlusValeurs["values"]=liste
  cbPlusValeurs.set(":)")
 




def OuvreChoix():

  global cbPlusChoix
  cbPlusChoix=tkinter.ttk.Combobox(frame, state="readonly",values=l)
  global cbPlusValeurs
  cbPlusValeurs=tkinter.ttk.Combobox(frame, state="readonly")
  cbPlusChoix.set("choix")
  cbPlusChoix.pack(pady=15)
  cbPlusValeurs.pack(pady=10)
  cbPlusChoix.bind("<<ComboboxSelected>>",action3)

l=recup_keys()
del l[0:2]
cb = tkinter.ttk.Combobox(frame, state="readonly",values=l)
cb1 = tkinter.ttk.Combobox(frame,state="readonly")





cb.set("choix")
cb.bind("<<ComboboxSelected>>", action2)
cb.pack(pady=15)
cb1.pack(pady=15)



def ET():
  OuvreChoix()
  et = Button(frame,text="ET",command=ET)
  et.pack(pady=10,padx=30)

def OU():
  OuvreChoix()
  ou = Button(frame,text="OU",command=OU)
  ou.pack(pady=10,padx=30)

et = Button(frame,text="ET",command=ET)
et.pack(pady=10,padx=30)

ou = Button(frame,text="OU",command=OU)
ou.pack(pady=10,padx=30)

frame.pack(side=TOP, padx=10)

win_game.mainloop()
