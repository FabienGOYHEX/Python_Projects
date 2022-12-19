def ask_age(name):
    age = 0
    while age == 0:
        age_str = input(name + " Quel est votre age ? ")
        try:
            age = int(age_str)
        except:
            print("Pour votre age un nombre est nécessaire")
    return age


def ask_name() :
    nom =""
    while nom =="":
        nom = input("Quel est votre nom ? ")
    return nom
def ask_size(name):
    size=""
    while size =="":
        size =input("Quel est votre taille ? "+ str(name))
    return size

def Display_personnal_informations(name, age,taille = 0) :
    def display_size():
        if not taille == 0 :
            return taille

    print("Gros Scoop  " + name + " cette année tu as " + str(
        age) + " ans " + name + "  . L'an prochain tu auras " + str(age + 1) + " ans. Tu mesures " +str(display_size()) +" m." )

def Minor_person(age):
    if  age == 17 :
        print("vous êtes presque majeur")
    elif  12 <= age < 18 :
        print("vous êtes adolescent")
    elif age == 1 or 2 :
        print("vous êtes un bébé")
    elif age == 18 :
        print("Félicitations tout juste majeur ! ")
    elif age >= 60:
        print("vous etes seniors")
    elif age < 10:
        print("vous êtes un enfant")
    elif age > 18 :
        print("Vous etes majeurs")
    else :
        print("vous êtes mineurs")
    

NB_PERSON = 1

for i in range(0,NB_PERSON):
    nom = "personne " +str(i +1)
    age = ask_age(nom)
    size = ask_size(nom)





"""nom1 = ask_name()
nom2 = ask_name()


age1 = ask_age(nom1)
age2 = ask_age(nom2)


#Display_personnal_informations(nom1,age1)
#Display_personnal_informations(nom2,age2)
Minor_person(age1)
Minor_person(age2)"""



#print("Gros Scoop  " + nom1 + " cette année tu as " + str(age1) +" ans " +nom1 +"  . L'an prochain tu auras " + str(age1+1) +" ans.")
#print("Gros Scoop  " + nom2 + " cette année tu as " + str(age2) +" ans " +nom2 +"  . L'an prochain tu auras " + str(age2+1) +" ans.")


