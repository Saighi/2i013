import main
import game

n = 0

lj1=[game.joueur1,0]
lj2=[game.joueur2,0]

while n < 100:

	score = main.play()

	if score == 1 :
	
		if game.joueur1 == lj1[0]:
		
			lj1[1]+=1
			
		else:
		
			lj2[1]+=1
	
	elif score == 2:
	
		if game.joueur2 == lj2[0]:
		
			lj2[1]+=1
			
		else:
		
			lj1[1]+=1
		
	n+=1
	
	t=game.joueur1
	game.joueur1=game.joueur2
	game.joueur2=t
	
print("le joueur "+str(lj1[0])+" a gagne " + str(lj1[1]) + " fois")

print("le joueur "+str(lj2[0])+" a gagne " + str(lj2[1]) + " fois")
