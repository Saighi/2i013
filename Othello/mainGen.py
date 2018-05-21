import othello
import sys
import random
sys.path.append("..")
import game
game.game = othello
sys.path.append("./Joueurs")
import joueur_InfluenceMap
import joueur_greedy
Joueur1=joueur_InfluenceMap
game.joueur1 = Joueur1
game.joueur2 = joueur_greedy

def play():

    jeu = game.initialiseJeu()
    
    while len(jeu[3]) < 4:

        valides = game.getCoupsValides(jeu)

        if game.finJeu(jeu):
            break
        if len(valides) !=0:
            coup = random.choice(valides)

        game.joueCoup(jeu,coup)


    while True:

        #game.affiche(jeu)
        valides = game.getCoupsValides(jeu)

        if game.finJeu(jeu):
            break

        if len(valides) !=0:

             coup = game.saisieCoup(jeu)


        game.joueCoup(jeu,coup)

    #print("Le gagnant est : " + str(game.getGagnant(jeu)))

    return fitness(jeu)


def fitness(jeu):

    joueur = 1 if game.joueur1 == Joueur1 else 2

    enemi = 1 if joueur == 2 else 2

    f = 0.0
    n = 0

    if joueur == game.getGagnant(jeu):

        f += min(jeu[4][joueur-1]*1.0/jeu[4][enemi-1]*1.0, 5) if jeu[4][enemi-1] > 0 else 5

    if enemi == game.getGagnant(jeu):

        f -= min(jeu[4][enemi-1]*1.0/jeu[4][joueur-1]*1.0, 5) if jeu[4][joueur-1] > 0 else 5

    f += 0 if jeu[4][enemi-1] > 0 else 5

    f += 0 if jeu[4][joueur-1] > 0 else 5

    n += 1 if jeu[0][0][0] == joueur else 0

    n += 1 if jeu[0][0][7] == joueur else 0

    n += 1 if jeu[0][7][0] == joueur else 0

    n += 1 if jeu[0][7][7] == joueur else 0

    n *= 2

    f += n

    return f

