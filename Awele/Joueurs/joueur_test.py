import sys
sys.path.append("../..")
import game
import random

precedent = [6,6]

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	listc = jeu[2]
	global precedent
	
	n = random.randint(0,len(listc)-1)
	
	while listc[n][1] == precedent[1]+1 and len(listc) > 1:
	
		n = random.randint(0,len(listc)-1)
		
	precedent = listc[n]
	return listc[n]
	
