import sys
sys.path.append("../..")
import game

joueur = 0
precedent = 0
TabVal = [[500,-150,30,10,10,30,-150,500],
		  [-150,-250,0,0,0,0,-250,-150],
		  [30,0,1,2,2,1,0,30],
		  [10,0,2,16,16,2,0,10],
		  [10,0,2,16,16,2,0,10],
		  [30,0,1,2,2,1,0,30],
		  [-150,-250,0,0,0,0,-250,-150],
		  [500,-150,30,10,10,30,-150,500]]
		  

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

	valides = game.getCoupsValides(jeu)

	if profondeur==0 or game.finJeu(jeu):
		return eval(jeu,profondeur)
	
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
		
	precedent = maxi
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
	valides = game.getCoupsValides(jeu)

	if profondeur==0 or game.finJeu(jeu):
		return eval(jeu,profondeur)
	
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
	
def eval(jeu,profondeur):
	
	global joueur
	global TabVal
	
	statut = len(jeu[3])
	
	if statut <= 12:
		a1=0
		a2=1
		a3=1
	if statut >= 60-profondeur:
		a1=1
		a2=0
		a3=0
	else:
		a1=1
		a2=1
		a3=1
	
	score = jeu[4][joueur-1]
	
	nbcoup = len(jeu[2])
	
	force=0
	for x in range(8):
		for y in range(8):
			if joueur == jeu[0][x][y]:
				force += TabVal[x][y]

	return a1*score + a2*nbcoup + a3*force
	
		
			
				 
=======
	
	return saisieCoupSimu(jeu , profondeur-1)
			 

	
def eval(jeu):

	return jeu[4][joueur-1]
	
    
>>>>>>> 7272842f9b02a725f0255ff151ac785b6fbebe80
