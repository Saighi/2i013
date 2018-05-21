import sys
sys.path.append("../..")
import game

joueur = 0

def saisieCoup(jeu):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    global joueur
    joueur = jeu[1]

    maxi=-10000
    imax=0

    for i in range(len(jeu[2])):

        score = saisieCoupSimuMin(0, game.getCopieJeu(jeu), jeu[2][i])

        if score > maxi:

            maxi=score
            imax=i


    return jeu[2][imax]


def saisieCoupSimuMax(profondeur,jeu,coup):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    global joueur

    Pscore = jeu[4][joueur - 1]
    game.joueCoup(jeu, coup)
    valides = game.getCoupsValides(jeu)

    if profondeur == 0 or game.finJeu(jeu):
        return eval(jeu) - Pscore
    else:

        maxi=-1000

        for i in range(len(jeu[2])):

            score = saisieCoupSimuMin(profondeur-1, game.getCopieJeu(jeu), jeu[2][i])

            if score > maxi:

                maxi=score

    return maxi

def saisieCoupSimuMin(profondeur,jeu,coup):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    global joueur

    Pscore = jeu[4][joueur-1]
    game.joueCoup(jeu, coup)
    valides = game.getCoupsValides(jeu)

    if profondeur == 0 or game.finJeu(jeu):
        return eval(jeu) - Pscore

    else:

        score=[]

        for i in range(len(jeu[2])):

            score.append(saisieCoupSimuMax(profondeur-1, game.getCopieJeu(jeu), jeu[2][i]))

            estimate=[]
            si=0

            for s in score:

                i=s-639
                si+=i
                estimate.append(i)

            for ie in range(len(estimate)):

                estimate[ie]=estimate[ie]*1.0/si*1.0

            finalScore=0
            for fi in range(len(estimate)):

                score[fi]=score[fi]*1.0*estimate[fi]
                finalScore+=score[fi]

        return finalScore



def eval(jeu):

    return jeu[4][joueur-1]
