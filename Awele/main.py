from __future__ import print_function
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

jeu = game.initialiseJeu()

while not game.finJeu(jeu):

	game.affiche(jeu)
	valides = game.getCoupsValides(jeu)
	
	if len(valides) !=0:
	
		 coup = game.saisieCoup(jeu)
		 
	game.joueCoup(jeu,coup)
		
print("Le gagnant est : ", getGagnant(jeu))
