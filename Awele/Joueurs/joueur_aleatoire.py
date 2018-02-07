import sys
sys.path.append("../..")
import game
import random

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	listc = jeu[2]
	
	n = random.randint(0,len(listc)-1)
	
	
		
	return listc[n]
	
