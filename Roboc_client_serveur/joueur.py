#-*- coding:utf-8 -*-

"""Ce module contient la classe Joueur. Un joueur est composé de :
    - des coorodnnées
    - des identifiants (IP, port)
"""


class Joueur:

    """Classe représentant un robot."""

    symbole = "X"
    nom = "robot"
    nombre = 0 #nombre de joueur



    def __init__(self, x, y, ip, port, socket, pas=0, direction=""):

        """ Initialise un nouveau joueur défini par sa position (x,y), ses coordonnées (ip, port).
        Le nombre de joueur est indrémenté à chaque fois.
        Le pas et la direction sont utilisés lors des déplacement multiples pour sauvegarder les choix du joueur. """

        self.x = x
        self.y = y
        self.ip = ip
        self.port = port
        self.socket = socket
        Joueur.nombre += 1
        self.pas = pas
        self.direction = direction


    def __repr__(self):
        return "Joueur {} x={} y={} > connecté depuis {}:{}".format(self.nombre, self.x, self.y, self.ip, self.port)


    def __str__(self):
        return "Joueur {} {},{} > connecté depuis {}:{}".format(self.nombre,self.x, self.y, self.ip, self.port)
