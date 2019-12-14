#-*- coding:utf-8 -*-

"""Ce module contient la classe Robot.
Un robot est représenté par : 
- un symbole
- ses coordonnées"""

class Robot :
    
    def __init__(self) :
        self.symbol = "X"
        self.coordinates = [0,0]



    def setSymbol (new_symbol) :
    
        """ Fonction permettant de chqnger le sy;bole du robot """

        self.symbol = new_symbol



    def moveRobot (self, new_line, new_column) :
    
        """ Fonction qui met à jour les coordonnées du robot """
        
        self.coordinates[0] = new_line
        self.coordinates[1] = new_column



    def getSymbol (self) :
        
        """ Retourne le symbole du robot """
        
        return (self.symbol)



    def deplacement (self, direction) :
    
        """ Fonction qui retourne les nouvelles coordonnées après un déplacement du robot """

        if direction == "n" : #nord
            ligne = self.coordinates[0] - 1
            colonne = self.coordinates[1]
        elif direction == "s" : #sud
            ligne = self.coordinates[0] + 1
            colonne = self.coordinates[1]
        elif direction == "e" : #est
            ligne = self.coordinates[0]
            colonne = self.coordinates[1]+1
        elif direction == "w" : #ouest
            ligne = self.coordinates[0]
            colonne = self.coordinates[1]-1
        return (ligne, colonne)



