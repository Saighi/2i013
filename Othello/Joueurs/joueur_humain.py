import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer
	"""
	listc = jeu[2]
	n = 0
	print(" Coup possible :"+str(jeu[2])+"\n")
	
	for coup in listc:
	
		print("coup "+ str(n) + " x = " + str(coup[0]) + " y = " + str(coup[1]) + "\n")
		
		n += 1
		
	
	n = int(input("Quel coup choisissez vous : "))
	
	while n < 0 or n >len(listc):
	
		n = int(input("Quel coup choisissez vous : "))
		
	return listc[n]
	
