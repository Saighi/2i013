import sys
sys.path.append("../..")
import game
import random
import time

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	
	TimeDebut= time.time()
	
	while True:
	
		TimeFin=time.time()
	
		if TimeFin - TimeDebut > 0.5:
			break"""
			
	listc = jeu[2]
	
	n = random.randint(0,len(listc)-1)
	
	
		
	return listc[n]
	
