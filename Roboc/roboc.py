import os
import re
from labyrinthe import *

from robot import *

###VARIABLES###
dossier_cartes = "cartes"
bool_saisie_carte = False
bool_quitter_labyrinthe = False
labyrinthe_en_cours = Labyrinthe ()
regex = re.compile (r"^([nsweNSWE])(\d*)$")
bool_sortie = False
bool_continuer_partie = False



#TODO : traiter le cas de quitter



#Choix du fichier
cartes=[] #liste de toutes les cartes
i=1
for nom_fichier in os.listdir(dossier_cartes) :
	cartes.append(nom_fichier)
	print ("{} - {}".format(i, nom_fichier))
	i+=1

#Le joueur fait son choix
while bool_saisie_carte==False :
    choix = input("Choisir un numéro de carte (1-"+str(i-1)+") ou q pour quitter : ")
    if choix=="Q" or choix=="q" :
        bool_quitter_labyrinthe = True
        bool_saisie_carte = True
    else :
        try :
            choix = int (choix)
        except Exception :
            print ("Erreur de saisie, recommencez.")
        else :
            if choix>0 and choix-1 < len(cartes) :
                if cartes[choix-1] == "partie_en_cours" :
                    bool_continuer_partie = True
                partie_choisie = cartes[choix-1]
                bool_saisie_carte = True
            else : print ("Cette carte n'existe pas")

print (cartes[choix-1])
#on ouvre le fichier
if bool_continuer_partie==False :
    labyrinthe_en_cours.creerLabyrinthe(nom_fichier)
else :
    labyrinthe_en_cours.importer_labyrinthe()



#Afficher le labyrinthe
print (labyrinthe_en_cours)


while bool_quitter_labyrinthe == False and bool_sortie == False:
    choix=input(">")
    if choix=="Q" or choix=="q" :
        bool_quitter_labyrinthe = True
    elif regex.match(choix) is None :
        print ("Erreur de saiaie \n")
    else :
        direction = regex.search(choix).group(1)
        pas = int(regex.search(choix).group(2) or 1)
        deplacement_autorise = True
        ligne_old = labyrinthe_en_cours.robot_joueur.coordinates[0]
        colonne_old = labyrinthe_en_cours.robot_joueur.coordinates[1]
        while pas > 0 :
            nouvelle_ligne, nouvelle_colonne = labyrinthe_en_cours.robot_joueur.deplacement(direction)
            nouveau_symbole = labyrinthe_en_cours.grille[nouvelle_ligne][nouvelle_colonne]
            if nouveau_symbole == "O" :
                print ("Les murs ne sont pas là pour décorer")
                deplacement_autorise = False
                break
            elif nouveau_symbole == "U" and pas > 1 :
                print ("Vous êtes hors limites")
                deplacement_autorise = False
                break
            elif nouveau_symbole == "U" and pas == 1 :
                print ("GG : vous êtes sortis !")
                bool_sortie = True
            else :
                labyrinthe_en_cours.robot_joueur.moveRobot(nouvelle_ligne , nouvelle_colonne)
            pas-=1
        if deplacement_autorise == True :
            print (labyrinthe_en_cours)
            labyrinthe_en_cours.sauvegarderLabyrinthe()
        else :
            labyrinthe_en_cours.robot_joueur.moveRobot(ligne_old, colonne_old)





