from tkinter import *
import tkinter as tk
import json
import os
from PIL import ImageTk
import random

mes_images = []
nbrCol = 0
nbrLi = 0

def localisation_json(loca_json):
    global fichier
    fichier = loca_json

def liste_json():
    liste = os.listdir("json")
    return liste

def affichage_possibilite():
    mes_perso = []
    with open("json/" + fichier, 'r',encoding='utf-8') as f:
        data = json.load(f)
    possibilites = data["possibilites"]
    for i in data["possibilites"]:
        perso = possibilites[str(i)]
        my_img = "images_theme/" + data["images"] + perso["fichier"]
        mes_images.append(my_img)
        mes_perso.append(perso["nom"])
def recup_keys(): #retourne la liste des keys qui décrivent les perso: exemple: ['fichier', 'nom', 'genre', 'cheveux', 'lunettes', 'chauve']
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
    data = json.load(f)
    possibilites = data["possibilites"]

    infoPerso = possibilites["0"]
    keys = list(infoPerso)  #liste des keys du dictionnaire

    # for i in range(len(keys)) :  #affiche toutes les key du dictionnaire
    #   print(keys[i])

    return keys

#fonction qui ranvoie le perso choisi par l'ordi
def randompersonnage ():
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    nbperso=int(data["colonne"])*int(data["ligne"])
    r=random.randint(0,nbperso-1)
    infoPerso = possibilites[str(r)]
    return(infoPerso)



def nbrColonne():
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
        data = json.load(f)
  return data["colonne"]

def nbrLigne():
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
        data = json.load(f)
  return data["ligne"]

def tri_keys(caract):
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    nbperso=int(data["colonne"])*int(data["ligne"])
    possibles=[]
    for i in range(nbperso):
      if possibilites[str(i)][caract] not in possibles:
        possibles.append(possibilites[str(i)][caract])
  return(possibles)

#crée une liste de prénom correspondant à la valeur du caractere (toute les personnes qui ont les cheveux roux par ex)
def creerliste(caract,valeur):
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    nbperso=int(data["colonne"])*int(data["ligne"])
    possibles=[]
    for i in range(nbperso):
      if possibilites[str(i)][caract]==valeur :
        possibles.append(possibilites[str(i)]['nom'])
  return(possibles)
