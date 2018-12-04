directions={'n':(0,1),'ne':(1,0),'se':(1,-1),'s':(0,-1),'sw':(-1,0),'nw':(-1,1)}

#distance from the origin to the given position
def distance(coord):
    if (coord[0]<=0 and coord[1]<=0) or (coord[0]>=0 and coord[1]>=0):
        return abs(coord[0]+coord[1])

    #small=min(coord)
    big=max(coord)
    return big#small+(big-small) move se or nw till there is just 0,n or n,0 then add n=big-small

def getCoords(path):
    curr=[0,0]
    maxDistance=0

    for d in path:
        move=directions[d]
        curr[0]+=move[0]
        curr[1]+=move[1]

        maxDistance=max(maxDistance,distance(curr))

    return curr,maxDistance



f=open('input/input11.txt')
s=f.read().replace('\n', '')
f.close()
kidPath=s.split(',')
kidCoords,maxDistance=getCoords(kidPath)

#kids coords happen to be both negative so i can just add them by going s and sw
print abs(kidCoords[0]+kidCoords[1])#original method I used to solve part 1

#part 2

print maxDistance