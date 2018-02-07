# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup: Pair[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:N-UPLET[plateau nat List[coup] List[coup] Pair[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2


#Fonctions minimales 

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    plat = []
    for i in range (game.ligneNum):
    	plat.append([])
    n = 0
    
    
    for ligne in jeu[0]:
    	
    	plat[n] = ligne[:]
    	
    	n += 1
    
    tour = jeu[1]
    
    
    liste1= jeu[2][:]
    
    liste2= jeu[3][:]
    
    score = jeu[4][:]
    
  
    return [plat,tour,liste1,liste2,score]

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return game.fin(jeu)

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    if jeu[1] == 1:
    	return joueur1.saisieCoup(jeu)
    if jeu[1] == 2:
    	return joueur2.saisieCoup(jeu)
    	

def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu a jour (sauf coups valides qui est fixee a None)
    """
    game.joueCoup(jeu,coup)

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    return game.init()

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    
    if finJeu:
    
    	if jeu[4][0] < jeu[4][1]:
    	
    		return 2
    		
    	elif jeu[4][0] > jeu[4][1]:
    	
    		return 1
    		
    	else:
    	
    		return 0

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    
    n = 0;
    s="     |"
    
    if jeu[3] != [] :
    	print('Coup joue = '+ str(jeu[3][-1]))
    print('Scores = '+ str(jeu[4][0]) + ',' + str(jeu[4][1]))
    print('Plateau :')
    
    
    
    for i in range(game.ligneSize):
    	 s+= "     " +str(i)+"     |"
     
    
    for j in jeu[0] :
    	s+="\n"
    	s+="  "+str(n)+"  |"
    	for e in j:
    		s+="     "+str(e)+"     |"
    	
    	
    	n+=1
    print(s)
    
    
	
# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    return jeu[0]

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met a jour la liste des coups valides
    """
    
    if jeu[2] == None:
    	jeu[2]=game.CoupValides(jeu)
    
    return jeu[2]

def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]



def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
     
    if getJoueur(jeu)== 1:
    	jeu[1]= 2
    else:
    	jeu[1]= 1
    	

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    if joueur == 1:
    	return getScores(jeu)[0]
    else :
    	getScores(jeu)[1]

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    return getPlateau(jeu)[ligne][colonne]
    
    




