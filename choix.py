from tkinter import *
import tkinter as tk
import tkinter.ttk


win_game= Tk()
win_game.title("Qui est-ce ?2")
win_game.geometry("750x550")
win_game.minsize(700,500)

win_game.config(background='grey')

frame=Frame(win_game,bg="pink")

label_title = Label(frame,font=("Courrier",12), bg="pink",text="Choisissez votre question !")
label_title.pack(pady=20)

def action(event) : 
  select = cb.get()
  if select == "Genre" :
    cb1.pack(pady=25)
    cb2.pack_forget()
    cb3.pack_forget()
  elif select == "cheveux" :
    cb3.pack(pady=25)
    cb1.pack_forget()
    cb2.pack_forget()
  elif select == "lunettes" or "chauve" :
    cb2.pack(pady=25)
    cb1.pack_forget()
    cb3.pack_forget()


def combobox_choix():
  cb = tkinter.ttk.Combobox(frame,state="readonly")
  cb['values'] = ["Genre","cheveux","lunettes","chauve"]
  cb.set("choix")
  cb.bind("<<ComboboxSelected>>", action)
  cb.pack(pady=25)

  cb1 = tkinter.ttk.Combobox(frame,state="readonly")
  cb1['values']=["Femme","Homme"]
  cb1.set("Femme ou Homme")

  cb2 = tkinter.ttk.Combobox(frame,state="readonly")
  cb2['values']=["oui","non"]
  cb2.set("Oui ou Non")

  cb3 = tkinter.ttk.Combobox(frame,state="readonly")
  cb3['values']=["Blond","Blanc","Brun","Chatain","Roux"]
  cb3.set("couleur de cheveux ?")


frame.pack(side=RIGHT, padx=10)

win_game.mainloop()