from tkinter import *
import tkinter as tk
from recup import *
from PIL import Image, ImageTk
from tkinter import ttk

win= Tk()
win.title("Qui est-ce ?")
win.geometry("750x550")
win.minsize(700,500)

win.config(background='grey')


label_title = Label(win, text="C KI ?",font=("Courrier",40), bg='grey')
label_title.pack()



def window_game():
  win.destroy()
  affichage_possibilite()
  win2= Tk()
  win2.geometry("750x550")

  wrapper1 = LabelFrame(win2)
  
  mycanvas = Canvas(wrapper1)
  mycanvas.pack(side=LEFT, fill="both", expand="yes")

  yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical",command=mycanvas.yview)
  yscrollbar.pack(side=RIGHT, fill="y")

  mycanvas.configure(yscrollcommand=yscrollbar.set)

  mycanvas.bind('<Configure>',  lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

  
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

  #fonction on_click sur une image sans croix
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
    
    
    
  #fonction on_click sur une image avec croix
  def on_reclick(event,r,c,h,w,nom_img,id):
    image = ImageTk.PhotoImage(Image.open(nom_img))
    panel = Label(myframe, image=image)
    panel.image = image
    panel.grid(row=r, column=c, sticky='nw')
    panel.bind('<Button-1>', lambda event, r=r,c=c,h=h,w=w,nom_img=nom_img,id=id:on_click(event,r,c,h,w,nom_img,id))
    

Start_Button = Button(win, text= "Play", font=("Courrier",20), bg='white',command=window_game)
Start_Button.pack(pady=25)
Leave_Button = Button(win, text= "Leave", font=("Courrier",20),bg='white',command=win.quit)
Leave_Button.pack(pady=25)



win.mainloop()