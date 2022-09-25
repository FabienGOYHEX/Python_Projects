import random
import time
import os

#_________________________ FUNCTIONS _________________________________
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def initial_number():
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    for i in range(4):
        random_number = random.randint(0,9)
        if number1 == 0 :
            number1 = str(random_number)
        elif number2 == 0 :
            number2 = str(random_number)
        elif number3 == 0 :
            number3 = str(random_number)
        elif number4 == 0 :
            number4 = str(random_number)
    return  number1 + number2 + number3 + number4

def add_additionnal_number():
    additional_number = str(random.randint(1,9))
    return additional_number


def compare_reponse(referal_number, user_response):
    if referal_number == user_response :
        return True
    else:
        return False


def update_referal_number(player_status) :
    if player_status == True :
        additionnal_number = add_additionnal_number()
        new_referal_number = str(REFERAL_NUMBER)+ str(additionnal_number)
        return new_referal_number

#_________________________ UTILS _________________________________

player_status = True
REFERAL_NUMBER =""
SCORE= 0

#_________________________ PROGRAM _________________________________

print("Retenez la séquence :")
initial_number = initial_number()
print(initial_number)
REFERAL_NUMBER= initial_number
time.sleep(3)
#os.system('clear')
clear_screen()
response = input("Votre réponse : ")
compare_response = compare_reponse(REFERAL_NUMBER, response)
if compare_response == True :
    SCORE = SCORE +1
    print(f" votre score est de {SCORE}")

while compare_response == True :
    referal_number = update_referal_number(player_status)
    print(f"{referal_number}")
    REFERAL_NUMBER=referal_number
    time.sleep(3)
    #os.system('clear')
    clear_screen()
    response = input("Votre réponse : ")
    compare_response = compare_reponse(REFERAL_NUMBER, response)
    if compare_response == True :
        SCORE= SCORE +1
        print(f" votre score est de {SCORE}")
else :
    print(f"Dommage, la bonne réponse était :{REFERAL_NUMBER} votre score est de {SCORE} ")