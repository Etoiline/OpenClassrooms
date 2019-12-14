#-*- coding:utf-8 -*-

""" Ce fichier contient des fonctions générales utilisées par le programme """

import os #module contenant les fonctions système
import sys #module pour interragir avec le système
import config
import select
from joueur import *


def lister_cartes_existantes (dossier_cartes) :

	""" Fonction qui liste es cartes existantes
	Retourne la liste des cartes """

	cartes=[] #liste de toutes les cartes
	for nom_fichier in os.listdir(dossier_cartes) :
		if nom_fichier.endswith(".txt"):
			cartes.append(nom_fichier)

	return cartes



def afficher_cartes (liste_cartes) :

	""" Fonction pour afficher plus joliment la liste des cartes """
	
	i=1
	for carte in liste_cartes :
		print ("{} - {}".format(i, carte))
		i+=1



def choisir_cartes (liste_cartes) :

	""" Fonction permettant de sélectionner un labyrinthe
	Retourne le numéro de la carte """
	
	carte = 0
	bool_saisie_carte = False
	while bool_saisie_carte==False :
		choix = input("Choisir un numéro de carte (1-"+str(len(liste_cartes))+") ou q pour quitter : ")
		if choix=="Q" or choix=="q" : #le serveur choisi de quitter
			print ("Vous avez choisi de quitter le jeu.")
			quitter_jeu()
		else :
			try :
				choix = int (choix)
			except Exception :
				print ("Erreur de saisie, recommencez.")
			else :
				if choix>0 and choix-1 < len(liste_cartes) :
					carte = choix-1
					bool_saisie_carte = True
				else : print ("Cette carte n'existe pas")
	return carte



def quitter_jeu (connexion_principale, joueurs) :

	""" Fonction quittant le jeu proprement
	en fermant toutes les connexions puis terminant le programme """

	# déconnexion des clients
	for joueur in joueurs:
		print("DEBUG  : quit")
		joueur.socket.close()

	# fermeture de la connexion
	connexion_principale.close()

	#on quitte le programme
	sys.exit()



def saisie_joueur (joueur) :

	""" Fonction qui s'occupe de récupérer la saisie du joueur
	Retourne la saisie quand celle ci est valide """
	
	msg_a_envoyer = "Que voulez-vous faire ?"
	joueur.socket.send(msg_a_envoyer.encode()) # envoie la demande au joueur
	choix_valide = False
	while not choix_valide :
		msg_recu = joueur.socket.recv(2014) #réponse du client
		msg_recu = msg_recu.decode()
		if config.regex_deplacement.match(msg_recu) is not None or config.regex_action.match(msg_recu) is not None or msg_recu.upper() == "Q":
			choix_valide = True
		else :
			msg_a_envoyer = "Erreur de saisie. Recommencez \n"
			joueur.socket.send(msg_a_envoyer.encode())
	return msg_recu




