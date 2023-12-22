"""
- Oeufs à la coque : 3 minutes
- Oeufs mollets : 6 minutes
- Oeufs durs : 9 minutes

import time
time.sleep(1)
print(".", end="", flush=True)

d = 100
min = d//60 # division entière (pas de virgules)
sec = d-min*60

print(f"{min:02d}")

"""

# Import module
import time
import beepy

# Menus utilisateur
titre = " Le minuteur pour la cuisson des oeufs "
longueur = len(titre) + 4
print("*" * longueur)
print("* " + titre + " *")
print("*" * longueur)
print()
print("Choississez un temps de cuisson:")
print("--------------------------------")
print()
print("a) Oeuf à la coque => 3 minutes")
print("b) Oeuf mollets => 6 minutes")
print("c) Oeuf durs => 9 minutes")
print()

ATTENTE_CUISSON = 10

# Gestion erreur choix
while True:
    choix = input("Entrer votre choix : (a, b, c)")
    if choix == "a" or choix == "b" or choix == "c":
        break
    print("ERREUR: Vous devez choisir a, b ou c ")

# Gestion temps de cuisson
temps_cuisson = 0
if choix == "a":
    temps_cuisson = 3 * 60
    oeuf = "oeuf à la coque"
    print(f"Le temps d'attente est de : {temps_cuisson/60} minutes")
elif choix == "b":
    temps_cuisson = 6*60
    oeuf = "oeuf mollet"
    print(f"Le temps d'attente est de : {temps_cuisson/60} minutes")
else:
    temps_cuisson = 9*60
    oeuf = "oeuf durs"
    print(f"Le temps d'attente est de : {temps_cuisson/60} minutes")

# Affichage "." et transformation du temps
while True:
    for i in range(ATTENTE_CUISSON):
        time.sleep(1)
        print(".", end="", flush=True)
        temps_cuisson -= 1
        if temps_cuisson <= 0:
            break
    if temps_cuisson <= 0:
        break

    minute = temps_cuisson // 60
    seconde = temps_cuisson - minute * 60
    print()
    print(f"Temps restant avant dégustation : {minute:01d} minutes et {seconde:02d} secondes")
    print(end="", flush=True)
print()
print(f"La cuisson de votre {oeuf} est terminé , bonne appétit !")
beepy.beep(sound="ping")



