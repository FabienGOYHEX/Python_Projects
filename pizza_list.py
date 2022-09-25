pizzas=["4 Formages", "Végétarienne", "Hawai", "Calzone"]

#def personalize_sort(e):
#    return e

def print_pizza (collection, arg = len(pizzas)):
    print("---- Liste des pizzas", "(",len(collection),") ----")
#    collection.sort( key = personalize_sort)
    if len(collection) != 0:
        for i in collection[0:arg]:
            print(i)
        print()
        print("Première pizza : ", collection[0])
        print("Dernière pizza : ", collection[-1])
    else:
        print("Aucune pizza Disponible")

"""def add_pizza( ):
    user_input = input("Pizza à ajouter : ")
    if pizza_existe(user_input, pizzas) :
        print(" Cette pizza existe déjà")
    else :
         pizzas.append(user_input)"""

def pizza_existe(user_input, collection) :
    for i in collection :
        if user_input == i :
            return True
    return False


def add_pizza(collection):
    user_input = input("Pizza à ajouter : ")
    if user_input in collection :
        print("cette pizza existe déjà")
    else :
        collection.append(user_input)
vide =()
#add_pizza(pizzas)
print_pizza(pizzas)
