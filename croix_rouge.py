
import json
import random
from recup import *
# import afficheimg

def affiche() :
  with open('perso.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    
    infoPerso = possibilites["0"]
    keys= list(infoPerso)
    print(keys)
    for i in range(len(keys)) :
      print(keys[i])

  # for i in range (3):
  #   print(possibilites[str(i)])
  
  # lperso = possibilites["0"]
  # print(lperso[1])
  

def randomize():
  with open('perso.json', 'r') as f:
        data = json.load(f)
  l=len(data["possibilites"])
  r = random.randint(0,l-1)
  print(r)

affiche()
# afficheimg.afficheimage()
# randomize()

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

# --- functions ---

root = Tk()
def on_click(event=None):
  global image
  image = Image.open("red2.png")
  photo = ImageTk.PhotoImage(image)
  print(type(photo))
  red = tk.Label(root, image=photo)
  red.image = photo
  red.grid(row=1,column=1, sticky='nw')
  
  print("image clicked")
  

# --- main ---

# init    


# load image
image = Image.open("personnages/"+"samuel.png")
photo = ImageTk.PhotoImage(image)

# label with image
l = Label(root, image=photo)
l.image = image
l.grid(row=1,column=1, sticky='nw')


# bind click event to image
l.bind('<Button-1>', on_click)

# # button with image binded to the same function 
# b = tk.Button(root, image=photo, command=on_click)
# b.pack()

# # button with text closing window
# b = tk.Button(root, text="Close", command=root.destroy)
# b.pack()
    
# # "start the engine"
root.mainloop()