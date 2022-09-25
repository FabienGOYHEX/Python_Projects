# LISTES - EXERCICES / DEMANDER LE NOM DES PERSONNES

"""
=> demandes le nom des perssones
=> boucle infinie, sort quand le nom est vide
 => seulement à la fin afficher la liste des personnes
  """
"""
names = []
while True:
    ask_name = input("Quel est votre nom ? ")
    if ask_name == "":
        break
    names.append(ask_name)
print()

for name in names:
    print("Nom des personnes " + name)

"""
# LISTES - ALGO / VALEUR LA PLUS PETITE

nom_chauffeur = [ "Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distances_chauffeurs_kms =[1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

distance_min = distances_chauffeurs_kms[0]

for distance in distances_chauffeurs_kms :
    if distance < distance_min:
        distance_min = distance
index = distances_chauffeurs_kms.index(distance_min)
conducteur_name = nom_chauffeur[index]

print("Notre conducteur le plus proche est ", conducteur_name, "il est à une distance de ", distance_min, "kms")
print(index)



