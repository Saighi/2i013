import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_aleatoire
import joueur_MinMax
game.joueur1=joueur_MinMax
game.joueur2=joueur_MinMax


def play():

	jeu = game.initialiseJeu()

	while True:
	
	

		game.affiche(jeu)
		valides = game.getCoupsValides(jeu)
	
		if game.finJeu(jeu):
			break
			
		
		if len(valides) !=0:
	
			 coup = game.saisieCoup(jeu)
	
			 
		game.joueCoup(jeu,coup)
		
	print("Le gagnant est : " + str(game.getGagnant(jeu)))
	return game.getGagnant(jeu)
	

		
play()
