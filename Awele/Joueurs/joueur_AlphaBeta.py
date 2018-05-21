# -*- coding: cp1252 -*-

import sys
sys.path.append("../..")
import game

joueur = 0
LIGNESIZE = 6

Pond = [0.1986,0.19,0.3707,1.0,0.4188,0.5659]

Alpha = -10000
Beta = 10000

def saisieCoup(jeu):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	global joueur
	joueur = jeu[1]
	
	maxi=-10000
	imax=0

	score= -10000
	rightest = True
	
	for i in range(len(jeu[2])):
	
		score = CoupMin(5, game.getCopieJeu(jeu), jeu[2][i],rightest)
		rightest = False

		if score > maxi:
		
			maxi=score
			imax=i
		
		
	return jeu[2][imax]
		
	
def CoupMax(profondeur,jeu,coup,rightest):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	game.joueCoup(jeu,coup)
		
	valides = game.getCoupsValides(jeu)
	
	if game.finJeu(jeu) or profondeur==0:
	
		return eval(jeu,coup,rightest)
	
	else:
	
		global Alpha
		global Beta

		score = -10000
		rightest = True
	
		for i in range(len(jeu[2])):
	
			score = max(score,CoupMin(profondeur-1, game.getCopieJeu(jeu), jeu[2][i],rightest))
			rightest = False
	
			if score >= Beta:
			
				return score
			
			Alpha = max(Alpha,score)

	return score
		
def CoupMin(profondeur,jeu,coup,rightest):
	""" jeu -> coup
	Retourne un coup a jouer aleatoire 
	"""
	game.joueCoup(jeu,coup)
		
	valides = game.getCoupsValides(jeu)
	
	if game.finJeu(jeu) or profondeur==0:
	
		return eval(jeu,coup,rightest)
	
	else:
	
		global Alpha
		global Beta

		score = 10000
		rightest = True
	
		for i in range(len(jeu[2])):
	
			score = min(score,CoupMax(profondeur-1, game.getCopieJeu(jeu), jeu[2][i],rightest))
			rightest = False
	
			if score <= Alpha:
			
				return score
			
			Beta = min(Beta,score)
		
	return score
	
def eval(jeu,coup,rightest):


	return jsp(jeu,coup,rightest)

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
			
	return count
	
def algo2(jeu):

	global LIGNESIZE
	
	count = 0
	
	enemi=1 if joueur == 2 else 2

	for i in range(len(jeu[0][joueur-1])):
		estMarche=True
		
		if jeu[0][joueur-1][i] == 0:
		
				estMarche=False

		for j in range(i,len(jeu[0][joueur-1])):
		
			if jeu[0][joueur-1][i] == 0 and i+jeu[0][joueur-1][i] >= j:
			
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
			
	return count + jeu[4][joueur-1] - jeu[4][enemi-1]
		
def dif_mob_menace(jeu):

        mobilite = 0
        menace = 0
        dif=0

        enemi=1 if joueur == 2 else 2

        for i in range(6):

                if jeu[0][joueur-1][i]!=0:

                        mobilite+=1
                        dif+=jeu[0][joueur-1][i]

                if jeu[0][enemi-1][i]!=0:

                        menace+=1
                        dif-=jeu[0][enemi-1][i]

        dif = jeu[4][joueur-1] - jeu[4][enemi-1]

        return dif*100+menace*33+mobilite*22
        
def jsp(jeu,coup,rightest):

	global Pond

	enemi=1 if joueur == 2 else 2

	h1=max(jeu[0][joueur-1])
	h2=0
	
	for i in jeu[0][joueur-1]:
	
		h2+=i
		
	h3=len(jeu[2]) if jeu[2]!=None else 0
	
	h4=jeu[4][joueur-1]
	
	h5=1 if rightest else 0
	
	h6=jeu[4][enemi-1]
	
	return h1*Pond[0]+h2*Pond[1]+h3*Pond[2]+h4*Pond[3]+h5*Pond[4]-h6*Pond[5]
                
