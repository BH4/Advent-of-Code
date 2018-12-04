from time import sleep


def getBin(num):
    b=bin(num)[2:]
    while len(b)<8:
        b='0'+b
    return b

def xor(nums):
    assert len(nums)==16
    result=nums[0]
    for i in xrange(1,len(nums)):
        result^=nums[i]
    return result

def reverse(nums,currInd,length):
    if length>len(nums) or length==1:
        return nums

    temp=nums[currInd:]+nums[:currInd]
    temp=temp[:length][::-1]+temp[length:]
    nums=temp[-currInd:]+temp[:-currInd]
    return nums

def oneRound(nums,currInd,skip,lengths):
    for l in lengths:
        nums=reverse(nums,currInd,l)
        currInd=(currInd+l+skip)%len(nums)
        skip+=1

    return nums,currInd,skip

def knotHashBin(chars):
    nums=range(256)
    currInd=0
    skip=0

    lengths=[ord(x) for x in chars]+[17, 31, 73, 47, 23]

    for i in xrange(64):
        nums,currInd,skip=oneRound(nums,currInd,skip,lengths)

    denseHash=[xor(nums[16*i:16*(i+1)]) for i in xrange(16)]

    KnotHash=''
    for x in denseHash:
        KnotHash+=getBin(x)
    return KnotHash

def overWriteRegion(grid,i,j):
    neighbors=[(1,0),(0,-1),(0,1),(-1,0)]

    curr=(i,j)
    q=[(i,j)]
    while len(q)>0:
        curr=q.pop(0)
        grid[curr[0]][curr[1]]=0
        for n in neighbors:
            test=(curr[0]+n[0],curr[1]+n[1])
            if test[0]>=0 and test[0]<=127 and test[1]>=0 and test[1]<=127 and (grid[test[0]][test[1]]==1) and (not test in q):
                q.append(test)

    return grid




key='uugsqrei'
#print knotHashBin('flqrgnkx-0')


grid=[]

tot=0
for i in xrange(128):
    row=knotHashBin(key+'-'+str(i))
    grid.append([int(x) for x in row])
    tot+=row.count('1')

print tot

numR=0
seen=set()
for i in xrange(128):
    for j in xrange(128):
        if grid[i][j]==1:
            numR+=1
            #print grid
            grid=overWriteRegion(grid,i,j)
            #print grid
            #sleep(5)

print numR
