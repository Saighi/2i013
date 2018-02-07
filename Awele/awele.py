ligneSize = 6
ligneNum = 2


def init():

	plateau = []
	for i in range(ligneNum):
		plateau.append([])
	
	for ligne in plateau:
		
		for case in range(ligneSize):
		
			ligne.append(4)
			
			
	return [plateau,1,None,[],[0,0]]
	
def CoupValides(jeu):
	
	coupValides = []
	
	e = jeu[1]-1
	
	if e == 0:
	
		ligne = jeu[0][0]
		adver = jeu[0][1]
	
	else:
	
		ligne = jeu[0][1]
		adver = jeu[0][0]
		
	s=0
	
	for case in adver:
	
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
	
			if coup[1]+jeu[0][coup[0]][coup[1]] < ligneSize and coup[0] == 1:
		
				coupValides.remove([coup[0],coup[1]])
				
			elif ligneSize-1-coup[1]+jeu[0][coup[0]][coup[1]] < ligneSize and coup[0] == 0:
			
				coupValides.remove([coup[0],coup[1]])
	
	if len(coupValides) == 0:
		return None
	
	print(coupValides)
	
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
			
		if prochaineCase != coup :
			
			jeu[0][prochaineCase[0]][prochaineCase[1]] += 1
		
		
		if jeu[0][prochaineCase[0]][prochaineCase[1]] < 4 and jeu[0][prochaineCase[0]][prochaineCase[1]] > 1 and prochaineCase[0] != (jeu[1]-1):
		
			
			gagne.append([prochaineCase[0],prochaineCase[1]])
			gagne.append(jeu[0][prochaineCase[0]][prochaineCase[1]])
		
			jeu[4][jeu[1]-1] += jeu[0][prochaineCase[0]][prochaineCase[1]]
			
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

	i=0
	
	if s==0:
	
		
		while i < len(gagne)/2:
		
			jeu[0][gagne[i][0]][gagne[i][1]] += gagne[i+1]
		
			jeu[4][ancien-1]-= gagne[i+1]
			
			i += 2
		
		
	jeu[3].append(coup)
	jeu[2] = None
	
def fin(jeu):

	print("Nombre de tour : " + str(len(jeu[3])))

	if len(jeu[3]) >= 500:
		
		return True	
		
	elif jeu[2] == None:
		return True
	
	elif jeu[4][0] >=25 or jeu[4][1] >=25:
	
		return True
	
	else:
		return False
	
	
