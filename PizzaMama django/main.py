# Installer django => pip install django puis django-admin startproject pizzamama

# Lancer le projet ⇒ se placer dans le projet et faire : python(3) manage.py runserver

# Créer application menu pizzamama => python manage.py startapp menu

# Aller dans menu et model pour créer modele de pizza

# Il faut enregistrer l'application au niveau du projet (dans le settings.py) ⇒ dans INSTALLED_APPS' ajouter =>
# menu.apps.MenuConfig',

# Faire une migration ⇒ python manage.py makemigrations et crée un nouveau fichier dans menu / migration et 0001_initial

# Appliquer la modification à la base de donnée ⇒ python manage.py migrate ⇒ changement dans db. SQLite

# Installer sqlitebrowser pour voir la base de donnée ⇒ sudo dnf install sqlitebrowser

# Interface admin => http://127.0.0.1:8000/admin

# créer utilisateur base de donéée ⇒ python manage.py createsuperuser

# Ajouter pizza => menu / admin.py et taper:
# from .models import Pizza
# python manage.py createsuperuser

# changer langue admin => settings.py => middleware => en dessous de sessionmiddleware => ajouter =>
# 'django.middleware.locale.LocaleMiddleware'

# Ajouter une pizza dans l'interface admin ensuite faire enregistrer et ajouter un nouveau

# Ameliorer interface admin (afficher nom pizzas) : dans models =>
# def __str__(self):
#         return self.nom
# Dans admin (afficher autre infos) =>
# class PizzaAdmin(admin.ModelAdmin):
#       list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
#       search_fields = ['nom']
# et rajouter : admin.site.register(Pizza, PizzaAdmin)

# Configurer la vue ⇒ aller dans views :
# from django.http import HttpResponse
# def index(request):
# return HttpResponse("Les pizzas")

# Dans menu créer nouveau fichier urls.py
# Y mettre :
# from . import views
# urlpatterns = [
#     path('', views.index, name="index"),
# ]

# Modifier le fichier urls.py de pizzamama en mettant:
# from django.contrib import admin
# from django.urls import path, include
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('menu/', include('menu.urls'))
# ]

# Récupérer la lise des pizzas :
# Aller dans views.py :
# from .models import Pizza
# def index(request):
#     pizzas = Pizza.objects.all()
#     pizzas_names = [pizza.nom for pizza in pizzas]
#     pizzas_names_str = ", ".join(pizzas_names)
#     return HttpResponse(f"Les pizzas : {pizzas_names_str} ")

# Creer un template :
# un crer un nouveau dossier appeller templates et dans ce dossier un nouveau dossier appeller menu
# Dans ce dossier un nouveau fichier index.html
# Pour lier le fichier HTML : aller dans view et faire :
# from django.shortcuts import render
# def index(request):
# return render(request, 'menu/index.html')

# Passer les donées des pizzza au html :
# dans view rajouter :
#    pizzas = Pizza.objects.all()
#    return render(request, 'menu/index.html', { 'pizzas': pizzas})
# Ajouter dans le html :
# <ul>
#     {% for pizza in pizzas %}
#     <li>{{pizza.nom}} : {{pizza.prix}}€</li>
#
#     {% endfor %}
#
# </ul>

# Créer réprteoire static pour mettre les images et les feuilles de style

# Importer feuille de style
# Dans html :
# {% load static %}
# <link rel="stylesheet" href="{% static 'menu/style.css' %}">

# Trier les pizza par prix 
# Aller dans view : 
# pizzas = Pizza.objects.all().order_by('prix')