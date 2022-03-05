from tkinter import *
import tkinter as tk
from tkinter import ttk
from recup import *
from PIL import Image, ImageTk
from save import *
import tkinter.ttk


import time
def window():
    global win
    win= Tk()
    win.title("Qui est-ce ?")
    win.resizable(False, False)

    window_height = 900
    window_width = 1400

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    win.config(background='#0d6768')


    photo = PhotoImage(file="images\logo.png")
    LabImg = Label(win, image=photo,bg='#0d6768')
    LabImg.pack()

    Start_Button = Button(win, text= "Jouer", font=("Courrier",30,'bold'), bg='white', fg='#0d6768', width = 10,command=window_mode)
    Start_Button.pack(pady=25)
    Continue_Button = Button(win, text= "Continuer", font=("Courrier",30,'bold'),bg='white',fg='#0d6768', width = 10, command=win.destroy)
    Continue_Button.pack(pady=25)
    Leave_Button = Button(win, text= "Quitter", font=("Courrier",30,'bold'),bg='white',fg='#0d6768', width = 10, command=win.destroy)
    Leave_Button.pack(pady=25)
    win.mainloop()

def window_mode():
    win.destroy()
    global win_mode
    win_mode= Tk()
    win_mode.resizable(False, False)
    win_mode.config(background='#0d6768')

    window_height = 900
    window_width = 1400

    screen_width = win_mode.winfo_screenwidth()
    screen_height = win_mode.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win_mode.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))



    labelText = Label(win_mode, text = "Veuillez choisir votre mode de jeux", font=("Courrier",30,'bold'),bg='#0d6768')
    labelText.pack(pady = 40)

    frame_boutton = Frame(win_mode, bg = "#0d6768")

    image_1 = PhotoImage(file='images/player.png')
    img1_label = Label(image=image_1)

    mode_1 = Button(frame_boutton, image=image_1, command=win_theme, borderwidth=0,bg='#0d6768')
    mode_1.grid(row=0, column=1)
    label1 = Label(frame_boutton, text = "Classique", font=("Courrier",30,'bold'),bg='#0d6768')
    label1.grid(row=1, column=1 )

    Frame(frame_boutton, width=80, background='#0d6768').grid(column=2)

    image_2 = PhotoImage(file='images/playervsia.png')
    img2_label = Label(image=image_2)

    mode_2 = Button(frame_boutton, image=image_2 , command=win_theme, borderwidth=0,bg='#0d6768')
    mode_2.grid(row=0,column=3)
    label2 = Label(frame_boutton, text = "Joueur vs IA", font=("Courrier",30,'bold'),bg='#0d6768')
    label2.grid(row=1, column=3)
    frame_boutton.pack( pady = 70)
    win_mode.mainloop()

def win_theme():
    win_mode.destroy()
    global win_theme
    win_theme= Tk()
    win_theme.resizable(False, False)
    win_theme.config(background='#0d6768')

    window_height = 900
    window_width = 1400

    screen_width = win_theme.winfo_screenwidth()
    screen_height = win_theme.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win_theme.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    liste_split = []
    liste = liste_json()

    for i in range(len(liste)):
        liste_split.append(os.path.splitext(liste[i])[0])


    labelText = Label(win_theme, text = "Veuillez choisir votre Thème", font=("Courrier",30,'bold'),bg='#0d6768')
    labelText.pack(pady = 40)

    frame_boutton = Frame(win_theme, bg = "#0d6768")
    i = 1
    y = 1
    incr = 0

    while incr < (len(liste_split)):
        if y == 7 :
            y = 1
            i += 1
            Frame(frame_boutton, height=15, background='#0d6768').grid(row=i)
            i += 1

        afficher_theme = Button(frame_boutton, text=liste_split[incr],font=("Courrier",30,'bold'),bg='grey',width = 10, command=lambda g = incr: window_game(liste[g]))
        afficher_theme.grid(row=i, column=y)
        y += 1
        Frame(frame_boutton, width=20, background='#0d6768').grid(column=y)
        incr += 1
        y += 1

    frame_boutton.pack( pady = 70)

    win_theme.mainloop()


def window_game(fichier):

    localisation_json(fichier)

    init_save("json/" + fichier)
    win_theme.destroy()
    affichage_possibilite()
    win2= Tk()
    win2.resizable(False, False)
    win2.config(background='#0d6768')
    window_height = 900
    window_width = 1400

    screen_width = win2.winfo_screenwidth()
    screen_height = win2.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    labelText = Label(win2, text = "Qui est-ce ?", font=("Courrier",30,'bold'),bg='#0d6768')
    labelText.grid(row=0,column=2)

    wrapper1 = LabelFrame(win2)


    mycanvas = Canvas(wrapper1,height=500, width=1000,bg="#0d6768")
    mycanvas.pack(side=LEFT, fill="both", expand="yes")

    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical",command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")


    mycanvas.bind('<Configure>',  lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    mycanvas.configure(yscrollcommand=yscrollbar.set)



    global myframe
    myframe = Frame(mycanvas,bg="#0d6768")
    mycanvas.create_window((0,0), window=myframe, anchor="nw")

    taille = len(mes_images)
    nbrCol = int(nbrColonne())
    nbrLi = int(nbrLigne())
    incr = 0




    incr = 0

    for i in range (nbrCol):
        Frame(myframe,height = 50, width= 1000 / nbrCol, background='#0d6768').grid(row = 0, column=i)

    for i in range (nbrLi) :
        for y in range(nbrCol):
            if taille-1 >= i+y :
                image = ImageTk.PhotoImage(Image.open(mes_images[incr]))
                panel = Label(myframe, image=image)
                panel.image = image



                panel.grid(row=i, column=y)
                panel.bind('<Button-1>', lambda event, r=i,c=y,h=image.height(),w=image.width(),nom_img=mes_images[incr],id=incr:on_click(event,r,c,h,w,nom_img,id))



                incr += 1



    Frame(win2,height = 10, width=200, background='#0d6768').grid(row = 1, column=1)
    wrapper1.grid(row= 2, column = 2)
    Frame(win2, width=200, background='#0d6768').grid(row = 1, column=3)
    myframe_box = Frame(win2,bg="#0d6768").grid(row= 3, column = 2)
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
        framebravo=Frame(myframe_box,bg="pink",relief=RAISED,bd=3)
        labelbravo=Label(framebravo,
                              font=("Courrier", 26),
                              bg="pink",
                              text=" BRAVO c'est bien  " + perso)
        framebravo.grid(row = 3, column = 2)
        labelbravo.grid(columnspan=2,ipadx=20,ipady=20)


        recommencer=Button(framebravo,text="Recommencer",command= lambda : partie())
        recommencer.grid(row=2,pady=5)

        quitter=Button(framebravo,text="Quitter",command=win2.destroy)
        quitter.grid(row=2,column=1,pady=5)

      else:
        NON()
        perd=1
        frameperdu=Frame(myframe_box,bg="pink",relief=RAISED,bd=3)
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

      frameMain = Frame(myframe_box, relief=RAISED, bg="DarkTurquoise", bd=4)
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

      frameMain.grid(row=4, column=2, padx=10, sticky = W)
      frameConnect.grid(row=2, columnspan=2, padx=0)


      framereponse = Frame(myframe_box, relief=RAISED, bg="pink", bd=4)
      framereponse.grid(row=4, column=2, padx=10, sticky = E)

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
      global dicoperso,perd
      dicoperso = randompersonnage()  #choix du personnage
      perd=0
      print(dicoperso)
      question()


     #initialise la partie au premier lancement du programme
    partie()


    win2.mainloop()

def on_click(event,r,c,h,w,nom_img,id):
    global image
    red = Image.open("images/"+"red.png")
    red2= red.resize((w,h), Image.ANTIALIAS)
    image = Image.open(nom_img)

    image.paste(red2,(0,0),red2)
    image.save('red2.png',"PNG")

    photo2 = ImageTk.PhotoImage((Image.open("red2.png")).resize((w,h), Image.ANTIALIAS))

    red = tk.Label(myframe, image=photo2)

    red.image = photo2
    red.grid(row=r,column=c)
    print("r1=",r,"  c1=",c)
    red.bind('<Button-1>', lambda event, r=r,c=c,h=h,w=w,nom_img=nom_img,id=id:on_reclick(event,r,c,h,w,nom_img,id))
    clicked_save(id)


def on_reclick(event,r,c,h,w,nom_img,id):
    image = ImageTk.PhotoImage(Image.open(nom_img))
    panel = Label(myframe, image=image)
    panel.image = image
    panel.grid(row=r, column=c)
    panel.bind('<Button-1>', lambda event, r=r,c=c,h=h,w=w,nom_img=nom_img,id=id:on_click(event,r,c,h,w,nom_img,id))
    reclicked_save(id)



window()



