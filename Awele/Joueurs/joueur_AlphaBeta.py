import sys
sys.path.append("../..")
import game

joueur = 0
precedent = 0
LIGNESIZE = 6

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global joueur
	joueur = jeu[1]
	
	maxi=-10000
	imax=0
	
	for i in range(len(jeu[2])):
	
		score = saisieCoupSimuMin(3, game.getCopieJeu(jeu), jeu[2][i])
	
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


	return algo2(jeu)

def algo1(jeu):

	count = 0
	enemi = 0
	
	enemi=1 if joueur == 2 else 2
	
	for case in jeu[0][joueur-1]:
	
		if case > 2:
		
			count+=1
		
		else:
		
			count-=1
			
	for case in jeu[0][enemi-1]:
	
		if case == 1:
		
			count+=1
			
		elif case == 2:
		
			count+=2
		
		else:
		
			count-=1
	
			
	count+= jeu[4][joueur-1]
			
	print(count)
	return count
	
def algo2(jeu):

	global LIGNESIZE
	
	count = 0
	
	enemi=1 if joueur == 2 else 2

	for i in range(len(jeu[0][joueur-1])):
		estMarche=True
		
		if jeu[0][joueur-1][i] == 0:
		
				estMarche=False
	
		if not(i+jeu[0][joueur-1][i] <LIGNESIZE ) and joueur-1 == 1:
		
				estMarche=False
				
		elif not(LIGNESIZE-1-i+jeu[0][joueur-1][i] < LIGNESIZE) and joueur-1 == 0:
			
				estMarche=False
				
		if joueur-1 == 1:
		
				n = jeu[0][joueur-1][i]-1
			
				while n > 0 and i+jeu[0][joueur-1][i]-n<LIGNESIZE:
				
					case=i+jeu[0][joueur-1][i]-n
					
					if jeu[0][joueur-1][case]==0:
					
						for e in range(len(jeu[0][enemi-1])):
						
							if not(jeu[0][enemi-1][e] < case+e ) and enemi-1 == 0:
			
								estMarche=False
					
					n-=1
					
					
				
		elif joueur-1 == 0:
			
				n = jeu[0][joueur-1][i]-1
			
				while n > 0 and LIGNESIZE-1-i+jeu[0][joueur-1][i]-n<LIGNESIZE:
				
					case=LIGNESIZE-1-i+jeu[0][joueur-1][i]-n
					
					if jeu[0][joueur-1][case]==0:
					
						for e in range(len(jeu[0][enemi-1])):
						
							if not(jeu[0][enemi-1][e] < LIGNESIZE-e+case ) and enemi-1 == 1:
			
								estMarche=False
				
					n-=1
					
					
		if estMarche:
		
			count+=1
			
	print(count)
	return count
		
			
				 
