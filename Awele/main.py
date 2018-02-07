from __future__ import print_function
import awele
import sys
sys.path.append("..")
import game
game.game=awele
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
	
		elif valides != None:
	
			 coup = game.saisieCoup(jeu)
			 
		game.joueCoup(jeu,coup)
		
	print("Le gagnant est : ", game.getGagnant(jeu))
	
	return game.getGagnant(jeu)
