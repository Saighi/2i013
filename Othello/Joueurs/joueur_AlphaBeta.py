import sys
sys.path.append("../..")
import game

joueur = 0
LIGNESIZE = 6

Pond = [9, 9, 5, 6, 6, 1, 8, 4, 7]

#[6, 4, 9, 5, 7, 5, 3, 10, 2]

#[3, 6, 10, 8, 1, 5, 5, 9, 1]
#[9, 9, 5, 6, 6, 1, 8, 4, 7]
#[4, 8, 10, 8, 5, 2, 7, 2, 2]
#[0,0,0,0,0,0,0,0,0]

Alpha = -10000
Beta = 10000
TabVal = [[500,-150,30,10,10,30,-150,500],
          [-150,-250,0,0,0,0,-250,-150],
          [30,0,1,2,2,1,0,30],
          [10,0,2,16,16,2,0,10],
          [10,0,2,16,16,2,0,10],
          [30,0,1,2,2,1,0,30],
          [-150,-250,0,0,0,0,-250,-150],
          [500,-150,30,10,10,30,-150,500]]


def saisieCoup(jeu):
    """ jeu -> coup
    Retourne un coup a jouer aleatoire
    """
    global joueur
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
    global Pond

    statut = len(jeu[3])

    if statut <= 12:
        a1=Pond[0]
        a2=Pond[1]
        a3=Pond[2]
    if statut >= 60:
        a1=Pond[3]
        a2=Pond[4]
        a3=Pond[5]
    else:
        a1=Pond[6]
        a2=Pond[7]
        a3=Pond[8]

    score = jeu[4][joueur-1]

    nbcoup = len(jeu[2])

    force=0
    for x in range(8):
        for y in range(8):
            if joueur == jeu[0][x][y]:
                force += TabVal[x][y]

    return a1*score + a2*nbcoup + a3*force

