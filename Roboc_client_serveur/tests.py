#-*- coding:utf-8 -*-

"""Module de tests unitaires pour le jeu de labyrinthe"""

import random # Module pour faire du pseudo aléatoire
import re # Module pour la gestion des expressions regulières
import unittest
import socket


from joueur import Joueur
import utils
from labyrinthe import Labyrinthe



###### Classe de test pour le module utils ######

class UtilsTest(unittest.TestCase):

	""" Test des fonctions dans le fichier utils """

	def test_lister_cartes_existantes(self):

		""" Teste la fonction 'lister_cartes_existantes' """

		# Construction manuelle d'une liste de 2 cartes situées dans le dossier 'cartes'

		liste_cartes = []

		nom1 = "facile.txt"
		nom2 = "prison.txt"
		liste_cartes.append(nom1)
		liste_cartes.append(nom2)
		
		# Construction de la liste avec la fonction à tester
		liste_obtenue = utils.lister_cartes_existantes("cartes")

		# Tester si les deux listes(ici les noms) sont les mêmes
		for carte in liste_obtenue:
			self.assertIn(carte,liste_cartes)



	
	def test_choisir_cartes(self):

		""" Teste la fonction 'choisir_cartes' """

		# Construction manuelle d'une liste de 3 cartes situées dans le dossier 'cartes'

		liste_cartes = []

		nom1 = "facile.txt"
		nom2 = "prison.txt"
		liste_cartes.append(nom1)
		liste_cartes.append(nom2)

		liste_numeros = [0,1,"q", "Q"]

		# récupération du résultat de la fonction
		numero_obtenu = utils.choisir_cartes(liste_cartes)

		# Ce numéro est t-il valide ?
		self.assertIn(numero_obtenu, liste_numeros)




###### Classe de test pour le module Labyrinthe ######

class LabyrintheTest(unittest.TestCase):

	""" Teste les fonctionnalités du Labyrinthe """

	#################################################

	def test_placer_robot(self):

		""" Teste la fonction 'placer_robot'
			Cette méthode génère une positive libre pour un robot
		"""
		
		# On réalise l'opération manuellement sur une carte
		nom_fichier = random.choice(["facile","prison"])
		labyrinthe_jeu = Labyrinthe()
		labyrinthe_jeu.creerLabyrinthe(nom_fichier+".txt")

		i = 0
		liste_vides = []
		for ligne in labyrinthe_jeu.grille :
			j = 0
			liste_ligne = []
			for caractere in labyrinthe_jeu.grille[ligne]:
				if caractere == " ":
					liste_vides.append((i,j))
				j += 1 
			i += 1 

		joueurs = []
		# On réalise l'opération via la méthode à tester
		labyrinthe_jeu = Labyrinthe()
		labyrinthe_jeu.creerLabyrinthe(nom_fichier+".txt")
		(x,y) = labyrinthe_jeu.placer_robot(joueurs)
		#la position obtenue est t-elle dans la liste des positions libres manuellement trouvées ?
		self.assertIn((x,y),liste_vides)



	#################################################

	def test_generer_contenu(self):

		""" Teste la fonction 'generer_contenu' 
			
			Cette méthode de la classe Labyrinthe permet de
			générer un affichage personnalisé du Labyrinthe
			sur l'interface d'un joueur :
			- Son robot apparait en grand X
			- les autres robots en petit x

		"""
		
		# On réalise l'opération manuellement sur une carte
		nom_fichier = random.choice(["facile","prison"])
		labyrinthe_jeu = Labyrinthe()
		labyrinthe_jeu.creerLabyrinthe(nom_fichier+".txt")
		joueurs=[]

		x1,y1 = labyrinthe_jeu.placer_robot(joueurs)
		socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip1 = 'localhost'
		port1 = 12345
		joueur1 = Joueur(x1,y1,ip1,port1,socket1)
		joueurs.append(joueur1)

		x2,y2 = labyrinthe_jeu.placer_robot(joueurs)
		socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip2 = 'localhost'
		port2 = 12348
		joueur2 = Joueur(x2,y2,ip2,port2,socket2)
		socket1.close()
		socket2.close()
		joueurs.append(joueur2)

		joueur_en_cours = joueurs[0]
		contenu_joueur1 = ""
		i = 0
		for ligne in labyrinthe_jeu.grille:
			new_line = ""
			j = 0
			for case in labyrinthe_jeu.grille[ligne] :
				bool_joueur_trouve = False
				for joueur in joueurs :
					if (joueur.x == i) and (joueur.y == j):
						if (joueur == joueur_en_cours) :
							new_line += "X"
						else :
							new_line +="x"
						bool_joueur_trouve = True
				if bool_joueur_trouve == False :
					new_line+=case
				j+=1
			contenu_joueur1+=new_line+"\n"
			i+=1
		
		#ligne = ("").join(ligne) # On reconstruire la chaine à afficher à partir de la liste
		#contenu_genere_pour_joueur1 += ligne

    	# On réalise l'opération via la méthode à tester
		contenu_fonction = labyrinthe_jeu.generer_contenu(joueur1, joueurs)
		# On test si les deux contenu obtenu sont idententiques
		self.assertEqual(contenu_fonction,contenu_joueur1)



	#################################################

	def test_deplacement_joueur(self):

		""" Teste la fonction 'deplacement_joueur'

			Cette méthode retourne un entier :
			- 0 : déplacement effectué
			- 1 : le déplacement a échoué (mur, hors limites, ...)
			- 2 : le joueur a trouvé la sortie
		"""
		

		nom_fichier = random.choice(["facile","prison"])
		labyrinthe_cree = Labyrinthe()
		labyrinthe_cree.creerLabyrinthe(nom_fichier+".txt")
		
		joueurs = []
		x1,y1 = labyrinthe_cree.placer_robot(joueurs)
		socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip1 = 'localhost'
		port1 = 12345
		joueur1 = Joueur(x1,y1,ip1,port1,socket1)
		joueurs.append(joueur1)

		x2,y2 = labyrinthe_cree.placer_robot(joueurs)
		socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip2 = 'localhost'
		port2 = 12348
		joueur2 = Joueur(x2,y2,ip2,port2,socket2)
		joueurs.append(joueur2)
		socket1.close()
		socket2.close()
		num_tour = random.randint(0,1)

		# Cas 1 : déplacement Nord, Sud, Est, Ouest sans pas (donc pas = 1)
		msg_recu = random.choice(['N','S','W','E'])
		joueur1.direction = msg_recu
		joueur2.direction = msg_recu
		joueur = joueurs[num_tour]
		retour = labyrinthe_cree.deplacement_joueur(joueur, joueurs)
		self.assertIn(retour,[0,1,2])

"""
		# Cas 2 : déplacement Nord, Sud, Est, Ouest avec précision du pas et p >= 1
		pas = random.randint(1,30)
		Np = "N"+ str(pas)
		Sp = "S"+ str(pas)
		Op = "O"+ str(pas)
		Ep = "E"+ str(pas)
		sg_recu = random.choice([Np,Sp,Op,Ep])
		fin, msg_a_envoyer = carte_obtenue.labyrinthe.deplacer_robot(num_tour,msg_recu)
		self.assertIn(fin,[True, False])
		self.assertIn(msg_a_envoyer,Labyrinthe.MSG.values())

		# Cas 3 : Murer(M) une porte ou Trouer(P) un mur
		pas = random.choice(['MN','MS','MO','ME','PN','PS','PO','PE'])
		fin, msg_a_envoyer = carte_obtenue.labyrinthe.deplacer_robot(num_tour,msg_recu)
		self.assertIn(fin,[True, False])
		self.assertIn(msg_a_envoyer,Labyrinthe.MSG.values())
"""



###### Si on exécute direcetement ce fichier ######

if __name__ == "__main__":

	unittest.main()




