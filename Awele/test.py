import main

n = 0

j1=0
j2=0

while n < 100:

	if main.play() == 1:
	
		j1+=1
	
	elif main.play() == 2:
	
		j2+=1
		
	n+=1
	
	
print("le joueur 1 a gagne " + str(j1) + " fois")

print("le joueur 2 a gagne " + str(j2) + " fois")
