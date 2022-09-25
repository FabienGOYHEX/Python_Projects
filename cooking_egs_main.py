import time
import beepy

#FUNCTIONS

def min_print (value):
    min = value//60
    return min

def sec_print (value):
    min = value//60
    sec = value - min * 60
    return sec


#Functions to dispach the cooking times depending on the user selecction
def time_selected(value_selected):
    if value_selected == 1:
        return 180
    elif value_selected == 2:
        return 360
    elif value_selected == 3:
        return 540
    else :
        print("erreur dans la sélection. FIN DU PROGRAMME")


def dot():
    for i in range(10):
        time.sleep(1)
        print(f".", end="", flush=True)


def chrono(minuts_value):
    minutsaccount = minuts_value
    while not minutsaccount == 0:
        seconds_acount = 6
        print(f"temps de cuisson: {minutsaccount} minutes ",end="", flush = True)
        dot()
        print("")
        if minutsaccount > 0:
            minutsaccount = minutsaccount -1
        for i in range(5) :
            if seconds_acount >0 :
                seconds_acount = seconds_acount -1
                print(f"temps de cuisson: {minutsaccount} : {seconds_acount}0 secondes ",end="", flush=True)
                dot()
                print("")

    print("Cuisson terminée")
    beepy.beep(sound="ping")

    # PROGRAM

print("Trois cuissons sont disponibles : ")
print("")
print("               1 - Oeufs à la coque : 3 minute")

print("               2 - Oeufs mollets : 6 minutes")

print("               3 - Oeufs durs : 9 minutes")

print("")

user_selection =  int(input("Quelle cuisson souhaitez vous (1, 2, 3) ? "))
cooking_time = time_selected(user_selection)
min_count = min_print(cooking_time)
sec_count = sec_print(cooking_time)
chrono(min_count)
