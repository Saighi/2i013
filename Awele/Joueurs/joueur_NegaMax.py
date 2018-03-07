import sys
sys.path.append("../..")
import game

joueur = 0
enemi = 0
precedent = 0
LIGNESIZE = 6
PROFONDEUR = 3

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global joueur
	global enemi
	joueur = jeu[1]
	
	enemi=1 if joueur == 2 else 2
	
	maxi=-10000
	imax=0
	
	for i in range(len(jeu[2])):
	
		score = saisieCoupSimuNegaBeta(0, game.getCopieJeu(jeu), jeu[2][i])
	
		if score > maxi:
		
			maxi=score
			imax=i
		
		
	return jeu[2][imax]
		
	
def saisieCoupSimuNegaBeta(profondeur,jeu,coup):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global enemi
	global PROFONDEUR
	
	ScorePrecedent = jeu[4]
	game.joueCoup(jeu,coup)
	valides = game.getCoupsValides(jeu)

	if profondeur == PROFONDEUR or game.finJeu(jeu):
	
		if profondeur % 2 == 0:
			return eval(jeu,ScorePrecedent)
		else:
			return -eval(jeu,ScorePrecedent)
	
	else:
	
		global precedent
		imax=0
		maxi=-1000
	
		for i in range(len(jeu[2])):
	
			score = saisieCoupSimuNegaBeta(profondeur+1, game.getCopieJeu(jeu), jeu[2][i])
			
			if score >= precedent:
			
				return calcul(score,(jeu[4][joueur-1]-ScorePrecedent[joueur-1] - jeu[4][enemi-1] - ScorePrecedent[enemi-1]))
	
			elif score > maxi:
		
				maxi=score
			
		precedent = max
		return calcul(maxi,(jeu[4][joueur-1]-ScorePrecedent[joueur-1] - jeu[4][enemi-1] - ScorePrecedent[enemi-1]))
		
				
		
	
def eval(jeu,ScorePrecedent):

	diff = (jeu[4][joueur-1]-jeu[4][enemi-1])
	gain = (jeu[4][joueur-1]-ScorePrecedent[joueur-1] - jeu[4][enemi-1] - ScorePrecedent[enemi-1])
	pond=0.1
	

	return gain

def calcul(score,gain):

	return gain - score
	
		
			
				 
