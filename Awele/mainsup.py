from __future__ import print_function
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_aleatoire
import joueur_AlphaBeta_prof1
import joueur_AlphaBeta_prof5

game.joueur1=joueur_AlphaBeta_prof1
game.joueur2=joueur_aleatoire
oracle=joueur_AlphaBeta_prof5

score = []

lj1=[game.joueur1,0]
lj2=[game.joueur2,0]

h=10
W=joueur_AlphaBeta_prof1.Pond
Alpha= 0.05

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




def play():

    global W
    global Alpha

    jeu = game.initialiseJeu()
    print(game.joueur1)
    
    while True:




        #game.affiche(jeu)
        valides = game.getCoupsValides(jeu)
        print(EvalCoupHorizon1(game.getCopieJeu(jeu),valides[0]))
        print(oracle.scorescoups(jeu)[0])


        """if jeu[2] !=None:
            scoresoracle= oracle.scorescoups(jeu)


            o=EvalCoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu))

            for i in range(len(valides)):
                if scoresoracle[i] < max(scoresoracle):
                    if (o-EvalCoupHorizon1(game.getCopieJeu(jeu),valides[i]))<1:

                        W[0]= W[0]-Alpha*(h1CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h1CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))
                            
                        W[1]= W[1]-Alpha*(h2CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h2CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

                        W[2]= W[2]-Alpha*(h3CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h3CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

                        W[3]= W[3]-Alpha*(h4CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h4CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

                        W[4]= W[4]-Alpha*(h5CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h5CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))

                        W[5]= W[5]-Alpha*(h6CoupHorizon1(game.getCopieJeu(jeu),valides[i])-h6CoupHorizon1(game.getCopieJeu(jeu),oracle.saisieCoup(jeu)))
        """







    
        if game.finJeu(jeu):
    
            break
    
        elif valides != None:
    
            coup = game.saisieCoup(jeu)
             
        game.joueCoup(jeu,coup)
        
    
    return game.getGagnant(jeu)

play()

