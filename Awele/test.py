import main
import game

score = []

lj1=[game.joueur1,0]
lj2=[game.joueur2,0]

h=10

def run():

    n=0

    while n < 100:

        if main.play() == 1:

            if game.joueur1==lj1[0]:
                lj1[1] += 1
            else:
                lj2[1] +=1

        elif main.play() == 2:

            if game.joueur2==lj2[0]:
                lj2[1] += 1
            else:
                lj1[1] +=1

        n += 1

        t = game.joueur1
        game.joueur1 = game.joueur2
        game.joueur2 = t

    print("le joueur 1 a gagne " + str(lj1[1]) + " fois")

    print("le joueur 2 a gagne " + str(lj2[1]) + " fois")

run()

