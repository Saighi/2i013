import mainGen
import game
import random

Pmin = 0
Pmax =10

score = []

n = 0

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


def multirun(n):

    f=run()

    for i in range(n):

        f=(f+run())/2

    return f

def start():

    global Pmax,Pmin

    PondList=[]
    FinessList=[]
    
    maxi=0
    maxiPond= []

    for i in range(21):

        for h in range(len(game.joueur1.Pond)):

            game.joueur1.Pond[h] = random.randint(Pmin, Pmax)

        f = multirun(50)

        pond = game.joueur1.Pond[:]

        PondList.append(pond)
        FinessList.append(f)

        #print(str(game.joueur1.Pond) + " f= " + str(f))

    global n

    while n<20 and max(FinessList)<18:

        if maxi < max(FinessList):
            maxi = max(maxi,max(FinessList))
            maxiPond = PondList[FinessList.index(maxi)]

        PondList=NextGen(PondList, FinessList)

        FinessList = []

        for p in PondList:

            game.joueur1.Pond = p

            f = multirun(50)

            FinessList.append(f)

            #print(str(game.joueur1.Pond) + " f= " + str(f))


    Winner(PondList,FinessList)
    
    print("max : "+str(maxiPond)+" "+str(maxi))

def best():

    PondList = []

    FinessList = []

    for pond in PondList:

        game.joueur1.Pond = pond[:]

        FinessList.append(run())

    for c, pond in enumerate(PondList):

        print(str(pond)+ " f: "+str(FinessList[c]))

def NextGen(PondList,FinessList):

        global n,Pmax,Pmin

        tailleI = len(PondList)

        print(" Next Gen ! "+ str(n)+ " f : "+str(max(FinessList)) +"P : "+ str(PondList[FinessList.index(max(FinessList))]))

        n+=1

        FitnessSum=sum(FinessList)

        Winner=[]
        NormFit=[]
        """
        for i in range(len(FinessList)):

            NormFit.append(FinessList[i]/FitnessSum)

        #print("  ")
        #print( "Winner !!!")

        for e in range(tailleI//4):
        
            i=weighted_choice_king(NormFit)
            NormFit.remove(NormFit[i])
            Winner.append(PondList[i])
            PondList.remove(PondList[i])
        
        """
        for e in range(tailleI//7):

            maxi = max(FinessList)
            i= FinessList.index(maxi)
            #print(str(PondList[i])+" f: "+str(FinessList[i]))
            FinessList.remove(maxi)


        for k in range(tailleI//9):

            r= random.choice(PondList)
            #print(str(r) + " f: " + str(FinessList[PondList.index(r)]))
            Winner.append(r)
            PondList.remove(r)

        #print("  ")
        PondList = Winner[:]

        while len(PondList) < tailleI:

            d = random.randint(0,len(Winner)-1)
            m = random.randint(0,len(Winner)-1)

            while m == d:
                m = random.randint(0, len(Winner)-1)

            dad = Winner[d]
            mom = Winner[m]

            swappingIndex = random.randint(0,len(game.joueur1.Pond)-1)

            dad1 = dad[:swappingIndex]
            dad2 = dad[swappingIndex:]

            mom1 = mom[:swappingIndex]
            mom2 = mom[swappingIndex:]

            dad1.extend(mom2)
            dad= dad1
            mom1.extend(dad2)
            mom= mom1

            PondList.append(dad)
            #no_doublon(PondList,dad)

            PondList.append(mom)
            #no_doublon(PondList,mom)
           
        while len(PondList) < tailleI:

            r = []

            for h in range(len(game.joueur1.Pond)):

                r.append(random.randint(Pmin, Pmax))

            PondList.append(r)

        for z in range(tailleI//10):

            m = random.choice(PondList)
            m[random.randint(0,len(game.joueur1.Pond)-1)]=random.randint(Pmin, Pmax)

        return PondList


def Winner(PondList,FinessList):

    maxi = max(FinessList)
    i = FinessList.index(maxi)

    print("Winner : "+  str(PondList[i]) + " fitness :" + str(FinessList[i]))

def weighted_choice_king(weights):
    total = 0
    winner = 0
    for i, w in enumerate(weights):
        total += w
        if random.random() * total < w:
            winner = i
    return winner

def no_doublon(PondList,pond):



    count = 0

    for j in PondList:

        if pond==j:
            count+=1

    if count > 1:

        for n in range(count-1):
            PondList.remove(pond)

print(start())