"""Ce module contient la classe Robot.
Un robot est représenté par : 
- un symbole
- ses coordonnées"""

class Robot :
    
    def __init__(self) :
        self.symbol = "X"
        self.coordinates = [0,0]

    def setSymbol (new_symbol) :
        self.symbol = new_symbol

    def moveRobot (self, new_line, new_column) :
        self.coordinates[0] = new_line
        self.coordinates[1] = new_column

    def getSymbol (self) :
	    return (self.symbol)

    def deplacement (self, direction) :
        if direction == "n" :
            ligne = self.coordinates[0] - 1
            colonne = self.coordinates[1]
        elif direction == "s" :
            ligne = self.coordinates[0] + 1
            colonne = self.coordinates[1]
        elif direction == "e" :
            ligne = self.coordinates[0]
            colonne = self.coordinates[1]+1
        elif direction == "w" :
            ligne = self.coordinates[0]
            colonne = self.coordinates[1]-1
        return (ligne, colonne)



