ligneSize = 6
ligneNum = 2


def init():

	plateau = []
	for i in range(ligneNum):
		plateau.append([])
	
	for ligne in plateau:
		
		for case in range(ligneSize):
		
			ligne.append(1)
			
			
	return [plateau,1,None,[],[0,0]]
	
def CoupValides(jeu):
	
	coupValides = []
	
	e = jeu[1]-1
	
	if e == 0:
	
		ligne = jeu[0][1]
	
	else:
	
		ligne = jeu[0][0]
		
	s=0
	
	for case in ligne:
	
		s+=case
	
	ligne = jeu[0][e]
	
	n = 0
		
	for case in ligne:
		
		if case != 0:
			coupValides.append([e,n])
			
		n += 1
		
	if s == 0:
	
		for coup in coupValides:
	
			print(coup[1]+jeu[0][coup[0]][coup[1]])
			if coup[1]+jeu[0][coup[0]][coup[1]] < ligneSize :
		
				coupValides.remove([coup[0],coup[1]])
	
	return coupValides
	
def joueCoup(jeu,coup):

	print(coup)

	n = jeu[0][coup[0]][coup[1]]
	jeu[0][coup[0]][coup[1]] = 0
	prochaineCase = [coup[0],coup[1]]
	gagne = []
	
	while n > 0:
		
		if prochaineCase[0] == 1:
			
			prochaineCase[1] += 1
			
		elif prochaineCase[0] == 0:
		
			prochaineCase[1] -= 1
		
		if prochaineCase[1] == ligneSize and prochaineCase[0] == 1:
		
			prochaineCase[0] = 0
			
			prochaineCase[1] = ligneSize-1
			
		elif prochaineCase[1] == -1 and prochaineCase[0] == 0:
			
			prochaineCase[0] = 1
			
			prochaineCase[1] = 0
			
			
		jeu[0][prochaineCase[0]][prochaineCase[1]] += 1
		
		
		if jeu[0][prochaineCase[0]][prochaineCase[1]] < 4 and jeu[0][prochaineCase[0]][prochaineCase[1]] > 1 and prochaineCase[0] != (jeu[1]-1):
		
			jeu[4][jeu[1]-1] += jeu[0][prochaineCase[0]][prochaineCase[1]]
			
			gagne.append(prochaineCase)
			gagne.append(jeu[0][prochaineCase[0]][prochaineCase[1]])
			
			jeu[0][prochaineCase[0]][prochaineCase[1]] = 0
		
		n-=1	
		
	s=0
	ancien=0
		
	if jeu[1] == 1:
		ancien=1
		jeu[1]=2
		ligne = jeu[0][1]
	elif jeu[1] == 2:
		ancien=2
		jeu[1]=1	
		ligne = jeu[0][0]
		
	for case in ligne:
		
		s+=case
		
	print(s)
	i=0
	
	if s==0:
	
		while i < len(gagne/2):
		
			jeu[0][gagne[i][0]][gagne[i][1]] += gagne[i+1]
		
			jeu[4][ancien-1]-= gagne[i+1]
		
	jeu[3].append(coup)
	jeu[2] = None
	
def fin(jeu):

	if len(jeu[3]) >= 100:
		return True	
	else:
		return False
	
	
