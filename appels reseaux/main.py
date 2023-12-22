# FAIRE DES APPELS RÉSEAU AVEC REQUESTS
#
# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html

import requests 

reponse1 = requests.get("https://codeavecjonathan.com/res/programmation.txt")

if reponse1.status_code   == 200:
  reponse1.encoding = "utf-8"
  print(reponse1.text)
  print(reponse1.status_code)
else:
  print ("ERREUR code : " + str(reponse1.status_code))
