from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import tkinter.ttk
import os.path
from recup import *
from save import *


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

    photo = PhotoImage(file="images/logo.png")
    LabImg = Label(win, image=photo,bg='#0d6768')
    LabImg.pack()

    Start_Button = Button(win, text= "Jouer", font=("Courrier",30,'bold'), bg='white', fg='#0d6768', width = 10,command=lambda :window_mode())
    Start_Button.pack(pady=25)
    Continue_Button = Button(win, text= "Continuer", font=("Courrier",30,'bold'),bg='white',fg='#0d6768', width = 10, command=lambda :save_verif())
    Continue_Button.pack(pady=25)
    Leave_Button = Button(win, text= "Quitter", font=("Courrier",30,'bold'),bg='white',fg='#0d6768', width = 10, command=win.destroy)
    Leave_Button.pack(pady=25)
    win.mainloop()

def window_mode():
    win.destroy()
    global win_mode
    win_mode= Tk()
    win_mode.title("Mode")
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

    mode_1 = Button(frame_boutton, image=image_1, borderwidth=0,bg='#0d6768', command=lambda :win_theme([1,0]))
    mode_1.grid(row=0, column=1)
    label1 = Label(frame_boutton, text = "Classique", font=("Courrier",30,'bold'),bg='#0d6768')
    label1.grid(row=1, column=1 )

    Frame(frame_boutton, width=80, background='#0d6768').grid(column=2)

    image_2 = PhotoImage(file='images/playervsia.png')
    img2_label = Label(image=image_2)

    mode_2 = Button(frame_boutton, image=image_2 , borderwidth=0,bg='#0d6768', command=lambda :window_dif())
    mode_2.grid(row=0,column=3)
    label2 = Label(frame_boutton, text = "Joueur vs IA", font=("Courrier",30,'bold'),bg='#0d6768')
    label2.grid(row=1, column=3)
    frame_boutton.pack( pady = 70)
    win_mode.mainloop()
def window_dif():
    win_mode.destroy()
    global win_dif
    win_dif= Tk()
    win_dif.title("IA vs Joueur")
    win_dif.resizable(False, False)
    win_dif.config(background='#0d6768')

    window_height = 900
    window_width = 1400

    screen_width = win_dif.winfo_screenwidth()
    screen_height = win_dif.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win_dif.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


    labelText = Label(win_dif, text = "Veuillez choisir votre niveau de difficulté", font=("Courrier",30,'bold'),bg='#0d6768')
    labelText.pack(pady = 40)

    frame_boutton_dif = Frame(win_dif, bg = "#0d6768")

    dif1 = Button(frame_boutton_dif, text="Niveau 1",font=("Courrier",30,'bold'),bg='grey',width = 10, command=lambda : win_theme([2,1]))
    dif1.grid(row=1, column=1)

    dif2 = Button(frame_boutton_dif, text="Niveau 2",font=("Courrier",30,'bold'),bg='grey',width = 10, command=lambda : win_theme([2,2]))
    dif2.grid(row=1, column=2)

    dif2 = Button(frame_boutton_dif, text="Niveau 3",font=("Courrier",30,'bold'),bg='grey',width = 10, command=lambda : win_theme([2,3]))
    dif2.grid(row=1, column=3)

    frame_boutton_dif.pack( pady = 70)

    win_dif.mainloop()

def win_theme(mode):
    if mode[0] == 2:
        win_dif.destroy()
    else:
        win_mode.destroy()

    global win_theme
    win_theme= Tk()
    win_theme.resizable(False, False)
    win_theme.config(background='#0d6768')
    win_theme.title("Thème")
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

        afficher_theme = Button(frame_boutton, text=liste_split[incr],font=("Courrier",30,'bold'),bg='grey',width = 10, command=lambda g = incr: window_game(liste[g],False,mode,False))
        afficher_theme.grid(row=i, column=y)
        y += 1
        Frame(frame_boutton, width=20, background='#0d6768').grid(column=y)
        incr += 1
        y += 1

    frame_boutton.pack( pady = 70)

    win_theme.mainloop()


def window_game(fichier,save,mode,restart):
    global dicoperso

    localisation_json(fichier)
    affichage_possibilite()

    if save != True:
      dicoperso = randompersonnage()  #choix du personnage à trouver
      with open("json/" + fichier, 'r',encoding='utf-8') as f:
        data = json.load(f)
        possibilites =data["possibilites"]
        for i in data["possibilites"]:
          if dicoperso==possibilites[str(i)]:
            cible = str(i)
      init_save(fichier,mode,cible)
      if restart == False:
        win_theme.destroy()
    else:
      with open('save_file.json', 'r') as f:
        data = json.load(f)
        cible = data["cible"]

      with open("json/" + fichier, 'r',encoding='utf-8') as f:
        data = json.load(f)
        possibilites =data["possibilites"]
        dicoperso = possibilites[cible]
    if mode[0] == 2:
      bd_ia(fichier,save)



    win2= Tk()
    win2.resizable(False, False)
    win2.config(background='#0d6768')
    win2.title("Qui est-ce ?")
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

    global Liste_pos
    Liste_pos = []
    for i in range (nbrCol):
        Frame(myframe,height = 50, width= 1000 / nbrCol, background='#0d6768').grid(row = 0, column=i)

    for i in range (nbrLi) :
      for y in range(nbrCol):
        pos = [i,y]
        Liste_pos.append(pos)
        if taille-1 >= i+y :
          image = ImageTk.PhotoImage(Image.open(mes_images[incr]))
          r=i
          c=y
          h=image.height()
          w=image.width()
          nom_img=mes_images[incr]
          id=incr

          if save == True:
            with open('save_file.json', 'r') as f:
              data = json.load(f)
              possibilites = data["possibilites"]
              if possibilites[str(incr)] == "1":
                crossed(r,c,h,w,nom_img,id)
              else:
                notcrossed(r,c,h,w,nom_img,id)
          else:
            notcrossed(r,c,h,w,nom_img,id)

          incr += 1

    Frame(win2,height = 10, width=200, background='#0d6768').grid(row = 1, column=1)
    wrapper1.grid(row= 2, column = 2)
    Frame(win2, width=200, background='#0d6768').grid(row = 1, column=3)

    myframe_box = Frame(win2).grid(row= 3, column = 2)




        #Saisie le choix de la première question + la grise
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

    def enlevedouble(liste):

      l=[]
      i=0
      while i<=len(liste)-1:
        if liste[i] not in l:
          l.append(liste[i])
        i=i+1
      return l



      #renvoie la liste des personnes qui vérifient les choix
    def listepersonne():
      global choixliste
      liste=choixliste

      l1=[]
      if liste!=[]:
        l1=creerliste(liste[0],liste[1])
        del liste[0:2]
      l3=[]
      while liste != []:
                l2=creerliste(liste[0],liste[1])
                if connecteur=="ET":
                  for i in range (len(l2)):
                    if l2[i] in l1:
                      l3.append(l2[i])
                  l1=l3
                elif connecteur=="OU":
                  for i in range (len(l2)):
                    if l2[i] not in l1:
                      l1.append(l2[i])
                del liste[0:2]
      l1=enlevedouble(l1) #why?
      return(l1)


    #renvoie le complement des prenoms de liste
    def complementliste(liste):

        l=tri_keys('nom')
        for i in range (len(liste)):
          if liste[i] in l:
            l.remove(liste[i])
        return(l)


    #ouvre les choix des prochains critères
    def OuvreChoix():
        global cbPlusChoix, line, cbPlusValeurs,frameMain
        cbPlusChoix = tkinter.ttk.Combobox(frameMain, state="readonly", values=l)
        cbPlusValeurs = tkinter.ttk.Combobox(frameMain, state="readonly")
        cbPlusChoix.set("choix")
        cbPlusChoix.grid(row=line,column=0,columnspan=2, pady=10)
        cbPlusValeurs.grid(row=line, column=2,columnspan=2, pady=10)
        line += 1
        cbPlusChoix.bind("<<ComboboxSelected>>", action3)


    #vérification des valeurs saisies par rapport aux valeurs à trouver
    def verif(liste):
        global connecteur, dicoperso

        if connecteur == "":
            if liste != [] and dicoperso[liste[0]] ==liste[1]:
                return ("TRUE")
            else:
                return ("FALSE")
        elif connecteur == "ET":
            i=0
            while i<=len(liste)-1:
                if dicoperso[liste[i]] == liste[i+1]:
                    i=i+2
                else:
                    return ("FALSE")

            return ("TRUE")
        elif connecteur == "OU":
            i=0
            while i<=len(liste)-1:
                if dicoperso[liste[i]] != liste[i+1]:
                    i=i+2
                else:
                    return ("TRUE")
            return ("FALSE")


    #vérification après selection du prenom
    def OK(event):
      global frameperdu,perd,perso
      perso = cbprenom.get()
      if dicoperso["nom"]==perso:
        frameMain.destroy()
        framereponse.destroy()
        framebravo=Frame(myframe_box,bg="DarkTurquoise",relief=RAISED,bd=3)
        labelbravo=Label(framebravo,
                              font=("Courrier", 26),
                              bg="DarkTurquoise",
                              text=" BRAVO c'est bien  " + perso)
        framebravo.grid(row = 3, column = 2)
        labelbravo.grid(columnspan=2,ipadx=20,ipady=20)

        recommencer=Button(framebravo,text="Recommencer",command=re_partie)
        recommencer.grid(row=2,pady=5)

        quitter=Button(framebravo,text="Quitter",command=win2.destroy)
        quitter.grid(row=2,column=1,pady=5)

      else:
        if reste == 1:
          frameMain.destroy()
          framereponse.destroy()
          framebravo=Frame(myframe_box,bg="DarkTurquoise",relief=RAISED,bd=3)
          labelbravo=Label(framebravo,
                                font=("Courrier", 26),
                                bg="DarkTurquoise",
                                text=" PERDU, l'Ia a trouvé " + dicoperso["nom"] + " avant vous!")
          framebravo.grid(row = 3, column = 2)
          labelbravo.grid(columnspan=2,ipadx=20,ipady=20)

          recommencer=Button(framebravo,text="Recommencer",command=re_partie)
          recommencer.grid(row=2,pady=5)

          quitter=Button(framebravo,text="Quitter",command=win2.destroy)
          quitter.grid(row=2,column=1,pady=5)
        else:
          NON()
          perd=1
          frameperdu=Frame(myframe_box,bg="DarkTurquoise",relief=RAISED,bd=3)
          frameperdu.grid(row=1,column=2)
          perdu=Label(frameperdu,text="Perdu, essaye encore !",bg="DarkTurquoise",font=("Courrier", 15))
          perdu.grid(padx=20,pady=20)


    def NON():
      if reste == 1:
        frameMain.destroy()
        framereponse.destroy()
        framebravo=Frame(myframe_box,bg="DarkTurquoise",relief=RAISED,bd=3)
        labelbravo=Label(framebravo,
                              font=("Courrier", 26),
                              bg="DarkTurquoise",
                              text=" PERDU, l'Ia a trouvé " + dicoperso["nom"] + " avant vous!")
        framebravo.grid(row = 3, column = 2)
        labelbravo.grid(columnspan=2,ipadx=20,ipady=20)

        recommencer=Button(framebravo,text="Recommencer",command=re_partie)
        recommencer.grid(row=2,pady=5)

        quitter=Button(framebravo,text="Quitter",command=win2.destroy)
        quitter.grid(row=2,column=1,pady=5)
      else:
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



    #affichage vrai test sur la deuxieme frame
    def vraitest():
      global framesuite,label_reponse,oui,non,label_perso,perd,frameperdu,choixliste,reste
      t=verif(choixliste)
      reste = 0
      if test:
        if mode[0] == 2: #si choisis JoueurVsIa
          if mode[1] == 1: #niveau 1
            reste = ia_opti(True)
          elif mode[1] == 2: #niveau 2
            r=random.choice([True, False])
            reste = ia_opti(r)
          else: #niveau 3 (default)
            reste = ia_opti(False)
        if reste==1:
          label_reponse = Label(framereponse,
                                  font=("Courrier", 12),
                                  bg="DarkTurquoise",
                                  text=" La réponse est " + t + ".\n L'ia a trouvé le personnage.")
          label_reponse.grid(columnspan=5, pady=20, padx=10)
        else:
          if mode[0] == 2:
            label_reponse = Label(framereponse,
                                    font=("Courrier", 12),
                                    bg="DarkTurquoise",
                                    text=" La réponse est " + t + ".\n Il reste " + str(reste) + " choix à l'ia \n pour trouver le personnage")
            label_reponse.grid(columnspan=5, pady=20, padx=10)
          else:
            label_reponse = Label(framereponse,
                                    font=("Courrier", 12),
                                    bg="DarkTurquoise",
                                    text=" La réponse est " + t )
            label_reponse.grid(columnspan=5, pady=20, padx=10)
        framesuite = Frame(framereponse, relief=GROOVE, bg="DarkTurquoise", bd=4)
        framesuite.grid(row=1, column=0, padx=10,pady=10)
        label_perso=Label(framesuite,font=("Courrier", 12),
                                bg="DarkTurquoise",
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


          labeltriche=Label(framereponse,font=("Courrier", 12),
                                bg="DarkTurquoise",
                                text= str(len(perso_elim(liste_id_nom(personne))))+" personnages à éliminer")
          labeltriche.grid(row=3, column=0, pady=10, padx=5)
          crossed_cheat(fichier,liste_id_nom(personne))
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


      Frame(myframe_box, height=250, bg="#0d6768").grid(row = 4, column=2)

      frameMain.grid(row=4, column=2, padx=100, sticky = W)
      frameConnect.grid(row=2, columnspan=2, padx=0)


      framereponse = Frame(myframe_box, relief=RAISED, bg="DarkTurquoise", bd=4)
      framereponse.grid(row=4, column=2, padx=100, sticky = E)

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
    def re_partie():
      win2.destroy()
      window_game(fichier,False,mode,True)

    def partie():
      global perd

      perd=0
      question()
     #initialise la partie au premier lancement du programme
    partie()

    win2.mainloop()


#affiche l'image avec une croix
def crossed(r,c,h,w,nom_img,id):
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
  red.bind('<Button-1>', lambda event, r=r,c=c,h=h,w=w,nom_img=nom_img,id=id:on_reclick(event,r,c,h,w,nom_img,id))
  clicked_save(id)

#affiche l'image
def notcrossed(r,c,h,w,nom_img,id):
  image = ImageTk.PhotoImage(Image.open(nom_img))
  panel = Label(myframe, image=image)
  panel.image = image
  panel.grid(row=r, column=c)
  panel.bind('<Button-1>', lambda event, r=r,c=c,h=h,w=w,nom_img=nom_img,id=id:on_click(event,r,c,h,w,nom_img,id))


#affiche une image avec une croix et change la valeur dans le save_file
def on_click(event,r,c,h,w,nom_img,id):
  crossed(r,c,h,w,nom_img,id)
  clicked_save(id)

#affiche une image sans croix et change la valeur dans le save_file
def on_reclick(event,r,c,h,w,nom_img,id):
  notcrossed(r,c,h,w,nom_img,id)
  reclicked_save(id)

def crossed_cheat(fichier,Liste_id):
  for i in range(len(Liste_id)):
    id = Liste_id[i]
    image = ImageTk.PhotoImage(Image.open(mes_images[id]))
    h=image.height()
    w=image.width()
    nom_img=mes_images[id]
    position = Liste_pos[id]
    r = position[0]
    c = position[1]
    crossed(r,c,h,w,nom_img,id)

#vérifie si le fichier save_file existe, et si c'est le cas lance directement la partie
def save_verif():
  if os.path.isfile('save_file.json'):
    with open('save_file.json', 'r') as f:
      data = json.load(f)
      theme = data['theme']
      mode = data['mode']
      win.destroy()
      window_game(theme,True,mode,False)
  else:
    messagebox.showerror("Error Example", "Aucune sauvegarde")

window()