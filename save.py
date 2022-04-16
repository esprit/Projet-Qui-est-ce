import json
#créer un fichier json pour la save où tout est initialisé à 0 (pas cocher)
def init_save(theme,mode,cible):
  with open("json/"+theme, 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    size = len(possibilites)
  tab = {} 
  for i in range(size):
     tab[str(i)] = "0"
    
  input = {
    "theme" : theme, 
    "mode" : mode,
    "cible" : cible,
    "possibilites" : tab,
   
  }
  with open('save_file.json', 'w') as outfile:
    json.dump(input, outfile)
    
      
#initialise la base de donnée pour le mode JvIA (dans save_file.json)
def bd_ia(theme,save):
  with open("json/"+theme, 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    infoPerso = possibilites["0"]
    keys = list(infoPerso)
    ia = {}
  
    for i in range(2,len(keys),1):
      val_list = []
      for j in range(len(possibilites)):
        infoPerso = possibilites[str(j)]
        keys = list(infoPerso)
        arg = keys[i]
        val = infoPerso[arg]
        if val not in val_list:
          val_list.append(val)
      ia[keys[i]] = val_list
  
  with open('save_file.json', 'r') as f:
    data_save = json.load(f)
    if save != True:
      data_save["trouve"] = []
      data_save["historique"] = []
  data_save["ia"] = ia
  
  with open('save_file.json', 'w') as outfile:
    json.dump(data_save, outfile)

    
#change la valeur de l'id de l'image dans save en 1(image cocher)
def clicked_save(id):
  with open('save_file.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
  possibilites[str(id)] = possibilites[str(id)].replace("0","1")
  data["possibilites"] = possibilites
  with open('save_file.json', 'w') as outfile:
    json.dump(data, outfile)

#change la valeur de l'id de l'image dans save en 0(image pas cocher)
def reclicked_save(id):
  with open('save_file.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
  possibilites[str(id)] = possibilites[str(id)].replace("1","0")
  data["possibilites"] = possibilites
  with open('save_file.json', 'w') as outfile:
    json.dump(data, outfile)