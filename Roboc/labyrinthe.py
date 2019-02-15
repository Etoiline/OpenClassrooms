"""Ce module contient la classe Labyrinthe.
Un labyrinthe est représenté par : 
- un Robot
- une grille
- des obstacles"""
import os
import pickle

from robot import *
#import robot
from obstacles import *

class Labyrinthe : 

    def __init__(self):
        self.robot_joueur = Robot()
        self.grille = {}

    
    
    def creerLabyrinthe (self, fichier_choisi) :
        #Cette fonction permet de créer un labyrinthe à partir d'une carte au format txt
        contenu=""
        carte_trouvee=False
        sortie = 0
        
        #Recuperation de la carte choisir ('nom_carte')
        chemin = os.path.join("cartes", fichier_choisi)
        with open(chemin,'r') as fichier :
	        contenu = fichier.read()
	        carte_trouvee=True
	    #Si la carte n'a pas été trouvée ou si le fichier est vide.
        if carte_trouvee == False :
	        print ("La carte n'a pas été trouvée")
	        sortie = 1
        elif contenu=="" :
	        print ("Problème de lecture du fichier")
	        sortie = 1
        else : 
	        #On construit la grille
            liste_lignes = contenu.split("\n")
            no_ligne = 0
            ligne_correcte=True
            for ligne in liste_lignes:
		        #On vérifie que les symboles utilisés dans le fichier sont autorisés
		        #On pourrait trouver un moyen de vérifier que la carte est un labyrinthe bien formé : le labyrinthe est entouré de murs ou de sorties, il existe une solution, il n'y a qu'un seul robot ...
                #La on se contente de chercher le robot et de remplir la grille en supprimant le robot (ses coordonnées seront stockées à part, là c'est juste la grille du jeu)
                if (str(self.robot_joueur.getSymbol()) in ligne) :
                    no_colonne = 0
                    for case in ligne :
                        if case == self.robot_joueur.getSymbol() :
                            print("robot trouve")
                            self.robot_joueur.moveRobot(no_ligne, no_colonne)
                            ligne = ligne.replace(str(self.robot_joueur.getSymbol()), " ")
                            print (self.robot_joueur.coordinates[0], self.robot_joueur.coordinates[1])
                            break
                        no_colonne += 1
                self.grille[no_ligne] = ligne
                no_ligne+=1

        return sortie


    def importer_labyrinthe(self) :
        sortie = 1
        #labyrinthe_charge = Labyrinthe()
        fichier = os.path.join("cartes", "partie_en_cours")
        with open(fichier,"rb") as fichier_partie_sauvee:
            mon_depickler = pickle.Unpickler(fichier_partie_sauvee)
            lab_charge = mon_depickler.load()
            self.robot_joueur = lab_charge.robot_joueur
            self.grille = lab_charge.grille
            sortie = 0
        return sortie


            

    def __repr__(self) :
        #Fonction pour afficher le labyrinthe
        #Ne pas oublier le robot !!!!
        affichage="\n\n"
        for ligne in self.grille :
            if ligne == self.robot_joueur.coordinates[0] :
                new_line =self.grille[ligne][:self.robot_joueur.coordinates[1]]+"X"+self.grille[ligne][self.robot_joueur.coordinates[1]+1:]
                affichage+=new_line+"\n"
            else :
                affichage+=self.grille[ligne]+"\n"
            ligne +=1
        return (affichage)


    def sauvegarderLabyrinthe (self) :
        fichier = os.path.join ("cartes", "partie_en_cours")
        with open (fichier, "wb") as fichier_partie_en_cours :
            mon_pickler = pickle.Pickler(fichier_partie_en_cours)
            mon_pickler.dump(self)

