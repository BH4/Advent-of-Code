import numpy as np
DIM=3

def posT(p,v,a,t):

    pT=[p[i]+t*v[i]+a[i]*(t*(t+1))/2 for i in xrange(3)]
    return pT

def mag(x):
    return abs(x[0])+abs(x[1])+abs(x[2])

#returns list of indices that are currently overlapping with any others
def collisions(pos):
    numP=len(pos)/3
    collided=set()
    for i in xrange(numP-1):
        for j in xrange(i+1,numP):
            if (pos[DIM*i:DIM*i+3]==pos[DIM*j:DIM*j+3]).all():
                collided.add(i)
                collided.add(j)

    return collided

def isPerfectSquare(x):
    if np.sqrt(x)**2==x:
        return True
    return False

#return None if no collisions
def earliestCollisionTime(p0,p1,v0,v1,a0,a1):
    timesPerIndex=[]
    for i in xrange(3):
        t=[]#holds time that positions are the same. None if never (0-inf in the integers) and -1 if always

        dp=p1[i]-p0[i]
        dv=v1[i]-v0[i]
        da=a1[i]-a0[i]
        if da%2!=0:
            da=float(da)

        if da==0:
            if dv==0 and dp==0:
                t.append(-1)
            elif dv==0:
                return None
            else:
                ans=-dp/dv
                if ans>=0 and int(ans)==ans:
                    t.append(int(ans))
                else:
                    return None
        else:
            a=da/2
            b=dv+a
            c=dp
            D=b**2-4*a*c
            #if not isPerfectSquare(D):
            #    return None

            s=[(-b+np.sqrt(D))/(2*a),(-b-np.sqrt(D))/(2*a)]
            #print s
            t=[int(x) for x in s if x>=0 and int(x)==x]

            if len(t)==0:
                return None
        timesPerIndex.append(t)

    #print timesPerIndex
    #timesPerIndex=timesPerIndex[1:]+timesPerIndex[0]
    #print timesPerIndex
    #ignore the posibility that two particles could start and evolve exactly the same
    while timesPerIndex[0]==[-1]:
        timesPerIndex=timesPerIndex[1:]+[timesPerIndex[0]]

    #print timesPerIndex
    inAll=[]
    for a in timesPerIndex[0]:
        if (a in timesPerIndex[1] and a in timesPerIndex[2]) or (a in timesPerIndex[1] and -1 in timesPerIndex[2]) or (-1 in timesPerIndex[1] and a in timesPerIndex[2]) or (-1 in timesPerIndex[1] and -1 in timesPerIndex[2]):
            inAll.append(a)

    if len(inAll)==0:
        return None
    #print inAll
    return min(inAll)



pos=[]
vel=[]
acc=[]
f=open('input/input20.txt')
for line in f:
    pva=line[:-1].split(', ')
    pos.extend([int(x) for x in (pva[0][3:-1]).split(',')])
    vel.extend([int(x) for x in (pva[1][3:-1]).split(',')])
    acc.extend([int(x) for x in (pva[2][3:-1]).split(',')])
f.close()
pos=np.array(pos)
vel=np.array(vel)
acc=np.array(acc)
numP=len(pos)/3

smallest=None
sVal=10**50
t=100000
for i in xrange(numP):
    pTmag=mag(posT(pos[DIM*i:DIM*i+3],vel[DIM*i:DIM*i+3],acc[DIM*i:DIM*i+3],t))
    if pTmag<sVal:
        sVal=pTmag
        smallest=i
    elif pTmag==sVal:
        print i
print smallest


#part 2
#print earliestCollisionTime(np.array([-6,0,0]),np.array([-4,0,0]),np.array([3,0,0]),np.array([2,0,0]),np.array([0,0,0]),np.array([0,0,0]))

allCollisions=[]#(t,i,j)
for i in xrange(numP-1):
    for j in xrange(i+1,numP):
        t=earliestCollisionTime(pos[DIM*i:DIM*i+3],pos[DIM*j:DIM*j+3],vel[DIM*i:DIM*i+3],vel[DIM*j:DIM*j+3],acc[DIM*i:DIM*i+3],acc[DIM*j:DIM*j+3])
        if not t is None:
            allCollisions.append((t,i,j))

allCollisions.sort()
exist=set(range(numP))
while len(allCollisions)>0:
    c=allCollisions.pop(0)
    t=int(c[0])
    inds=set([c[1],c[2]])
    while len(allCollisions)>0 and allCollisions[0][0]==t:
        c=allCollisions.pop(0)
        inds.add(c[1])
        inds.add(c[2])

    if len(exist&inds)>=2:
        for i in inds:
            if i in exist:
                exist.remove(i)
print len(exist)

#assert len(collisions(pos))==0

"""
for t in xrange(10000):
    vel=vel+acc
    pos=pos+vel

    for i in collisions(pos):
        pos=np.append(pos[:DIM*i],pos[DIM*i+4:])
        vel=np.append(vel[:DIM*i],vel[DIM*i+4:])
        acc=np.append(acc[:DIM*i],acc[DIM*i+4:])

    print t,len(pos)/3
"""