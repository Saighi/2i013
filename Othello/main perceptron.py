import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_ABInflenceMap
import joueur_AlphaBetaTarget
Joueur1=joueur_ABInflenceMap
game.joueur1 = Joueur1
game.joueur2 = joueur_AlphaBetaTarget


def play():

    jeu = game.initialiseJeu()

    while True:



        #game.affiche(jeu)
        valides = game.getCoupsValides(jeu)

        if game.finJeu(jeu):
            break


        if len(valides) !=0:

             coup = game.saisieCoup(jeu)


        game.joueCoup(jeu,coup)

    print("Le gagnant est : " + str(game.getGagnant(jeu)))
    return game.getGagnant(jeu)

def prediction(coupPossible):

	o=[]
	
	for coup in coupPossible:
	
		

play()
