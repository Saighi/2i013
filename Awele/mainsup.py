from __future__ import print_function
import awele
import sys
sys.path.append("..")
import testsup
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_aleatoire
import joueur_AlphaBeta
import joueur_AlphaBeta_prof1
import joueur_AlphaBeta_prof5

game.joueur1=joueur_AlphaBeta_prof1
game.joueur2=joueur_aleatoire
oracle=joueur_AlphaBeta_prof5



def play():

	jeu = game.initialiseJeu()
	print(game.joueur1)
	
	while True:




		#game.affiche(jeu)
		valides = game.getCoupsValides(jeu)



		scoresoracle= oracle.scorescoups(jeu)

		o=EvalCoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu))

		for i in range(valides):
			if scoresoracle[i] <scoresoracle[oracle.saisieCoup(jeu)]:
				if (o-EvalCoupHorizon1(game.getCopieJeu(jeu),valides[i]))<1:

					testsup.W[0]= testsup.W[0]-testsup.Alpha*(h1CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h1CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))
						
					testsup.W[1]= testsup.W[1]-testsup.Alpha*(h2CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h2CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

					testsup.W[2]= testsup.W[2]-testsup.Alpha*(h3CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h3CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

					testsup.W[3]= testsup.W[3]-testsup.Alpha*(h4CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h4CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

					testsup.W[4]= testsup.W[4]-testsup.Alpha*(h5CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h5CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

					testsup.W[5]= testsup.W[5]-testsup.Alpha*(h6CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h6CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))








	
		if game.finJeu(jeu):
	
			break
	
		elif valides != None:
	
			 coup = game.saisieCoup(jeu)
			 
		game.joueCoup(jeu,coup)
		
	print("Le gagnant est : ", game.getGagnant(jeu))
	
	return game.getGagnant(jeu)

def EvalCoupHorizon1(jeu,coup):
	if jeu[2][0]==coup:
		Leftest=True
	else:
		Leftest=False
	game.joueCoup(jeu,coup)

	return oracle.eval(jeu,coup,Leftest)

def h1CoupHorizon1(jeu,coup):
	if jeu[2][0]==coup:
		Leftest=True
	else:
		Leftest=False
	game.joueCoup(jeu,coup)

	return max(jeu[0][joueur-1])

def h2CoupHorizon1(jeu,coup):
	if jeu[2][0]==coup:
		Leftest=True
	else:
		Leftest=False
	game.joueCoup(jeu,coup)

	h2=0
	
	for i in jeu[0][joueur-1]:
	
		h2+=i

	return h2

def h3CoupHorizon1(jeu,coup):
	if jeu[2][0]==coup:
		Leftest=True
	else:
		Leftest=False
	game.joueCoup(jeu,coup)

	h3=len(jeu[2]) if jeu[2]!=None else 0

	return h3


def h4CoupHorizon1(jeu,coup):
	if jeu[2][0]==coup:
		Leftest=True
	else:
		Leftest=False
	game.joueCoup(jeu,coup)

	

	return jeu[4][joueur-1]

def h5CoupHorizon1(jeu,coup):
	if jeu[2][0]==coup:
		Leftest=True
	else:
		Leftest=False
	game.joueCoup(jeu,coup)

	h5=1 if leftest else 0

	return h5


def h6CoupHorizon1(jeu,coup):
	if jeu[2][0]==coup:
		Leftest=True
	else:
		Leftest=False
	game.joueCoup(jeu,coup)

	

	return -jeu[4][enemi-1]


