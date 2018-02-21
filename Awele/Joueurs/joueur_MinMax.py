import sys
sys.path.append("../..")
import game

joueur = 0

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global joueur
	joueur = jeu[1]
	
	listc = jeu[2]
	
	scores = []
	
	for coup in listc:
	
		scores.append( simulation(6, game.getCopieJeu(jeu), coup))

		
	return listc[scores.index(max(scores))]
		
	
def saisieCoupSimu(jeu,profondeur):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global joueur
	
	listc = jeu[2]
	
	scores = []
	
	for coup in listc:
	
		scores.append( simulation(profondeur,game.getCopieJeu(jeu), coup))
		
		
	if jeu[1] == joueur:
				
		return max(scores)
			
	else:
		
		return min(scores)
	
def simulation(profondeur, jeu, coup):
	
	game.joueCoup(jeu,coup)

	if profondeur==0:
		return eval(jeu)
		
	valides = game.getCoupsValides(jeu)
	
	if game.finJeu(jeu):
	
		return eval(jeu)
	
	
	return saisieCoupSimu(jeu , profondeur-1)
	
def eval(jeu):

	return jeu[4][joueur-1]
	
