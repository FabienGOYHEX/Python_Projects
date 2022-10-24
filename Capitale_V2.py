# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

def response_comparator(question):
    true_response_str = question[2]
    choice = question[1]
    for i in range(len(choice)):
        if true_response_str == choice[i]:
            return i+1


def poser_question(question):
    choice = question[1]
    bonne_reponse = response_comparator(question)
    global score

    print("QUESTION")
    print("  ", question[0])

    for i in range(len(choice)):
        print("", i+1, "-", choice[i])

    print()
    reponse_str = input("Votre réponse entre 1 et " + str(len(choice))+":")
    reponse_int = int(reponse_str)

    if reponse_int == bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")

    print()


score = 0

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

question1 = ("Quelle est la capitale de la France ?",
             ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?",
             ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# response_comparator(question1)
# response_comparator(question2)
# poser_question("Quelle est la capitale de la France ?",
#            "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)
