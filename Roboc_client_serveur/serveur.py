#-*- coding:utf-8 -*-

""" Ce fichier contient la partie serveur du programme """

import socket
import select
import re #module pour les expressions régulières
import sys #module pour les actions système
from joueur import *
from labyrinthe import *
import time #module pour la gestion du temps
import config as cfg #module contenant les variables de configuration
import utils


###### Variables générales ######
regex_deplacement = cfg.regex_deplacement
regex_action = cfg.regex_action
hote = cfg.hote
port = cfg.port

###### Variable locales ######
bool_quitter_labyrinthe = False
labyrinthe_en_cours = Labyrinthe () #Création de l'objet
joueurs = []



###### Choix du labyrinthe ######

cartes=utils.lister_cartes_existantes(cfg.dossier_cartes) #liste de tous les labyrinthes
utils.afficher_cartes (cartes) #affichage des labyrinthes
carte = utils.choisir_cartes(cartes) #choix de l'utilisateur
labyrinthe_en_cours.creerLabyrinthe(cartes[carte]) #On remplit l'objet lbyrinthe


###### Création de la connexion et attente des clients ######

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    connexion_principale.bind((hote, port))
except socket.error:
    print("Problème de liaison avec le port")
    sys.exit()

connexion_principale.listen(5)
print("Le serveur écoute sur le port {}".format(port))



commencer = False
clients_connectes = []

# Attente des clients
while not commencer:

    # On récupère les connexions avec select
    connexions_demandees, wlist, xlist = select.select([connexion_principale],[],[],0.03)
    
    for connexion in connexions_demandees:
        connexion_client, (ip, port) = connexion.accept()
        #on ajoute le socket connecté à la liste des clients
        clients_connectes.append(connexion_client)
        # On vérifie que le client n'a lancé qu'une connexion
        nouveau_client = True
        for joueur in joueurs:
            if joueur.ip == ip and joueur.port == port:
                nouveau_client = False
        # Si c'est un nouveau connecté, on l'ajoute au labyrinthe
        if nouveau_client :
            x, y = labyrinthe_en_cours.placer_robot(joueurs)
            joueurs.append (Joueur(x,y,ip,port,connexion_client))
            
            print("{} joueur(s) connecté(s)".format(Joueur.nombre))
            # On informe tous les joueurs selectionnés de l'arrivée du nouveau
            for joueur in joueurs:
                msg_a_envoyer = "Bienvenue, Joueur {} \n".format(joueurs.index(joueur))
                joueur.socket.send(msg_a_envoyer.encode())
                msg_a_envoyer = labyrinthe_en_cours.generer_contenu(joueur, joueurs)
                joueur.socket.send(msg_a_envoyer.encode())
                # Si le nombre de joueur est > 1, on peut commencer la partie si quelqu'un saisie "C"
                if Joueur.nombre > 1:
                    msg_a_envoyer = "\nEntrez C pour commencer a jouer :\n"
                    joueur.socket.send(msg_a_envoyer.encode())


    # On récupère à partir des connexions acceptées la liste
    # des connexion à lire (Ceux qui on envoyé un message au serveur)
    liste_clients = []
    try:
        liste_clients, wlist, xlist = select.select(clients_connectes,[],[],0.03)
    except select.error:
        pass
    else:
        for client in liste_clients:
            msg_recu = client.recv(1024)
            msg_recu = msg_recu.decode()
            # Si le joueur est seul
            if Joueur.nombre < 2:
                msg_a_envoyer = "En attente des joueurs"
                client.send(msg_a_envoyer.encode())
            # Si le nombre de  joueurs est > 1 et que quelqu'un saisi "C", on commence la partie
            elif msg_recu.upper() == "C":
                commencer = True
                print("La partie commence et est en cours...") #Coté serveur
                break
            else : # Erreur de saisie
                msg_a_envoyer = "Saisie invalide. reprenez !"
                client.send(msg_a_envoyer.encode())
        # La partie commence, on informe les joueurs selectionnés
        if commencer:
            for joueur in joueurs:
                msg_a_envoyer = "Début de la partie\n"
                joueur.socket.send(msg_a_envoyer.encode())
                msg_a_envoyer = labyrinthe_en_cours.generer_contenu(joueur, joueurs)
                joueur.socket.send(msg_a_envoyer.encode())
                msg_a_envoyer = "Attendez votre tour\n"
                joueur.socket.send(msg_a_envoyer.encode())
            # On ne prend plus de joueurs on sort de la boucle while
            break





###### La partie commence et finit lorsqu'un joueur trouve la sortie ######

bool_sortie = False

reprise_deplacement = False
nb_joueurs = len(joueurs)
no_joueur = 0 
retour_deplacement = 0


while not bool_sortie :
    # On récupère le joueur dont c'est le tour
    joueur = joueurs[no_joueur]
    deplacement_effectue = False
    
    print ("DEBUG : c'est au joueur {} de jouer".format(no_joueur))


    while not deplacement_effectue :
        if joueur.pas > 0 : # reprise du déplacement précédent
            print ("DEBUG : on continue ")
            retour_deplacement = labyrinthe_en_cours.deplacement_joueur(joueur, joueurs)
            if retour_deplacement == 2 :
                bool_sortie = True
                break
            elif retour_deplacement == 0 :
                print ("DEBUG : avance encore ")
                deplacement_effectue = True
                no_joueur = (no_joueur+1)%len(joueurs)
                break

        msg_joueur = utils.saisie_joueur(joueur)


        if msg_joueur.upper() == "Q":
            if len(joueurs) == 2 : #S'il n'y avait que 2 joueurs la partie s'arrête
                no_joueur = (no_joueur+1)%len(joueurs)
                bool_sortie = True
                break
            else : # Sinon on supprime le joueur de la liste et on met à jour le numéro du tour
                msg_a_envoyer = "Vous quittez la partie\n"
                joueur.socket.send(msg_a_envoyer.encode())
                # Pour éviter une déconnexion brutale delai de 2 secondes
                tps=time.time()
                while time.time() - tps < 2:
                    pass
                # On ferme son socket
                joueur.socket.close()
                joueur.port = 0
                # On iinforme les autres joueurs
                for autre_joueur in joueurs :
                    msg_a_envoyer = "Le joueur {} vient de quitter la partie\n".format(joueur.no_joueur)
                    autre_joueur.socket.send(msg_a_envoyer.encode())
                    msg_a_envoyer = labyrinthe_en_cours.generer_contenu(autre_joueur)
                    autre_joueur.socket.send(msg_a_envoyer.encode())
                # On attend un délai de 2 sécondes pour passer au tour suivant
                tps=time.time()
                while time.time() - tps < 2:
                    pass
                joueurs.remove(joueur)
                no_joueur = (no_joueur+1)%len(joueurs)
                retour_joueur = True
            

        #Les actions des joueurs
        elif regex_action.match(msg_joueur) is not None :
            action = regex_action.search(msg_joueur).group(1)
            direction = regex_action.search(msg_joueur).group(2)
            retour_action = labyrinthe_en_cours.action_joueur (action, direction, joueur, joueurs)
            if retour_action == 0 :
                deplacement_effectue = True
                for chaque_joueur in joueurs:
                    msg_a_envoyer = labyrinthe_en_cours.generer_contenu(chaque_joueur, joueurs)
                    chaque_joueur.socket.send(msg_a_envoyer.encode())
                no_joueur = (no_joueur+1)%len(joueurs)


        else :
            direction = regex_deplacement.search(msg_joueur).group(1)
            pas = regex_deplacement.search(msg_joueur).group(2) or "1"
            print ("DEBUG : deplacement vers "+direction)
            print ("DEBUG : pas vers "+pas)
            joueur.direction = direction
            joueur.pas = int(pas)
            deplacement_retour = labyrinthe_en_cours.deplacement_joueur(joueur, joueurs)
            print("DEBUG : retour deplacement : "+str(deplacement_retour))
            if deplacement_retour == 2 :
                bool_sortie = True
                deplacement_effectue = True
                break
            elif deplacement_retour == 0 :
                deplacement_effectue = True
                for chaque_joueur in joueurs:
                    msg_a_envoyer = labyrinthe_en_cours.generer_contenu(chaque_joueur, joueurs)
                    chaque_joueur.socket.send(msg_a_envoyer.encode())
                    print ("labyrinthe envoyé")
                no_joueur = (no_joueur+1)%len(joueurs)
            else :
                deplacement_effectue = False
    
        print("DEBUG : fin tour "+str(no_joueur))
        # On affiche pour tous le nouvel état du labyrinthe suite au déplacement récent du joueur dont c'était le tour


print("DEBUG : ON EST SORTI")



###### Fin de la partie ######
joueur_vainqueur = joueurs[no_joueur]

# On informe tous les joueurs que la partie est finie
for joueur in joueurs:
    print("DEBUG : Envoi essage de fin")
    if joueur.ip != joueur_vainqueur.ip or joueur.port != joueur_vainqueur.port:
        msg_a_envoyer = "Le joueur {} a gagné. Vous avez perdu !\n".format(no_joueur)
        joueur.socket.send(msg_a_envoyer.encode())
    else :
        msg_a_envoyer = "Bravo, vous abez gagné !\n"
        joueur.socket.send(msg_a_envoyer.encode())
    msg_a_envoyer = "La partie est finie. Vous allez être déconnecté."
    joueur.socket.send(msg_a_envoyer.encode())

# On attent 3 secondes
tps=time.time()
while time.time() - tps < 3 :
    pass


utils.quitter_jeu(connexion_principale, joueurs)


