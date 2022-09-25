
"""
def question(capitale,a,b,c,d,true_response):
    global score
    print("Quel est la Capitale de", capitale, "?")
    print("(a)", a)
    print("(b)", b)
    print("(c)", c)
    print("(d)", d)
    user_responce = input("Votre réponse : ")

    if true_response == user_responce:
        score = score +1
        print("Bonne réponse ! votre score est de ", score)
    else:
        print("Mauvaise réponse votre score est de ", score)



score = 0

question("France", "Marseille", "Nice", "Paris", "Nantes","c")
question("Italie", "Milan", "Palerme", "Rome", "Naple", "c")
"""
""" 




### FONCTION RECURSIVE
def usr_choise(min , max):
    user_response_str = input("Sélectionnez un nombre entre " + str(min) + " et " + str(max))
    try :
        user_response_int = int(user_response_str)
        if not min <= user_response_int <= max :
            print("ERROR NUMBER: Sélectionnez un nombre entre " + str(min) + " et " + str(max))
            return usr_choise(min, max)
        return print(str(user_response_int))
    except:
         print("ERROR EXCEPT: Sélectionnez un nombre entre " + str(min) + " et " + str(max))
         return usr_choise(min, max)


#usr_choise(1 , 4)

#FONCTION GENERIQUE

def afficher_table(n, operator_str, opération_cbk) :
    for i in range (1,10):
        print(i,operator_str,n, "=", opération_cbk(i,n))

def mult_calback(a,b):
   return a*b

def add_calback(a,b):
   return a+b



afficher_table(3, "x",mult_calback)
print()
afficher_table(3, "+",add_calback)

# Function lambda
afficher_table(2,"/", lambda a, b : a/b)
print()
afficher_table(2,"^", lambda a, b : pow(a, b))
"""

# TUPLE
# Un tupple est un tableau créé avec des parentèses, il est similaire à la liste à la différence qu'il est readunly, il est fixe, on ne peu pas rajouter des éléments
# Tuple : immutable, modifiable se créé avec des ()
persones_tuple = ("Martin", "Jean", "Pierre", "Didier")

# LISTE
# Liste : mutable rajouter /supprimer/ modifier les éléments se créé avec des []
persones_list = ["Martin", "Jean", "Pierre", "Didier"]

# print(persones_list) # print la liste de prénom
# print(len(persones_list))# print le nombre de valeurs présente dans la liste
# print(persones_list[0]) # print la première valeur présente dans la liste

# for i in range (0, len(persones_list)): #tu boucles à les valeurs de la liste de 0 au nombre de valeurs présentent dans la liste
#    print(persones_list[i]) # à chaque tour tu print la valeur stockée dans i

# La boucle for avec in range met les éléments dans une liste par défaut. Les données étant déjà contenues dans une liste, on peut s'en passer.
"""
for i in persones_list:
    print(i)
    print(len(i))
    print(i[0])

#si j'utilise la fonctin len(i) j'obtien le nombre lettre de chaque prénom
#Si j'utilise les crochets et l'index je récupère la première lettre du prénom, les chaines de caractères se comportent comme un tuple

#--------------------------- Manipulation de listes ------------------------

# ajouter un élément avec append
nouvelle_personne = "david"
persones_list.append(nouvelle_personne)
print(persones_list)

# supprimer un élément avec del + l'index de l'élément à supprimer
del persones_list[4]
print(persones_list)

def afficher_personnes(colection):
    for i in colection :
        print(i)
def modifier_valeur(a):
    a = 10
afficher_personnes(persones_list)
"""


def informations_personnes():
    return "Mélanie", 37, 1.54

# def afficher_informations():
#    print("nom : ", nom, "age : ", age, "taille : ", taille)
# nom , age, taille = informations_personnes()


def afficher_informations(nom, age, taille):
    print("nom : ", nom, "age : ", age, "taille : ", taille)


infos = informations_personnes()

afficher_informations(*infos)
print('hello world')
