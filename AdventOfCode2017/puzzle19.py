from time import sleep

diagram=[]
f=open('input/input19.txt')
for line in f:
    diagram.append([line[x] for x in xrange(len(line)-1)])
f.close()

def checkPos(pos):
    if pos[0]<0 or pos[1]<0 or pos[0]>=len(diagram[0]) or pos[1]>=len(diagram):
        return None
    return diagram[pos[1]][pos[0]]

currPos=[]
for i,s in enumerate(diagram[0]):
    if s=='|':
        currPos=[i,0]

currVel=[0,1]

currS=checkPos(currPos)

totSteps=0
letters=[]
while currS!=' ':
    if currS=='|' or currS=='-':#continue as normal
        currPos=[currPos[0]+currVel[0],currPos[1]+currVel[1]]
    elif currS=='+':
        if currVel[0]==0:
            testPos1=[currPos[0]+1,currPos[1]]
            testS1=checkPos(testPos1)
            testPos2=[currPos[0]-1,currPos[1]]
            testS2=checkPos(testPos2)
            if testS1!=' ' and testS1!='|':
                #print 'turn right',testS1
                currVel=[1,0]
                currPos=[currPos[0]+currVel[0],currPos[1]+currVel[1]]
            elif testS2!=' ' and testS2!='|':
                #print 'turn left'
                currVel=[-1,0]
                currPos=[currPos[0]+currVel[0],currPos[1]+currVel[1]]
            else:
                print "ending?"
        else:
            testPos1=[currPos[0],currPos[1]+1]
            testS1=checkPos(testPos1)
            testPos2=[currPos[0],currPos[1]-1]
            testS2=checkPos(testPos2)
            if testS1!=' ' and testS1!='-':
                #print 'turn down'
                currVel=[0,1]
                currPos=[currPos[0]+currVel[0],currPos[1]+currVel[1]]
            elif testS2!=' ' and testS2!='-':
                #print 'turn up'
                currVel=[0,-1]
                currPos=[currPos[0]+currVel[0],currPos[1]+currVel[1]]
            else:
                print "ending?"
    elif currS is None:
        print 'wrong turn'
    else:
        #should be a letter
        letters.append(currS)
        currPos=[currPos[0]+currVel[0],currPos[1]+currVel[1]]


    currS=checkPos(currPos)
    totSteps+=1
    #print currPos,currS
    #sleep(.001)

ans=''
for x in letters:
    ans+=x

print ans
print totSteps