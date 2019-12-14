#-*- coding:utf-8 -*-

"""Ce module contient la classe Labyrinthe.
Un labyrinthe est représenté par : 
- un Robot
- une grille
- des obstacles"""


import os #module système
import pickle
import random #module aléatoire

from robot import *

class Labyrinthe :

    def __init__(self):
        
        """ Constructeur du labyrinthe : il est composé d'un robot et d'une grille """
        
        self.robot_joueur = Robot()
        self.grille = {}



    def creerLabyrinthe (self, fichier_choisi) :

        """ Création du labyrinthe à partir du fichier choisi """

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
                            self.robot_joueur.moveRobot(no_ligne, no_colonne)
                            ligne = ligne.replace(str(self.robot_joueur.getSymbol()), " ")
                            break
                        no_colonne += 1
                self.grille[no_ligne] = ligne
                no_ligne+=1

        return sortie




    def __repr__(self) :

        """Fonction pour afficher le labyrinthe"""

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





    def placer_robot (self, joueurs):

        """Méthode permettant de générer une position aléatoire libre pour un nouveau joueur"""

        i = 0
        liste_cases_possibles = [] # Liste des espaces vides (Une liste de tuple(x,y))
        #print (self.grille)
        for ligne in self.grille :
            j = 0
            for case in self.grille[ligne] :
                if case == " ":
                    coordonnees = (i,j)
                    #On vérifie qu'il n'y a pas déjà un joueur sur cette case
                    place_libre = True
                    for joueur in joueurs :
                        if (joueur.x == i and joueur.y == j ) :
                            place_libre = False
                    #La case est libre pour acceuillir un joueur
                    if place_libre :
                        liste_cases_possibles.append(coordonnees)
                j += 1
            i += 1
        #Choix aléatoire de la case
        case_choisie = random.choice(liste_cases_possibles)

        return case_choisie[0], case_choisie[1]






    def generer_contenu(self, joueur_en_cours, joueurs):

        """Méthode permettant de générer le contenu du labyrinthe à envoyer à chaque client.
            On a choisi de représenter :
            - le robot du joueur en cours par un X
            - les autres robots par des x
            Ici, on part du principe que le joueur n'a pas besoin de savoir à qui sont précisément les autres robots."""

        contenu = ""
        i = 0
        for ligne in self.grille:
            new_line = ""
            j = 0
            for case in self.grille[ligne] :
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
            contenu+=new_line+"\n"
            i+=1
        return contenu



    def case_objectif (self, direction, x, y) :
    
        """ Méthode retournant la case qui est l'objectif du joueur """
        
        coordinates = []
        coordinates.append(x)
        coordinates.append (y)
        if direction.upper() == "N" :
            ligne = coordinates[0] - 1
            colonne = coordinates[1]
        elif direction.upper() == "S" :
            ligne = coordinates[0] + 1
            colonne = coordinates[1]
        elif direction.upper() == "E" :
            ligne = coordinates[0]
            colonne = coordinates[1]+1
        elif direction.upper() == "W" :
            ligne = coordinates[0]
            colonne = coordinates[1]-1
        return (ligne, colonne)



    def limites_deplacement (self, ligne, colonne) :
    
        """ Méthode permettant de voir si le déplacement reste dans les limites du labyrinthe"""

        hors_limite = False
        if ligne >= len(self.grille) or colonne >= len(self.grille[0]) or ligne == 0 or colonne == 0 :
            hors_limite = True
        return hors_limite




    def action_joueur (self, action, direction, joueur, joueurs) :
    
        """Méthode effectuant les action du joueur :
            - murer une porte
            - percer un mur"""
        
        print ("DEBUG : Action!")
        action_validee = 0
        ligne, colonne = self.case_objectif (direction, joueur.x, joueur.y)
        if (self.limites_deplacement(ligne, colonne)) == True :
            action_validee = 1
        elif (action.upper() == "M") and self.grille[ligne][colonne] == "." :
            tmp = list(self.grille[ligne])
            tmp[colonne] = "O"
            self.grille[ligne] = "".join(tmp)

        elif (action.upper() == "P") and self.grille[ligne][colonne] == "O" :
            tmp = list(self.grille[ligne])
            tmp[colonne] = "."
            self.grille[ligne] = "".join(tmp)

        else :
            action_validee = 1
        return action_validee



    def mise_a_jour_coordonnees_joueur (ligne, colonne) :
    
        """ Fonction qui mes à jour les coordonnées du joueur """

        print("DEBUG deplacement de ("+str(joueur.x)+","+str(joueur.y)+") vers ("+str(ligne)+","+str(colonne)+")")
        joueur.x = ligne
        joueur.y = colonne
    



    def deplacement_joueur (self, joueur, joueurs):
    
        """ Méthode pour déplacer le robot"""
        
        deplacement_validee = 0
        ligne = joueur.x
        colonne = joueur.y
        for i in range (0, joueur.pas) :
            ligne, colonne = self.case_objectif (joueur.direction, ligne, colonne)
        if self.limites_deplacement (ligne, colonne) == True :
            deplacement_validee = 1
        else :
            ligne, colonne = self.case_objectif (joueur.direction, joueur.x, joueur.y)
            print("DEBUG deplacement de ("+str(joueur.x)+","+str(joueur.y)+") vers ("+str(ligne)+","+str(colonne)+")")
            if self.grille[ligne][colonne] == " " or self.grille[ligne][colonne] == "." :
                #on déplace et on décrémente le pas
                joueur.x = ligne
                joueur.y = colonne
                joueur.pas -= 1
            elif self.grille[ligne][colonne] == "U" :
                deplacement_validee = 2
            else :
                print ("DEBUG : c'est un mur")
                deplacement_validee = 1
                joueur.pas = 0
        return deplacement_validee



