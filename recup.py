from tkinter import *
import tkinter as tk
import json
import random

mes_images = []
nbrCol = 0
nbrLi = 0

def affichage_possibilite():    
    mes_perso = []
    with open('perso.json', 'r') as f:
        data = json.load(f)
    possibilites = data["possibilites"]
    for i in data["possibilites"]:
        perso = possibilites[str(i)]
        my_img = "personnages/" + perso["fichier"]
        mes_images.append(my_img)
        mes_perso.append(perso["prenom"])

    
def recup_keys(): #retourne la liste des keys qui décrivent les perso: exemple: ['fichier', 'prenom', 'genre', 'cheveux', 'lunettes', 'chauve']
  with open('perso.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    infoPerso = possibilites["0"]
    keys = list(infoPerso)  #liste des keys du dictionnaire
    # for i in range(len(keys)) :  #affiche toutes les key du dictionnaire
    #   print(keys[i])
    return keys 
    
def randompersonnage ():
  #fonction qui ranvoie le perso choisi par l'ordi
  with open('perso.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    nbperso=int(data["colonne"])*int(data["ligne"])
    r=random.randint(0,nbperso-1)
    infoPerso = possibilites[str(r)]
    return(infoPerso)



def nbrColonne():
  with open('perso.json', 'r') as f:
        data = json.load(f) 
  return data["colonne"]

def nbrLigne(): 
  with open('perso.json', 'r') as f:
        data = json.load(f)
  return data["ligne"]

# crée une liste de valeur pour chaque key
def tri_keys(caract): 
  with open('perso.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    nbperso=int(data["colonne"])*int(data["ligne"])
    possibles=[]
    for i in range(nbperso):
      if possibilites[str(i)][caract] not in possibles:
        possibles.append(possibilites[str(i)][caract])
  return(possibles)

def creerliste(caract,valeur): 
  with open('perso.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    nbperso=int(data["colonne"])*int(data["ligne"])
    possibles=[]
    for i in range(nbperso):
      if possibilites[str(i)][caract]==valeur :
        possibles.append(possibilites[str(i)]['prenom'])
  return(possibles)
