import json

#créer un fichier json pour la save où tout est initialisé à 0 (pas cocher)
def init_save(theme):
  with open(theme, 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
    size = len(possibilites)
  tab = {} 
  for i in range(size):
     tab[str(i)] = "0"
    
  input = {
    "theme" : theme,
    "possibilites" : tab
  }
  with open('save_file.json', 'w') as outfile:
    json.dump(input, outfile)

#change la valeur de l'id de l'image dans save en 1(image cocher)
def clicked_save(id):
  with open('save_file.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
  possibilites[str(id)] = possibilites[str(id)].replace('0','1')
  data["possibilites"] = possibilites
  with open('save_file.json', 'w') as outfile:
    json.dump(data, outfile)

#change la valeur de l'id de l'image dans save en 0(image pas cocher)
def reclicked_save(id):
  with open('save_file.json', 'r') as f:
    data = json.load(f)
    possibilites = data["possibilites"]
  possibilites[str(id)] = possibilites[str(id)].replace('1','0')
  data["possibilites"] = possibilites
  with open('save_file.json', 'w') as outfile:
    json.dump(data, outfile)