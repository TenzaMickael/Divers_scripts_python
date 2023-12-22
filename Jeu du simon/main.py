import time
import random
import os


# Pour effacer l'ecran


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


# Générer chiffres initial
sequence_nombres = ""
for i in range(4):
    chiffre = random.randint(0, 9)
    sequence_nombres += str(chiffre)
# Effacer l'écran
clear_screen()


# Menus utilisateur
titre = " Bonjour, bienvenue dans le jeu du Simon numérique "
longueur = len(titre) + 4
print("*" * longueur)
print("* " + titre + " *")
print("*" * longueur)
print()

score_joueur = 0

while True:
    print("* Retenez cette séquence numérique *")
    print("------------------------------------")
    # Bloque l'affichage pendant 1 seconde
    time.sleep(1)
    print(sequence_nombres)
    time.sleep(3)
    clear_screen()

    rep_utilisateur = input("Votre réponse : ")
    if rep_utilisateur == sequence_nombres:
        print("Bonne réponse , vous marquez un point ")
        score_joueur += 1
    else:
        break

    chiffre = random.randint(0, 9)
    sequence_nombres += str(chiffre)
    clear_screen()

print("Dommage, ce n'est pas la bonne réponse")
print(f"La séquence était : {sequence_nombres}")
print(f"Votre score total est de : {score_joueur} points")
