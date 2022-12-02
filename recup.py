from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import json
import os
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
    global mes_perso
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

    return keys

#fonction qui renvoie le perso choisis par l'ordi
def randompersonnage ():
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    nbperso=int(data["colonne"])*int(data["ligne"])
    r=random.randint(0,nbperso-1)
    infoPerso = possibilites[str(r)]
    return(infoPerso)

def liste_id_nom(liste_nom):
    liste_id = []
    for i in range (len(mes_perso)):
        for y in range (len(liste_nom)):
            if liste_nom[y] == mes_perso[i]:
                liste_id.append(i)
    return liste_id


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

#crée une liste de prénom correspondant à la valeur du caractère (toute les personnes qui ont les cheveux roux par ex)
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

def creerlisteId(caract,valeur):
  with open("json/" + fichier, 'r',encoding='utf-8') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    possibles=[]
    for i in range(len(possibilites)):
      if possibilites[str(i)][caract]==valeur :
        possibles.append(str(i))
  return(possibles)

#fonction "optimimal", l'ia pose la question qui peut potentiellement enlever le plus de personnages
def ia_opti(randomize):
  with open("json/" + fichier, 'r',encoding='utf-8') as file:
    datum = json.load(file)
    possibilites = datum["possibilites"]
  with open("save_file.json", 'r') as f:
    data = json.load(f)
    bd_ia = data["ia"]
    keys = list(bd_ia) #liste des arguments (keys)
    max=["","",0,[]] #max[argument,valeur,nbr_occurence,liste_perso_correspondant]
    trouve = data["trouve"] #liste des id des perso trouvé
    cible = data["cible"] #id du perso à trouver
    historique = data["historique"] #liste des questions déja posé
    reste = len(possibilites)-len(trouve) #nbr de perso restant à cocher
    chance=[True]
    r=True

    for i in range(0,len(keys),1):
      arg_ia = keys[i] #argument
      val = bd_ia[arg_ia] #liste valeurs argument
      for j in range(len(val)):
        val_ia = val[j] #valeur argument
        l_id = creerlisteId(arg_ia,val[j]) #liste des personnes avec les caractéristiques correspondantes
        compteur = len(l_id)
        verif = [arg_ia, val_ia]
        if verif not in historique: #si question jamais posé avant
          for k in range(len(l_id)): #calcul le nbr de perso pas encore trouvés
            if l_id[k] in trouve:
              compteur -= 1
          if randomize: #si on veut une question random
            if (reste > compteur):
              chance.append(not(r))
              r=random.choice(chance)
              if r or (max==["","",0,[]]): #entre s'il y a au moins 2 perso à trouver ET si r est true, OU si max est vide(pour au moins choisir une question)
                max[0]=arg_ia
                max[1]=val_ia
                max[2]=compteur
                max[3]=l_id
          else:
            if (reste>compteur)and(compteur>max[2]): #remplace max si plus grand
              max[0]=arg_ia
              max[1]=val_ia
              max[2]=compteur
              max[3]=l_id
  t = max[3]
  ajoute = []

  if cible not in t: #"coche" les perso dans t
    for i in range(len(t)):
      ajoute.append(str(t[i]))
  else :  #"coche" tous les perso qui ne sont pas dans t
    for i in range(len(possibilites)):
      if str(i) not in t:
        ajoute.append(str(i))
  for i in range(len(ajoute)):
    if ajoute[i] not in trouve:
      trouve.append(ajoute[i])

  historique.append([max[0],max[1]])
  data["trouve"] = trouve
  reste = len(possibilites)-len(trouve)
  with open("save_file.json", "w") as outfile:
    json.dump(data, outfile)

  return(reste) #return reste



#rempli la liste "trouve" avec les perso à enlever
def ia_find(Liste_id):
  with open('save_file.json', 'r') as f:
    data_save = json.load(f)
    trouve = data_save["trouve"]
    for i in range(len(Liste_id)):
      trouve.append(Liste_id(i))



def perso_elim(liste_perso):
    with open('save_file.json', 'r') as f:
        data_save = json.load(f)
        possibilites = data_save["possibilites"]
        liste_supr = []
        for i in range(len(liste_perso)):

            if possibilites[str(liste_perso[i])] == "1":
                liste_supr.append(liste_perso[i])
    for element in liste_supr:
        if element in liste_perso:
            liste_perso.remove(element)
    return liste_perso
