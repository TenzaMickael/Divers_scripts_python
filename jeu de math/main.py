import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 4


def poser_questions():
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    o = random.randint(0, 1)
    operateur_str = "+"

    if o == 1:
        operateur_str = "x"
    reponse_str = input(f"Calculer {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a + b
    print()
    if o == 1:
        calcul = a * b

    if reponse_int == calcul:
        return True
    return False


nb_points = 0

for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i + 1} sur {NB_QUESTIONS} :")

    if poser_questions():
        print("Bonne réponse !")
        nb_points += 1
    else:
        print("Mauvaise réponse !")
        print()

print(f"Votre résultat est de : {nb_points} bonne réponse sur {NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS / 2)

if nb_points == NB_QUESTIONS:
    print("Super tu as cartonné !!")
elif nb_points == 0:
    print("C'est pas grave, tu feras mieux la prochaine fois !")
elif nb_points > moyenne:
    print("Super, tu est au dessus de la moyenne")
else:
    print("Tu est en dessous de la moyenne , mais c'est pas grave")
