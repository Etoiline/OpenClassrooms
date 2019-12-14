#-*- coding:utf-8 -*-

import socket # module de gestion des connexions
import threading # module de gestion des threads
import time
import sys


###### Definition de 2 Threads : envoi et reception ######

class Recevoir(threading.Thread):
	
	""" Thread pour la réception des messages"""
	
	def __init__(self, connexion):
		threading.Thread.__init__(self)
		self.connexion = connexion

	def run(self):
		while True:
			try:
				msg_recu = self.connexion.recv(1024)
			except socket.error:
				print("Vous êtes déconnecté du serveur")
				break
			else:
				msg_recu = msg_recu.decode()
				print(msg_recu)
		tps=time.time()
		while time.time() - tps < 3 :
			pass
		self.connexion.close()
		sys.exit()



class Envoyer(threading.Thread):
	
	""" Thread pour l'émission des messages"""
	
	def __init__(self, connexion):
		threading.Thread.__init__(self)
		self.connexion = connexion

	def run(self):
		while True:
			try:
				msg_a_envoyer = input()
			except socket.error:
				print("Vous êtes déconnecté du serveur")
			else:
				self.connexion.send(msg_a_envoyer.encode())
				if msg_a_envoyer.upper() == "Q":
					break
		tps=time.time()
		while time.time() - tps < 3 :
			pass
		self.connexion.close()
		sys.exit()




###### Programme principal du client : Connexion avec le serveur ######

hote = "localhost"
port = 65000

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

# dialogue avec le serveur
thread_envoi = Envoyer(connexion_avec_serveur)
thread_reception = Recevoir(connexion_avec_serveur)  

thread_reception.start()
thread_envoi.start()

thread_reception.join()
thread_envoi.join()
