# Si probleme d'import installer : python3-tkinter
# Importer un module
import turtle

# On crée un objet
t = turtle.Turtle()


# Faire avancer la tortue de 100px
# t.forward(100)
# Tourne de 90°
# t.left(90)
# Avance de 50
# t.forward(50)
# Recule de 100
# t.backward(100)
# Tourne de 45°
# t.right(45)
# Avance de 200px
# t.forward(200)

# Exercice : Faire un escalier de 5 marches de 30px sur 30 px
# def escalier(taille, nb):
# for i in range(0, nb):
# t.forward(taille)
# t.left(90)
# t.forward(taille)
# t.right(90)
# modifier la taille des marches a chaque tour de boucle (décrémenter)
# taille -= 10
# t.forward(taille)
# escalier(60, 5)

# Exercice: Faire un carré et en parametre la taille avec une boucle for

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


# carre(100)

# Exercice: Faire des carrées de différente taille, en faisant une fonction carres et en parametre taille_depart et
# le nombre de carrés a faire Garder la fenetre active de turtles

def carres(taille_depart, nb_carres):
    for i in range(0, nb_carres):
        taille = (i + 1) * taille_depart
        carre(taille)


carres(10, 10)

turtle.done()
