from tkinter import *
import tkinter as tk
import tkinter.ttk
from recup import *
import time

#Saisie le choix de la première question + la grise
def getchoix(event):
    global test, choixliste
    choixliste.append(str(cb1.get()))
    cb1['state']=DISABLED
    test = TRUE

#Pareil pour la valeur du choix de la question
def getvaleur(event):
    global test, choixliste,cb1
    choixliste.append(cbPlusValeurs.get())
    cbPlusValeurs['state']=DISABLED
    test = TRUE

  
#choix du premier critère
def action2(event):  
    global choixliste,frameperdu,perd
    if perd==1:
      frameperdu.destroy()
      perd=0
    cb['state']=DISABLED
    choix = cb.get()
    liste = tri_keys(choix)
    choixliste.append(choix)
    cb1["values"] = liste
    cb1.set(":)")
    cb1.bind("<<ComboboxSelected>>", getchoix)

  
#choix de l valeur du critère
def action3(event):  
    global choixliste
    choix = cbPlusChoix.get()
    liste = tri_keys(choix)
    cbPlusChoix['state']=DISABLED
    choixliste.append(choix)
    cbPlusValeurs["values"] = liste
    cbPlusValeurs.set(":):)")
    cbPlusValeurs.bind("<<ComboboxSelected>>", getvaleur)

#ouvre les choix des prochains critères
def OuvreChoix():  
    global cbPlusChoix, line, choixliste, cbPlusValeurs,frameMain
    cbPlusChoix = tkinter.ttk.Combobox(frameMain, state="readonly", values=l)
    cbPlusValeurs = tkinter.ttk.Combobox(frameMain, state="readonly")
    cbPlusChoix.set("choix")
    cbPlusChoix.grid(row=line,column=0,columnspan=2, pady=10)
    cbPlusValeurs.grid(row=line, column=2,columnspan=2, pady=10)
    line += 1
    cbPlusChoix.bind("<<ComboboxSelected>>", action3)


#vérification des valeurs saisies par rapport aux valeurs à trouver
def verif():
    global connecteur, dicoperso, choixliste
    
    liste=choixliste
    if connecteur == "":
        if liste != [] and dicoperso[liste[0]] ==liste[1]:
            return ("TRUE")
        else:
            return ("FALSE")
    elif connecteur == "ET":
        while liste != []:
            if dicoperso[liste[0]] == liste[1]:
                del liste[0:2]
            else:
                return ("FALSE")
        return ("TRUE")
    elif connecteur == "OU":
        while liste != []:
            if dicoperso[liste[0]] != liste[1]:
                del liste[0:2]
            else:
                return ("TRUE")
        return ("FALSE")

      
#vérification après selection du prenom
def OK(event):
  global frameperdu,perd
  perso = cbprenom.get()
  if dicoperso["nom"]==perso:
    frameMain.destroy()
    framereponse.destroy()
    framebravo=Frame(win_game,bg="pink",relief=RAISED,bd=3)
    labelbravo=Label(framebravo,
                          font=("Courrier", 26),
                          bg="pink",
                          text=" BRAVO c'est bien  " + perso)
    framebravo.pack(side=TOP)
    labelbravo.grid(columnspan=2,ipadx=20,ipady=20)

    recommencer=Button(framebravo,text="Recommencer",command=partie)
    recommencer.grid(row=2,pady=5)

    quitter=Button(framebravo,text="Quitter",command=win_game.destroy)
    quitter.grid(row=2,column=1,pady=5)
    
  else:
    NON()
    perd=1
    frameperdu=Frame(win_game,bg="pink",relief=RAISED,bd=3)
    frameperdu.grid(row=1,column=2)
    perdu=Label(frameperdu,text="Perdu, essaye encore !",bg="pink",font=("Courrier", 15))
    perdu.grid(padx=20,pady=20)
    
    


    
def NON(): 
  frameMain.destroy()
  framereponse.destroy()
  question()


def OUI():
  global cbprenom
  oui.destroy()
  non.destroy()
  liste=tri_keys("nom")
  cbprenom = tkinter.ttk.Combobox(framesuite, state="readonly", values=liste)
  cbprenom.grid(row=2,columnspan=4, pady=10, padx=5)
  cbprenom.bind("<<ComboboxSelected>>", OK)


  
  #renvoie la liste des personnes qui vérifient les choix
def listepersonne():
  liste=choixliste
  l1=[]
  if liste!=[]:
    l1=creerliste(liste[0],liste[1])
    del liste[0:2]
  l3=[]
  while liste != []:
            l2=creerliste(liste[0],liste[1])
            if connecteur=="ET":
              for i in range (len(l2)-1):
                if l2[i] in l1:
                  l3.append(l2[i])
              l1=l3
            elif connecteur=="OU":
              for i in range (len(l2)-1):
                if l2[i] not in l1:
                  l1.append(l2[i])
            del liste[0:2]
  return(l1)

  
#renvoie le complement des prenoms de liste
def complementliste(liste):
    
    l=tri_keys('nom')
    for i in range (len(liste)):
      if liste[i] in l:
        l.remove(liste[i])
    return(l)
  
  
  
#affichage vrai test sur la deuxieme frame
def vraitest():
  global framesuite,label_reponse,oui,non,label_perso,perd,frameperdu
  t=verif()
  if  test:
    label_reponse = Label(framereponse,
                            font=("Courrier", 12),
                            bg="pink",
                            text=" La réponse est " + t)
    label_reponse.grid(columnspan=5, pady=20, padx=10)  
    framesuite = Frame(framereponse, relief=GROOVE, bg="pink", bd=4)
    framesuite.grid(row=1, column=0, padx=10,pady=10)
    label_perso=Label(framesuite,font=("Courrier", 12),
                            bg="pink",
                            text="M'avez-vous trouvé?")
    label_perso.grid(columnspan=5, pady=10, padx=50)
    oui = Button(framesuite, text="OUI",command=OUI)
    oui.grid(row=2, column=1, pady=0, padx=5)
    
    non = Button(framesuite, text="NON",command=NON)
    non.grid(row=2, column=3, pady=10, padx=5)
    if val.get()==1:
      personne=listepersonne()
      if t=="TRUE":
        personne=complementliste(personne)
      print(personne, "     personne à éliminer")
      
      labeltriche=Label(framereponse,font=("Courrier", 12),
                            bg="pink",
                            text= str(len(personne))+" image(s) à cocher")
      labeltriche.grid(row=3, column=0, pady=10, padx=5)
  else:
    print("fais ton choix :)")


def ET():
    global test, connecteur
    connecteur = "ET"
    if test:
        OuvreChoix()
        et = Button(frameConnect, text="ET", command=ET)
        ou['state'] = DISABLED
        test = FALSE
    else:
        print("fais un choix")


def OU():
    global test, connecteur
    connecteur = "OU"
    if test:
        OuvreChoix()
        ou = Button(frameConnect, text="OU", command=OU)
        et['state'] = DISABLED
        test = FALSE
    else:
        print("fais un choix")


#Deux premieres combobox + les boutons de la premiere frame
def question():    
  global cb,cb1,l,line,test,choixliste,connecteur,frameMain,frameConnect,ou,et,framereponse,val

  frameMain = Frame(win_game, relief=RAISED, bg="DarkTurquoise", bd=4)
  frameConnect = Frame(frameMain, bg="DarkTurquoise")
  
  
  label_title = Label(frameMain,
                      font=("Courrier", 12),
                      bg="DarkTurquoise",
                      text="  Faites vos choix !  ")
  label_title.grid(column=0,columnspan=3, pady=10, padx=5)
  
  test = FALSE
  line = 4
  choixliste = []
  l = recup_keys()
  del l[0:1]
  cb = tkinter.ttk.Combobox(frameMain, state="readonly", values=l)
  cb1 = tkinter.ttk.Combobox(frameMain, state="readonly")
  cb.set("choix")
  cb.bind("<<ComboboxSelected>>", action2)
  cb.grid(row=1, column=0,columnspan=2, pady=15, padx=5)
  cb1.grid(row=1, columnspan=2,column=2, pady=15, padx=5)
  connecteur = ""  #choix du et, ou ,rien
  
  frameMain.grid(row=1, column=1, padx=10)
  frameConnect.grid(row=2, columnspan=2, padx=0)

  
  framereponse = Frame(win_game, relief=RAISED, bg="pink", bd=4)
  framereponse.grid(row=1, column=2, padx=10)
  
  annuler = Button(frameMain, text="annuler", command=NON)
  annuler.grid(row=2, column=0,pady=15, padx=5)  
    
  et = Button(frameMain, text="ET", command=ET)
  et.grid(row=2, column=1, pady=10, padx=5)
  
  ou = Button(frameMain, text="OU", command=OU)
  ou.grid(row=2, column=2, pady=10, padx=5)
  
  valider = Button(frameMain, text="valider", command=vraitest)
  valider.grid(row=2, column=3, pady=10, padx=5)  

  val=IntVar()
    
  triche= Checkbutton(frameMain,text="triche",background="DarkTurquoise",bd=4,relief=GROOVE,variable=val)
  triche.grid(row=0,column=3,columnspan=2, padx=5,ipady=5,ipadx=7)



  
#relance une nouvelle partie
def partie():
  global win_game,dicoperso,perd
  win_game = Tk()
  win_game.title("Qui est-ce ?")
  win_game.geometry("1050x750")
  win_game.minsize(1050, 700)
  win_game.config(background='paleturquoise')
  dicoperso = randompersonnage()  #choix du personnage
  perd=0
  print(dicoperso)
  question()


 #initialise la partie au premier lancement du programme 
partie()
 

win_game.mainloop()
