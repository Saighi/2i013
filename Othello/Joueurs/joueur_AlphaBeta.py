import sys
sys.path.append("../..")
import game

joueur = 0
precedent = 0

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global joueur
	joueur = jeu[1]
	
	maxi=-10000
	imax=0
	
	for i in range(len(jeu[2])):
	
		score = saisieCoupSimuMin(2, game.getCopieJeu(jeu), jeu[2][i])
	
		if score > maxi:
		
			maxi=score
			imax=i
		
		
	return jeu[2][imax]
		
	
def saisieCoupSimuMax(profondeur,jeu,coup):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	game.joueCoup(jeu,coup)

	if profondeur==0:
		return eval(jeu)
		
	valides = game.getCoupsValides(jeu)
	
	if game.finJeu(jeu):
	
		return eval(jeu)
	
	else:
	
		global precedent
	
		imax=0
		maxi=-1000
	
		for i in range(len(jeu[2])):
	
			score = saisieCoupSimuMin(profondeur-1, game.getCopieJeu(jeu), jeu[2][i])
	
			if score >= precedent:
			
				return score
	
			elif score > maxi:
		
				maxi=score
		
	precedent = max
	return maxi
		
def saisieCoupSimuMin(profondeur,jeu,coup):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	game.joueCoup(jeu,coup)

	if profondeur==0:
		return eval(jeu)
		
	valides = game.getCoupsValides(jeu)
	
	if game.finJeu(jeu):
	
		return eval(jeu)
	
	else:
	
		global precedent
	
		imin=0
		mini=1000
	
		for i in range(len(jeu[2])):
	
			score = saisieCoupSimuMax(profondeur-1, game.getCopieJeu(jeu), jeu[2][i])
	
			if score <= precedent:
			
				return score
	
			if score < mini:
		
				mini=score
		
	precedent = mini
	return mini
	
def eval(jeu):


	return jeu[4][joueur-1]

	"""if joueur == 1:
		
		return jeu[4][0] - jeu[4][1]
				
	else:
	
		return jeu[4][1] - jeu[4][0]"""
	
		
			
				 
