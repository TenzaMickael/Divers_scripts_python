# Importe le module random pour générer des nombre aléatoire
import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0

    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")

        try:
            nombre_int = int(nombre_str)
        except ValueError:
            print("ERREUR:Vous devez rentrer un nombre. Réessayer")
        # Pose la limite du nombre min et max rentrer par l'utilisateur
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit etre entre {nb_min} et {nb_max}. Réessayer")
                # On force a reboucler pour eviter de tomber dans le bloc de condition
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
# Execute le module random pour générer un nombre aléatoire
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

# AVEC BOUCLE WHILE
"""nombre = 0
vies = NB_VIES

while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -= 1
    else:
        print("Le nombre magique est plus grand")
        vies -= 1

if vies == 0:
    print(f"Vous avez perdu! Le nombre magique était : {NOMBRE_MAGIQUE}")"""

# AVEC BOUCLE FOR
gagne = False

for i in range(0, NB_VIES):
    vies = NB_VIES - i
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
        gagne = True
        # Pour sortir de la boucle
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Le nombre magique est plus grand")

# if vies == 0:
if not gagne:
    print(f"Vous avez perdu! Le nombre magique était : {NOMBRE_MAGIQUE}")
