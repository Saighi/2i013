ligneSize = 8
ligneNum = 8

def init():

	plateau = []
	
	for i in range(ligneNum):
		plateau.append([])
	
	for ligne in plateau:
		for case in range(ligneSize):
			ligne.append(0)
			
	plateau[3][3]=1
	plateau[3][4]=2
	plateau[4][4]=1
	plateau[4][3]=2
	
	return [plateau,1,None,[],[0,0]]
	
def CoupValides(jeu):
	
		
	coupValides = []
	
	n=0
	m=1
	
	
	for ligne in jeu[0]:
		for case in ligne:
			
			if case == jeu[1]:
			
				if n+2 <= ligneSize :
				    
				    if jeu[0][n+1][m]!= jeu[1] and jeu[0][n+1][m]!= 0  and jeu[0][n+2][m]== 0:
						coupValides.append([n+2,m])
				if n-2 <= ligneSize :
					if jeu[0][n-1][m]!= jeu[1] and jeu[0][n-1][m]!= 0 and jeu[0][n-2][m]== 0 : 
						coupValides.append([n-2,m])
				if m+2 <= ligneSize :
					if jeu[0][n][m+1]!= jeu[1] and jeu[0][n][m+1]!= 0 and jeu[0][n][m+2]== 0 and m+2 <= ligneSize : 
						coupValides.append([n,m+2])
				if m-2 <= ligneSize :
					if jeu[0][n][m-1]!= jeu[1] and jeu[0][n][m-1]!= 0 and jeu[0][n][m-2]== 0 and m-2 <= ligneSize : 
						coupValides.append([n,m-2])
				
				
			m+=1
		m=0	
		n += 1
	
	
	
	return coupValides
	
	
def joueCoup(jeu,coup):
	
	jeu[0][coup[0]][coup[1]]=jeu[1]
	
	if coup[0]+2 <= ligneSize :
		if jeu[0][coup[0]+1][coup[1]]!= jeu[1] and jeu[0][coup[0]+1][coup[1]]!= 0 and jeu[0][coup[0]+2][coup[1]]== jeu[1]:
			jeu[0][coup[0]+1][coup[1]] = jeu[1]
	if coup[0]-2 <= ligneSize :
	 	if jeu[0][coup[0]-1][coup[1]]!= jeu[1] and jeu[0][coup[0]-1][coup[1]]!= 0 and jeu[0][coup[0]-2][coup[1]]== jeu[1]:
			jeu[0][coup[0]-1][coup[1]] = jeu[1]
	if coup[1]+2 <= ligneSize :
		if jeu[0][coup[0]][coup[1]+1]!= jeu[1] and jeu[0][coup[0]][coup[1]+1]!= 0 and jeu[0][coup[0]][coup[1]+2]== jeu[1]:
			jeu[0][coup[0]][coup[1]+1] = jeu[1]
	if coup[1]-2 <= ligneSize :
		if jeu[0][coup[0]][coup[1]-1]!= jeu[1] and jeu[0][coup[0]][coup[1]-1]!= 0 and jeu[0][coup[0]][coup[1]-2]== jeu[1]:
			jeu[0][coup[0]][coup[1]-1] = jeu[1]
			
	if jeu[1] == 1:
		
		jeu[1]=2
		
	elif jeu[1] == 2:
	
		jeu[1]=1
		
	jeu[2]=None	
		

def fin(jeu):
	for ligne in jeu[0]:
		for case in ligne:
			if case==0:
				return False
	return True


