from tkinter import *
import tkinter as tk
from tkinter import ttk
from recup import *
from PIL import Image, ImageTk

def window():
    global win
    win= Tk()
    win.title("Qui est-ce ?")
    win.resizable(False, False)

    window_height = 800
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


    window_height = 800
    window_width = 1400

    screen_width = win_mode.winfo_screenwidth()
    screen_height = win_mode.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win_mode.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    for i in range(10):
        Frame(win_mode, width=80, height=40, background='#0d6768').grid(row=0, column=i)

    for j in range(10):
        Frame(win_mode, width=80, height=40, background='#0d6768').grid(column=0, row=j)
    image_1 = PhotoImage(file='images/player.png')
    img1_label = Label(image=image_1)

    mode_1 = Button(win_mode, image=image_1, command=window_game, borderwidth=0,bg='#0d6768')
    mode_1.grid(row=4,column=4)
    label1 = Label(win_mode, text = "Classique", font=("Courrier",30,'bold'),bg='#0d6768')
    label1.grid(row=5, column=4)


    image_2 = PhotoImage(file='images/playervsia.png')
    img2_label = Label(image=image_2)

    mode_2 = Button(win_mode, image=image_2 , command=window_game, borderwidth=0,bg='#0d6768')
    mode_2.grid(row=4,column=6)
    label2 = Label(win_mode, text = "Joueur vs IA", font=("Courrier",30,'bold'),bg='#0d6768')
    label2.grid(row=5, column=6)

    win_mode.mainloop()

def win_theme():
    win_mode.destroy()
    global win_theme
    win_theme= Tk()
    win_theme.resizable(False, False)
    win_mode.config(background='#0d6768')

    window_height = 800
    window_width = 1400

    screen_width = win_theme.winfo_screenwidth()
    screen_height = win_theme.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win_theme.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))











def window_game():
    win_mode.destroy()
    affichage_possibilite()
    win2= Tk()
    win2.resizable(False, False)
    win2.config(background='#0d6768')
    window_height = 800
    window_width = 1400

    screen_width = win2.winfo_screenwidth()
    screen_height = win2.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    wrapper1 = LabelFrame(win2)

    mycanvas = Canvas(wrapper1)
    mycanvas.pack(side=LEFT, fill="both", expand="yes")

    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical",command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)

    mycanvas.bind('<Configure>',  lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    global myframe
    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window=myframe, anchor="nw")

    taille = len(mes_images)
    nbrCol = int(nbrColonne())
    nbrLi = int(nbrLigne())
    incr = 0


    for i in range (nbrCol) :
        for y in range(nbrLi):
            if taille-1 > i+y :
                image = ImageTk.PhotoImage(Image.open(mes_images[incr]))
                panel = Label(myframe, image=image)
                panel.image = image
                panel.grid(row=y, column=i, sticky='nw')
                panel.bind('<Button-1>', lambda event, r=y,c=i,h=image.height(),w=image.width(),nom_img=mes_images[incr],id=incr:on_click(event,r,c,h,w,nom_img,id))

                incr += 1

    wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
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
    red.grid(row=r,column=c, sticky='nw')
    print("r1=",r,"  c1=",c)
    red.bind('<Button-1>', lambda event, r=r,c=c,h=h,w=w,nom_img=nom_img,id=id:on_reclick(event,r,c,h,w,nom_img,id))



def on_reclick(event,r,c,h,w,nom_img,id):
    image = ImageTk.PhotoImage(Image.open(nom_img))
    panel = Label(myframe, image=image)
    panel.image = image
    panel.grid(row=r, column=c, sticky='nw')
    panel.bind('<Button-1>', lambda event, r=r,c=c,h=h,w=w,nom_img=nom_img,id=id:on_click(event,r,c,h,w,nom_img,id))


window()



