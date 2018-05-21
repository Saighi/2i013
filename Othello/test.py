import mainGen
import game

score = []

lj1=[game.joueur1,0]
lj2=[game.joueur2,0]

h=10

def run():

    f1 = mainGen.play()

    t=game.joueur1
    game.joueur1= game.joueur2
    game.joueur2= t

    f2 = mainGen.play()

    t = game.joueur1
    game.joueur1 = game.joueur2
    game.joueur2 = t

    return (f1+f2)/2


print("le joueur "+str(lj1[0])+" a gagne f : " + str(run()))

