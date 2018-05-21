import sys
sys.path.append("../..")
import game

joueur = 0

Pond = [5, 8, 3, 8, 7, 5, 1, 0]

A = Pond[0]
B = Pond[1]
C = Pond[2]
D = Pond[3]
E = Pond[4]
F = Pond[5]
G = Pond[6]
H = Pond[7]

TabVal = [[10, A, C, F, F, C, A, 10],
          [A, B, D, G, G, D, B, A],
          [C, D, E, H, H, E, D, C],
          [F, G, H, 0, 0, H, G, F],
          [F, G, H, 0, 0, H, G, F],
          [C, D, E, H, H, E, D, C],
          [A, B, D, G, G, D, B, A],
          [10, A, C, F, F, C, A, 10]]

def saisieCoup(jeu):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    global joueur
    TabValUp()
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
    game.joueCoup(jeu, coup)
    valides = game.getCoupsValides(jeu)

    if profondeur == 0 or game.finJeu(jeu):
        return eval(coup)
    else:

        global joueur

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

    game.joueCoup(jeu, coup)
    valides = game.getCoupsValides(jeu)

    if profondeur == 0 or game.finJeu(jeu):
        return eval(coup)

    else:

        global joueur
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



def eval(coup):

    return TabVal[coup[0]][coup[1]]


def TabValUp():

    global Pond
    global TabVal

    A = Pond[0]
    B = Pond[1]
    C = Pond[2]
    D = Pond[3]
    E = Pond[4]
    F = Pond[5]
    G = Pond[6]
    H = Pond[7]

    TabVal = [[10, A, C, F, F, C, A, 10],
              [A, B, D, G, G, D, B, A],
              [C, D, E, H, H, E, D, C],
              [F, G, H, 0, 0, H, G, F],
              [F, G, H, 0, 0, H, G, F],
              [C, D, E, H, H, E, D, C],
              [A, B, D, G, G, D, B, A],
              [10, A, C, F, F, C, A, 10]]