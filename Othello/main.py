import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_aleatoire
game.joueur1=joueur_aleatoire
game.joueur2=joueur_aleatoire


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
		

