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
	m=0
	
	
	for ligne in jeu[0]:
		for case in ligne:
			scan=0
			
			if case == jeu[1]:
			
				if n+1 < ligneSize :
						
					scan = 0
					while jeu[0][n+1+scan][m]!= jeu[1] and jeu[0][n+1+scan][m]!= 0 and n+2+scan < ligneSize :
						if jeu[0][n+2+scan][m]== 0:
							coupValides.append([n+2+scan,m])
						scan+=1
							
				if n-1 >= 0 :
				
					scan = 0
					while jeu[0][n-1-scan][m]!= jeu[1] and jeu[0][n-1-scan][m]!= 0 and n-2-scan >=0:
						if jeu[0][n-2-scan][m]== 0:
							coupValides.append([n-2-scan,m])
						scan+=1
							
				if m+1 < ligneSize :
				
					scan = 0
					while jeu[0][n][m+1+scan]!= jeu[1] and jeu[0][n][m+1+scan]!= 0 and m+2+scan < ligneSize :
						if jeu[0][n][m+2+scan]== 0:
							coupValides.append([n,m+2+scan])
						scan+=1
							
				if m-1 >= 0 :
				
					
					
					scan = 0
					while jeu[0][n][m-1-scan]!= jeu[1] and jeu[0][n][m-1-scan]!= 0 and m-2-scan >=0:
						if jeu[0][n][m-2-scan]== 0:
							coupValides.append([n,m-2-scan])
						scan+=1
				
				
				if n+1 < ligneSize and m+1 < ligneSize:
						
					scan = 0
					while jeu[0][n+1+scan][m+1+scan]!= jeu[1] and jeu[0][n+1+scan][m+1+scan]!= 0 and n+2+scan < ligneSize and m+2+scan < ligneSize :
						if jeu[0][n+2+scan][m+2+scan]== 0:
							coupValides.append([n+2+scan,m+2+scan])
						scan+=1
							
				if n-1 >= 0 and m-1 >= 0 :
				
					scan = 0
					while jeu[0][n-1-scan][m-1-scan]!= jeu[1] and jeu[0][n-1-scan][m-1-scan]!= 0 and n-2-scan >=0 and m-2-scan >=0:
						if jeu[0][n-2-scan][m-2-scan]== 0:
							coupValides.append([n-2-scan,m-2-scan])
						scan+=1
							
				if m+1 < ligneSize and n-1 >= 0 :
				
					scan = 0
					while jeu[0][n-1-scan][m+1+scan]!= jeu[1] and jeu[0][n-1-scan][m+1+scan]!= 0 and m+2+scan < ligneSize and  n-2-scan >= 0  :
						if jeu[0][n-2-scan][m+2+scan]== 0:
							coupValides.append([n-2-scan,m+2+scan])
						scan+=1
							
				if m-1 >= 0 and n+1 < ligneSize :
				
					
					
					scan = 0
					while jeu[0][n+1+scan][m-1-scan]!= jeu[1] and jeu[0][n+1+scan][m-1-scan]!= 0 and m-2-scan >=0 and n+2+scan < ligneSize:
						if jeu[0][n+2+scan][m-2-scan]== 0:
							coupValides.append([n+2+scan,m-2-scan])
						scan+=1
				
				
			m+=1
		m=0	
		n+= 1
	
	for nbr in coupValides:
		c=coupValides.count(nbr)
		if c>1:
			for i in range(c-1):
				coupValides.remove(nbr)
		
	
	return coupValides
	
	
def joueCoup(jeu,coup):
	
	jeu[0][coup[0]][coup[1]]=jeu[1]
	
	scan=0
	while coup[0]+2+scan < ligneSize :
	
		if jeu[0][coup[0]+1+scan][coup[1]]!= jeu[1] and jeu[0][coup[0]+1+scan][coup[1]]!= 0:
			if jeu[0][coup[0]+2+scan][coup[1]]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]+1+scan][coup[1]] = jeu[1]
					scan-=1
					
				
				break

		scan+=1
		
	
	scan=0	
	while coup[0]-2-scan >= 0 :
	
	 	if jeu[0][coup[0]-1-scan][coup[1]]!= jeu[1] and jeu[0][coup[0]-1-scan][coup[1]]!= 0:
			if jeu[0][coup[0]-2-scan][coup[1]]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]-1-scan][coup[1]] = jeu[1]
					scan-=1
					
				
				break
	
		scan+=1
		
	scan=0
	while coup[1]+2+scan < ligneSize :
	
		if jeu[0][coup[0]][coup[1]+1+scan]!= jeu[1] and jeu[0][coup[0]][coup[1]+1+scan]!= 0:
			if jeu[0][coup[0]][coup[1]+2+scan]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]][coup[1]+1+scan] = jeu[1]
					scan-=1
					
				
				break

		scan+=1
	
	scan=0	
	while coup[1]-2-scan >= 0 :
	
		if jeu[0][coup[0]][coup[1]-1-scan]!= jeu[1] and jeu[0][coup[0]][coup[1]-1-scan]!= 0:
			if jeu[0][coup[0]][coup[1]-2-scan]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]][coup[1]-1-scan] = jeu[1]
					scan-=1
					
				
				break
		scan+=1
		

	scan=0
	while coup[0]+2+scan < ligneSize and coup[1]+2+scan < ligneSize:
	
		if jeu[0][coup[0]+1+scan][coup[1]+1+scan]!= jeu[1] and jeu[0][coup[0]+1+scan][coup[1]+1+scan]!= 0:
			if jeu[0][coup[0]+2+scan][coup[1]+2+scan]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]+1+scan][coup[1]+1+scan] = jeu[1]
					scan-=1
					
				
				break

		scan+=1
		
	
	scan=0	
	while coup[0]-2-scan >= 0 and coup[1]-2-scan >= 0 :
	
	 	if jeu[0][coup[0]-1-scan][coup[1]-1-scan]!= jeu[1] and jeu[0][coup[0]-1-scan][coup[1]-1-scan]!= 0:
			if jeu[0][coup[0]-2-scan][coup[1]-2-scan]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]-1-scan][coup[1]-1-scan] = jeu[1]
					scan-=1
					
				
				break
	
		scan+=1
		
	scan=0
	while coup[1]+2+scan < ligneSize and coup[0]-2-scan >= 0:
	
		if jeu[0][coup[0]-1-scan][coup[1]+1+scan]!= jeu[1] and jeu[0][coup[0]-1-scan][coup[1]+1+scan]!= 0:
			if jeu[0][coup[0]-2-scan][coup[1]+2+scan]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]-1-scan][coup[1]+1+scan] = jeu[1]
					scan-=1
					
				
				break

		scan+=1
	
	scan=0	
	while coup[1]-2-scan >= 0 and coup[0]+2+scan < ligneSize :
	
		if jeu[0][coup[0]+1+scan][coup[1]-1-scan]!= jeu[1] and jeu[0][coup[0]+1+scan][coup[1]-1-scan]!= 0:
			if jeu[0][coup[0]+2+scan][coup[1]-2-scan]== jeu[1]:
				jeu[4][jeu[1]-1]+=scan+1
				while scan >=0:
					jeu[0][coup[0]+1+scan][coup[1]-1-scan] = jeu[1]
					scan-=1
					
				
				break
		scan+=1
		
	if jeu[1] == 1:
		
		jeu[1]=2
		
	elif jeu[1] == 2:
	
		jeu[1]=1
		
	jeu[2]=None	
		

def fin(jeu):
	AuMoinsUneCaseVide=False
	AuMoinsUnPionJ1=False
	AuMoinsUnPionJ2=False
	if len(jeu[2])==0:
		return True
	for ligne in jeu[0]:
		for case in ligne:
			if case==0:
				AuMoinsUneCaseVide=True
			if case==1:
				AuMoinsUnPionJ1=True
			if case==2:
				AuMoinsUnPionJ2=True
	if AuMoinsUneCaseVide and AuMoinsUnPionJ1 and AuMoinsUnPionJ2:
		return False
	
	else : return True 


