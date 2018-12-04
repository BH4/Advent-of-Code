import numpy as np
from collections import defaultdict
#from time import sleep

num=325489

if num==1:
    print 0
else:
    rightLine=lambda n:4*n*n-3*n+1
    upLine=lambda n:4*n*n-1*n+1
    leftLine=lambda n:4*n*n+1*n+1
    downLine=lambda n:4*n*n+3*n+1

    lines=[rightLine,upLine,leftLine,downLine]

    rightN=int((3+np.sqrt(9+16*(num-1)))/8)
    upN=int((1+np.sqrt(1+16*(num-1)))/8)
    leftN=int((-1+np.sqrt(1+16*(num-1)))/8)
    downN=int((-3+np.sqrt(9+16*(num-1)))/8)

    ns=[rightN,upN,leftN,downN]

    differences=[num-lines[i](ns[i]) for i in xrange(4)]
    ind=differences.index(min(differences))

    #if the number has turned the corner use the next point
    sideLen=2*ns[ind]+1
    if differences[ind]>(sideLen-1)/2:
        ind=(ind+1)%4
        ns=[x+1 for x in ns]

    MagFirstCoord=ns[ind]
    SecondCoord=lines[ind](ns[ind])-num

    print MagFirstCoord+abs(SecondCoord)


currPos=[0,0]
currV=1
direction=[1,0]

maxPos=1

adjacent=[(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
previous=defaultdict(int)
previous[tuple(currPos)]=currV

while currV<num:
    currPos=[currPos[i]+direction[i] for i in xrange(2)]

    currV=sum([previous[tuple([currPos[i]+x[i] for i in xrange(2)])] for x in adjacent])
    previous[tuple(currPos)]=currV

    nextPos=[currPos[i]+direction[i] for i in xrange(2)]
    if abs(nextPos[0])>maxPos or abs(nextPos[1])>maxPos:
        if direction[0]==1:
            if previous[tuple([currPos[0],currPos[1]+1])]==0:
                direction=[0,1]
            else:
                maxPos+=1
        elif direction[1]==1:
            direction=[-1,0]
        elif direction[0]==-1:
            direction=[0,-1]
        elif direction[1]==-1:
            direction=[1,0]



print currV