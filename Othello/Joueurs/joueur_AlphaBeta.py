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
	
<<<<<<< HEAD
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
=======
	listc = jeu[2]
	
	scores = []
	
	for coup in listc:
	
		scores.append(simulation(5, game.getCopieJeu(jeu), coup))
		
		
	return listc[scores.index(max(scores))]
		
	
def saisieCoupSimu(jeu,profondeur):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global joueur
	global precedent
	
	listc = jeu[2]
	
	scores = []
	
	for coup in listc:
	
		scores.append( simulation(1, game.getCopieJeu(jeu), coup))
		
		if jeu[1] == joueur:
		
			if scores[-1] >= precedent:
			
				break
				
		else:
		
			if scores[-1] <= precedent:
			
				break
				
	if jeu[1] == joueur:
				
		retour = max(scores)
		precedent = retour
		return retour
			
	else:
		
		retour = min(scores)
		precedent = retour
		return precedent
	
def simulation(profondeur, jeu, coup):
	
>>>>>>> 7272842f9b02a725f0255ff151ac785b6fbebe80
	game.joueCoup(jeu,coup)

	if profondeur==0:
		return eval(jeu)
		
	valides = game.getCoupsValides(jeu)
	
	if game.finJeu(jeu):
	
		return eval(jeu)
	
<<<<<<< HEAD
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
	
		
			
				 
=======
	
	return saisieCoupSimu(jeu , profondeur-1)
			 

	
def eval(jeu):

	return jeu[4][joueur-1]
	
    
>>>>>>> 7272842f9b02a725f0255ff151ac785b6fbebe80
