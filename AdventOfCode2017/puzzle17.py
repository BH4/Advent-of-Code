
steps=366
#steps=3
numPoints=2017

b=[0]
curr=0
for i in xrange(1,numPoints+1):
    realSteps=steps%i
    new=(curr+realSteps)%i
    b.insert(new+1,i)
    curr=new+1

    #print new
    #print b
ind=b.index(numPoints)
print b[(ind+1)%len(b)]



steps=366
numPoints=50000000
#steps=3
#numPoints=9

curr=0
ans=None
for i in xrange(1,numPoints+1):
    realSteps=steps%i
    new=(curr+realSteps)%i
    curr=new+1
    if new==0:
        ans=i

print ans