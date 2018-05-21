import sys
sys.path.append("../..")
import game

joueur = 0
LIGNESIZE = 6

Weight = [9, 9, 5, 6, 6, 1, 8, 4, 7]

#[3, 6, 10, 8, 1, 5, 5, 9, 1]
#[9, 9, 5, 6, 6, 1, 8, 4, 7]
#[4, 8, 10, 8, 5, 2, 7, 2, 2]
#[0,0,0,0,0,0,0,0,0]

Alpha = -10000
Beta = 10000

Pond = [-198, 251, -33, 54, -390, -292, -298, 475, 398]

#[-311, 436, -450, 49, -390, -431, 265, 475, 163]

A = Pond[0]
B = Pond[1]
C = Pond[2]
D = Pond[3]
E = Pond[4]
F = Pond[5]
G = Pond[6]
H = Pond[7]
I = Pond[8]

TabVal = [[500, A, C, F, F, C, A, 500],
          [A, B, D, G, G, D, B, A],
          [C, D, E, H, H, E, D, C],
          [F, G, H, I, I, H, G, F],
          [F, G, H, I, I, H, G, F],
          [C, D, E, H, H, E, D, C],
          [A, B, D, G, G, D, B, A],
          [500, A, C, F, F, C, A, 500]]


def saisieCoup(jeu):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    global joueur
    TabValUp()
    joueur = jeu[1]

    maxi=-10000
    imax=0

    score= -10000

    for i in range(len(jeu[2])):

        score = CoupMin(0, game.getCopieJeu(jeu), jeu[2][i])

        if score > maxi:

            maxi=score
            imax=i

    return jeu[2][imax]


def CoupMax(profondeur,jeu,coup):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    game.joueCoup(jeu,coup)
    valides = game.getCoupsValides(jeu)

    if profondeur==0 or game.finJeu(jeu):
        return eval(jeu)

    else:

        global Alpha
        global Beta

        score = -10000

        for i in range(len(jeu[2])):

            score = max(score,CoupMin(profondeur-1, game.getCopieJeu(jeu), jeu[2][i]))

            if score >= Beta:

                return score

            Alpha = max(Alpha,score)

    return score

def CoupMin(profondeur,jeu,coup):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    game.joueCoup(jeu,coup)
    valides = game.getCoupsValides(jeu)

    if profondeur==0 or game.finJeu(jeu):
        return eval(jeu)

    else:

        global Alpha
        global Beta

        score = 10000

        for i in range(len(jeu[2])):

            score = min(score,CoupMax(profondeur-1, game.getCopieJeu(jeu), jeu[2][i]))

            if score <= Alpha:

                return score

            Beta = min(Beta,score)

    return score

def eval(jeu):

    global joueur
    global TabVal
    global Weight

    statut = len(jeu[3])

    if statut <= 12:
        a1=Weight[0]
        a2=Weight[1]
        a3=Weight[2]
    if statut >= 60:
        a1=Weight[3]
        a2=Weight[4]
        a3=Weight[5]
    else:
        a1=Weight[6]
        a2=Weight[7]
        a3=Weight[8]

    score = jeu[4][joueur-1]

    nbcoup = len(jeu[2])

    force=0
    for x in range(8):
        for y in range(8):
            if joueur == jeu[0][x][y]:
                force += TabVal[x][y]

    return a1*score + a2*nbcoup + a3*force

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
    I = Pond[8]

    TabVal = [[10, A, C, F, F, C, A, 10],
              [A, B, D, G, G, D, B, A],
              [C, D, E, H, H, E, D, C],
              [F, G, H, I, I, H, G, F],
              [F, G, H, I, I, H, G, F],
              [C, D, E, H, H, E, D, C],
              [A, B, D, G, G, D, B, A],
              [10, A, C, F, F, C, A, 10]]
